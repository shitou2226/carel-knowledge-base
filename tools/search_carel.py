"""Search the portable CAREL notes locally, reading navigation before topics."""
from pathlib import Path
import argparse,json,re,shutil,subprocess,sys

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query');ap.add_argument('--root',type=Path)
    ap.add_argument('--scope',choices=['auto','topics','sources','all'],default='auto')
    ap.add_argument('--backend',choices=['auto','python','rg'],default='auto')
    ap.add_argument('--limit',type=int,default=12);ap.add_argument('--regex',action='store_true')
    args=ap.parse_args()
    root=(args.root or Path(__file__).resolve().parents[1]/'vault/03 PLC/CAREL').resolve()
    navigation=[{'path':str(p),'chars':len(p.read_text(encoding='utf-8'))} for p in [root/'00-首页与使用说明/CAREL 知识库首页.md',root/'资料总索引.md']]
    rg=shutil.which('rg');backend='rg' if args.backend=='auto' and rg else 'python' if args.backend=='auto' else args.backend
    if backend=='rg' and not rg:raise ValueError('ripgrep is not available; use --backend python.')
    pattern=re.compile(args.query if args.regex else re.escape(args.query),re.IGNORECASE)
    def search(scope):
        folders=[p for p in sorted(root.iterdir()) if p.is_dir() and p.name[:2] in {'02','03','04','05','06','07','08'}] if scope=='topics' else [root/'90-原始资料',root/'09-视频课程笔记'] if scope=='sources' else [root]
        if backend=='python':
            results=[]
            for folder in folders:
                for path in sorted(folder.rglob('*.md')):
                    count=0
                    for i,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
                        if pattern.search(line):
                            results.append({'path':str(path),'line':i,'text':line.strip()[:1000]});count+=1
                            if count==5:break
            return results
        cmd=[rg,'--json','--ignore-case','--glob','*.md','--max-count','5']
        if not args.regex:cmd.append('--fixed-strings')
        p=subprocess.run([*cmd,'--',args.query,*map(str,folders)],capture_output=True,encoding='utf-8',errors='replace')
        if p.returncode not in (0,1):raise ValueError(p.stderr)
        matches=[]
        for line in p.stdout.splitlines():
            event=json.loads(line)
            if event['type']=='match':
                d=event['data'];matches.append({'path':d['path']['text'],'line':d['line_number'],'text':d['lines']['text'].strip()[:1000]})
        return matches
    scope='topics' if args.scope=='auto' else args.scope;matches=search(scope);fallback=False
    if args.scope=='auto' and not matches:scope='sources';matches=search(scope);fallback=True
    print(json.dumps({'navigation_read_first':navigation,'edition':'public','backend':backend,'query':args.query,'scope':scope,'fallback_to_sources':fallback,'match_count':len(matches),'matches':matches[:max(1,args.limit)],'network_requests':0,'next_step':'Verify the original source; public source notes contain metadata, not original documents.' if matches else 'Expand synonyms and identify the missing model/version/source before online research.'},ensure_ascii=False,indent=2))
if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    try:main()
    except Exception as e:print(json.dumps({'error':str(e)},ensure_ascii=False),file=sys.stderr);sys.exit(2)

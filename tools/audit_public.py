"""Audit only public publication files; never print matched secret values."""
from pathlib import Path
import hashlib,json,re,sys,urllib.parse
ROOT=Path(__file__).resolve().parents[1]
def files(root):
    return [p for p in root.rglob('*') if p.is_file() and not any(x in {'.git','__pycache__','.venv'} for x in p.relative_to(root).parts) and p.name!='public-audit.json']
def audit(root=ROOT):
    issues=[];paths=files(root);links=0
    patterns={'absolute_local_path':re.compile(r'(?i)\b[A-Z]:[\\/]|'+'file'+r':/|/(?:Users|home)/[^\s/]+/'),
              'credential':re.compile(r'(?i)(?:gh[pousr]_[A-Za-z0-9]{24,}|github_pat_[A-Za-z0-9_]{25,}|sk-[A-Za-z0-9_-]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)'),
              'private_network':re.compile(r'\b(?:192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b')}
    for p in paths:
        rel=p.relative_to(root).as_posix()
        if p.name not in {'.gitignore','.gitattributes'} and p.suffix.lower() not in {'.md','.py','.json','.yml','.yaml','.st'}:issues.append({'file':rel,'type':'unapproved_file_type'});continue
        if p.stat().st_size>500_000:issues.append({'file':rel,'type':'unexpected_large_file'})
        try:text=p.read_text(encoding='utf-8')
        except UnicodeError:issues.append({'file':rel,'type':'not_utf8'});continue
        for kind,pat in patterns.items():
            if pat.search(text):issues.append({'file':rel,'type':kind})
        if p.suffix!='.md':continue
        if p.is_relative_to(root/'vault') and not text.startswith('---\n'):issues.append({'file':rel,'type':'missing_frontmatter'})
        # Ignore code examples when auditing navigational Markdown.
        clean=re.sub(r'```[^\n]*\n[\s\S]*?\n```','',text)
        if '{{' in clean or '[[' in clean:issues.append({'file':rel,'type':'unresolved_template_or_wikilink'})
        for label,target in re.findall(r'(?<!!)\[([^\]\n]*)\]\(([^)\n]+)\)',clean):
            u=urllib.parse.urlsplit(target)
            if u.scheme in {'https','http','mailto'}:continue
            links+=1;dest=(p.parent/urllib.parse.unquote(u.path)).resolve() if u.path else p
            if not dest.is_relative_to(root.resolve()):issues.append({'file':rel,'type':'link_outside_repository'});continue
            if not dest.is_file():issues.append({'file':rel,'type':'missing_link','target':target});continue
            if u.fragment and dest.suffix=='.md':
                headings=[x.casefold() for x in re.findall(r'^#{1,6} +(.+?)\s*$',dest.read_text(encoding='utf-8'),re.M)]
                if urllib.parse.unquote(u.fragment).casefold() not in headings:issues.append({'file':rel,'type':'missing_heading','target':target})
    return {'files':len(paths),'markdown':sum(p.suffix=='.md' for p in paths),'local_links':links,'issues':issues,'file_sha256':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    result=audit();(ROOT/'public-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='file_sha256'},ensure_ascii=False,indent=2))
    sys.exit(bool(result['issues']))

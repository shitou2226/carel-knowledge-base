from pathlib import Path
import importlib.util,json,shutil,subprocess,sys,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('audit',ROOT/'tools/audit_public.py');audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
def search(q,*args):
    p=subprocess.run([sys.executable,str(ROOT/'tools/search_carel.py'),q,*args],capture_output=True,encoding='utf-8')
    return p,json.loads(p.stdout) if p.returncode==0 else None
class PublicKnowledgeBase(unittest.TestCase):
    def test_publication_files_and_links(self):self.assertEqual(audit.audit()['issues'],[])
    def test_inventory_counts(self):
        data=json.loads((ROOT/'data/edition.json').read_text(encoding='utf-8'));self.assertEqual(data['curated_topics'],22);self.assertEqual(data['course_guides'],35);self.assertFalse(data['original_documents_included'])
    def test_six_question_types(self):
        for query,expected in [('c.pCO mini','端口与硬件'),('Build Solution','工程创建'),('Online error','Modbus从站'),('实例','函数与功能块'),('Retries','Modbus主站'),('NO LINK','NO LINK')]:
            with self.subTest(query=query):
                p,x=search(query,'--backend','python','--limit','100');self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(len(x['navigation_read_first']),2);self.assertTrue(any(expected in m['path'] for m in x['matches']))
    def test_negative_query(self):
        p,x=search('未提供型号设备40001的上电默认值','--backend','python');self.assertEqual(p.returncode,0);self.assertEqual(x['match_count'],0);self.assertEqual(x['network_requests'],0)
    def test_source_fallback(self):
        p,x=search('Appendix_B_HowToTranslateInRussian.mp4','--backend','python');self.assertEqual(p.returncode,0);self.assertTrue(x['fallback_to_sources']);self.assertGreater(x['match_count'],0)
    def test_regex_error(self):
        p,_=search('[','--regex','--backend','python');self.assertEqual(p.returncode,2)
    def test_both_backends(self):
        if not shutil.which('rg'):self.skipTest('rg optional; Python backend already checked')
        _,a=search('PID_Adv_2','--backend','python','--limit','100');_,b=search('PID_Adv_2','--backend','rg','--limit','100')
        self.assertEqual({(m['path'],m['line']) for m in a['matches']},{(m['path'],m['line']) for m in b['matches']})
    def test_secret_and_local_path_rejection(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'note.md';p.write_text('C'+':'+chr(92)+'personal'+chr(92)+'private.txt\n'+'gh'+'p_'+'X'*36,encoding='utf-8')
            types={x['type'] for x in audit.audit(Path(tmp))['issues']};self.assertIn('absolute_local_path',types);self.assertIn('credential',types)
    def test_demo_alarm_not_output_inhibit(self):
        line=next(s for s in (ROOT/'examples/temperature_fan_body.st').read_text(encoding='utf-8').splitlines() if s.startswith('FanRunCmd :='));self.assertNotIn('HighTempAlarm',line)
if __name__=='__main__':unittest.main()

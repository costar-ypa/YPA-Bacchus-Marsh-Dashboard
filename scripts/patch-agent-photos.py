from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
photos={
'Vickie Ramon':'images/agents/vickie-ramon.jpg',
'Ryan Anders':'images/agents/ryan-anders-cheyanne-kollar.jpg',
"Shane O'Brien":'images/agents/shane-obrien-katelyn-taylor.jpg',
'Jodi Nash':'images/agents/jodi-nash.jpg',
'Kate McGlone':'images/agents/kate-mcglone-ryan-fernandes.jpg',
'Costa Rodriguez':'images/agents/costa-rodriguez.jpg',
'Mark Edwards':'images/agents/mark-edwards.jpg',
'Ricky Frew':'images/agents/ricky-frew.jpg',
'Cory Cassar':'images/agents/cory-cassar.jpg'
}
for name,path in photos.items():
    token=f'name:"{name}",'
    repl=f'name:"{name}", photo:"{path}",'
    if repl not in s:
        if token not in s:
            raise SystemExit(f'Missing directory entry for {name}')
        s=s.replace(token,repl,1)
s=s.replace("const photo = source && source.agentPhoto ? String(source.agentPhoto) : '';","const photo = person.photo || (source && source.agentPhoto ? String(source.agentPhoto) : '');",1)
s=s.replace('width:92px;\n    height:92px;\n    border-radius:50%;','width:180px;\n    height:220px;\n    border-radius:16px;',1)
s=s.replace('flex:0 0 92px;','flex:0 0 180px;',1)
s=s.replace('width:74px;\n        height:74px;','width:120px;\n        height:150px;',1)
p.write_text(s,encoding='utf-8')

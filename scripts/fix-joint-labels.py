from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
while '+ Melton + Melton' in s:
    s=s.replace('+ Melton + Melton','+ Melton')
p.write_text(s,encoding='utf-8')
print('Cleaned duplicate joint labels.')

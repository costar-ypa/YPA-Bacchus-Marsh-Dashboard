from pathlib import Path
p=Path('index.html')
s=p.read_text()
old='<link rel="apple-touch-icon" href="images/ypa-logo-transparent.png">'
new='<link rel="apple-touch-icon" sizes="180x180" href="images/ypa-app-icon-180.png?v=2">'
if old in s:
    s=s.replace(old,new,1)
elif 'images/ypa-app-icon-180.png' not in s:
    raise SystemExit('Apple touch icon marker not found')
p.write_text(s)

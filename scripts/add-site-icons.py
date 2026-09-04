from pathlib import Path
p=Path('index.html')
s=p.read_text()
old='<link rel="apple-touch-icon" sizes="180x180" href="images/ypa-app-icon-180.png?v=2">'
new='''<link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png">\n<link rel="apple-touch-icon-precomposed" sizes="180x180" href="./apple-touch-icon.png">'''
if old in s:
    s=s.replace(old,new,1)
elif '<link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png">' not in s:
    marker='<link rel="icon" type="image/svg+xml" href="favicon.svg">'
    if marker not in s:
        raise SystemExit('favicon marker not found')
    s=s.replace(marker, marker+'\n'+new,1)
if '<link rel="manifest" href="./site.webmanifest">' not in s:
    s=s.replace('<link rel="manifest" href="site.webmanifest">','<link rel="manifest" href="./site.webmanifest">',1)
meta='''<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="default">\n<meta name="apple-mobile-web-app-title" content="YPA Guide">'''
if 'apple-mobile-web-app-capable' not in s:
    marker='<meta name="theme-color" content="#030914">'
    if marker not in s:
        raise SystemExit('theme marker not found')
    s=s.replace(marker, marker+'\n'+meta,1)
p.write_text(s)

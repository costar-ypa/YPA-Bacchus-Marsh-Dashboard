from pathlib import Path
p=Path('index.html')
s=p.read_text()
marker='<meta name="description" content="The Weekend Property Guide from YPA Bacchus Marsh + Melton. Explore this weekend\'s inspections, properties and local opportunities.">'
block='''\n<link rel="icon" type="image/svg+xml" href="favicon.svg">\n<link rel="apple-touch-icon" href="images/ypa-logo-transparent.png">\n<link rel="manifest" href="site.webmanifest">\n<meta name="theme-color" content="#030914">'''
if 'rel="manifest" href="site.webmanifest"' not in s:
    if marker not in s:
        raise SystemExit('Head marker not found')
    s=s.replace(marker, marker+block, 1)
p.write_text(s)

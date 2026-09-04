from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace('<div class="ypa-logo">ypa.</div>','<div class="ypa-logo"><img src="images/ypa-logo-transparent.png" alt="YPA"></div>')
s=s.replace('<div class="ypa-launch-logo">ypa<span class="dot">.</span></div>','<div class="ypa-launch-logo"><img src="images/ypa-logo-transparent.png" alt="YPA"></div>')
s=s.replace('.ypa-logo{\n    font-family:Montserrat,sans-serif;\n    font-size:34px;\n    font-weight:800;\n    letter-spacing:-3px;\n    color:#fff;\n}', '.ypa-logo{display:flex;align-items:center}.ypa-logo img{display:block;width:84px;height:auto}')
launch_css='''<style id="real-ypa-logo-fix">#ypa-launch-screen .ypa-launch-logo{width:min(300px,58vw);height:auto;font-size:0;line-height:0}#ypa-launch-screen .ypa-launch-logo img{display:block;width:100%;height:auto;filter:drop-shadow(0 12px 35px rgba(0,0,0,.2))}</style>'''
header_css='''<style id="header-ypa-logo-navy">.header .ypa-logo img{filter:brightness(0) saturate(100%) invert(8%) sepia(20%) saturate(1812%) hue-rotate(171deg) brightness(91%) contrast(103%) !important;}</style>'''
if 'id="real-ypa-logo-fix"' not in s:
    s += '\n'+launch_css+'\n'
if 'id="header-ypa-logo-navy"' not in s:
    s += '\n'+header_css+'\n'
p.write_text(s)

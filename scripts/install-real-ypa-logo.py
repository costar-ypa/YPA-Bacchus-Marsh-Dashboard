from pathlib import Path
p=Path('index.html')
s=p.read_text()
s=s.replace('<div class="ypa-logo">ypa.</div>','<div class="ypa-logo"><img src="images/ypa-logo-transparent.png" alt="YPA"></div>')
s=s.replace('<div class="ypa-launch-logo">ypa<span class="dot">.</span></div>','<div class="ypa-launch-logo"><img src="images/ypa-logo-transparent.png" alt="YPA"></div>')
s=s.replace('.ypa-logo{\n    font-family:Montserrat,sans-serif;\n    font-size:34px;\n    font-weight:800;\n    letter-spacing:-3px;\n    color:#fff;\n}', '.ypa-logo{display:flex;align-items:center}.ypa-logo img{display:block;width:84px;height:auto}')
s += '\n<style id="real-ypa-logo-fix">#ypa-launch-screen .ypa-launch-logo{width:min(300px,58vw);height:auto;font-size:0;line-height:0}#ypa-launch-screen .ypa-launch-logo img{display:block;width:100%;height:auto;filter:drop-shadow(0 12px 35px rgba(0,0,0,.2))}</style>\n'
p.write_text(s)

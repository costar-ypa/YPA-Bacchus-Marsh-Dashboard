from pathlib import Path
import json

p=Path('index.html')
s=p.read_text()
for old in [
    '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png?v=4">',
    '<link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png">',
    '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">'
]:
    s=s.replace(old,'<link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon-v5.png">')
s=s.replace('<link rel="apple-touch-icon-precomposed" sizes="180x180" href="./apple-touch-icon.png">','')
s=s.replace('<link rel="manifest" href="site.webmanifest?v=4">','<link rel="manifest" href="./site-v5.webmanifest">')
s=s.replace('<link rel="manifest" href="./site.webmanifest">','<link rel="manifest" href="./site-v5.webmanifest">')
s=s.replace('<link rel="manifest" href="site.webmanifest">','<link rel="manifest" href="./site-v5.webmanifest">')
p.write_text(s)

manifest={
  'name':'YPA Weekend Property Guide',
  'short_name':'YPA Guide',
  'id':'./?pwa=v5',
  'start_url':'./?pwa=v5',
  'scope':'./',
  'display':'standalone',
  'background_color':'#030914',
  'theme_color':'#030914',
  'icons':[
    {'src':'./images/ypa-app-icon-v5-192.png','sizes':'192x192','type':'image/png','purpose':'any'},
    {'src':'./images/ypa-app-icon-v5-512.png','sizes':'512x512','type':'image/png','purpose':'any'}
  ]
}
Path('site-v5.webmanifest').write_text(json.dumps(manifest,separators=(',',':')))

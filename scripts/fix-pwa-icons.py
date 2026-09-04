from pathlib import Path
import json

p=Path('index.html')
s=p.read_text()
s=s.replace('<link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png">','<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png?v=4">')
s=s.replace('<link rel="apple-touch-icon-precomposed" sizes="180x180" href="./apple-touch-icon.png">','')
s=s.replace('<link rel="manifest" href="./site.webmanifest">','<link rel="manifest" href="site.webmanifest?v=4">')
p.write_text(s)

manifest={
  'name':'YPA Weekend Property Guide',
  'short_name':'YPA Guide',
  'id':'./',
  'start_url':'./',
  'scope':'./',
  'display':'standalone',
  'background_color':'#030914',
  'theme_color':'#030914',
  'icons':[
    {'src':'images/ypa-app-icon-192.png?v=4','sizes':'192x192','type':'image/png','purpose':'any'},
    {'src':'images/ypa-app-icon-512.png?v=4','sizes':'512x512','type':'image/png','purpose':'any'}
  ]
}
Path('site.webmanifest').write_text(json.dumps(manifest,separators=(',',':')))

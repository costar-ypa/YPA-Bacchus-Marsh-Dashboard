from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

photos = {
    'Vickie Ramon':'images/agents/vickie-ramon.jpg',
    'Ryan Anders':'images/agents/ryan-anders-cheyanne-kollar.jpg',
    "Shane O'Brien":'images/agents/shane-obrien-katelyn-taylor.jpg',
    'Jodi Nash':'images/agents/jodi-nash.jpg',
    'Kate McGlone':'images/agents/kate-mcglone-ryan-fernandes.jpg',
    'Costa Rodriguez':'images/agents/costa-rodriguez.jpg',
    'Mark Edwards':'images/agents/mark-edwards.jpg',
    'Ricky Frew':'images/agents/ricky-frew.jpg',
    'Cory Cassar':'images/agents/cory-cassar.jpg',
}

# Add photo property to each directory object if missing.
for name, photo in photos.items():
    pattern = r'(\{name:' + re.escape('"'+name+'"') + r',[^\n]*?profile:"[^"]+")(?=,?\s*(?:assistant:|\}))'
    def repl(m):
        text = m.group(1)
        if 'photo:' in text:
            return text
        return text + ', photo:"' + photo + '"'
    s, n = re.subn(pattern, repl, s, count=1)
    if not n:
        raise SystemExit(f'Could not attach photo for {name}')

# Ensure profile renderer uses the supplied photo.
old = '''        profile.innerHTML = `\n            <div class="agent-profile-photo agent-profile-photo-empty" aria-label="Photo space for ${esc(person.name)}"></div>'''
new = '''        profile.innerHTML = `\n            ${person.photo ? `<img class="agent-profile-photo" src="${esc(person.photo)}" alt="${esc(person.name)}" loading="lazy">` : `<div class="agent-profile-photo agent-profile-photo-empty" aria-label="Photo space for ${esc(person.name)}"></div>`}'''
if old not in s:
    raise SystemExit('Profile photo placeholder block not found')
s = s.replace(old, new, 1)

# Upgrade portrait presentation while preserving the existing light palette.
style = '''\n<style id="agent-photo-panel-style">\n.agent-profile{\n    grid-template-columns:minmax(180px,250px) 1fr auto;\n    align-items:stretch;\n}\n.agent-profile-photo{\n    width:100%;\n    height:320px;\n    max-width:250px;\n    border-radius:14px;\n    object-fit:cover;\n    object-position:center 24%;\n    background:#DDE7EE;\n    border:1px solid #D9E2EC;\n}\n.agent-profile-photo-empty{\n    width:100%;\n    height:320px;\n    max-width:250px;\n    border-radius:14px;\n}\n.agent-profile-copy{\n    align-self:center;\n}\n.agent-profile-actions{\n    align-self:center;\n}\n@media(max-width:800px){\n    .agent-profile{grid-template-columns:1fr;}\n    .agent-profile-photo,.agent-profile-photo-empty{\n        width:100%;\n        max-width:none;\n        height:min(430px,110vw);\n    }\n    .agent-profile-actions{grid-column:auto;}\n}\n</style>\n'''
if 'id="agent-photo-panel-style"' not in s:
    s = s.replace('</head>', style + '\n</head>', 1)

p.write_text(s, encoding='utf-8')

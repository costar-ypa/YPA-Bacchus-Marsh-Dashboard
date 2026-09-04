from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
old = '''            <div class="agent-profile-photo agent-profile-photo-empty" aria-label="Photo space for ${esc(person.name)}"></div>'''
new = '''            <div class="agent-profile-photo" aria-label="Photo of ${esc(person.name)}">
                <img src="${esc(person.photo)}" alt="${esc(person.name)}" loading="lazy">
            </div>'''
if old not in s:
    raise SystemExit('Expected blank agent photo markup not found; refusing unsafe patch')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

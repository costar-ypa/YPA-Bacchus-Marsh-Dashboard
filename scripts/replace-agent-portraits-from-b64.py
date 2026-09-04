from pathlib import Path
import base64

root = Path('images/agents')
for name in ('vickie-ramon','ryan-anders-cheyanne-kollar','ricky-frew','cory-cassar'):
    src = root / f'{name}.quality.b64'
    if src.exists():
        (root / f'{name}.jpg').write_bytes(base64.b64decode(''.join(src.read_text().split()), validate=True))
        src.unlink()

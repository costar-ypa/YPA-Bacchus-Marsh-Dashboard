from pathlib import Path
import base64

root = Path('images/agents')
for staged in root.glob('*-fixed.b64'):
    target = root / staged.name.replace('-fixed.b64', '.jpg')
    data = ''.join(staged.read_text().split())
    target.write_bytes(base64.b64decode(data, validate=True))
    staged.unlink()

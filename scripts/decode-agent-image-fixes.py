from pathlib import Path
import base64

# Decode staged portrait payloads into real JPEG files.
root = Path('images/agents')
for pattern, suffix in (('*-fixed.b64', '-fixed.b64'), ('*-fix.b64', '-fix.b64')):
    for staged in root.glob(pattern):
        target = root / staged.name.replace(suffix, '.jpg')
        data = ''.join(staged.read_text().split())
        target.write_bytes(base64.b64decode(data, validate=True))
        staged.unlink()

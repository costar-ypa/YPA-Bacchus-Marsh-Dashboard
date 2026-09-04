from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
css = '''
<style id="agent-photo-sizing-fix">
.agent-profile{
    align-items:stretch !important;
}
.agent-profile-photo{
    width:100% !important;
    max-width:250px !important;
    height:320px !important;
    min-height:320px !important;
    border-radius:14px !important;
    overflow:hidden !important;
    background:#DDE7EE !important;
    border:1px solid #D9E2EC !important;
}
.agent-profile-photo img{
    display:block !important;
    width:100% !important;
    height:100% !important;
    object-fit:cover !important;
    object-position:center center !important;
}
@media(max-width:800px){
    .agent-profile-photo{
        max-width:100% !important;
        width:100% !important;
        height:300px !important;
        min-height:300px !important;
    }
}
</style>
'''
if 'id="agent-photo-sizing-fix"' in s:
    start=s.index('<style id="agent-photo-sizing-fix">')
    end=s.index('</style>', start)+len('</style>')
    s=s[:start]+css.strip()+s[end:]
else:
    s=s.replace('</head>', css+'\n</head>', 1)
p.write_text(s, encoding='utf-8')

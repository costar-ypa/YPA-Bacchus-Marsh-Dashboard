from pathlib import Path

path = Path('index.html')
text = path.read_text()

if 'id="ypa-launch-screen"' in text:
    raise SystemExit('YPA launch screen already present')

style = r'''
<style id="ypa-launch-screen-styles">
#ypa-launch-screen{
    position:fixed;
    inset:0;
    z-index:99999;
    display:grid;
    place-items:center;
    background:var(--navy-950,#030914);
    opacity:1;
    visibility:visible;
    transition:opacity .48s ease, visibility .48s ease;
}
#ypa-launch-screen.is-exiting{
    opacity:0;
    visibility:hidden;
}
#ypa-launch-screen .ypa-launch-logo{
    font-family:Montserrat,sans-serif;
    font-size:clamp(72px,12vw,124px);
    font-weight:800;
    letter-spacing:-8px;
    line-height:1;
    color:#fff;
    opacity:0;
    transform:scale(.965);
    animation:ypaLaunchLogo 1.45s cubic-bezier(.22,.61,.36,1) forwards;
    will-change:opacity,transform;
}
#ypa-launch-screen .ypa-launch-logo .dot{
    color:var(--gold,#FFD600);
}
@keyframes ypaLaunchLogo{
    0%{opacity:0;transform:scale(.965)}
    24%{opacity:1;transform:scale(1)}
    68%{opacity:1;transform:scale(1)}
    100%{opacity:0;transform:scale(1.025)}
}
@media (prefers-reduced-motion:reduce){
    #ypa-launch-screen{
        transition:opacity .2s ease,visibility .2s ease;
    }
    #ypa-launch-screen .ypa-launch-logo{
        animation:none;
        opacity:1;
        transform:none;
    }
}
</style>
'''

screen = r'''
<div id="ypa-launch-screen" aria-hidden="true">
    <div class="ypa-launch-logo">ypa<span class="dot">.</span></div>
</div>
'''

script = r'''
<script id="ypa-launch-screen-script">
(function(){
    const screen=document.getElementById('ypa-launch-screen');
    if(!screen) return;

    const reduced=window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const hold=reduced ? 250 : 1500;
    const removeAfter=reduced ? 500 : 2050;

    window.setTimeout(()=>screen.classList.add('is-exiting'),hold);
    window.setTimeout(()=>screen.remove(),removeAfter);
})();
</script>
'''

if '</head>' not in text or '<body>' not in text or '</body>' not in text:
    raise SystemExit('Expected HTML anchors not found')

text = text.replace('</head>', style + '\n</head>', 1)
text = text.replace('<body>', '<body>\n' + screen, 1)
text = text.replace('</body>', script + '\n</body>', 1)

path.write_text(text)

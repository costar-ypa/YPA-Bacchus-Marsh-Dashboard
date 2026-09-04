from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

marker = '/* YPA SCREENSHOT PALETTE OVERRIDE */'
if marker in text:
    raise SystemExit('Palette override already present')

css = r'''

/* YPA SCREENSHOT PALETTE OVERRIDE */
:root{
    --navy-950:#07354D;
    --navy-900:#0A3A54;
    --navy-850:#0C405D;
    --navy-800:#104763;
    --navy-750:#16516F;
    --navy-700:#245F7E;

    --gold:#FFD600;
    --gold-light:#FFD600;

    --white:#FFFFFF;
    --text:#102A43;
    --muted:#63758A;
    --muted-light:#53677E;

    --border:#D9E2EC;
    --border-light:#C8D4E0;

    --shadow:0 14px 34px rgba(15,52,77,.10);
}

body{
    background:#EEF3F7;
    color:#102A43;
}

.header{
    background:rgba(255,255,255,.96);
    border-bottom:1px solid #D9E2EC;
    box-shadow:0 1px 0 rgba(15,52,77,.04);
}

.ypa-logo,
.brand-title,
.header-nav a{
    color:#07354D;
}

.brand-divider{
    background:#D9E2EC;
}

.header-nav a:hover{
    background:#E8F0F6;
    color:#07354D;
}

.header-weekend{
    border-color:#C8D4E0;
    background:#F7FAFC;
    color:#07354D;
}

.hero{
    background:
        radial-gradient(circle at 80% 15%, rgba(255,214,0,.13), transparent 28%),
        linear-gradient(145deg,#0D405B 0%,#07354D 68%);
    border-bottom-color:#D9E2EC;
}

.hero::before{
    background:
        linear-gradient(90deg,rgba(7,53,77,.96) 0%,rgba(7,53,77,.76) 46%,rgba(7,53,77,.34) 100%),
        linear-gradient(0deg,rgba(7,53,77,.84) 0%,transparent 54%);
}

.hero-pattern{
    border-color:rgba(255,214,0,.15);
}

.hero-pattern::after{
    border-color:rgba(255,214,0,.10);
}

.hero h1,
.hero-stat strong,
.weekend-title,
.weekend-summary strong{
    color:#FFFFFF;
}

.hero-subtitle{
    color:#DCE7EF;
}

.hero-stats{
    border-color:rgba(255,255,255,.15);
    background:rgba(255,255,255,.15);
}

.hero-stat{
    background:rgba(7,53,77,.82);
}

.hero-stat span{
    color:#C7D5E0;
}

.section-title{
    color:#0B2F46;
}

.section-copy{
    color:#63758A;
}

.weekend-section,
.editorial,
.people{
    background:#EEF3F7;
    border-color:#D9E2EC;
}

.weekend-date,
.section-kicker,
.card-suburb,
.weekend-time,
.editorial-link,
.agent-contact{
    color:#D7B400;
}

.weekend-summary,
.weekend-suburb,
.weekend-empty span,
.card-price,
.card-stat,
.editorial-small p,
.agent-role{
    color:#63758A;
}

.weekend-dashboard{
    background:#D9E2EC;
    border-color:#D9E2EC;
}

.weekend-item,
.weekend-empty,
.property-card,
.editorial-small,
.agent,
.no-results{
    background:#FFFFFF;
    border-color:#D9E2EC;
}

.weekend-address,
.weekend-empty strong,
.card-address,
.card-headline,
.card-stat strong,
.editorial-small h4,
.agent-name,
.no-results strong{
    color:#0B2F46;
}

.weekend-remove{
    color:#63758A;
}

.weekend-remove:hover{
    color:#07354D;
}

.search-wrap input{
    border-color:#C8D4E0;
    background:#FFFFFF;
    color:#102A43;
    box-shadow:0 1px 2px rgba(15,52,77,.03);
}

.search-wrap input::placeholder{
    color:#8192A5;
}

.search-wrap input:focus{
    border-color:#2F80ED;
    box-shadow:0 0 0 3px rgba(47,128,237,.10);
}

.search-icon{
    color:#63758A;
}

.filter-btn{
    border-color:#C8D4E0;
    background:#FFFFFF;
    color:#52677D;
}

.filter-btn:hover{
    border-color:#86A9C3;
    color:#07354D;
    background:#F7FAFC;
}

.filter-btn.active{
    background:#07354D;
    border-color:#07354D;
    color:#FFFFFF;
}

.property-card{
    box-shadow:0 3px 12px rgba(15,52,77,.05);
}

.property-card:hover{
    border-color:#B7C8D6;
    box-shadow:0 16px 38px rgba(15,52,77,.12);
}

.card-photo{
    background:#DDE7EE;
}

.card-content{
    background:#FFFFFF;
}

.card-stats{
    border-top-color:#E4EBF1;
}

.card-main-btn{
    border-color:#07354D;
    background:#07354D;
    color:#FFFFFF;
}

.card-main-btn:hover{
    background:#FFD600;
    border-color:#FFD600;
    color:#07354D;
}

.card-save-btn{
    border-color:#C8D4E0;
    background:#FFFFFF;
    color:#07354D;
}

.card-save-btn.saved{
    color:#07354D;
    border-color:#FFD600;
    background:#FFF8CC;
}

.editorial-feature{
    background:
        radial-gradient(circle at 80% 20%,rgba(255,214,0,.15),transparent 25%),
        linear-gradient(135deg,#104763,#07354D);
    border-color:#0D405B;
}

.editorial-feature p{
    color:#DCE7EF;
}

.agent-photo{
    background:#DDE7EE;
}

.footer{
    background:#07354D;
    border-top-color:#0D405B;
}

.footer-copy{
    color:#C7D5E0;
}

.footer-right strong,
.footer .ypa-logo{
    color:#FFFFFF;
}

.floating-weekend{
    border-color:#FFD600;
    background:#07354D;
    color:#FFFFFF;
    box-shadow:0 14px 35px rgba(7,53,77,.22);
}

.modal{
    background:rgba(7,32,48,.72);
}

.modal-shell{
    border:1px solid #D9E2EC;
    box-shadow:0 30px 80px rgba(7,53,77,.24);
}

@media (max-width:900px){
    .header{
        background:rgba(255,255,255,.98);
    }
}
'''

if '</style>' not in text:
    raise SystemExit('Could not find closing style tag')

text = text.replace('</style>', css + '\n</style>', 1)
path.write_text(text, encoding='utf-8')

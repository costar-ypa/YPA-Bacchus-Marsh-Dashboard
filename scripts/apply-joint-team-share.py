from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Joint Bacchus Marsh + Melton branding.
replacements = {
    '<title>The Weekend Property Guide | YPA Bacchus Marsh</title>': '<title>The Weekend Property Guide | YPA Bacchus Marsh + Melton</title>',
    'content="The Weekend Property Guide from YPA Bacchus Marsh. Explore this weekend\'s inspections, properties and local opportunities."': 'content="The Weekend Property Guide from YPA Bacchus Marsh + Melton. Explore this weekend\'s inspections, properties and local opportunities."',
    'Weekend Property Guide<br>\n            Bacchus Marsh': 'Weekend Property Guide<br>\n            Bacchus Marsh + Melton',
    'YPA BACCHUS MARSH': 'YPA BACCHUS MARSH + MELTON',
    'YPA Bacchus Marsh': 'YPA Bacchus Marsh + Melton',
    "Your guide to this weekend's properties, inspections and opportunities across Bacchus Marsh and surrounding areas.": "Your guide to this weekend's properties, inspections and opportunities across Bacchus Marsh, Melton and surrounding areas.",
    'our team understands the Bacchus Marsh market and the people who live in it.': 'our team understands the Bacchus Marsh and Melton markets and the communities we serve.',
}
for old, new in replacements.items():
    text = text.replace(old, new)

# Replace the previous agent directory with authoritative team data and blank photo slots.
agent_script = r'''<script id="agent-tabs-script">
(function(){
    const directory = [
        {
            name:"Costa Rodriguez",
            role:"Senior Property Consultant/Auctioneer",
            mobile:"0484 134 841",
            profile:"https://www.ypa.com.au/costa-rodriguez/698142"
        },
        {
            name:"Mark Edwards",
            role:"Property Consultant/Auctioneer",
            mobile:"0422 017 068",
            profile:"https://www.ypa.com.au/mark-edwards/656854"
        },
        {
            name:"Ryan Anders",
            role:"Sales Manager",
            mobile:"0434 900 300",
            profile:"https://www.ypa.com.au/ryan-anders/656856",
            assistant:{name:"Cheyenne Kollar", mobile:"0484 385 522"}
        },
        {
            name:"Ricky Frew",
            role:"Sales Consultant/Auctioneer",
            mobile:"0402 007 100",
            profile:"https://www.ypa.com.au/ricky-frew/656868"
        },
        {
            name:"Jodi Nash",
            role:"Sales Manager",
            mobile:"0419 342 120",
            profile:"https://www.ypa.com.au/jodi-nash/656704"
        },
        {
            name:"Shane O'Brien",
            role:"Sales Manager",
            mobile:"0431 766 082",
            profile:"https://www.ypa.com.au/shane-obrien/656695",
            assistant:{name:"Katelyn Taylor", mobile:"0411 800 780"}
        },
        {
            name:"Cory Cassar",
            role:"Property Consultant",
            mobile:"0422 765 386",
            profile:"https://www.ypa.com.au/cory-cassar/708559"
        },
        {
            name:"Kate McGlone",
            role:"Sales Team Leader/OIEC",
            mobile:"0401 853 244",
            profile:"https://www.ypa.com.au/kate-mcglone/656859",
            assistant:{name:"Ryan Fernandes", mobile:"0422 298 811"}
        },
        {
            name:"Vickie Ramon",
            role:"Director",
            mobile:"0403 194 621",
            profile:"https://www.ypa.com.au/vickie-ramon/656693"
        }
    ];

    function phoneHref(phone){
        return String(phone || '').replace(/[^0-9+]/g,'');
    }

    function renderProfile(index){
        const person = directory[index] || directory[0];
        document.querySelectorAll('.agent-tab').forEach((tab,i) => {
            tab.classList.toggle('active', i === index);
            tab.setAttribute('aria-selected', i === index ? 'true' : 'false');
        });

        const profile = document.getElementById('agentProfile');
        if(!profile) return;

        const assistant = person.assistant ? `
            <div class="agent-assistant-block">
                <div class="agent-assistant-label">Sales Assistant</div>
                <div class="agent-assistant-name">${esc(person.assistant.name)}</div>
                <a class="agent-assistant-phone" href="tel:${phoneHref(person.assistant.mobile)}">${esc(person.assistant.mobile)}</a>
            </div>
        ` : '';

        profile.innerHTML = `
            <div class="agent-profile-photo agent-profile-photo-empty" aria-label="Photo space for ${esc(person.name)}"></div>
            <div class="agent-profile-copy">
                <div class="agent-profile-kicker">YPA Bacchus Marsh + Melton</div>
                <div class="agent-profile-name">${esc(person.name)}</div>
                <div class="agent-profile-role">${esc(person.role)}</div>
                <a class="agent-profile-phone" href="tel:${phoneHref(person.mobile)}">${esc(person.mobile)}</a>
                ${assistant}
            </div>
            <div class="agent-profile-actions">
                <a class="agent-appraisal-btn" href="${esc(person.profile)}" target="_blank" rel="noopener">Request Appraisal</a>
            </div>
        `;
    }

    function buildTabs(){
        const tabs = document.getElementById('agentTabs');
        if(!tabs) return;
        tabs.innerHTML = directory.map((person,index) => `
            <button type="button" class="agent-tab ${index === 0 ? 'active' : ''}" role="tab" aria-selected="${index === 0 ? 'true' : 'false'}" data-agent-index="${index}">${esc(person.name)}</button>
        `).join('');
        tabs.addEventListener('click', event => {
            const button = event.target.closest('.agent-tab');
            if(!button) return;
            renderProfile(Number(button.dataset.agentIndex || 0));
        });
        renderProfile(0);
    }

    window.refreshAgentDirectory = function(){
        const active = Array.from(document.querySelectorAll('.agent-tab')).findIndex(tab => tab.classList.contains('active'));
        renderProfile(active >= 0 ? active : 0);
    };

    if(document.readyState === 'loading'){
        document.addEventListener('DOMContentLoaded', buildTabs);
    }else{
        buildTabs();
    }

    const originalRenderAgents = window.renderAgents;
    if(typeof originalRenderAgents === 'function'){
        window.renderAgents = function(){
            originalRenderAgents();
            window.refreshAgentDirectory();
        };
    }
})();
</script>'''

text, count = re.subn(r'<script id="agent-tabs-script">.*?</script>', agent_script, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit('Could not replace agent-tabs-script')

# Add CSS for blank headshot area, assistant details and itinerary sharing.
extra_css = r'''
<style id="joint-team-share-style">
.agent-profile-photo-empty{
    display:block;
    background:#F2F6F9;
    border:1px dashed #B8C8D5;
    box-shadow:inset 0 0 0 6px #FFFFFF;
}
.agent-assistant-block{
    margin-top:16px;
    padding:12px 14px;
    background:#F2F6F9;
    border:1px solid #E0E8EF;
    border-radius:10px;
    width:max-content;
    max-width:100%;
}
.agent-assistant-label{
    color:#7B8DA0;
    font-size:9px;
    font-weight:800;
    letter-spacing:1.1px;
    text-transform:uppercase;
}
.agent-assistant-name{
    margin-top:3px;
    color:#07354D;
    font-size:12px;
    font-weight:800;
}
.agent-assistant-phone{
    display:inline-block;
    margin-top:3px;
    color:#63758A;
    font-size:11px;
}
.weekend-share-btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:7px;
    margin-top:12px;
    border:1px solid #07354D;
    background:#FFFFFF;
    color:#07354D;
    border-radius:8px;
    padding:10px 13px;
    font-size:10px;
    font-weight:800;
    letter-spacing:.8px;
    text-transform:uppercase;
    transition:.2s ease;
}
.weekend-share-btn:hover{
    background:#07354D;
    color:#FFFFFF;
}
.drawer-share-btn{
    width:100%;
    margin:-8px 0 20px;
    border:1px solid #C8D4E0;
    background:#FFFFFF;
    color:#07354D;
    border-radius:8px;
    padding:13px;
    font-size:10px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
}
.share-status{
    margin-top:8px;
    min-height:16px;
    color:#63758A;
    font-size:10px;
}
@media(max-width:800px){
    .agent-assistant-block{width:100%;}
}
</style>
'''
text = text.replace('</head>', extra_css + '\n</head>', 1)

# Sharing uses the saved property IDs in a URL and imports them automatically for recipients.
share_script = r'''
<script id="weekend-sharing-script">
(function(){
    const PARAM = 'weekend';

    function importedWeekendIds(){
        try{
            const raw = new URL(window.location.href).searchParams.get(PARAM);
            if(!raw) return [];
            return raw.split('~').map(value => decodeURIComponent(value)).map(normaliseId).filter(Boolean);
        }catch(error){
            return [];
        }
    }

    function buildShareUrl(){
        const url = new URL(window.location.href);
        const ids = weekendIds.map(normaliseId).filter(Boolean);
        if(ids.length){
            url.searchParams.set(PARAM, ids.map(encodeURIComponent).join('~'));
        }else{
            url.searchParams.delete(PARAM);
        }
        url.hash = 'my-weekend';
        return url.toString();
    }

    function setShareStatus(message){
        document.querySelectorAll('.share-status').forEach(node => {
            node.textContent = message || '';
        });
    }

    window.shareWeekendItinerary = async function(){
        if(!weekendIds.length){
            setShareStatus('Save at least one property first.');
            return;
        }

        const url = buildShareUrl();
        const shareData = {
            title:'My YPA Weekend Property Itinerary',
            text:'Here is my YPA Bacchus Marsh + Melton weekend property itinerary.',
            url
        };

        try{
            if(navigator.share){
                await navigator.share(shareData);
                setShareStatus('Itinerary shared.');
                return;
            }
            if(navigator.clipboard && navigator.clipboard.writeText){
                await navigator.clipboard.writeText(url);
                setShareStatus('Share link copied.');
                return;
            }
            window.prompt('Copy this itinerary link:', url);
            setShareStatus('Share link ready.');
        }catch(error){
            if(error && error.name === 'AbortError') return;
            window.prompt('Copy this itinerary link:', url);
        }
    };

    function addShareControls(){
        const summary = document.querySelector('.weekend-summary');
        if(summary && !summary.querySelector('.weekend-share-btn')){
            summary.insertAdjacentHTML('beforeend', `
                <button type="button" class="weekend-share-btn" onclick="shareWeekendItinerary()">Share My Weekend</button>
                <div class="share-status" aria-live="polite"></div>
            `);
        }

        const route = document.querySelector('.drawer-body .route-btn');
        if(route && !document.querySelector('.drawer-share-btn')){
            route.insertAdjacentHTML('afterend', `
                <button type="button" class="drawer-share-btn" onclick="shareWeekendItinerary()">Share This Itinerary</button>
                <div class="share-status" aria-live="polite"></div>
            `);
        }
    }

    const imported = importedWeekendIds();
    if(imported.length){
        weekendIds = imported;
        saveWeekendIds();
    }

    if(document.readyState === 'loading'){
        document.addEventListener('DOMContentLoaded', addShareControls);
    }else{
        addShareControls();
    }
})();
</script>
'''
text = text.replace('</body>', share_script + '\n</body>', 1)

path.write_text(text, encoding='utf-8')
print('Applied joint branding, authoritative agent directory, blank photo slots and itinerary sharing.')

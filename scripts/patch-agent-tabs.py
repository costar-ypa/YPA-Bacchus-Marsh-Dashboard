from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''
<style id="agent-tabs-style">
/* Weekend contrast on light palette */
.weekend-section .weekend-title,
.weekend-section .weekend-summary strong{
    color:#07354D !important;
}

/* Agent tab directory */
.agent-directory{
    margin-top:8px;
}

.agent-tabs{
    display:flex;
    gap:8px;
    overflow-x:auto;
    padding:2px 2px 12px;
    scrollbar-width:thin;
}

.agent-tab{
    flex:0 0 auto;
    border:1px solid #C8D4E0;
    background:#FFFFFF;
    color:#52677D;
    border-radius:10px;
    padding:11px 15px;
    font-size:11px;
    font-weight:800;
    letter-spacing:.35px;
    transition:.2s ease;
    white-space:nowrap;
}

.agent-tab:hover{
    border-color:#86A9C3;
    color:#07354D;
    background:#F7FAFC;
}

.agent-tab.active{
    background:#07354D;
    color:#FFFFFF;
    border-color:#07354D;
}

.agent-profile{
    display:grid;
    grid-template-columns:auto 1fr auto;
    align-items:center;
    gap:28px;
    padding:30px;
    margin-top:10px;
    background:#FFFFFF;
    border:1px solid #D9E2EC;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(15,52,77,.06);
}

.agent-profile-photo,
.agent-profile-initials{
    width:92px;
    height:92px;
    border-radius:50%;
    object-fit:cover;
    flex:0 0 92px;
}

.agent-profile-initials{
    display:grid;
    place-items:center;
    background:#E8F0F6;
    color:#07354D;
    font-family:Montserrat,sans-serif;
    font-size:26px;
    font-weight:800;
}

.agent-profile-kicker{
    color:#D7B400;
    font-size:10px;
    font-weight:800;
    letter-spacing:1.6px;
    text-transform:uppercase;
}

.agent-profile-name{
    margin-top:5px;
    color:#07354D;
    font-family:Montserrat,sans-serif;
    font-size:28px;
    font-weight:800;
    letter-spacing:-1px;
}

.agent-profile-role{
    margin-top:5px;
    color:#63758A;
    font-size:13px;
}

.agent-profile-phone{
    display:inline-block;
    margin-top:10px;
    color:#07354D;
    font-size:12px;
    font-weight:700;
}

.agent-assistant{
    margin-top:16px;
    display:inline-flex;
    align-items:center;
    gap:8px;
    padding:8px 11px;
    border-radius:9px;
    background:#F2F6F9;
    color:#52677D;
    font-size:11px;
}

.agent-assistant strong{
    color:#07354D;
}

.agent-appraisal-btn{
    min-width:190px;
    border:1px solid #07354D;
    background:#07354D;
    color:#FFFFFF;
    border-radius:9px;
    padding:13px 18px;
    font-size:10px;
    font-weight:800;
    letter-spacing:1px;
    text-transform:uppercase;
    text-align:center;
    transition:.2s ease;
}

.agent-appraisal-btn:hover{
    background:#FFD600;
    border-color:#FFD600;
    color:#07354D;
}

/* Keep the old data-driven agent grid available to JS but out of view. */
#agents.agents{
    display:none !important;
}

@media(max-width:800px){
    .agent-profile{
        grid-template-columns:auto 1fr;
        gap:18px;
        padding:22px;
    }

    .agent-profile-actions{
        grid-column:1/-1;
    }

    .agent-appraisal-btn{
        display:block;
        width:100%;
    }

    .agent-profile-photo,
    .agent-profile-initials{
        width:74px;
        height:74px;
    }
}
</style>
'''

if 'id="agent-tabs-style"' not in s:
    s = s.replace('</head>', css + '\n</head>', 1)

old = '''    <div class="agents" id="agents">\n\n        <div class="loading">\n            Loading team...\n        </div>\n\n    </div>'''
new = '''    <div class="agent-directory" id="agentDirectory">\n        <div class="agent-tabs" id="agentTabs" role="tablist" aria-label="YPA Bacchus Marsh agents"></div>\n        <div class="agent-profile" id="agentProfile"></div>\n    </div>\n\n    <div class="agents" id="agents">\n        <div class="loading">Loading team...</div>\n    </div>'''

if 'id="agentDirectory"' not in s:
    if old not in s:
        raise SystemExit('Agent grid insertion point not found')
    s = s.replace(old, new, 1)

js = r'''
<script id="agent-tabs-script">
(function(){
    const directory = [
        {name:"Costa Rodriguez", role:"Sales Consultant"},
        {name:"Mark Edwards", role:"Sales Consultant"},
        {name:"Ryan Anders", role:"Sales Consultant", assistant:"Cheyanne Kollar"},
        {name:"Ricky Frew", role:"Sales Consultant"},
        {name:"Jodi Nash", role:"Sales Consultant"},
        {name:"Shane O'Brien", role:"Sales Consultant", assistant:"Katelyn Taylor"},
        {name:"Cory Cassar", role:"Sales Consultant"},
        {name:"Kate McGlone", role:"Sales Consultant", assistant:"Ryan Fernandes"},
        {name:"Vickie Ramon", role:"Director"}
    ];

    function initials(name){
        return name.split(/\s+/).filter(Boolean).map(part => part[0]).join('').slice(0,2).toUpperCase();
    }

    function sheetAgent(name){
        if(!Array.isArray(window.homes)) return null;
        return window.homes.find(h => String(h.agent || '').trim().toLowerCase() === name.toLowerCase()) || null;
    }

    function renderProfile(index){
        const person = directory[index] || directory[0];
        const source = sheetAgent(person.name);
        const photo = source && source.agentPhoto ? String(source.agentPhoto) : '';
        const phone = source && source.agentPhone ? String(source.agentPhone) : '';
        const tabs = document.querySelectorAll('.agent-tab');
        tabs.forEach((tab,i) => {
            tab.classList.toggle('active', i === index);
            tab.setAttribute('aria-selected', i === index ? 'true' : 'false');
        });

        const profile = document.getElementById('agentProfile');
        if(!profile) return;

        const image = photo
            ? `<img class="agent-profile-photo" src="${esc(photo)}" alt="${esc(person.name)}" onerror="this.outerHTML='<div class=&quot;agent-profile-initials&quot;>${initials(person.name)}</div>'">`
            : `<div class="agent-profile-initials">${initials(person.name)}</div>`;

        const assistant = person.assistant
            ? `<div class="agent-assistant"><span>Sales Assistant</span><strong>${esc(person.assistant)}</strong></div>`
            : '';

        const subject = encodeURIComponent(`Appraisal Request - ${person.name}`);
        const body = encodeURIComponent(`Hi ${person.name},\n\nI would like to request a property appraisal.\n\nPlease contact me to arrange a suitable time.\n`);

        profile.innerHTML = `
            ${image}
            <div>
                <div class="agent-profile-kicker">YPA Bacchus Marsh</div>
                <div class="agent-profile-name">${esc(person.name)}</div>
                <div class="agent-profile-role">${esc(person.role)}</div>
                ${phone ? `<a class="agent-profile-phone" href="tel:${esc(phone.replace(/\s+/g,''))}">${esc(phone)}</a>` : ''}
                ${assistant}
            </div>
            <div class="agent-profile-actions">
                <a class="agent-appraisal-btn" href="mailto:crodriguez@ypa.com.au?subject=${subject}&body=${body}">Request Appraisal</a>
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
</script>
'''

if 'id="agent-tabs-script"' not in s:
    s = s.replace('</body>', js + '\n</body>', 1)

p.write_text(s, encoding='utf-8')

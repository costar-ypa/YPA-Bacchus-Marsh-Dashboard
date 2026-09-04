from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

new_directory = '''    const directory = [
        {name:"Vickie Ramon", role:"Director", mobile:"0403 194 621", profile:"https://www.ypa.com.au/vickie-ramon/656693"},
        {name:"Ryan Anders", role:"Sales Manager", mobile:"0434 900 300", profile:"https://www.ypa.com.au/ryan-anders/656856", assistant:{name:"Cheyenne Kollar", mobile:"0484 385 522"}},
        {name:"Shane O'Brien", role:"Sales Manager", mobile:"0431 766 082", profile:"https://www.ypa.com.au/shane-obrien/", assistant:{name:"Katelyn Taylor", mobile:"0411 800 780"}},
        {name:"Jodi Nash", role:"Sales Manager", mobile:"0419 342 120", profile:"https://www.ypa.com.au/jodi-nash/"},
        {name:"Kate McGlone", role:"Sales Team Leader/OIEC", mobile:"0401 853 244", profile:"https://www.ypa.com.au/kate-mcglone/656859", assistant:{name:"Ryan Fernandes", mobile:"0422 298 811"}},
        {name:"Costa Rodriguez", role:"Senior Property Consultant/Auctioneer", mobile:"0484 134 841", profile:"https://www.ypa.com.au/costa-rodriguez/698142"},
        {name:"Mark Edwards", role:"Property Consultant/Auctioneer", mobile:"0422 017 068", profile:"https://www.ypa.com.au/mark-edwards/"},
        {name:"Ricky Frew", role:"Sales Consultant/Auctioneer", mobile:"0402 007 100", profile:"https://www.ypa.com.au/ricky-frew/"},
        {name:"Cory Cassar", role:"Property Consultant", mobile:"0422 765 386", profile:"https://www.ypa.com.au/cory-cassar/"}
    ];'''

start = s.find('    const directory = [', s.find('id="agent-tabs-script"'))
if start < 0:
    raise SystemExit('Agent directory start not found')
end = s.find('    ];', start)
if end < 0:
    raise SystemExit('Agent directory end not found')
end += len('    ];')
s = s[:start] + new_directory + s[end:]

# Correct the combined-team label and assistant spelling everywhere in the tab UI.
s = s.replace('YPA Bacchus Marsh agents', 'YPA Bacchus Marsh + Melton agents')
s = s.replace('YPA Bacchus Marsh</div>', 'YPA Bacchus Marsh + Melton</div>')
s = s.replace('Cheyanne Kollar', 'Cheyenne Kollar')

p.write_text(s, encoding='utf-8')

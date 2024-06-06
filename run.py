from pypdf import PdfReader 
import re

# TODO: Change if required
TARGET_FILE = "2022ENGG_CAP1_CutOff.pdf"



SELECTION_PATTERN_INNER_SHORT = "([0-9]{4}) - "
SELECTION_PATTERN_INNER_LONG = "([0-9]{9}) - "
SELECTION_PATTERN_COLLEGE = re.compile(f"{SELECTION_PATTERN_INNER_SHORT}(.+)", re.IGNORECASE)
SELECTION_PATTERN_BRANCH = re.compile(f"{SELECTION_PATTERN_INNER_LONG}(.+)", re.IGNORECASE)
SELECTION_PATTERN_CUTOFF = re.compile(r"\((?P<main>[0-9\.]+[0-9]+)\)(.+)")

CITY_FILTER = [
    'Pune',
    'Mumbai'
]

reader = PdfReader(TARGET_FILE) 
pages_len = len(reader.pages)
print(f"Found {pages_len} pages")
print()

colleges = {}
active = None

for index in range(pages_len):
    page = reader.pages[index]
    
    content = page.extract_text()
    
    for line in content.split('\n'):
        line = line.replace('\n','')

        match = SELECTION_PATTERN_CUTOFF.fullmatch(line)
        if match:
            cutoff = match.groupdict()['main']
            active_branches = colleges[active]['branches']                  
            if active_branches and 'cutoff' not in active_branches[-1]:
                colleges[active]['branches'][-1]['cutoff'] = cutoff
                print('\t^', cutoff)

        if line.__contains__('-') and SELECTION_PATTERN_COLLEGE.fullmatch(line):
            name = re.sub(SELECTION_PATTERN_INNER_SHORT, '', line).strip()
            active = name
            if name not in colleges:
                colleges[name] = dict(branches=[])
            print()
            print('@' + name)
            
        if line.__contains__('-') and SELECTION_PATTERN_BRANCH.fullmatch(line):
            branch = re.sub(SELECTION_PATTERN_INNER_LONG, '', line).strip()
            colleges[active]['branches'].append({'branch':branch})
            print('\t*', branch)


import json

with open('cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(colleges, f, indent=2)
      

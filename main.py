import json
import re
import sys
from datetime import date

today = date.today()
count = 0
with open(sys.argv[1], 'r+') as f:
    content = f.read()
    content_new = re.sub(r'^\/\*\s.*\s\*\/$', ',', content, flags=re.M)

with open('outrundeck.json', 'w') as fh:
    fh.write(content_new)

with open('outrundeck.json', 'r') as read_obj, open('final.json', 'w') as write_obj:
    read_obj.__next__()
    write_obj.write('[\n')
    for line in read_obj:
        write_obj.write(line)

with open('final.json', 'r') as read_obj, open('out.json', 'w') as write_obj:
    for line in read_obj:
        write_obj.write(line)
    write_obj.write(']')

with open('out.json') as f:
    data = json.load(f)

pathfile = 'test_' + str(today) +'-' + str(count) + '.csv'

with open(pathfile, 'a') as g:
    for i in data:
        instructionSetId = i['instructionSetId']
        instruction = i['instruction']
        for j in instruction:
            instructionId = j['instructionId']
        g.write(instructionSetId + ',')
        g.write(instructionId + '\n')
g.close()
count = count + 1



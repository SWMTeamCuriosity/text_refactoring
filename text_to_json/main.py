import os
import json
import unicodedata

address = "./stt_translated"
file = os.listdir(address)
doc = []
num = 0
files = [unicodedata.normalize('NFC', f) for f in os.listdir(u'.')]


for i in file:
    print(type(i))
    if '.txt' in i:
        with open(address + "/" + i, 'r', encoding='utf-8') as file:
            contents = file.readlines()
        contents = ''.join(contents)
        contents = contents.replace("\n", "")
        contents = contents.replace(".", "")
        doc.append( contents)

with open("stt.json", 'w') as f:
    json.dump(doc, f)


#!/usr/bin/python3

from collections import defaultdict
import re, json, sys

with open("figureAndImg.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

def img_search(line, loaded_data):
    """look for the loaded data in each line, if matches, print an additional line to stdout for
    adding a line to the image
    loaded data format looks like 
    [('4.2.2-1', '002'), ('4.2.2-1', '003'), ('4.2.2-2', '004'), ('4.2.2-3', '005'),]
    """
    for i in loaded_data:
        if re.search(i[0]+':',line):
            print(f"![Figure](./38321-g60.files/image{i[1]}.png)\n")

record_list=[]
    # loaded data format looks like 
    # [('4.2.2-1', '002'), ('4.2.2-1', '003'), ('4.2.2-2', '004'), ('4.2.2-3', '005'),]
for i in loaded_data:
    for j in range(len(loaded_data.get(i))):
        record_list +=[(i, loaded_data.get(i)[j])]

for line in sys.stdin:
    img_search (line, record_list)
    print(line.strip())


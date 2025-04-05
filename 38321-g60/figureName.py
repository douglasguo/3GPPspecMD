#!/usr/bin/python3

import sys, re, json
from collections import defaultdict

img_list = []
figureDict = defaultdict(list)

for line in sys.stdin:
    figure = re.search(r'Figure\s(([0-9]\.)+[0-9].*\d)\:', line)
    img = re.search(r'image([0-9]+).png\"></span></p>', line)
    if img != None:
        img_list += [str(img.group(1))]
    if figure != None:
        new_figure_item = str(figure.group(1))
        img_list += [new_figure_item]
        new_figure_item_index = img_list.index(new_figure_item)
        for i in range(0,new_figure_item_index):    
            figureDict[new_figure_item].append(img_list[i])
        img_list=[]

                
with open("figureAndImg.json", "w", encoding="utf-8") as f:
    json.dump(figureDict, f, indent=4) 






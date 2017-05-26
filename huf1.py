#!/usr/bin/python
import heapq

text = 'testowy text'
data = []
tree = {}
print (text)
def uniq(inlist):
    uniques = []
    for item in inlist:
        if item not in uniques:
            uniques.append(item)
    return uniques
#jak czesto pojawa sie dana litera
for i in uniq(text):
    how_often = text.count(i)
    print (data, i, how_often)
    heapq.heappush(data, (how_often, i))

#ulozenie drzwa wg. cxestosci wystepowania
while len(data) > 1:
    symilar1 = heapq.heappop(data)
    symilar2 = heapq.heappop(data)
    tree[symilar1[1]] = symilar1[0]
    heapq.heappush(data, (symilar1[0]+symilar2[0], symilar1[1]+symilar2[1]))

    print (symilar1, symilar2)
#wydruk drzewa
if len(data) > 0:
    symilar1 = heapq.heappop(data)
    tree[symilar1[1]] = symilar1[0]

print (tree)

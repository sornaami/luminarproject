#intersection
#union
#difference

set1={10,11,12,13}
set2={12,13,14,15,16}

unionset=set1.union(set2)
print(unionset)

inter=set1.intersection(set2)
print(inter)

diff=set1.difference(set2) #removing diff element from set1 that is 12,13
print(diff)
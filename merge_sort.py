# Merge sorted arrays

l1 = [1,2,4]

l2 = [1,3,4]


l3 = []

pl1 = 0
pl2 = 0
result = []

while pl1 < len(l1) and pl2 < len(l2):
    print(pl1, pl2)
    if l1[pl1] <= l2[pl2]:
        result.append(l1[pl1])
        pl1 += 1
    else:
        result.append(l2[pl2])
        pl2 += 1

remained = l1[pl1:] + l2[pl2:]
result.extend(remained)

result

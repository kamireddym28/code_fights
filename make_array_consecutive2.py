def makeArrayConsecutive2(statues):
    count = []
    statues.sort()
    for i in range(len(statues)-1):
        diff = statues[i+1]-statues[i]
        count.append(diff-1)
    return sum(count)

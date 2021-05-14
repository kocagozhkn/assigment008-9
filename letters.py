letterToCount = "hippo runs to us!"

countDict = {}
counter = 0

for i in letterToCount:
    for j in range(1, len(letterToCount)):
        if i == letterToCount[j]:
            counter+=1
            countDict[i] = counter
  
    counter = 0
print(countDict)

list1 = []
list2 = []

with open("puzzle1input.txt", "r") as inputfile:
    for line in inputfile:
        loc1, loc2 = map(int, line.split())

        list1.append(loc1)
        list2.append(loc2)

similarityScore = 0

for i in range(len(list1)):
    appearances = list2.count(list1[i])
    similarityScore += list1[i]*appearances

print(similarityScore)

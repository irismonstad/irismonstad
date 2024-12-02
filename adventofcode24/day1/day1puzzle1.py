list1 = []
list2 = []

with open("puzzle1input.txt", "r") as inputfile:
    for line in inputfile:
        loc1, loc2 = map(int, line.split())

        list1.append(loc1)
        list2.append(loc2)

def sort(tall):
    tallKopi = tall[:]
    tallSortert = []

    for i in tall:
        minst = min(tallKopi)
        tallSortert.append(minst)
        tallKopi.remove(minst)

    return tallSortert

sortedlist1 = sort(list1)
sortedlist2 = sort(list2)

totalDistance = 0

for i in range(len(list1)):
    difference = abs(sortedlist1[i]-sortedlist2[i])
    totalDistance += difference

print(totalDistance)

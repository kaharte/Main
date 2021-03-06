#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      katie
#
# Created:     26/01/2016
# Copyright:   (c) katie 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


"""This is the order puzzle solver! Make sure you spell everything correctly
and consistently (caps etc.)!!"""

#make sure you don't have an item called x, make sure you don't have more than 1 of the same item
"""make it so that you can have clues like 'so and so was not third' or 'so and
so was not last' maybe make it so you can just type in the whole clue? (too ambitious?)"""

import numbers

orderList = []
knownItems = {}

listGo = True

while listGo:
    orderList.append(input("Name of thing on list"))
    listYes = input("Are there more items on the list?")
    if listYes.lower() == "no":
        break

print(orderList)

numOrderList = {}

#list of things that are in front of each item
frontList = {}
#find a way to add to lists by checking themselves

#list of things behind each item
behindList = {}

for i in orderList:
    numOrderList[i]= [x for x in range(1, len(orderList) + 1)]
    frontList[i] = []
    behindList[i] = []

print(numOrderList)

def clueFinder():
    thing = input("Which thing on the list does the first clue involve?")
    forBeh = input("Is the next item 'in front of' or 'behind' %s" % (thing))
    thing2 = input("What is %s %s" % (forBeh, thing))
    if forBeh.lower() == 'behind':
        behindList[thing].append(thing2)
        frontList[thing2].append(thing)
        print('%s is behind %s' % (thing2, thing))
        print(numOrderList[thing])
        numOrderList[thing][len(orderList) - 1] = 'x'
        numOrderList[thing2][0] = 'x'
    if forBeh.lower() == "in front of":
        frontList[thing].append(thing2)
        behindList[thing2].append(thing)
        print('%s is in front of %s' % (thing2, thing))
        numOrderList[thing][0] = 'x'
        numOrderList[thing2][len(orderList) - 1] = 'x'
    print(numOrderList)

def horizontalCheck():
    #below is the check to see if an item only has one possible position
    for i in numOrderList:
        appendTo = i
        if numOrderList[i].count('x') == len(orderList) - 1:
            print("the position of %s has been determined" % (i))
            for k in numOrderList[i]:
                if k == 'x':
                    pass
                else:
                    knownPosition = k
                    knownItems[appendTo] = knownPosition
                    #below is the check to see if other items are in the known position
                    for l in numOrderList:
                        if l != i:
                            for m in numOrderList[l]:
                                if m == knownPosition:
                                    numOrderList[l][m - 1] = 'x'
            print("%s is in position %s" % (i, knownPosition))

#check to see if a certain position is eliminated for all but one item
def verticalCheck():
    #cycles through positions
    for i in range(0, len(orderList)):
        #print("i = ", i),
        total = 0
        #counts how many items have an x for a certian position
        for k in numOrderList:
            #print("k = ", k)
            if numOrderList[k][i] == 'x':
                total += 1
            else:
                tempKnown = k #tempKnown is the item that the postition has been found out for
        #gives knownPosition if only one item has that position
        if total == len(orderList) - 1:
            knownPosition = i + 1
            knownItems[tempKnown] = knownPosition
            print("knownPosition = ", knownPosition)
            for l in numOrderList:
                if l == tempKnown:
                    for m in numOrderList[l]:
                        if m != knownPosition:
                            if m != 'x':
                                numOrderList[l][m-1] = 'x'
            print("%s is in position %s" % (tempKnown, knownPosition))

def clueResubmit():
    for i in frontList:
        thing = i
        listy = numOrderList[i]
        filteredList = [x for x in listy if isinstance(x, numbers.Number)]
        print(filteredList)
        if i not in knownItems:
            print(i)
            frontPosition = min(filteredList)
            print(frontPosition)
            backPosition = max(filteredList)
            print(backPosition)
            for j in frontList[i]:
                print(j)
                thing2 = j
                if j not in knownItems:
                    print(numOrderList[thing])
                    print(numOrderList[thing2])
                    numOrderList[thing][frontPosition - 1] = 'x'
                    numOrderList[thing2][backPosition - 1] = 'x'
                    print(numOrderList[thing])
                    print(numOrderList[thing2])

def frontBehindCheck():
    for i in frontList:
        tempFrontThings = []
        tempBehindThings = []
        for j in behindList:
            if i == j:
                for k in frontList[i]:
                    tempFrontThings.append(k)
                for l in behindList[i]:
                    tempBehindThings.append(l)
                for m in tempFrontThings:
                    for n in tempBehindThings:
                        if n not in behindList[m]:
                            behindList[m].append(n)
                for p in tempBehindThings:
                    for q in tempFrontThings:
                        if q not in frontList[p]:
                            frontList[p].append(q)

#check this dicitonary with frontlist and behindlist

while True:
    clueFinder()
    horizontalCheck()
    horizontalCheck()
    verticalCheck()
    horizontalCheck()
    horizontalCheck()

    """horizontalCheck()
    horizontalCheck()
    verticalCheck()
    horizontalCheck()
    horizontalCheck()
    verticalCheck()
    verticalCheck()"""
    clueYes = input("Are there any more clues?")
    if clueYes == 'no':
        break

clueResubmit()
horizontalCheck()
horizontalCheck()
verticalCheck()
horizontalCheck()
horizontalCheck()
frontBehindCheck()

print(numOrderList)
print(knownItems)
print("FrontList: ", frontList)
print("BehindList: ", behindList)
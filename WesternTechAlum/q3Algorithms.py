
# //Question 3: travel compatibility
# //given a list of strings representing your own travel preferences, 
# //and a list of lists representing each of your friend's preferences, 
# //return the index of the friend who's list has the most items in common w urs
# //ex. ["YYZ, "JFK", "SFO"], [["YXU", "YYZ"], ["SFO, "BOS, "JFK"], ["LGA"]] -> 1

def mostCommonFriendIndex(myList, friendTravelList):
    mostItemNum = 0
    mostItemIndex = -1
    currentItemNum = 0
    myPlaces = {}
    
    #convert my list to dictionary with key
    for place in range(len(myList)):
        myPlaces[myList[place]] = True
    print(myPlaces)

    for i in range(len(friendTravelList)) :
        for j in range(len(friendTravelList[i])) :
            if myPlaces.get(friendTravelList[i][j]) :
                currentItemNum+=1

        if currentItemNum > mostItemNum : 
            mostItemNum = currentItemNum
            mostItemIndex = i

        currentItemNum = 0

    return mostItemIndex



print(mostCommonFriendIndex(["YYZ", "JFK", "SFO"],[["YXU", "YYZ"], ["SFO", "BOS", "JFK"], ["LGA"]]))
print(mostCommonFriendIndex(["YVR"], [["A"], ["B"], ["LGA"]]))
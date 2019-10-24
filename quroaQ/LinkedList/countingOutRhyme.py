# A number of people are standing ina  circle getting ready to play an elimination game
# there are initially n people in the circle, and the game involces counting around the 
# circle of remaining people, eliminating every kth person. Once someone is eliminated, the 
# counting restarts with th enext person in the circle. The game continues until only one person remains

# given n and k, task is return an array of ints representing the indicees of people in the 
# order they will be eliminated (indices are 1-based)

# for n = 5 and k = 3, output should be countingOutRhyme(n, k) = [3, 1, 5, 2], k and n are at least 1

#create a linkedList to the nth element -> nth element should link back to head ref
#peopleLeft to keep track of num of people left
# if peopleLeft == 1, return arr
# loop through linkedlist, when count = k-1, ListNode.next = ListNode.next.next, peopleLeft-=1

#O(N) runtime 
#pattern  - if an element needs to loop back, use linkedlist
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def countingOutRhyme(n, k):
    gamePlayers = ListNode(0)
    head = gamePlayers
    peopleLeft = n
    count = 0
    results = []

    for i in range(1, n+1):
        gamePlayers.next = ListNode(i)
        gamePlayers = gamePlayers.next
    head = head.next
    gamePlayers.next = head
    tracker = head

    while peopleLeft > 1:
        count +=1
        if count == k - 1:
            results.append(tracker.next.val)
            tracker.next = tracker.next.next
            peopleLeft -=1
            count = 0
        tracker = tracker.next
    return results

    #[[], 2, [], 4, []]
    # for n = 5 and k = 3, output should be countingOutRhyme(n, k) = [3, 1, 5, 2], k and n are at least 1

print(countingOutRhyme(5, 3))
print(countingOutRhyme(8, 2))



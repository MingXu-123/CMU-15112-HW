#################################################
# Hw7
# Your andrewID:mxu2
# Your section: 2N
#################################################
import time

"""
# 1A: This function just exchange the first and the last
# element of a list
def slow1(lst): # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop()    # O(1)
    b = lst.pop(0)   # O(N)
    lst.insert(0, a) # O(N)
    lst.append(b)    # O(1)
# 1B: O(N)

def fast1(lst):
    assert(len(lst) >= 2)
    lst[0],lst[-1] = lst[-1],lst[0] #O(1)

# 1D: O(1)


# 2A: This function returns how many different numbers in a list
def slow2(lst): # N is the length of the list lst
    counter = 0                   # O(1)
    for i in range(len(lst)):     # Loops N times
        if lst[i] not in lst[:i]: # O(N**2)
            counter += 1          # O(1)
    return counter                # O(1)
    
# 2B: O(N**3)


def fast2(lst):
    a = set(lst) #O(N)
    return len(a) #O(1)
    
# 2D: O(N)


# 3A: This function returns a letter (lowercase) in a string,
# which appears the most number of times.
# If two letter's appear frequency is equal, return
# the smaller letter

import string
def slow3(s): # N is the length of the string s
    maxLetter = ""                              # O(1)
    maxCount = 0                                # O(1)
    for c in s:                                 # Loops N times
        for letter in string.ascii_lowercase:   # Loops O(1) == 26 times
            if c == letter:                     # O(1)
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and \
                   c < maxLetter:               # O(N)
                    maxCount = s.count(c)       # O(N)
                    maxLetter = c               # O(1)
    return maxLetter                            # O(1)
# 3B: O(N**2)


def fast3(s):
    maxLetter = ""  #O(1)
    maxCount = 0  #O(1)
    d = dict()  #O(1)
    for c in s:  # Loop O(N)
        if c.islower(): # O(1)
            if c not in d: 
                d[c] = 1
            else:
                d[c] += 1
    for char in d:  # Loop O(N)
        if d[char] > maxCount or d[char] == maxCount and \
         char < maxLetter:  #O(1)
            maxCount = d[char] #O(1)
            maxLetter = char #O(1)
    return maxLetter #O(1)
    
# 3D: O(N)


# 4A: This function return the maximum value
# of difference of values in two lists
def slow4(a, b): # a and b are lists with the same length N
    assert(len(a) == len(b))
    result = abs(a[0] - b[0])    # O(1)
    for c in a:                  # Loops N times
        for d in b:              # Loops N times
            delta = abs(c - d)   # O(1)
            if (delta > result): # O(1)
                result = delta   # O(1)
    return result                # O(1)
    
# 4B: O(N**2)

def fast4(a, b):
    minOfa = min(a) #O(N)
    maxOfa = max(a) #O(N)
    minOfb = min(b) #O(N)
    maxOfb = max(b) #O(N)
    delta1 = abs(maxOfa - minOfb) #O(1)
    delta2 = abs(maxOfb - minOfa) #O(1)
    if delta1 > delta2: #O(1)
        return delta1 #O(1)
    else:
        return delta2 #O(1)
    
# 4D: O(N)
"""


# This is the function of checking whether it
# # contains Pythagorean Triple
def containsPythagoreanTriple(lst):
    lst.sort()
    for i in range(len(lst) - 2):
        a = lst[i]**2
        b = lst[i + 1]**2
        c = a + b
        if c**0.5 in lst[i + 2: len(lst)]:
            return True
        else:
            continue
    return False




def getPairSum(lst, target):
    if len(lst) <= 1:
        return None
    s = set()
    for i in range(len(lst)):
        b = target - lst[i]
        if b in s: # b has been seen before
            return(b, lst[i])
        else:
            s.add(lst[i])
    return None


# this is a helper function to swap number in list
def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])


# this function is the algorithm of selection sort list
def instrumentedSelectionSort(lst):
    start = time.time()
    n = len(lst)
    numOfComparisons = 0
    numOfSwaps = 0
    for startIndex in range(n):
        minIndex = startIndex
        for i in range(startIndex + 1, n):
            numOfComparisons += 1
            if (lst[i] < lst[minIndex]):
                minIndex = i
        swap(lst, startIndex, minIndex)
        numOfSwaps += 1
    end = time.time()
    timeToRun = (end - start) / 1  # millisecond
    return (numOfComparisons, numOfSwaps, timeToRun)


# this function is the algorithm of bubble sort list
def instrumentedBubbleSort(lst):
    start = time.time()
    n = len(lst)
    end = n
    numOfComparisons = 0
    numOfSwaps = 0
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end):
            numOfComparisons += 1
            if (lst[i - 1] > lst[i]):
                swap(lst, i - 1, i)
                numOfSwaps += 1
                swapped = True
        end -= 1
    end = time.time()
    timeToRun = (end - start) / 1  # millisecond
    return (numOfComparisons, numOfSwaps, timeToRun)


# This function return a random generating list
def getARandomList():
    import random
    result = []
    lenOflist = 1000
    for i in range(lenOflist):
        result.append(random.randint(0, 50))  # generate random number
    return result


# This function generate a random list
def generateARandomList():
    import random
    result = []
    lenOflist = 500
    for i in range(lenOflist):
        result.append(random.randint(0, 100))  # generate random number
    return result


# This is a helper function for selectionSortVersusBubbleSort
def verifyBigO(l1, l2):
    import math
    timeToRun3 = instrumentedSelectionSort(l1)[2]
    timeToRun4 = instrumentedSelectionSort(l2)[2]
    print("For function instrumentedSelectionSort, "
          "when the len of list is N the runtime is " + str(timeToRun3))
    print("For function instrumentedSelectionSort, "
          "when the len of list is 2N the runtime is " + str(timeToRun4))
    print("The ratio of runtime of len2N / that of lenN is " +
          str(math.ceil(timeToRun4 / timeToRun3)) +
          ". So verified it is a O(N**2)")
    timeToRun5 = instrumentedBubbleSort(l1)[2]
    timeToRun6 = instrumentedBubbleSort(l2)[2]
    print("For function instrumentedBubbleSort, "
          "when the len of list is N the runtime is " + str(timeToRun5))
    print("For function instrumentedBubbleSort, "
          "when the len of list is 2N the runtime is " + str(timeToRun6))
    print("The ratio of runtime of len2N / that of lenN is " +
          str(math.ceil(timeToRun6 / timeToRun5)) +
          ". So verified it is a O(N**2)")


# this function print the report of comparing the above two sorting algorithms
def selectionSortVersusBubbleSort():
    lst = getARandomList()
    l1 = generateARandomList()  # list for checking O(N**2)
    l2 = generateARandomList()*2
    verifyBigO(l1, l2)
    (numOfComparisons1, numOfSwaps1, timeToRun1) = \
        instrumentedSelectionSort(lst)
    (numOfComparisons2, numOfSwaps2, timeToRun2) = \
        instrumentedBubbleSort(lst)
    if numOfComparisons1 < numOfComparisons2:
        print("The function instrumentedSelectionSort() uses fewer"
              " comparisons")
    else:
        print("The function instrumentedBubbleSort() uses fewer comparisons")
    if numOfSwaps1 < numOfSwaps2:
        print("The function instrumentedSelectionSort() makes fewer swaps")
    else:
        print("The function instrumentedBubbleSort() makes fewer swaps")
    if timeToRun1 < timeToRun2:
        print("The function instrumentedSelectionSort() runs in less time")
    else:
        print("The function instrumentedBubbleSort() runs in less time")


# this is the function that report the information of the movie awards
def movieAwards(oscarResults):
    d = dict()
    movieNames = []
    for awards in oscarResults:
        movieNames.append(awards[1])
    for movieName in movieNames:
        if movieName not in d:
            d[movieName] = 1
        else:
            d[movieName] += 1
    return d  # this is the dictionary of the award


# this function return a dict of friends of friends
def getFriendsOfFriends(friend, d):
    return d[friend]


# this function return friends of my friends
def friendsOfMyFriend(myself, myfriends, d):
    lstOfFriendsOfMyFriend = []
    for friend in myfriends:
        lstOfFriendsOfMyFriend += list(getFriendsOfFriends(friend, d))
    setOfFriendsOfMyFriend = set(lstOfFriendsOfMyFriend)
    if myself in setOfFriendsOfMyFriend:
        setOfFriendsOfMyFriend.remove(myself)
    for myFriend in myfriends:
        if myFriend in setOfFriendsOfMyFriend:
            setOfFriendsOfMyFriend.remove(myFriend)
    return setOfFriendsOfMyFriend


# This is the main function of friends of friends
def friendsOfFriends(d):
    result = dict()
    for c in d:
        myself = c
        myFriends = d[c]
        setFriendsOfFriends = friendsOfMyFriend(myself, myFriends, d)
        result[myself] = setFriendsOfFriends
    return result


#################################################
# The following are test cases for this homework
#################################################

def testContainsPythagoreanTriple():
    print("Testing testContainsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]) == True)
    assert(containsPythagoreanTriple([1, 3, 6, 2, 1, 4]) == False)
    print("passed!")


def testGetPairSum():
    print("Testing testGetPairSum()...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [(5, 2), (2, 5)])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in\
        [(10, -8), (-8, 10), (-1, 3), (3, -1), (1, 1)])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    print("passed!")


def testMovieAwards():
    print("Testing testMovieAwards()...", end="")
    assert(movieAwards({
    ("Best Picture", "Green Book"),
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
    }) == {
    "Black Panther" : 2,
    "Bohemian Rhapsody" : 3,
    "The Favourite" : 1,
    "Green Book" : 1,
    "Roma" : 1
    })
    print("passed!")


def testFriendsOfFriends():
    print("Testing testFriendsOfFriends()...", end="")
    d = {}
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    assert(friendsOfFriends(d) == {
    'tyrion': {'arya', 'brienne'},
    'pod': {'jon'},
    'brienne': {'tyrion'},
    'arya': {'tyrion'},
    'jon': {'pod', 'jaime'},
    'jaime': {'pod', 'jon'},
    'ramsay': set()
    })
    print("Passed!")


# this is the test all function
def testAll():
    testContainsPythagoreanTriple()
    testGetPairSum()
    testMovieAwards()
    testFriendsOfFriends()
    selectionSortVersusBubbleSort()

testAll()


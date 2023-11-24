import matplotlib.pyplot as plt
import pylab
import time
import random

def for_loop(n):
    myList = []
    for i in range(n):
        myList.append(n)
    return myList

def list_comprehension(n):
    return [x for x in range(n)]


# for loop
forLoopX = []
forLoopY = []
for i in range(300):
    amountOfNumbers = random.randint(1_000, 2_000_000)
    start = time.time()
    for_loop(amountOfNumbers)
    end = time.time()
    timeTaken = (end - start)
    forLoopX.append(amountOfNumbers)
    forLoopY.append(timeTaken)


# list comp
listCompX = []
listCompY = []
for i in range(300):
    amountOfNumbers = random.randint(1_000, 2_000_000)
    start = time.time()
    list_comprehension(amountOfNumbers)
    end = time.time()
    timeTaken = (end - start)
    listCompX.append(amountOfNumbers)
    listCompY.append(timeTaken)


plt.scatter(forLoopX,forLoopY, c='b', label='for loop')
plt.scatter(listCompX, listCompY, c='r', label='list comprehension')
plt.legend(loc='upper left')
plt.title("Time Difference Between For Loops and List Comprehension")
plt.xlabel("Number Inputted")
plt.ylabel("Time Taken")
plt.show()
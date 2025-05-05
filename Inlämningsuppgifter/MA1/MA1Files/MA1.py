"""
Solutions to module 1
Student: Alva Christensson
Mail: Alvachristensson03@gmail.com
Reviewed by: Anton
Reviewed date: 2024-09-20
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""

import time
import math

def multiply(m: int, n: int) -> int:  
    #Base cases
    if n == 0 or m==0:
        return 0
    
    #Recursive part
    else:
        return m + multiply(m,n-1)


def harmonic(n: int) -> float:    
    #Base case
    if n < 2:
        return 1
    
    #Recursive part
    else:        
        return 1/n + harmonic(n-1)

def get_binary(x: int) -> str:  
    #Base cases
    if x == 0:
        return '0'
    
    elif x == 1:
        return '1'
    
    #If given numver is negative
    elif x < 0:
        return '-' + get_binary(-x)
    
    #Recursive part
    else:
        return get_binary(x//2) + str(x%2)

def reverse_string(s: str) -> str:     
    """Reverses the string"""   
    #Base case 
    if len(s) < 2:
        return s
    
    #Recursive part, breaking down the problem and rebuilding
    else:
        return  reverse_string(s[1:]) + s[0]

def largest(a: iter):                     
    """ Returns the largest element in a"""
    #Base case
    if len(a) == 1:
        return a[0]
    
    #Får inte vara innan basfallet och måste vara en variabel för annars blir det oändligt med rekursioner
    LargestNumber = largest(a[1:]) 

    #Cheks if 
    if a[0] < LargestNumber:
        return LargestNumber

    else: 
        return a[0]



def count(x, s: list) -> int:                
    """ Counts the number of occurences of x on all levels in s"""
    Counter = 0
    #Base cases
    if len(s) < 1:
        return 0

    elif s[0] == x:
        Counter += 1

    #Checks if element is an list and recursives on it
    if type(s[0]) == list:
        Counter += count(x,s[0])

    #Checks if list is empty
    if len(s[1:]) > 0:
        Counter += count(x,s[1:])

    return Counter    

def bricklek(startPos: str, finalPos: str, middlePos: str, n: int) -> str:  
    """ Returns a string of instruction how to move the tiles """
    Instructions = []
    #Base case
    if n== 0:
        return []
    
    else:
        #Moves all the bricks from the startin position to the middle position with
        # the final position as middleground, except the final brick
        Instructions += bricklek(startPos,middlePos,finalPos,n-1)

        #The largest brick is moved to the final position
        Instructions.append(startPos + "->" + finalPos)

        #All the bricks in the middle position is moved to the final position with
        #the start position as middleground, except the final brick
        Instructions += bricklek(middlePos, finalPos, startPos, n-1)


    return Instructions



def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    print('\nCode that demonstates my implementations\n')
    #exercise 9

    measuredTime = []

    print(f"Theoretical growthfactor: {1.618}")
    #Calulates time for fib(30) and adds it to the first position in measuredTime
    tstart = time.perf_counter()
    fib(30)
    tstop = time.perf_counter()
    measuredTime.append(tstop - tstart)
    j=0

    #Compares fib(n) with f(n-1) for n between 30 and 35
    for i in range(31,36):
        j +=1
        tstart = time.perf_counter()
        fib(i)
        tstop = time.perf_counter()
        measuredTime.append(tstop - tstart)
        print(f"Measured time for fib({i}): {round(tstop - tstart,2)} seconds")
        print(f"Measured growthfactor: {measuredTime[j]/measuredTime[j-1]}")
        print("-----")

    #from V1.04 we know that t(n)=c*1.618^n, we also know from above that t(35)=3.62, which gives us c=1.756*10^(-7)
    def estimatedTime(n):
        return 1.756e-7*1.618**n

    print(f"Estimated time for fib(50): {time.strftime('%H hours and %M minutes', time.gmtime(estimatedTime(50)))}")
    print(f"Estimated time for fib(100): {round(estimatedTime(100)// (365.25*24 * 3600*100),-3)} centuries")


    #Exercise 10
    memory = {0:0, 1:1}

    def fib_mem(n):
        if n not in memory:
            memory[n] = fib_mem(n-1) + fib_mem(n-2)
        return memory[n]

    tstart = time.perf_counter()
    fib_mem(100)
    tstop = time.perf_counter()
    print(f"Measured time for fib_mem({100}): {round(tstop - tstart,5)} seconds")
    print(f"fib_mem({100}): {fib_mem(100)} ")


    #EXERCISE 11

    #from V1.05 we know that t(n)=c*nlog(n), we also know from above that t(1000)=1, which gives us c=1/3*10e-3
    def estimatedTimeMergeSort(n):
        return 1/3*1e-3*n*math.log(n)

    #from V1.05 we know that t(n)=c*n^2, we also know from above that t(1000)=1, which gives us c=10e-6
    def estimatedTimeStickSort(n):
        return 1e-6*n**2

    print("-- n=10e6 --")
    print(f"Estimated time for merge sort: {round(estimatedTimeMergeSort(1e6)/(3600),3)} hours")
    print(f"Estimated time for stick sort: {round(estimatedTimeStickSort(1e6)/(24*3600),1)} days")

    print("-- n=10e9 --")
    print(f"Estimated time for merge sort: {round(estimatedTimeMergeSort(1e9)/(24*3600),3)} days")
    print(f"Estimated time for stick sort: {round(estimatedTimeStickSort(1e9)/(24*3600*365.25))} years")

    print('\n\nCode for analysing fib and fib_mem\n')


print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
    From example 11: 2^50 -1 seconds or around 36 million years
  
  Exercise 9: Time for Fibonacci:
    1 hour and 22 minutes for fib(50)
    44000 centuries
  
  Exercise 10: Time for fib_mem:
    0.23 ms
  
  Exercise 11: Comparison sorting methods:
    -- n=10e6 --
    Estimated time for merge sort: 1.279 hours
    Estimated time for stick sort: 11.6 days
    -- n=10e9 --
    Estimated time for merge sort: 79.95 days
    Estimated time for stick sort: 31 688 years
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
    A, size n problem take n seconds => ta(n)=n
    B, size n problem takes cnlog(n) => tb(a)=cnlog(n), where t(10)=1 gives c = 10^-1
    When is A faster then B, precisly when they are equal. ta(n)=tb(n) => n=cnlog(n) => n=10^10
  
  
"""

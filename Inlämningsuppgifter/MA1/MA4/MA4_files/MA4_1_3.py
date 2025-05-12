
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 

    return  

def hypersphere_exact(n,d):
    return

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     #using multiprocessor to perform 10 iterations of volume function  
     return 

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
     return 

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    for y in range (10):
        sphere_volume(n,d)


if __name__ == '__main__':
	main()

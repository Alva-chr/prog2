
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

from math import gamma, pi
import random 
from time import perf_counter as pc
import concurrent.futures as future

def sphere_volume(n, d, R=1):    
    def point_inside(point):
        if sum(x**2 for x in point) < R:
            return True
        else:
            return False

    rand = lambda x: random.uniform(-x,x)


    lst_cord = [[rand(R) for i in range(d)] for j in range(n)]
    
    n_c = len(list(filter(point_inside,lst_cord)))

    V = (2*R)**d*(n_c/n)

    return V

def hypersphere_exact(n,d,r=1):
    return (pi**(d/2))/(gamma(d/2+1))*(r**d)

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,R=1): 

    with future.ProcessPoolExecutor(max_workers=10) as ex:
        work = [ex.submit(sphere_volume,n,d,R) for j in range(10)]

        average_volume = sum(f.result() for f in work)/len(work)

    return average_volume


def insides(d,R,n):
    rand = lambda x: random.uniform(-x,x)
    n = int(n)
    n_c = 0
    for j in range(n):
        point = [rand(R) for i in range(d)]

        if sum(x**2 for x in point) < R*R:
            n_c += 1
    
    return n_c

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,R=1):
    N = n/10

    divides = [N for i in range(10)]

    with future.ProcessPoolExecutor(max_workers=10) as ex:
        divides_work = [ex.submit(insides, d, R, n_sample) for n_sample in divides]

        total_inside = sum(f.result() for f in divides_work)

    V = (2*R)**d*(total_inside/n)

    return V  

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    R=1
    volume = 0
    
    start = pc()
    for y in range (10):
        volume += sphere_volume(n,d)
    end = pc()

    print(f"Process took {round(end-start,2)} seconds for non parallel programming with n=10^5")
    print(f"Average volume: {volume/10}")

    start = pc()
    volume = sphere_volume_parallel1(n,d,R)
    end = pc()

    print(f"Process took {round(end-start,2)} seconds for parallel programming with n=10^5")
    print(f"Average volume: {volume}")

    start = pc()
    volume = sphere_volume(n*10,d,R)
    end = pc()

    print(f"Process took {round(end-start,2)} seconds for parallel programming with n=10^6")
    print(f"Average volume: {volume}")

    start = pc()
    volume = sphere_volume_parallel2(n*10,11)
    end = pc()
    print(f"Process took {round(end-start,2)} seconds for split data")
    print(f"Average volume: {volume}")

if __name__ == '__main__':
	main()

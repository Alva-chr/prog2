
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

from math import gamma, pi
import random 
import numpy as np

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

def hypersphere_exact(d,r=1):
    return (pi**(d/2))/(gamma(d/2+1))*(r**d)
     
def main():
    n = [100000,100000]
    d = [2,11]

    for i,j in zip(n,d):
        print(f"Approx volume: {sphere_volume(i,j)}")
        print(f"Exact volume {hypersphere_exact(j)}")


if __name__ == '__main__':
	main()


"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt 
from math import sqrt, pi

def approximate_pi(n):
    x_c = []
    y_c = []
    n_c = 0
    
    x_s = []
    y_s = []
    n_s = 0

    for i in range(n):
        x = r.uniform(-1,1)
        y = r.uniform(-1,1)

        distance = sqrt(x*x+y*y)

        if distance < 1:
            x_c.append(x)
            y_c.append(y)
            n_c +=1

        else:
            x_s.append(x)
            y_s.append(y)
            n_s +=1
    plt.figure(figsize=(10,10))
    plt.scatter(x_c, y_c, color = "red")
    plt.scatter(x_s,y_s, color="blue")
    plt.savefig(f"circleplot{n}.png")

    print(f"Number of points in circle: {n_c}")
    print(f"Pi is approx: {4*n_c/(n)}" )
    print(f"Pi is given as: {pi}")
    return 4/(n)
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()

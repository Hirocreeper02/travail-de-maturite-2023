#f = open("values/noms/personnages/noms.txt", "r")

#print(f.read())

# create a Perlin texture in 2D

import numpy as np
import matplotlib.pyplot as plot

def perlin(x, y, seed=0):

    np.random.seed(seed)
    ptable = np.arange(256, dtype=int)

    np.random.shuffle(ptable)

    ptable = np.stack([ptable, ptable]).flatten()
    
    xi, yi = x.astype(int), y.astype(int)
   
    xg, yg = x - xi, y - yi
    
    xf, yf = fade(xg), fade(yg)
   
    n00 = gradient(ptable[ptable[xi] + yi], xg, yg)
    n01 = gradient(ptable[ptable[xi] + yi + 1], xg, yg - 1)
    n11 = gradient(ptable[ptable[xi + 1] + yi + 1], xg - 1, yg - 1)
    n10 = gradient(ptable[ptable[xi + 1] + yi], xg - 1, yg)

    x1 = lerp(n00, n10, xf)
    x2 = lerp(n01, n11, xf)  
    return lerp(x1, x2, yf)  

def lerp(a, b, x):
    "linear interpolation i.e dot product"
    return a + x * (b - a)

def fade(f):
    
    return 6 * f**5 - 15 * f**4 + 10 * f**3

def gradient(c, x, y):
   
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
    gradient_co = vectors[c % 4]
    return gradient_co[:, :, 0] * x + gradient_co[:, :, 1] * y

lin_array = np.linspace(1, 10, 500, endpoint=False)

x, y = np.meshgrid(lin_array, lin_array)  

plot.imshow(perlin(x, y, seed=2), origin = 'upper')

plot.show()

#import glob

#print(glob.glob('values/*.txt'))

#print("\033[1;36m ========================================\033[0;37m")

#https://iq.opengenus.org/perlin-noise/
#f = open("values/noms/personnages/noms.txt", "r")

#print(f.read())


import random

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}
 
#res = key, val = random.choice(list(test_dict.items()))
res = random.choice(list(test_dict.items()))
# printing result
print("The random pair is : ", test_dict[res[0]])




#import glob

#print(glob.glob('values/*.txt'))

#print("\033[1;36m ========================================\033[0;37m")

#https://iq.opengenus.org/perlin-noise/
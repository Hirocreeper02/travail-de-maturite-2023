#f = open("values/noms/personnages/noms.txt", "r")

#print(f.read())


import os

path ="values"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    print(name)




#import glob

#print(glob.glob('values/*.txt'))

#print("\033[1;36m ========================================\033[0;37m")

#https://iq.opengenus.org/perlin-noise/
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:49:27 2019

@author: Januaty Halim
"""

#%%
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
s = file.read()
print(s[2])
#%%
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
file.readline()
print(file.readline(), end="")
#%%
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
for line in file: 
    print(line[0], end="")
#%%5
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
s = file.read()
xlist = s.split()
print(xlist[1])
#%% 6
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
s = file.read()
xlist = s.split('\n')
print(xlist[1])
#%% 7
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
xlist = file.readlines()
ylist = file.readlines()
print(len(xlist), len(ylist))
#%% 8
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
xlist = file.readlines()
file.seek(0)
ylist = file.readlines()
print(len(ylist), len(ylist))
#%% 9
file = open("C:/Users/Januaty Halim/Desktop/calvin/foo.txt", "r")
for x in file.readline(): 
    print(x, end=":")
#%%
    file = open("out.txt", "w")
s = "this"
print(s, "is a test", file=file)
file.close()
#%% 11
file = open("out.txt", "w")
s = "this"
file.write(s, "is a test")
file.close()
#%% 12
file = open("out.txt", "w")
s = "this"
file.write(s + "is a test")
file.close()
#%%13
file = open("out.txt", "w")
s = "this"
file.write("{} {}\n".format(s, "is a test"))
file.close() 
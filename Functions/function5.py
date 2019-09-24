#create anagram
#%% anagram mr,stavin using "sorted"
def check(s1,s2):
    if (sorted(s1)==sorted(s2)):
        print("it is an anagram.")
    else:
        print("it is NOT an anagram.")
#%%
def anagram(s1,s2):
    strings = {}
    strings2 = {}
    for x in strings:
        if x in strings:
            strings[x] += 1
        else:
            strings[x] = 1
    for x in strings2:
        if x in strings2:
            strings2[x] += 1
        else:
            strings2[x] = 1
            
    return strings == strings2

print(anagram("michael","lemicha"))
        
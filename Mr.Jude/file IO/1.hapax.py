#%%
import re

path = "C:/Users/Januaty Halim/Desktop/Mr.Jude/File IO/Queen of Austria.txt"
def hapax(file):
    file = open(path,encoding="UTF-8")
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print(word)
hapax(path)
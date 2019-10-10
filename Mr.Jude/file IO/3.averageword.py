#%%
import re
path = "C:/Users/Januaty Halim/Desktop/Mr.Jude/File IO/Queen of Austria.txt"
def averageword(filename):
    counts = {}
    file = open(path,encoding="UTF-8")
    for x in re.findall("[a-z]+", file.read().lower()):
        counts[x] = counts.get(x, 0) + 1
    total = 0
    totalwords = 0
    for key, val in counts.items():
        total += len(key)*val
        totalwords += val
    return total/totalwords


print(averageword(path))


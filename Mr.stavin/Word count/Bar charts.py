#%%homework
1. able to input string from a file
(file is plaintext, and directory is pre-defined)

2.make it looks decent (change it to make it cooler)
(scale the range, change the bar color, rotate it, and give it proper title for the charts and axis)

3.sort it from the highest(can use library)
#%%
import matplotlib.pyplot as plt
filename = "Indonesia.txt"
with open(filename,'r') as f:
    for line in f:
        string = str(line)
        list_string = line.split()
        dict_string = {}
        
for x in list_string:
    if x in dict_string:
        dict_string[x] = dict_string[x] + 1
    else:
        dict_string[x] = 1

count_list = dict_string.values()
indentation = dict_string.keys()
sortedIndentation = [words for frequency, words in sorted(zip(count_list, indentation))]
fig = plt.figure(dpi =100, figsize =(13,5))
plt.barh(sortedIndentation,sorted(count_list),color="red",edgecolor="blue")
plt.title("Word Count",fontsize = 20)
plt.xticks(range(1,11))
plt.xlabel("Frequency",fontsize= 16,color = "red")
plt.ylabel("Word",fontsize =16,color ="red")
plt.show()

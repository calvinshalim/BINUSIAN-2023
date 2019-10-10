#%%
import re
def splitter(filename):
    with open(filename,"r") as f:
        filecontent = f.read()
    sentences = re.sub(r"\n","",filecontent)
    sentences = re.sub(r"(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])",r".n\n\1",sentences)
    sentences = re.sub(r"!\s","!\n", sentences)
    sentences = re.sub(r"\?\s","?\n",sentences)
    print(sentences)
    
splitter("C:/Users/Januaty Halim/Desktop/Mr.Jude/File IO/splitter.txt")
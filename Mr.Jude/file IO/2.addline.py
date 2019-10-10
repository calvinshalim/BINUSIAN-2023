#%%
def addline(input_txt,output_txt):
    out = ""
    num = 1
    for line in open(input_txt):
        out = out + f"{num} | {line}"
        num = num + 1
    with open(output_txt,"w+") as handler:
        handler.write(out)

addline("C:/Users/Januaty Halim/Desktop/Mr.Jude/File IO/input.txt", "C:/Users/Januaty Halim/Desktop/Mr.Jude/File IO/output2.txt")


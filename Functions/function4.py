#%%function 4
def count(char):
    strings = {}
    for x in z:
        try:
            strings[x] += 1
        except KeyError:
            strings[x] = 1
    for data in strings:
        print(f"{data} = {strings[data]}")
z = input("message?:")
count(z)
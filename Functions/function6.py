#%% anagram w/out using "sorted() or dict"{}"
def isanagram(first,second):
    if len(first) == len(second):
        for chars in first:
            if chars in second:
                second.replace(chars,"")
            else:
                return False
        return True
    return False

print(isanagram("michael","limache"))
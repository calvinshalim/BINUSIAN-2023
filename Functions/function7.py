#%% task convert roman number to arabic number and vice versa
# limit 20
def int_to_roman(num):
    val = [10, 9, 5, 4, 1]
    syb = ["X", "IX", "V", "IV","I"]
    roman_num = ""
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
#%%
def roman_to_int(num):
       rom_val = {"I": 1, "V": 5, "X": 10}
       i = 0
       for a in range(len(num)):
           if a > 0 and rom_val[num[a]] > rom_val[num[a - 1]]:
               i += rom_val[num[a]] - 2 * rom_val[num[a - 1]]
           else:
               i += rom_val[num[a]]
       return i
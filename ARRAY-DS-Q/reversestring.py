# strings = 'Abcdefghijklmnopqrstuvwxyz'
# sl = len(strings)
# print(sl)

# print(strings[::-1],end="\nslicing\n")

# rev = strings.reverse()

# print(rev)

def toreverse(stt):
    
    if type(stt) != type('abhi'):
        
        return 'its not a string'
    elif len(stt) == 0:
        return 'Its a empty string'
    return stt[::-1]

backup = toreverse([1,3,9])
print(backup)



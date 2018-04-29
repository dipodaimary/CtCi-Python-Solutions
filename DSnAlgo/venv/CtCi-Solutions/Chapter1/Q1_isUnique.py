def isUnique(str):
    if len(str)>128:
        return False
    char_set = [False for _ in range(128)]
    for char in str:
        val = ord(char)
        if(char_set[val]):
            #char already in string
            return False
        char_set[val]=True
    return True

print(isUnique("dipodaimary"))
print(isUnique("dipo"))

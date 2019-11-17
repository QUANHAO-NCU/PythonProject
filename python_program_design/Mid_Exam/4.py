string = input()
key = int(input())
base_lo = ord('a')
base_up = ord('A')
new_string = ''
for i in string:
    if (i.isalpha()):
        i = ord(i)
        if(i>64 and i<91):
            i = base_up+(i-base_up + key+26)%26
        else:
            i = base_lo + (i - base_lo + key + 26) % 26
        i = chr(i)
    new_string += i
print(new_string)

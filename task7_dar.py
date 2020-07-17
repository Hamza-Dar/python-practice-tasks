seq= input("Enter comma seperated words: ")

s= seq.split(',')
s.sort()
print(s)
for i in range(0,len(s)):
    if(i!=len(s)-1):
        print(s[i]+',', end='')
    else:
        print(s[i], end='')


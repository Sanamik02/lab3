n = input()
d = len(n)//2

res = True
for i in range(0, d):
     if n[i] != n[-i-1]:
        res = False
        break

if res != True: 
    print("NO")

else: print("YES") 
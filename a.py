n= input()


for i in range(0, len(n)//2):
   if n[i] != n[-i-1]:
       ans = False
       break

if ans != True:
     print("NO")
else: print("YES") 
n = input()

s = len(n)

for i in range(s//2):
    if n[i] != n[-1-i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")
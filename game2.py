n = int(input())
makc = 0
for i in range(n):
    a = int(input())
    if a % 10 == 3 and a > makc:
        makc = a
print(makc)



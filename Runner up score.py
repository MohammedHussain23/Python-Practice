n = int(input())
arr = map(int, input().split())
arr = list(arr)
maxi = max(arr)
# print(maxi)
j = []
for i in arr:
    if i != maxi:
        j.append(i)
j.sort()
print(j[-1])

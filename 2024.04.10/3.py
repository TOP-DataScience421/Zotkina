k = int(input())
n = 1
r = []
while n <= k:
  if k % n == 0:
    r.append(n)
  n = n + 1
print(sum(r))

#50
#93
def uniqueE(L):
  a=[i for i in L if L.count(i)==1]
  return(sorted(a))
L = [int(i) for i in input().split()]
print(uniqueE(L))
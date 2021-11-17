A=set(input('introduceti multimea:'))
B=set(input('introduceti multimea:'))
a=set()
b=set()
for i in A :
    if (ord(str(i))>=65 and ord(str(i))<=90):
        a.add(str(i))
for j in B:
    if (ord(str(j))>=65 and ord(str(j))<=90):
        b.add(str(j))     
print('intersectia multimilor este',a.intersection(b))
print('reuniunea multimilor este',a.union(b))
print('diferenta multimilor(A-B) este',a.difference(b))
print('diferenta multimilor(B-A) este',a.difference(b))
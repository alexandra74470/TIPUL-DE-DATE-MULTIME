A=set(input('introduceti multimea:'))
B=set(input('introduceti multimea:'))
a=set()
b=set()
for i in A :
    if (ord(str(i))>=48 and ord(str(i))<=57):
        a.add(int(i))
for j in B:
    if (ord(str(j))>=48 and ord(str(j))<=57 ):
        b.add(int(j))       
print('intersectia multimilor este',a.intersection(b))
print('reuniunea multimilor este',a.union(b))
print('diferenta multimilor(A-B) este',a.difference(b))
print('diferenta multimilor(B-A) este',a.difference(b))
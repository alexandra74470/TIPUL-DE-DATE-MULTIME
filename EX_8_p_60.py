A=set(input('introduceti multimea:'))
B=set(input('introduceti multimea:'))
#intersectia multimilor A si B
print('intersectia multimilor este',A.intersection(B))
#reuniunea multimilor A si B
print('reuniunea multimilor este',A.union(B))
#diferenta multimilor A si B
print('diferenta multimilor(A-B) este',A.difference(B))
print('diferenta multimilor(B-A) este',B.difference(A))
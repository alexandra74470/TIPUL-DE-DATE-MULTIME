A=set(input('introdueti primul sir de caractere'))
B=set(input('introduceti  al doilea sir de caractere'))
print('a.caractere care se intilnesc cel putin in unul dintre siruri:',A.union(B))
print('b.caractere care se intilnesc in ambele siruri:',A.intersection(B))
print('c.caractere care apar in primul si nu apar in al doile:',A.difference(B))
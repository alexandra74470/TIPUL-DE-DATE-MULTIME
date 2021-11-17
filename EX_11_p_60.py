A={'A','B','C','D'}
B=[[]]
for a in A:
    B+=[b + [a] for b in B]
print(B)
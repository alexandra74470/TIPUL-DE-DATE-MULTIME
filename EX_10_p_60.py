A={1,2,3,4}
B=[[]]
for a in A:
    B+=[b + [a] for b in B]
print(B)
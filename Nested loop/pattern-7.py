for r in range(4):
    for c in range (4,r,-1):
        print(c,end=' ')
    print()

#oneliner
for r in range(4): print(*range(4, r, -1))
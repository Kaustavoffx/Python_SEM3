for r in range(1,10,2):
    for c in range(1,r,2):
        print(c,end=' ')
    print()

#oneliner
for r in range(1, 10, 2): print(*(range(1, r, 2)))
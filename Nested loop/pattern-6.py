n=5
sp=round(n/2)*2
for r in range (0,n,2):
    for c in range (0,sp+1):
        print(end=' ')
    for c in range(0,r+1):
        print('*',end=' ')
    sp-=2
    print()


#oneliner
for r in range(0, 5, 2): print(' ' * (6 - r) + '* ' * (r + 1))
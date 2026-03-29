n=20
for i in range (1,11):
    print(' '*n,end=' ')
    print('* '*(i))
    n-=1

#oneliner
for i in range(1, 11): print(' ' * (20 - i) + '* ' * i)

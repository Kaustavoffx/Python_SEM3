for r in range (1,6):
    for c in range (5,r,-1):
        print('*', end='')
    print()

#oneliner 
print('\n'.join('*' * i for i in range(4, 0, -1)))

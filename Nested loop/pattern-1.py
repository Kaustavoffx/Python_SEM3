for i in range (1,6):
    for c in range(1,i):
        print('*',end='')
    print()


# Oneliner
print('\n'.join('*' * i for i in range(5)))


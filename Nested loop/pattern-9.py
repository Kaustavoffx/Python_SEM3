res=input("do you want to try the oneliner or normal ? (one/nor/code) :")

if (res=="one"):
    #oneliner 
    for i in range(-2, 3): print(' ' * abs(i) + '* ' * (3 - abs(i)))


    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-9.py

        """)
    
elif (res=="nor") :
    n = 3 # Top half + middle = 3 lines
    sp = n - 1

    # Upper half (3 lines: 1, 2, 3 stars)
    for r in range(0, n):
        for c in range(0, sp):
            print(end=' ')
        for c in range(0, r + 1):
            print('*', end=' ')
        sp -= 1
        print()

    # Lower half (2 lines: 2, 1 stars)
    sp = 1
    for r in range(n - 1, 0, -1):
        for c in range(0, sp):
            print(end=' ')
        for c in range(0, r):
            print('*', end=' ')
        sp += 1
        print()

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-9.py

        """)
    
elif (res=="code"):
    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-9.py

        """)
    
else :
    print("Bye Bye")
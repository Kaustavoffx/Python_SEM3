res=input("do you want to try the oneliner or normal ? (one/nor/code) :")

if (res=="one"):
    #oneliner
    for i in range(1, 11): print(' ' * (20 - i) + '* ' * i)

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-4.py

        """)
    
elif (res=="nor") :
    n=20
    for i in range (1,11):
            print(' '*n,end=' ')
            print('* '*(i))
            n-=1

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-4.py

        """)
    
elif (res=="code"):
    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-4.py

        """)
    
else :
    print("Bye Bye")
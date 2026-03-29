res=input("do you want to try the oneliner or normal ? (one/nor/code) :")

if (res=="one"):
    #oneliner 
    print('\n'.join('*' * i for i in range(4, 0, -1))) 

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-2.py

        """)
    
elif (res=="nor") :
    for r in range (1,6):
        for c in range (5,r,-1):
            print('*', end='')
        print()

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-2.py

        """)
    
elif (res=="code"):
    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-2.py

        """)
    
else :
    print("Bye Bye")
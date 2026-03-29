res=input("do you want to try the oneliner or normal ? (one/nor/code) :")

if (res=="one"):
    #oneliner
    for r in range(1, 10, 2): print(*(range(1, r, 2)))

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-5.py

        """)
    
elif (res=="nor") :
    for r in range(1,10,2):
        for c in range(1,r,2):
            print(c,end=' ')
        print()

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-5.py

        """)
    
elif (res=="code"):
    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-5.py

        """)
    
else :
    print("Bye Bye")
res=input("do you want to try the oneliner or normal ? (one/nor/code) :")

if (res=="one"):
    #oneliner
    for i in range(1, 7): print('1' * i)

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-8.py

        """)
    
elif (res=="nor") :
    n=1
    for r in range (6):
        print(n)
        n=10*n+1

    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-8.py

        """)
    
elif (res=="code"):
    print ("""
    -------------------------------------------------------------------------------------------------------------------
        Check out the code here:
        ↓↓↓
        https://github.com/Kaustavoffx/Python_SEM3/blob/c3638097bc9868912aec0db9ce5f3123021de96b/Nested%20loop/pattern-8.py

        """)
    
else :
    print("Bye Bye")
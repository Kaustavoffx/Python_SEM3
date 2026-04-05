import webbrowser

def open_pattern9_link():
    # Updated dictionary with your links for pattern-9.py
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Nested%20loop/pattern-9.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Nested%20loop/pattern-9.py"
    }

    # Loop keeps asking until the user provides a valid answer
    while True:
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening the {res} version in your web browser...")
            webbrowser.open(url) 
            break 
            
        elif res == "run":
            print("\n--- Running Pattern 9 (Diamond) ---\n")
            
            # Your exact pattern-9 code execution
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
                
            print("\n-------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter exactly 'one', 'code', or 'run'.\n")

# Run the function
open_pattern9_link()
import webbrowser

def open_factorial_link():
    # Dictionary with the GitHub URLs for factorial
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Series/factorial.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Series/factorial.py"
    }

    # Keep asking until they give a valid answer
    while True:
        # Prompt updated to include the 'run' option
        res = input("Do you want to try the oneliner, normal, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version in your web browser...")
            webbrowser.open(url) 
            break
            
        elif res == "run":
            print("\n--- Running Factorial Calculation ---\n")
            
            # Your exact factorial code execution
            try:
                n = int(input("Enter a number: "))
                f = 1
                for i in range(1, n + 1):
                    f *= i
                print(f"Factorial of {n} is {f}")
            except ValueError:
                print("❌ Please enter a valid integer.")
                
            print("\n-------------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter exactly 'one', 'code', or 'run'.\n")

# Run the function
open_factorial_link()
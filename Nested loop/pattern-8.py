import webbrowser

def open_pattern8_link():
    # Dictionary updated with the pattern-8.py URLs
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Nested%20loop/pattern-8.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Nested%20loop/pattern-8.py"
    }

    # Loop keeps asking until the user provides a valid answer
    while True:
        # Prompt updated to include the 'run' option
        res = input("Do you want to try the oneliner, normal, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening the {res} version in your web browser...")
            
            # Directly opens the link in your default browser
            webbrowser.open(url) 
            break 
            
        elif res == "run":
            print("\n--- Running Pattern 8 ---\n")
            
            # Your exact pattern-8 code execution
            n = 1
            for r in range(6):
                print(n)
                n = 10 * n + 1
                
            print("\n-------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter exactly 'one', 'code', or 'run'.\n")

# Run the function
open_pattern8_link()
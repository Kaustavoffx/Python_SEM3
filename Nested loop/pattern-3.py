import webbrowser

def open_pattern3_link():
    # Dictionary updated with the pattern-3.py URLs
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Nested%20loop/pattern-3.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Nested%20loop/pattern-3.py"
    }

    # Keep asking until the user provides a valid answer
    while True:
        # Prompt updated to include the 'run' option
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening the {res} version in your web browser...")
            
            # Directly opens the link in your default browser
            webbrowser.open(url) 
            break 
            
        elif res == "run":
            print("\n--- Running Pattern 3 ---\n")
            
            # Your exact pattern-3 code execution
            for i in range(1, 11):
                print('' * -1, end='') 
                print('* ' * i)
                
            print("\n-------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter exactly 'one', 'code', or 'run'.\n")

# Run the function
open_pattern3_link()
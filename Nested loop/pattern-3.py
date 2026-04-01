import webbrowser

def open_pattern3_link():
    # Dictionary updated with the pattern-3.py URLs
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Nested%20loop/pattern-3.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Nested%20loop/pattern-3.py"
    }

    # Keep asking until the user provides a valid answer
    while True:
        res = input("Do you want to try the oneliner or normal? (one/code): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening the {res} version in your web browser...")
            
            # Directly opens the link in your default browser
            webbrowser.open(url) 
            break 
            
        else:
            print("❌ Invalid input. Please enter exactly 'one' or 'code'.\n")

# Run the function
open_pattern3_link()
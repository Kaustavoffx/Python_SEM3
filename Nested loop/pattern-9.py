import webbrowser

def open_pattern9_link():
    # Updated dictionary with your new links for pattern-9.py
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Nested%20loop/pattern-9.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Nested%20loop/pattern-9.py"
    }

    # Loop keeps asking until the user provides a valid answer
    while True:
        res = input("Do you want to try the oneliner or normal? (one/code): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening the {res} version in your web browser...")
            
            # This directly opens the link in Chrome, Edge, Safari, etc.
            webbrowser.open(url) 
            break # Exits the loop once the link is opened
            
        else:
            print("❌ Invalid input. Please enter exactly 'one' or 'code'.\n")

# Run the function
open_pattern9_link()
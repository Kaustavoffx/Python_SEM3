import webbrowser

def open_github_link():
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/873b44d9779a2c456f9c3cc3d599da24b830ce6c/Series/factorial.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/978fe4a37df2969d4f2695ab2d45f16cb8026d7a/Series/factorial.py"
    }

    # Keep asking until they give a valid answer
    while True:
        res = input("Do you want to try the oneliner or normal? (one/code): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version in your web browser...")
            
            # This is the magic line that actually opens the link!
            webbrowser.open(url) 
            break
            
        else:
            print("❌ Invalid input. Please enter exactly 'one' or 'code'.\n")

# Run the function
open_github_link()
import webbrowser
import os

def open_rectangle_link():
    # Update these with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/36ecb4aee42fdf24cb3eca4f2eb88d3dcf8765c3/Series/P3-Rectangle%20area.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/rectangle.py"
    }

    while True:
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version...")
            # Try standard browser, then fallback to Termux
            if not webbrowser.open(url):
                os.system(f"termux-open {url}")
            break
            
        elif res == "run":
            print("\n--- Rectangle Area Calculation ---\n")
            try:
                # Your exact rectangle logic
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                
                area = length * width
                
                print(f"\nArea of rectangle: {area} unit²")
                
            except ValueError:
                print("❌ Error: Please enter valid numerical values.")
                
            print("\n----------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_rectangle_link()
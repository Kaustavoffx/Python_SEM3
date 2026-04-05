import webbrowser
import os

def open_circle_link():
    # Replace these placeholders with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/circle.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/circle.py"
    }

    while True:
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version...")
            # Try standard browser first, fallback to Termux command
            if not webbrowser.open(url):
                os.system(f"termux-open {url}")
            break
            
        elif res == "run":
            print("\n--- Circle Calculations ---\n")
            try:
                # Your exact circle logic
                radius = float(input("Enter radius of the circle: "))
                pi = 3.1416
                
                circumference = 2 * pi * radius
                area = pi * radius**2
                
                print(f"Circumference of circle: {circumference:.4f} unit")
                print(f"Area of circle: {area:.4f} unit²")
                
            except ValueError:
                print("❌ Error: Please enter a valid numerical value for the radius.")
                
            print("\n--------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_circle_link()
import webbrowser
import os
import math  # Importing math to use the sqrt function

def open_heron_link():
    # Update these with your actual GitHub links
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/herons_formula.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/herons_formula.py"
    }

    while True:
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version...")
            if not webbrowser.open(url):
                os.system(f"termux-open {url}")
            break
            
        elif res == "run":
            print("\n--- Triangle Area (Heron's Formula) ---\n")
            try:
                a = float(input("Enter length of side A: "))
                b = float(input("Enter length of side B: "))
                c = float(input("Enter length of side C: "))

                # Check if it's a valid triangle (Triangle Inequality Theorem)
                if (a + b > c) and (a + c > b) and (b + c > a):
                    s = (a + b + c) / 2
                    
                    # Correct Heron's Formula: Adding the Square Root
                    area_squared = (s * (s - a) * (s - b) * (s - c))
                    area = math.sqrt(area_squared)
                    
                    print(f"\nSemi-perimeter (s): {s}")
                    print(f"Area of the triangle: {area:.2f} unit²")
                else:
                    print("\n❌ Error: Those sides cannot form a triangle!")
                
            except ValueError:
                print("❌ Error: Please enter valid numbers.")
                
            print("\n---------------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_heron_link()
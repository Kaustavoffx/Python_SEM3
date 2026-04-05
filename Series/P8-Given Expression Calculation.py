import webbrowser
import os

def open_expression_link():
    # Update these with your actual GitHub links for expression.py
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/expression.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/expression.py"
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
            print("\n--- Solving: 5x³ + 6y² + 2xy + 9z ---\n")
            try:
                x = float(input("Enter value of x: "))
                y = float(input("Enter value of y: "))
                z = float(input("Enter value of z: "))

                # Calculation based on your logic
                # Note: **3 is cube, **2 is square
                result = 5*x**3 + 6*y**2 + 2*x*y + 9*z 

                print(f"\nResult of the Expression 5x³ + 6y² + 2xy + 9z is: {result:.4f}")
                
            except ValueError:
                print("❌ Error: Please enter valid numerical values.")
                
            print("\n-------------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_expression_link()
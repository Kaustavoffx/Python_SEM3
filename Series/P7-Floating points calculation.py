import webbrowser
import os

def open_calculator_link():
    # Update these with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/calculator.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/calculator.py"
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
            print("\n--- Basic Arithmetic Calculator ---\n")
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))

                add = n1 + n2
                sub = n1 - n2
                mul = n1 * n2
                
                # Handling the division carefully
                if n2 != 0:
                    div = n1 / n2
                    div_display = f"{div:.4f}"
                else:
                    div_display = "Undefined (Cannot divide by zero)"

                print(f"""
Results:
----------
Addition:       {add}
Subtraction:    {sub}
Multiplication: {mul}
Division:       {div_display}
""")
                
            except ValueError:
                print("❌ Error: Please enter valid numerical values.")
                
            print("----------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_calculator_link()
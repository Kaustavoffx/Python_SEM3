import webbrowser
import os

def open_sum_link():
    # Placeholder URLs - update these with your actual GitHub links if you have them!
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/sum.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/sum.py"
    }

    while True:
        res = input("Do you want to try the oneliner, Source code, or run the code? (one/code/run): ").strip().lower()
        
        if res in links:
            url = links[res]
            print(f"Opening {res} version...")
            # This logic works for both PC and Termux (if termux-api is installed)
            if not webbrowser.open(url):
                os.system(f"termux-open {url}")
            break
            
        elif res == "run":
            print("\n--- Running Summation ---\n")
            try:
                # Fixed labels so the user knows which number they are entering
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                c = float(input("Enter third number: "))

                total = a + b + c
                # Using an f-string for a cleaner output
                print(f"\nSum = {total}")
            except ValueError:
                print("❌ Error: Please enter valid numbers (integers or decimals).")
                
            print("\n-------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_sum_link()
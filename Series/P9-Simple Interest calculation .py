import webbrowser
import os

def open_si_link():
    # Update these with your actual GitHub links for simple_interest.py
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/simple_interest.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/simple_interest.py"
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
            print("\n--- Simple Interest Calculator ---\n")
            try:
                p = float(input("Enter the principal amount: "))
                r = float(input("Enter rate of interest per year (%): "))
                t = float(input("Enter the time (in years): "))

                # The formula: I = (P * R * T) / 100
                simple_interest = (p * t * r) / 100
                total_amount = p + simple_interest

                print(f"\nSimple Interest: {simple_interest:.2f} Rupees")
                print(f"Total Amount (P + SI): {total_amount:.2f} Rupees")
                
            except ValueError:
                print("❌ Error: Please enter valid numerical values.")
                
            print("\n----------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_si_link()
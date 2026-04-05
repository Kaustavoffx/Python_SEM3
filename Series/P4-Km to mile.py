import webbrowser
import os

def open_km_to_miles_link():
    # Update these with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/main/Basic/km_to_miles.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/km_to_miles.py"
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
            print("\n--- Kilometers to Miles Converter ---\n")
            try:
                # Your exact logic
                km = float(input("Enter value in kilometers: "))
                miles = km * 0.621371
                
                # Using :.3f to keep the decimal length professional
                print(f"\nDistance in miles: {miles:.3f}")
                
            except ValueError:
                print("❌ Error: Please enter a valid numerical value.")
                
            print("\n-------------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_km_to_miles_link()
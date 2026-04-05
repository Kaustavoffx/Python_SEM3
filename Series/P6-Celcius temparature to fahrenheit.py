import webbrowser
import os

def open_temp_converter_link():
    # Update these with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/36ecb4aee42fdf24cb3eca4f2eb88d3dcf8765c3/Series/P6-Celcius%20temparature%20to%20fahrenheit.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/main/Basic/celsius_to_fahrenheit.py"
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
            print("\n--- Celsius to Fahrenheit Converter ---\n")
            try:
                # Your exact logic
                c = float(input("Enter value in Celsius: "))
                f = (c * 9/5) + 32
                
                print(f"\nTemperature in Fahrenheit: {f:.2f} F")
                
            except ValueError:
                print("❌ Error: Please enter a valid numerical value.")
                
            print("\n--------------------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_temp_converter_link()
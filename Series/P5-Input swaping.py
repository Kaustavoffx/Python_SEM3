import webbrowser
import os

def open_swap_link():
    # Update these with your actual GitHub links when you upload them
    links = {
        "one": "https://github.com/Kaustavoffx/CODE-Oneliner/blob/36ecb4aee42fdf24cb3eca4f2eb88d3dcf8765c3/Series/P5-Input%20swaping.py",
        "code": "https://github.com/Kaustavoffx/CODE-Normal/blob/ae8f13a5d665dfeca297f7ec04d8e155ff68bbe0/Series/P5-Input%20swaping.py"
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
            print("\n--- Swapping Two Numbers ---\n")
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))

                # Your exact swapping logic (The "Temp" Method)
                temp = n1
                n1 = n2
                n2 = temp
                
                # Pro-Tip: In Python, you can also swap in one line without 'temp':
                # n1, n2 = n2, n1

                print(f"\nAfter swapping:")
                print(f"----------")
                print(f"First number: {n1}")
                print(f"Second number: {n2}")
                
            except ValueError:
                print("❌ Error: Please enter valid numerical values.")
                
            print("\n----------------------------")
            break
            
        else:
            print("❌ Invalid input. Please enter 'one', 'code', or 'run'.\n")

# Run the function
open_swap_link()
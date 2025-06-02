from converter import *

def main():
    print("Technical Unit Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Pascal to Bar")
    print("6. Bar to Pascal")
    print("7. Joule to kWh")
    print("8. kWh to Joule")

    choice = input("Choose an option (1-8): ")
    value = float(input("Enter value: "))

    if choice == "1":
        print("Result:", celsius_to_fahrenheit(value))
    elif choice == "2":
        print("Result:", fahrenheit_to_celsius(value))
    elif choice == "3":
        print("Result:", celsius_to_kelvin(value))
    elif choice == "4":
        print("Result:", kelvin_to_celsius(value))
    elif choice == "5":
        print("Result:", pascal_to_bar(value))
    elif choice == "6":
        print("Result:", bar_to_pascal(value))
    elif choice == "7":
        print("Result:", joule_to_kwh(value))
    elif choice == "8":
        print("Result:", kwh_to_joule(value))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

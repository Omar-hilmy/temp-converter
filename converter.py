# Temperature Converter by Omar Hilmy

print("=== Temperature Converter ===")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose 1 or 2: ")
temp = float(input("Enter temperature: "))

if choice == "1":
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result}°F")
elif choice == "2":
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result}°C")
else:
    print("Wrong choice!")

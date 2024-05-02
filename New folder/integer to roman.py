num = int(input("Enter an integer: "))

# Define the symbols and their corresponding values
symbols = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
    1: 'I'
}

# Initialize the result string
roman_numeral = ''

# Iterate through the symbol-value pairs
for value, symbol in symbols.items():
    # Repeat the symbol as many times as possible
    while num >= value:
        roman_numeral += symbol
        num -= value

print(roman_numeral)
    

def max_unique_digit_sum(arr):
    max_sum = -1

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if has_unique_digits(arr[i], arr[j]):
                current_sum = arr[i] + arr[j]
                max_sum = max(max_sum, current_sum)

    return max_sum

def has_unique_digits(num1, num2):
    digits = set()

    for digit in str(num1):
        digits.add(digit)

    for digit in str(num2):
        if digit in digits:
            return False

    return True

# Example usage:
numbers = [12,23,44]
result = max_unique_digit_sum(numbers)

print("Maximum sum of two numbers with unique digits:", result)


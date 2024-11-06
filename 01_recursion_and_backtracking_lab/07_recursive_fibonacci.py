def fibonacci_numbers(number_length: int) -> int:
    old_number = 1
    new_number = 1
    fibonacci_numbers = []

    while len(fibonacci_numbers) < number_length + 1:
        fibonacci_numbers.append(old_number)
        old_number, new_number = new_number, old_number + new_number

    return fibonacci_numbers[number_length]


num = int(input())
print(fibonacci_numbers(num))

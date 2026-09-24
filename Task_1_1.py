def get_valid_number(prompt):

    while True:
        try:
            number = float(input(prompt))
            if 1 <= number <= 100:
                return number
            else:
                print("Помилка: число повинно бути в діапазоні від 1 до 100! Спробуйте ще раз.")
        except ValueError:
            print("Помилка: ви ввели не число! Будь ласка, введіть коректне значення.")


def calculate_x(a, b):

    if a < b:
        x = (b / a) - 1
    elif a == b:
        x = -295
    else:
        x = (a - 235) / b

    return x



print("Розрахунок значення X (Варіант 16)")

a = get_valid_number("Введіть значення a (від 1 до 100): ")
b = get_valid_number("Введіть значення b (від 1 до 100): ")

result_x = calculate_x(a, b)


print(f"\nВведені значення: a = {a}, b = {b}")
print(f"Результат обчислення X = {result_x}")

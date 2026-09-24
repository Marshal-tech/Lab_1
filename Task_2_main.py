import module1
import module2


def main():
    while True:
        print("\nГОЛОВНЕ МЕНЮ")
        print("1. Обчислити вираз ln(x) + cos(y)")
        print("2. Вивести таблицю розмноження амеб")
        print("0. Вийти з програми")

        choice = input("Оберіть дію (0-2): ")

        if choice == '1':
            print("\nОбчислення виразу")
            try:
                x = float(input("Введіть значення x (x > 0): "))
                y = float(input("Введіть значення y: "))

                result = module1.calc_expression(x, y)
                print(f"Результат обчислення: {result}")
            except ValueError:
                print("Помилка: Будь ласка, вводьте лише числа!")

        elif choice == '2':
            print("\nТаблиця розмноження амеб")
            module2.print_amoeba_table()

        elif choice == '0':
            print("\nПрограма завершила роботу. На все добре!")
            break

        else:
            print("\nНекоректний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()

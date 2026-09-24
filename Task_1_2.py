def get_valid_n(prompt):
    while True:
        try:
            n = int(input(prompt))
            if 1 <= n <= 10:
                return n
            else:
                print("Помилка: число повинно бути від 1 до 10! Спробуйте ще раз.")
        except ValueError:
            print("Помилка: ви ввели не ціле число! Спробуйте ще раз.")


def draw_pyramid(n):
    print(f"\n--- Побудова фігури для N = {n} ---\n")

    rows = []
    for i in range(1, n + 1):
        left_part = list(range(1, i + 1))
        right_part = list(range(i - 1, 0, -1))

        row_numbers = left_part + right_part
        row_str = " ".join(map(str, row_numbers))
        rows.append(row_str)

    max_width = len(rows[-1])

    for row in rows:
        print(row.center(max_width))

    for row in reversed(rows[:-1]):
        print(row.center(max_width))
    print("\n")


if __name__ == "__main__":
    N = get_valid_n("Введіть ціле число N (від 1 до 10) для побудови піраміди: ")

    draw_pyramid(N)
s

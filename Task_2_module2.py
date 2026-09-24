def print_amoeba_table():
    print("\n" + "=" * 35)
    print(f"{'Час (год)':^15} | {'Кількість амеб':^15}")
    print("=" * 35)

    amoeba_count = 1
    for hours in range(3, 49, 3):
        amoeba_count *= 2
        print(f"{hours:^15} | {amoeba_count:^15}")

    print("=" * 35 + "\n")

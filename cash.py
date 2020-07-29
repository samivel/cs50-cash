from cs50 import get_float

def main():
    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break

    centsOwed = int(change * 100)
    cash(centsOwed)


def cash(n):
    quarters = n / 25
    dimes = (n % 25) / 10
    nickels = ((n % 25) % 10) / 5
    pennies = ((n % 25) % 10) % 5

    print(f"Quarters: {int(quarters)}")
    print(f"Dimes: {int(dimes)}")
    print(f"Nickels: {int(nickels)}")
    print(f"Pennies: {int(pennies)}")


if __name__ == "__main__":
    main()


    
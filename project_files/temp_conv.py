def far_to_cel():
    while True:
        try:
            u_far_input = input("Enter temperature in fahrenheit: ")

            cel_calc = ((int(u_far_input) - 32) * 5/9)
            print(round(cel_calc))
            break

        except ValueError:
            print("Invalid input. Try again.\n")


def cel_to_far():
    while True:
        try:
            u_cel_input = input("Enter temperature in celsius: ")

            far_calc = ((int(u_cel_input) * 9/5) + 32)
            print(round(far_calc))
            break
        
        except ValueError:
            print("Invalid input. Try again.\n")


def main():
    print("The Termperature Converter!")
    print()

    print("MENU")
    print("1) Fahrenheit to Celsius")
    print("2) Celsius to Fahrenheit")

    while True:
        choice = input("Enter 1 or 2: ")

        if choice == "1" or choice == "2":

            if choice == "1":
                far_to_cel()
            elif choice == "2":
                cel_to_far()
            break
        
        else:
            print("Invalid Input. Try again.\n")

    input("Press 'Enter' to quit.")


if __name__ == "__main__":
    main()

    
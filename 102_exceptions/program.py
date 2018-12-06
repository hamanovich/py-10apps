print('--=== Calculator ===--')

def main():
    while True:
        try:
            a = float(input('a= '))
            b = float(input('b= '))

            print(a / b)
            break

        except ZeroDivisionError:
            print('⛔️  Division by Zero')
            print('Try again 🤞')

        except ValueError:
            print('⛔️  Only float numbers are expectable')
            print('Try again 🤞')

    print('Ending the calculation')


if __name__ == "__main__":
    main()
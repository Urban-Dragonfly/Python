from logger import logger

def perform_calculation(operation_type, numbers):
    if operation_type == 1:
        logger.info(f"Dodaję {' i '.join(map(str, numbers))}")
        result = sum(numbers)
    elif operation_type == 2:
        logger.info(f"Odejmuję {numbers[0]} i {numbers[1]}")
        result = numbers[0] - numbers[1]
    elif operation_type == 3:
        logger.info(f"Mnożę {' i '.join(map(str, numbers))}")
        result = 1
        for num in numbers:
            result *= num
    elif operation_type == 4:
        if numbers[1] == 0:
            logger.error("Nie można dzielić przez zero.")
            print("Eris umie dzielić przez zero, ten kalkulator nie!")
            return None
        logger.info(f"Dzielę {numbers[0]} i {numbers[1]}")
        result = numbers[0] / numbers[1]
    else:
        print("Niepoprawna operacja.")
        logger.debug(f"{operation_type} - Niepoprawna operacja.") #operation_type value
        return None
    return result

def get_numbers(operation_type):
    numbers = []
    if operation_type in [1, 3]:  # Dodawanie lub mnożenie
        while True:
            num = float(input("Podaj składnik: "))
            numbers.append(num)
            if input("Czy chcesz dodać więcej liczb? (t/n): ").lower() != 't':
                break
    else:  # Odejmowanie lub dzielenie (dokładnie dwa argumenty)
        for i in range(2):
            num = float(input(f"Podaj składnik {i + 1}. "))
            numbers.append(num)
    return numbers

def main():
    try:
        operation_type = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
        numbers = get_numbers(operation_type)
        result = perform_calculation(operation_type, numbers)
        if result is not None:
            print(f"Wynik to {result:.2f}")
    except ValueError:
        print("Podano nieprawidłową wartość.")

if __name__ == "__main__":
    main()
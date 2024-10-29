import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs/calculator.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

def get_operation():
    print("Wybierz operację:")
    for operation in operations:
        print(f"Wpisz {operation} aby uruchomić {operations[operation][1]}")
    operation = input()
    if operation in operations:
        logger.info(f"Wybrano operacje: {operations[operation][0]}")
        return operation
    else:
        logger.error(f"Niepoprawna operacja: {operation}")
        print("Niepoprawna operacja. Sprobuj ponownie.")
        return get_operation()
    
def get_numbers(operation):
    numbers = []
    if operation == "/":
        try:
            dividend = input("Podaj dzielną: ")
            numbers.append(float(dividend))
        except ValueError:
            logger.error("Podano nieprawidłową wartość. divisor = {divisor}")
            print("Podano nieprawidłową wartość. Sprobuj ponownie.")
            return get_numbers("/")
        while True:
            try:
                divisor = input("Podaj dzielnik, by skończyć naciśnij enter: ")
                if divisor == "":
                    if len(numbers) < 2:
                        print("Podano za mało składników. Sprobuj ponownie.")
                        continue
                    else:
                        return numbers
                if divisor == "0":
                    logger.error("Nie można dzielić przez zero.")
                    print("Eris umie dzielić przez zero, ten kalkulator nie!")
                    continue
                else:
                    numbers.append(float(divisor))
                    continue
            except ValueError:
                logger.error(f"Podano nieprawidłową wartość. divisor = {divisor}")
                print(f"Eris umie dzielić przez {divisor}, ten kalkulator nie!")
                continue
    else:
        while True:
            operand = input(f"Podaj składniki potrzebne aby wykonać {operations[operation][1]}, by skończyć naciśnij enter:")
            if operand == "":
                if len(numbers) < 2:
                    print("Podano za mało składników. Sprobuj ponownie.")
                    continue
                else:
                    logger.info(f"Wybrane składniki to: {' i '.join(map(str, numbers))}")
                    return numbers
            else:
                try:
                    num = float(operand)
                    numbers.append(num)
                    continue
                except ValueError:
                    logger.error("Podano nieprawidłową wartość: {operand}.")
                    print("Podano nieprawidłową wartość. Sprobuj ponownie.")
                    continue

def perform_calculation(operation, numbers):
    calculator = operations[operation][0]
    result = calculator(numbers)
    return result
    
def addition(numbers):
    return sum(numbers)

def subtraction(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiplication(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

operations = {
    "+": (addition, "dodawanie"),
    "-": (subtraction, "odejmowanie"),
    "*": (multiplication, "mnożenie"),
    "/": (division, "dzielenie")
}
def main():
    print("*** Witaj w kalkulatorze! ***")
    operation = get_operation()
    numbers = get_numbers(operation)
    result = perform_calculation(operation, numbers)
    print("Wynik:", result)
if __name__ == "__main__":
    main()
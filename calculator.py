import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs/calculator.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

def get_operation():
    print("Wybierz operację:")
    for operation in operations:
        print(f"Wpisz {operation} aby uruchomić {operations[operation][1]}")
    operation = input()
    if operation in operations:
        logger.debug(f"Wybrano operacje: {operations[operation][1]}")
        return operation
    else:
        logger.warning(f"Niepoprawna operacja: {operation}")
        print("Niepoprawna operacja. Sprobuj ponownie.")
        return get_operation()
    
def get_numbers(operation):
    numbers = []
    while True:
        if operation == "/" and not numbers:
            prompt = "Podaj dzielną: "
        elif operation == "/":
            prompt = "Podaj dzielnik, by skończyć naciśnij enter: "
        else:
            prompt = f"Podaj składnik, by skończyć naciśnij enter: "
        operand = input(prompt)
        if operand == "":
            if len(numbers) < 2:
                print("Podano za mało składników. Spróbuj ponownie.")
                continue
            else:
                logger.debug(f"Wybrane składniki to: {' i '.join(map(str, numbers))}")
                return numbers
        try:
            num = float(operand)
            if operation == "/" and num == 0 and len(numbers) > 0:
                logger.warning("Nie można dzielić przez zero.")
                print("Eris umie dzielić przez zero, ten kalkulator nie!")
                continue
            numbers.append(num)
        except ValueError:
            logger.error(f"Podano nieprawidłową wartość: {operand}.")
            print("Podano nieprawidłową wartość. Spróbuj ponownie.")
            continue

def perform_calculation(operation, *args):
    calculator = operations[operation][0]
    result = calculator(*args)
    return result

def addition(a, b, *args):
    operands = (a, b) + args
    logger.debug(f"Adding numbers: {operands}")
    try:
        result = sum(operands)
        logger.debug(f"Addition result: {result}")
        return result
    except ValueError as e:
        logger.error(f"ValueError in addition: {e}")
        raise

def subtraction(a, b, *args):
    operands = (a, b) + args
    logger.debug(f"Subtracting numbers: {operands}")
    try:
        result = a - b
        for num in args:
            result -= num
        logger.debug(f"Subtraction result: {result}")
        return result
    except ValueError as e:
        logger.error(f"ValueError in subtraction: {e}")
        raise

def multiplication(a, b, *args):
    operands = (a, b) + args
    logger.debug(f"Multiplying numbers: {operands}")
    try:
        result = a * b
        for num in args:
            result *= num
        logger.debug(f"Multiplication result: {result}")
        return result
    except ValueError as e:
        logger.error(f"ValueError in multiplication: {e}")
        raise

def division(a, b, *args):
    operands = (a, b) + args
    logger.debug(f"Dividing numbers: {operands}")
    try:
        result = a / b
        for num in args:
            result /= num
        logger.debug(f"Division result: {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"ZeroDivisionError in division: {e}")
        raise
    except ValueError as e:
        logger.error(f"ValueError in division: {e}")
        raise

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
    result = perform_calculation(operation, *numbers)
    print("Wynik:", f"{result:.2f}".rstrip('0').rstrip('.'))
if __name__ == "__main__":
    main()
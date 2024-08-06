def sum_two_numbers():
    number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

    result = number1 + number2

    return result

sum_result = sum_two_numbers()
print(f"ორ რიცხვის ჯამი არის: {sum_result}")
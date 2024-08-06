def check_number(number):
    if number > 10:
        return "მაგარია!"
    return "არ არის მაგარი!"

# გამოყენება
user_number = float(input("შეიყვანეთ რიცხვი: "))
message = check_number(user_number)
print(message)
def positive_or_negative(number):
    if number > 0:
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    return "ნეიტრალური"

# გამოყენება
user_number = float(input("შეიყვანეთ რიცხვი: "))
result = positive_or_negative(user_number)
print(result)
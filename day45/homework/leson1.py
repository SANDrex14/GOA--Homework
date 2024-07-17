# 1) ივარჯიშეთ გავლილ მასალაზე რაც იცით

# მაგალითი 1: for ციკლი
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} არის ლუწი რიცხვი.")
    else:
        print(f"{num} არ არის ლუწი რიცხვი.")



# მაგალითი 2: while ციკლი
i = 1
while i <= 5:
    if i % 2 == 0:
        print(f"{i} არის ლუწი რიცხვი.")
    else:
        print(f"{i} არ არის ლუწი რიცხვი.")
    i += 1



# მაგალითი 3: if-else ბრძანება
number = 7
if number % 2 == 0:
    print(f"{number} არის ლუწი რიცხვი.")
else:
    print(f"{number} არ არის ლუწი რიცხვი.")
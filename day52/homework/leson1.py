import random

print("კეთილი იყოს თქვენი მობრძანება ჯეირანის თამაშში!")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("გამოიცანით რიცხვი 1-დან 100-მდე: ")
    
    if not guess.isdigit():
        print("გთხოვთ შეიყვანოთ სწორი რიცხვი.")
        continue

    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        print("ცოტა მეტი.")
    elif guess > secret_number:
        print("ცოტა ნაკლები.")
    else:
        print(f"გილოცავთ! თქვენ გამოიცანით რიცხვი {attempts} მცდელობით.")
        break

#randint: ფუნქცია, რომელიც გენერირებს შემთხვევით მთელ რიცხვს მოცემული დიაპაზონიდან.
#continue: ციკლის ოპერატორი, რომელიც ახდენს ციკლის შემდეგი იტერაციის დაწყებას, გამოტოვებს მიმდინარე იტერაციის დარჩენილ ნაწილს.
#isdigit: სტრიქონის მეთოდი, რომელიც ამოწმებს, არის თუ არა სტრიქონი მხოლოდ ციფრებისგან შემდგარი.
#break: ოპერატორი, რომელიც აჩერებს ციკლს მყისიერად.
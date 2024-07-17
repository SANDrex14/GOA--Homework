word_list = []

while True:
    word = input("მიუთითეთ სიტყვა (6 ასოს არ უნდა აღემატებოდეს): ")
    if len(word) <= 6:
        word_list.append(word)
    else:
        print("სიტყვა ძალიან გრძელია, სცადეთ თავიდან.")
    
    continue_adding = input("გსურთ კიდევ სიტყვის დამატება? (დიახ/არა): ")
    if continue_adding.lower() == "არა":
        break

print(word_list)
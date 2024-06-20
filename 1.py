import datetime

today = datetime.date.today()
file_name = str(today) + "_to_do_list.txt"

with open(file_name, "w") as file:
    file.write("TO DO LIST for " + str(today) + ":\n")

    while True:
        to_do = input("Введите дела на сегодня (или 'выход' для финиша): ")
        if to_do.lower() == "выход":
            break
        file.write("-" + to_do + "\n")

print("TO DO LIST for " + str(today) + " has been saved to " + file_name)

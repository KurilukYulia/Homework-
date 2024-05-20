import Menu1
from age1 import parse_date, calculate_age


class Person:
    def __init__(self, name, surname, patronymic, birth_day):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_day = parse_date(birth_day)

    def person(self):
        return self.name, self.surname, self.patronymic, self.birth_day.strftime('%d-%m-%Y')

    def __repr__(self):
        age = calculate_age(self.birth_day)
        return f"{self.name} {self.surname} {self.patronymic} {self.birth_day.strftime('%d-%m-%Y')}, {age} years old"


persons = [
    Person('Ivan', 'Ivanov', 'Ivanovich', '12/10/1980'),
    Person('Bob', 'Smith', 'John', '09-01-2000'),
    Person('Maria', 'Garcia', 'Volodymyrivna', '31-07-1999'),
    Person('Karol', 'Kowal', '-', '26-03-2002'),
    Person('Ivan', 'Petrov', 'Sergeevich', '03-02-2005'),
    Person('Kamila', 'Kuznetsova', 'Dmitrievna', '11-12-2001')
]


def main():
    while True:
        Menu1.display_menu()
        choice = Menu1.get_choice()
        if choice == '1':
            Menu1.add_person(persons)
        elif choice == '2':
            Menu1.search_person(persons)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please select again.")

if __name__ == "__main__":
    main()

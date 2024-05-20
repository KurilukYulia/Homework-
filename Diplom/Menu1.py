import People
def display_menu():
    print('1. Add a new person')
    print('2. Search for a person')
    print('3. Exit')


def get_choice():
    return input("Select the option: ")


def add_person(people):
    name = input('Name: ')
    surname = input('Surname: ')
    patronymic = input('Patronymic: ')
    birth_day = input('Birthday day: ')
    try:
        person = People.Person(name, surname, patronymic, birth_day)
        people.append(person)
        print('Person successfully added')
    except ValueError as e:
        print(f'Error adding a person: {e}')


def search_person(people):
    search_person = input('Write a name of person: ')
    results = [person for person in people if search_person.lower() in person.name.lower()]
    if results:
        for result in results:
            print(result)
    else:
        print('Person not found.')

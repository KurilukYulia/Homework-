def numbers(input_str):
    if input_str.lower() in ["вихід", "exit", "quit", "e", "q"]:
        return "exit"

    if input_str.replace('.', '', 1).replace(',', '', 1).lstrip('-').isdigit():
        number = float(input_str.replace(',', '.'))
        if '.' in input_str:
            return f"You have entered {'positive' if number >= 0 else 'negative'} fractional number: {number}"
        else:
            return f"You have entered a {'positive' if number >= 0 else 'negative' } integer number: {int(number)}"
    else:
        return "You entered an incorrect number: " + input_str


while True:
    user_input = input("Enter a number or 'exit' to end ")
    result = numbers(user_input)
    if result == "exit":
        break
    else:
        print(result)

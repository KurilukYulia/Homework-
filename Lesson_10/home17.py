a = input('Type the first line:')
b = input('Enter the second line:')
c = input('Enter the third line:')
d = input('Enter the fourth line:')

data =f"{a}\n{b}\n"
data_2 =f"{c}\n{d}\n"

with open('01.txt', 'w') as f:
    f.write(data)

with open('01.txt', 'a') as f:
    f.write(data_2)

string = b'r\xc3\xa9sum\xc3\xa9'
print(string.decode())
string_1 = 'résumé'
print(string_1.encode('Latin-1'))
string_2 = b'r\xe9sum\xe9'
print(string_2.decode('Latin-1'))

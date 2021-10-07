from random import choice

options = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 1, 2, 3, 4,
        5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '^', '&'
        ]

password = []

while len(password) < 8:
    result = choice(options)

    if options not in password:
        password.append(result)

print("Your new password is: ")
print(password)

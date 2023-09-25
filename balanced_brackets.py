number_of_lines = int(input())
counter = 0
for lines in range(number_of_lines):
    string = input()
    if string == "(":
        counter += 1
    elif string == ")":
        counter -= 1
    if 0 != counter != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")

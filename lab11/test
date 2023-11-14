database = [['peter', 1234], ['eva', 2345], ['ib', '3456miaw'], ['kim', 'hjertefar']]
wrong_answers = 0
while wrong_answers < 5:
    if wrong_answers < 5:
        user_name = input("Enter your name: ")
        user_pin = input("Enter your PIN code: ")
        for entry in database:
            if entry[0] == user_name and str(entry[1]) == user_pin:
                print('You have entered the correct name and PIN code – welcome.')
                break
        else:
            print('You have entered an incorrect name and/or PIN code – try again.')
            wrong_answers += 1
    if wrong_answers == 5:
        print('You have entered incorrectly 5 times. Therefore, the program is stopping.')
    else:
        wrong_answers += 1
        break

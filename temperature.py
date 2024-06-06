while True:
    print('1 - Celcius to Farenheit')
    print('2 - Farenheit to Celcius')
    print('3 - Exit')

    choice = input('Enter Choice: ')

    if choice in ('1','2'):
        temperature = float(input('Enter Temperature: '))

        if choice == '1':
            print('Farenheit: ', ((temperature * 9/5) + 32))
        elif choice == '2':
            print('Celcius: ',((temperature - 32) * 5/9))
    elif choice == '3':
        break
    else:
        print('Invalid Input')
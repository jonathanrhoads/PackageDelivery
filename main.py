
class Main:

    distance = 0

    print(f'''
    Author: Jonathan Rhoads 
    #001891548
    --------------------------------------------------------------------------------------------------------------------
    
                                            WELCOME TO THE PACKAGE DELIVERY HUB
                                            
                                                    Total distance: {distance}
                                            
                                                How can we help you today?
                                                
    --------------------------------------------------------------------------------------------------------------------
    Please enter a number from the options below:
        1. Lookup all packages at a certain time.
        2. Exit the hub.
        
    ''')

    selection = input()

    if selection == '2':
        print('Thank you and have a nice day!')
        exit()
    elif selection == '1':
        while selection == '1':
            time = input('\nPlease enter the time desired in the format HH:MMn\n')
            (hour, minute) = time.split(':')
            print(f'hour: {hour} minute: {minute}')

            selection = input('Enter 1 to lookup another time or press any key to exit.')
            if selection != '1':
                print('Thank you and have a nice day!')
                exit()
    else:
        print('Invalid input, bye bye!')



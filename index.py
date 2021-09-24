import inquirer

def present_main_menu():
    main_menu = [
    inquirer.List('calculation_type',
        message="Which fitness calculation would you like to do?",
        choices=['Body Mass Index (BMI)', 'Estimated Body Fat Percentage', 'Height Percentile', 'Weight Percentile', 'Estimated Daily Caloric Intake', 'Estimated Daily Water Intake', 'Estimated Daily Protein Intake', 'Resting Heart Rate'],
        ),
    ]
    main_menu_answer = inquirer.prompt(main_menu)
    choose_sub_menu(main_menu_answer['calculation_type'])

def choose_sub_menu(user_choice):
    if(user_choice == 'Body Mass Index (BMI)'):
        print('You chose BMI')
    elif(user_choice == 'Estimated Body Fat Percentage'):
        print('You chose body fat percentage')
    elif(user_choice == 'Height Percentile'):
        print('You chose height percentile')
    elif(user_choice == 'Weight Percentile'):
        print('You chose weight percentile')
    elif(user_choice == 'Estimated Daily Caloric Intake'):
        print('You chose daily caloric intake')
    elif(user_choice == 'Estimated Daily Water Intake'):
        print('You chose daily water intake')
    elif(user_choice == 'Estimated Daily Protein Intake'):
        print('You chose protein intake')
    else:
        print('You chose resting heart rate')



present_main_menu()
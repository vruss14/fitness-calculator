import inquirer

def present_main_menu():
    main_menu = [
    inquirer.List('calculation_type',
                    message="Which fitness calculation would you like to do?",
                    choices=['Body Mass Index (BMI)', 'Estimated Body Fat Percentage', 'Height Percentile', 'Weight Percentile', 'Estimated Daily Caloric Intake', 'Estimated Daily Water Intake', 'Estimated Daily Protein Intake', 'Resting Heart Rate'],
                ),
    ]
    main_menu_answer = inquirer.prompt(main_menu)
    print(main_menu_answer['calculation_type'])

present_main_menu()
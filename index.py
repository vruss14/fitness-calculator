import inquirer

def present_main_menu():
    main_menu = [
    inquirer.List('calculation_type',
        message="Which fitness calculation would you like to do?",
        choices=['Body Mass Index (BMI)', 'Height Percentile', 'Weight Percentile', 'Estimated Daily Caloric Intake', 'Estimated Daily Water Intake', 'Estimated Daily Protein Intake', 'Resting Heart Rate'],
        ),
    ]
    main_menu_answer = inquirer.prompt(main_menu)
    choose_sub_menu(main_menu_answer['calculation_type'])

# Switches which calculation function runs based on user input

def choose_sub_menu(user_choice):
    if(user_choice == 'Body Mass Index (BMI)'):
        run_bmi_calculation()
    elif(user_choice == 'Height Percentile'):
        run_height_calculation()
    elif(user_choice == 'Weight Percentile'):
        run_weight_calculation()
    elif(user_choice == 'Estimated Daily Caloric Intake'):
        run_caloric_calculation()
    elif(user_choice == 'Estimated Daily Water Intake'):
        run_water_calculation()
    elif(user_choice == 'Estimated Daily Protein Intake'):
        run_protein_calculation()
    else:
        run_heart_calculation()

# BMI calculation estimate on the CDC website is height divided by weight squared, multiplied by 703
# The round method rounds the answer to two decimal places
# The user's BMI value is passed to the check_bmi function, which evaluates what range the BMI falls under.
 
def run_bmi_calculation():
    bmi_questions = [
    inquirer.Text('height', message="What is your height? Please enter a numeric value in inches."),
    inquirer.Text('weight', message="What is your body weight? Please enter a numeric value in pounds."),               
    ]
    bmi_responses = inquirer.prompt(bmi_questions)
    bmi_responses['BMI'] = round((int(bmi_responses['weight']) / (int(bmi_responses['height']) * int(bmi_responses['height']))) * 703, 2)
    print('\nYour estimated body mass index (BMI) is: '+ str(bmi_responses['BMI']) + '%')
    print(check_bmi(bmi_responses['BMI']))

# Accepts a user_bmi parameter and returns which range the BMI falls under (according to the CDC)

def check_bmi(user_bmi):
    if(user_bmi < 18.5):
        return('According to the CDC, your BMI falls within the underweight range.')
    elif(user_bmi > 18.5 and user_bmi < 24.9):
        return('According to the CDC, your BMI falls within the normal/healthy weight range.')
    elif(user_bmi > 25 and user_bmi < 29.9):
        return('According to the CDC, your BMI falls within the overweight range.')
    elif(user_bmi > 30):
        return('According to the CDC, your BMI falls within the obese range.')

def run_height_calculation():
    print('3')

def run_weight_calculation():
    print('4')

def run_caloric_calculation():
    print('5')

def run_water_calculation():
    print('6')

def run_protein_calculation():
    print('7')

def run_heart_calculation():
    print('8')

present_main_menu()

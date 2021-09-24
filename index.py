import inquirer

def present_main_menu():
    print('\nPlease keep in mind that this program does not store any of your information and will not ask any personal identification information. The estimates you receive from the calculations may not be entirely accurate. Please consult with a healthcare provider to make informed decisions about your health and wellness.\n')
    main_menu = [
    inquirer.List('calculation_type',
        message="Which fitness calculation would you like to do?",
        choices=['Body Mass Index (BMI)', 'Estimated Daily Caloric Intake', 'Estimated Daily Water Intake', 'Estimated Daily Protein Intake', 'Heart Rate'],
        ),
    ]
    main_menu_answer = inquirer.prompt(main_menu)
    choose_sub_menu(main_menu_answer['calculation_type'])

# Switches which calculation function runs based on user input

def choose_sub_menu(user_choice):
    if(user_choice == 'Body Mass Index (BMI)'):
        run_bmi_calculation()
    elif(user_choice == 'Estimated Daily Caloric Intake'):
        run_caloric_calculation()
    elif(user_choice == 'Estimated Daily Water Intake'):
        run_water_calculation()
    elif(user_choice == 'Estimated Daily Protein Intake'):
        run_protein_calculation()
    else:
        run_heart_calculation()

# BMI calculation estimate is height divided by weight squared, multiplied by 703
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
        print('According to the CDC, your BMI falls within the underweight range.\n')
    elif(user_bmi > 18.5 and user_bmi < 24.9):
        print('According to the CDC, your BMI falls within the normal/healthy weight range.\n')
    elif(user_bmi > 25 and user_bmi < 29.9):
        print('According to the CDC, your BMI falls within the overweight range.\n')
    elif(user_bmi > 30):
        print('According to the CDC, your BMI falls within the obese range.\n')
    new_calculation()

# This calculation first calculates the user's BMR then that value is multipled based on the amount of physical activity the person does

def run_caloric_calculation():
    print("\nThis calculation differs for men and women, since men tend to have higher basal metabolic rates (BMR) than women.")

    caloric_questions = [
    inquirer.List('body_type',
        message="\nKnowing this, which calculation do you feel would be most accurate for you?",
        choices=['Men', 'Women'],
        ),
    inquirer.Text('height', message="What is your height? Please enter a numeric value in inches."),
    inquirer.Text('weight', message="What is your body weight? Please enter a numeric value in pounds."),
    inquirer.Text('age', message="What is your age? Please enter an integer value in years."),
    inquirer.List('exercise',
        message="How much physical activity would you say that you do each day (on average)?",
        choices=['Sedentary (little to no exercise)', 'Lightly active (light exercise/sports 1–3 days/week)', 'Moderately active (moderate exercise/sports 3-5 days/week', 'Very active (hard exercise/sports 6-7 days/week', 'Extra active (very hard exercise/sports & physical job or 2x training'],
        ),               
    ]
    response = inquirer.prompt(caloric_questions)

    if(response['body_type'] == 'Men'):
        male_caloric_calculation(response)
    else:
        female_caloric_calculation(response)

def male_caloric_calculation(user_responses):
    # Need to calculate BMR first; then the caloric intake depends on how much exercise the person performs on average each day
    user_responses['BMR'] = round(66 + (6.3 * int(user_responses['weight'])) + (12.9 * int(user_responses['height'])) - (6.8 * int(user_responses['age'])), 2)
    final_caloric_calculation(user_responses)
    
def female_caloric_calculation(user_responses):
    # Calculating BMR
    user_responses['BMR'] = round(655 + (4.3 * int(user_responses['weight']) + (4.7 * int(user_responses['height']) - (4.7 * int(user_responses['age'])))), 2)
    final_caloric_calculation(user_responses)

def final_caloric_calculation(user_responses):
    if(user_responses['exercise'] == 'Sedentary (little to no exercise)'):
        user_responses['caloric_need'] = round(int(user_responses['BMR']) * 1.2, 2)
    elif(user_responses['exercise'] == 'Lightly active (light exercise/sports 1–3 days/week)'):
        user_responses['caloric_need'] = round(int(user_responses['BMR']) * 1.375, 2)
    elif(user_responses['exercise'] == 'Moderately active (moderate exercise/sports 3-5 days/week'):
        user_responses['caloric_need'] = round(int(user_responses['BMR']) * 1.55, 2)
    elif(user_responses['exercise'] == 'Very active (hard exercise/sports 6-7 days/week'):
        user_responses['caloric_need'] = round(int(user_responses['BMR']) * 1.725, 2)
    else:
        user_responses['caloric_need'] = round(int(user_responses['BMR']) * 1.9, 2)

    print('\nYour estimated daily caloric intake is: '+ str(user_responses['caloric_need']) + ' calories.\n')
    new_calculation()

# Amount of water is about half to two-thirds of a person's body weight
# Calculates a minimum and maximium in ounces, and then turns that into an approxmate range for glasses of water

def run_water_calculation():
    water_question = [inquirer.Text('weight', message="What is your body weight? Please enter a numeric value in pounds.")]
    response = inquirer.prompt(water_question)
    response['min'] = round(int(response['weight']) * 0.5, 2)
    response['max'] = round(int(response['weight']) * 0.6667, 2)
    response['min_glasses'] = int(response['min']) / 8
    response['max_glasses'] = int(response['max']) / 8

    print('\nIt\'s recommended that you drink between ' + str(response['min']) +  
    ' ounces and ' + str(response['max']) + ' oz per day. To put that into perspective, that\'s about ' + 
    str(response['min_glasses']) + ' to ' + str(response['max_glasses']) + 
    ' glasses of water per day.\n')

    new_calculation()

# Recommendation is 0.36 - 0.45 grams of protein per pound of body weight; 
# if exercising, then 0.8 to 1.0 gram per pound of body weight

def run_protein_calculation():
    print('\nYour amount of exercise is a significant factor in determining your recommended daily protein intake.')
    protein_questions = [
    inquirer.List('exercise',
        message="\nDo you exercise regularly (moderate/intense activity)?",
        choices=['Yes', 'No'],
        ),
    inquirer.Text('weight', message="What is your body weight? Please enter a numeric value in pounds.")
    ]
    response = inquirer.prompt(protein_questions)

    if(response['exercise'] == 'Yes'):
        response['min_protein'] = round(int(response['weight']) * 0.8)
        response['max_protein'] = round(int(response['weight']))
    else:
        response['min_protein'] = round(int(response['weight']) * 0.36)
        response['max_protein'] = round(int(response['weight']) * 0.45)
    
    print('\nYour recommended protein intake is: ' + str(response['min_protein']) + ' – ' + str(response['max_protein']) + ' grams.\n' )
    new_calculation()

def run_heart_calculation():
    print('\nPlace two fingers on a place where you can feel your pulse (like your wrist and neck). Count the beats for 30 seconds.')
    heart_question = [inquirer.Text('heartbeats', message="How many heartbeats did you count? Please enter an integer value.")]
    response = inquirer.prompt(heart_question)
    response['rate'] = int(response['heartbeats']) * 2
    print('\nYour current heart rate is: ' + str(response['rate']) + '.\n')
    new_calculation()

def new_calculation():
    repeat_question = [
    inquirer.List('repeat',
        message="\nWould you like to do another calculation?",
        choices=['Yes', 'No'],
    )]
    response = inquirer.prompt(repeat_question)

    if(response['repeat'] == 'Yes'):
        present_main_menu()
    else:
        print('\nThanks for using this application!')
        return

present_main_menu()

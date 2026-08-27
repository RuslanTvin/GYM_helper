import progress_control.dump_and_load_json
import progress_control.workout_file_modification_functions
import progress_control.workout_file_view_functions
import datetime 
import helpful_functions

def get_float(text):
    while True:
        try:
            float_request=float(input(text))
            return float_request
        except ValueError:
            print("Incorrect input.Enter number!")

def get_integer(text):
    while True:
        try:
            integer_request=int(input(text))
            return integer_request
        except ValueError:
            print("Incorrect input.Enter number!")

def get_string(text):
    string_request=str(input(text))
    return string_request.strip().lower()

def get_yes_or_no(text):
    while True:
        choice = input(text).strip().lower()
        if choice in ["yes", "y", "no", "n"]:
            return choice
        print("Incorrect input. Please enter 'yes' or 'no'.")

def validate_input(function,text,variable_name,zero_allowed):
    while True:
        input=function(text)
        if input >= 0 and zero_allowed == True:
            return input
        elif input > 0 and zero_allowed == False:
            return input
        else:
            print(variable_name,"cannot be negative or zero!")

def get_choice(text, choices,string_choice_allowed):
    while True:
        if not string_choice_allowed:
            choice = get_integer(text)
            if choice in choices:
                return choice
            print("Incorrect input. Please enter one of the following:",choices)
        else:
            choice = get_string(text)
            if choice in choices:
                return choice
            print("Incorrect input. Please enter one of the following:",choices)
            
def get_physical_data(weight_or_height_or_both):
    if weight_or_height_or_both == "both":
        weight=validate_input(get_float,"What is your weight? ","weight",False)
        height=validate_input(get_float,"What is your height? ","height",False)
        return weight,height
    elif weight_or_height_or_both == "height":
        height=validate_input(get_float,"What is your height? ","height",False)
        return height
    elif weight_or_height_or_both == "weight":
        weight=validate_input(get_float,"What is your weight? ","weight",False)
        return weight

def get_exercise_name():
    exercise_name=get_string("What is name of exercise? ")
    return exercise_name

def get_workout_data():
    amount_of_sets=validate_input(get_integer,"How many sets of this exercise did you do?(enter number) ","amount of sets",False)
    
    amount_of_reps=validate_input(get_integer,"How many reps of this exercise did you do in each set?(enter number) ","amount of reps",False)
    
    weight_for_exercise=validate_input(get_float,"With what weight did you exercise?(enter number) ","weight ",True)

    return amount_of_sets,amount_of_reps,weight_for_exercise

def get_workout_data_with_exercise_name():
    exercise_name = get_exercise_name()

    amount_of_sets,amount_of_reps,weight_for_exercise = get_workout_data()

    return exercise_name,amount_of_sets,amount_of_reps,weight_for_exercise

def add_up_exercise_to_record_of_training(record_note,exercise_name, sets, reps, weight):
    record_note["exercises"].append({
    "exercise": exercise_name,
    "sets": sets,
    "reps": reps,
    "weight": weight })
    return record_note

def get_date():
    while True:
        try:
            format_str = "%Y-%m-%d"
            day = get_choice("Enter day of month of your workout ",list(range(1,32)),False)
            month = get_choice("Enter month of your workout (It could be number or word) ",["january","february","march","april","may","june","july","august","september","october","november","december","1","2","3","4","5","6","7","8","9","10","11","12"],True)
            year = get_integer("Enter year of your workout ")
            date_str = str(year)+"-"+str(month)+"-"+str(day)
            date = str(datetime.datetime.strptime(date_str,format_str).date())
            is_date_correct = get_choice("Do you want to change entered date? "+str(date)+"\n1:Yes\n2:No ",[1,2],False)
            if is_date_correct == 2:
                return date
        except ValueError:
            print("Please enter correct date!!!")

def add_exercise_note_for_one_workout(record_note):
    exercise_name, sets, reps, weight = get_workout_data_with_exercise_name()
    record_note = add_up_exercise_to_record_of_training(record_note,exercise_name, sets, reps, weight)
    add_another_exericse = get_yes_or_no("Would you like to add another exercise for this date? ")
    while add_another_exericse == "yes":
        exercise_name, sets, reps, weight = get_workout_data_with_exercise_name()
        record_note = add_up_exercise_to_record_of_training(record_note,exercise_name, sets, reps, weight)
        add_another_exericse = get_yes_or_no("Would you like to add another exercise for this date? ")
    return record_note

def get_main_menu_option():
    return get_choice("\nWhat do you want to do:\n1:Convert pounds to kilos\n2:Calculate BMI\n3:Calories calculator\n4:Check your workout statistics\n5:Show workout progress\n6:Programm save menu\n0:exit\n",[1,2,3,4,5,6,0],False)
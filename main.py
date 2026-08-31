import calories
import bmi
import convert
import progress_control.workout_save_menu
import progress_control.workout_file_view_functions
import input_part
import progress_control.dump_and_load_json
import progress_control.workout_statistic_menu
print("Welcome to universal GYM helper.")
numeral_system = input_part.get_choice("Choose numeral system that is comfortable for you.\n1:Imperial(inches and pounds.)\n2: Metric (centimeters and kilograms.) ",[1,2],False)
if numeral_system == 1:
    print("Successfully was chosen imperial system.")
elif numeral_system == 2:
    print("Successfully was chosen metrical system.")
action=input_part.get_main_menu_option()
while action != 0:
    list_of_progress=progress_control.dump_and_load_json.load_file_with_progress_json("progress.json")
    if action == 1:
        print(convert.convert_menu())
    elif action == 2:
        print(bmi.bmi_menu(numeral_system))
    elif action == 3:
        print(calories.calories_calculation_menu(numeral_system))
    elif action == 4:
        progress_control.workout_statistic_menu.workout_statistics_menu(list_of_progress)
    elif action == 5:
        progress_control.workout_file_view_functions.show_progress_json(list_of_progress)
    elif action == 6:
        progress_control.workout_save_menu.workout_save_menu(list_of_progress,numeral_system)
    action=input_part.get_main_menu_option()
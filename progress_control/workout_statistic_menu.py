import input_part
import progress_control.output_for_statistic_menu_options as menu_output

def workout_statistics_menu(list_of_progress):
    print("You are in workout statistics menu.")
    user_option = input_part.get_choice("Here are your options:\n1:Check total number of your workouts\n2:Check total number of exercises\n3:Check total number of unique exercises\n4:Check statistic of one exercise\n5:Check one exercise progress.\n6:Exit back to main menu. ",[1,2,3,4,5,6],False)
    if list_of_progress:
        if user_option == 1:
            menu_output.output_for_option_one(list_of_progress)
        elif user_option == 2:
            menu_output.output_for_option_two(list_of_progress)
        elif user_option == 3:
            menu_output.output_for_option_three(list_of_progress)
        elif user_option == 4:
            menu_output.output_for_option_four(list_of_progress)
        elif user_option == 5:
            menu_output.output_for_option_five(list_of_progress)
        elif user_option == 6:
            pass
    else:
        print("Your statistic is unavailable,you dont have any workout records!!!")

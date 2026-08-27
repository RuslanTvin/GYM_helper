import input_part
import progress_control.workout_file_view_functions
import helpful_functions
import progress_control.workout_statistic_functions as statistic_functions

def output_for_option_one(list_of_progress):
    print("Total number of workouts is:",statistic_functions.total_number_of_workout_records(list_of_progress))

def output_for_option_two (list_of_progress):
    print("Total number of exercises is:",statistic_functions.total_number_of_exercises(list_of_progress))

def output_for_option_three (list_of_progress):
    print("Total number of unique exercises:",statistic_functions.total_number_of_unique_exercises(list_of_progress))

def output_for_option_four (list_of_progress):
    what_exercise = input_part.get_string("Statistic of what exercise you want to see: ")
    matching_workouts_list = progress_control.workout_file_view_functions.find_exercise(what_exercise,list_of_progress)
    times_trained = len(matching_workouts_list) 
    if times_trained :
        maximum_weight = statistic_functions.maximum_for_something(matching_workouts_list,"weight")
        average_weight = statistic_functions.average_of_something(matching_workouts_list,"weight")
        maximum_reps = statistic_functions.maximum_for_something(matching_workouts_list,"reps")
        average_reps = statistic_functions.average_of_something(matching_workouts_list,"reps")
        maximum_sets = statistic_functions.maximum_for_something(matching_workouts_list,"sets")
        exercise_statistics_printer(what_exercise,times_trained,maximum_weight,average_weight,maximum_reps,average_reps,maximum_sets)
    else:
        print("There is no exercise with that name!!!")
        
def output_for_option_five (list_of_progress):
    what_exercise = input_part.get_string("Statistic of what exercise you want to see: ")
    sorting_method = input_part.get_choice("How would like to sort workouts?\nSorting options:\n1:By date\n2:By weight(ascending)\n3:By weight(descending)",[1,2,3],False)
    matching_workouts_list = progress_control.workout_file_view_functions.find_exercise(what_exercise,list_of_progress)
    if matching_workouts_list:
        if sorting_method == 1:
            sorted_list = statistic_functions.sort_exercises_list_by_dates(matching_workouts_list)
        elif sorting_method == 2:
            sorted_list = statistic_functions.sort_exercises_list_by_weight(matching_workouts_list,False)
        elif sorting_method == 3:
            sorted_list = statistic_functions.sort_exercises_list_by_weight(matching_workouts_list,True)
        for workout_record in sorted_list:
            helpful_functions.show_workout_record_from_find_function(workout_record)
    else:
        print("There is no exercise with that name!!!")


def exercise_statistics_printer(exercise_name,times_trainded,maximum_weight,average_weight,maximum_reps,average_reps,maximum_sets):
    print("Statistic of "+exercise_name +":")
    print("Number of times you trained this exercise:",times_trainded)
    print("Maximum weight you used for this exercise:",maximum_weight)
    print("Average weight you used for this exercise:",average_weight)
    print("Maximum reps you did in one set for this exercise:",maximum_reps)
    print("Average reps you did in each set for this exercise:",average_reps)
    print("Maximum sets you did for this exercise:",maximum_sets)


'''''
date_str = "03-30-2026"
format_str = "%m-%d-%Y"
x = datetime.datetime.strptime(date_str,format_str)
print(x.date())
print(datetime.date.today())
def get_date():
    specific_date_of_user = input_part.get_yes_or_no("Would you like to save workout of date you choose?(In case of 'no' today`s date will be used) ")
    if specific_date_of_user == "yes" or specific_date_of_user == "y":
        while True:
            try:
                format_str = "%Y-%m-%d"
                day = input_part.get_choice("Enter day of month of your workout ",range(1,32),False)
                month = input_part.get_choice("Enter month of your workout (It could be number or word) ",["january","february","march","april","may","june","july","august","september","october","november","december","1","2","3","4","5","6","7","8","9","10","11","12"],True)
                if month in ["january","february","march","april","may","june","july","august","september","october","november","december"]:
                    month = helpful_functions.convert_word_month_to_number(month)
                year = input_part.get_integer("Enter year of your workout ")
                date_str = str(year)+"-"+str(month)+"-"+str(day)
                date = str(datetime.datetime.strptime(date_str,format_str).date())
                return date
            except ValueError:
                print("Please enter correct date!!!")
    else:   
        date = str(datetime.date.today())
        return date
    
print(get_date())

def add_record_of_training():
    record_note={"date":None,
                 "exercises":[
                 ]
                 }
    day_of_record=input_part.get_string("What is date of your training record? ")
    record_note["date"]=day_of_record
    while True:
        exercise_name, sets, reps, weight = input_part.get_workout_data_with_exercise_name()
        record_note["exercises"].append({
        "exercise": exercise_name,
        "sets": sets,
        "reps": reps,
        "weight": weight })
        add_another_exercise=input_part.get_yes_or_no("Would you like to add another exercise for this day record? ")
        if add_another_exercise == "no" or add_another_exercise == "n":
            break
    return record_note
lst=add_record_of_training()
orig=workout_save.dump_and_load_json.load_file_with_progress_json("progress.json")
def save_workout_progress(list_of_progress,workout_note,file_name):
    list_of_progress.append(workout_note)
    workout_save.dump_and_load_json.dump_file_with_progress_json(file_name,list_of_progress)
save_workout_progress(orig,lst,"progress.json")
'''''
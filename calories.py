import input_part
import convert
def daily_calories_amount_formula(weight: float,height: float,age: float,sex:str,activity:str)->float:
    try:
        calories_norm_male=(10*weight)+(6.25*height)-(5*age)+5
        calories_norm_female=(10*weight)+(6.25*height)-(5*age)-161
        multipliers={
            "high": 1.9,
            "medium": 1.55,
            "low":1.2
        }
        multiplier= multipliers[activity]
        if sex == "male":
            return calories_norm_male*multiplier
        if sex == "female":
            return calories_norm_female*multiplier
    except Exception as e:
        print(f"Error Type: {type(e).__name__} | Message: {e}")
    
def calories_calculation_menu()->str:
    try:
        weight,height=input_part.get_physical_data("both")
        age=input_part.validate_input(input_part.get_float,"What is your age? ","age",False)
        activity_level=input_part.get_choice("What is your activity level?(high,medium,low)",["low","medium","high"],True)
        sex=input_part.get_choice("What is your sex?(male or female)",["male","female"],True)
        convert_to_lbs=input_part.get_yes_or_no("Do you want to convert weight to kilos?(yes or no) ")
        if convert_to_lbs.strip()=="yes":
            weight=convert.pounds_to_kilos(weight)
            print("Successfully converted")
        elif convert_to_lbs=="no":
            pass
        amount_of_calories=daily_calories_amount_formula(weight,height,age,sex,activity_level)
        return str(amount_of_calories) + " calories you need"
    except Exception as e:
        print(f"Error Type: {type(e).__name__} | Message: {e}")

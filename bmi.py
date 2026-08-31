from convert import*
from input_part import*
def bmi_formula_metric(height: float,weight:float)-> float:
    height_in_meters=height/100
    imt_formula_result=weight / (height_in_meters ** 2 )
    return imt_formula_result

def bmi_formula_imperial(height: float, weight: float) -> float:
    return (weight * 703) / (height ** 2)

def bmi_recommendation(BMI:float)-> str:
    if BMI < 18.5 :
        return "You have "+ str(BMI) +" BMI  which is less than normal weight to height proportion!"
    elif BMI >= 18.5 and BMI < 25:
        return "You have "+ str(BMI) +" BMI  which is normal weight to height proportion!"
    else: 
        return "You have "+ str(BMI) +" BMI  which is higher than normal weight to height proportion!"

def bmi_menu(numeral_system)->str:
    if numeral_system == 1:
        try:
            weight, height = get_physical_data("both", numeral_system)
            result = round(bmi_formula_imperial(height, weight), 3)
            return bmi_recommendation(result)
        except Exception as e:
            print(f"Error Type: {type(e).__name__} | Message: {e}")
    elif numeral_system ==  2:
        try:
            weight, height = get_physical_data("both", numeral_system)
            result = round(bmi_formula_metric(height, weight), 3)
            return bmi_recommendation(result)
        except Exception as e:
            print(f"Error Type: {type(e).__name__} | Message: {e}")
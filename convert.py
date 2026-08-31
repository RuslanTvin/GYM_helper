from input_part import*
def  convert_menu()->str:
    amount_of_lbs=validate_input(get_float,"What is number of pounds you want to convert!? ","pounds amount",float('-inf'),float('inf'))
    try:
        amount_of_lbs=float(amount_of_lbs)
        result=pounds_to_kilos(amount_of_lbs)
        return round(result,3)
    except Exception as e:
        print(f"Error Type: {type(e).__name__} | Message: {e}")
    
def pounds_to_kilos(Weight: float) -> float:
    coefficient_to_lb=0.45359237
    kilograms=coefficient_to_lb*Weight
    return kilograms
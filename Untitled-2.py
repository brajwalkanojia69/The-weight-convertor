//Weight converter 


weight = float(input("Enter yourweight : "))
unit =input("Enter the unit (kg or lb) : ")
if unit == "kg":
    converted_weight = weight * 2.20462
    print(f"{weight} kg is equal to {converted_weight} lb.")                    
elif unit == "lb":
    converted_weight = weight / 2.20462
    print(f"{weight} lb is equal to {converted_weight} kg.")    
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")

print("Thank you for using the weight converter!")


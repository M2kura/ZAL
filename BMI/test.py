import bmi

result = bmi.calculate_bmi(input("What is body's weight (in kg)? "), input("What is body's height (in m)? "))
print("BMI of the body is " + str(result))
next = input("Want to translate this number into human lang? [yes/no] ")
if next == "yes":
    print(bmi.get_weight_group(result))
elif next == "no":
    print("ok :) ")
elif next != "yes" and next != "no":
    print("Couldn't understand you :( Bye! ")
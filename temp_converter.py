temp_choice = input("Enter starting units: (options are F for Fahrenheit or C for Celsius ").lower()
str(temp_choice)

# This conversion to a string isn't necessary, but I thought I'd include it just in case

if temp_choice == "c":
    temp_c = input("Enter temperature in ° Celcius ")
    float(temp_c)
    temp_c = float(temp_c)
    temp_c = temp_c*9/5+32
    print(temp_c)


if temp_choice == "f":
    temp_f = input ("enter temperature in ° Fahrenheit ")
    float(temp_f)
    temp_f = float(temp_f)
    temp_c = (temp_f-32)*5/9
    print(temp_c)



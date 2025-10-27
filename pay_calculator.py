string_hours = input ("Enter number of hours; ")
string_rate = input ("Enter your hourly rate in dollars; ")
float_hours = float(string_hours)
float_rate = float(string_rate)
regular_pay = float_hours * float_rate

if float_hours > 40:
    print("overtime")
    overtime_pay = (float_hours - 40.0) * (float_rate * 1.5)
    # this determines how many hours of overtime by subtracting 40 from the amount of total hours worked. The program then multiplies the hourly wages by 1.5 and calculates the pay for the overtime hours.
    printed_overtime_pay = str(overtime_pay)
    regular_pay = 40 * float_rate
    print("amount earned from overtime: " + printed_overtime_pay)
    total_pay = regular_pay+overtime_pay
    total_pay = str(total_pay)
    print("Total Pay: " +total_pay)

else:
    print("regular")
    print(regular_pay)



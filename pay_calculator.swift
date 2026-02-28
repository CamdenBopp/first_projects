var overtime = false
var overtimeRate = 0.00
var totalPay = 0.00
var overTimeTotal = 0.00
print("Enter hours worked: ")
if let numberOfHours = readLine(), let hoursWorked = Int(numberOfHours) {
    print("Enter hourly rate in dollars: ")
    if let hourlyRate = readLine(), let hourlyRate = Double(hourlyRate) {
        if hoursWorked <= 40 {
            overtime = false
            totalPay = Double(hoursWorked) * hourlyRate
        }
        else if hoursWorked > 40 {
            overtime = true
            overtimeRate = hourlyRate * 1.5
            overTimeTotal = overtimeRate * Double(hoursWorked - 40)
            totalPay = (40.0 * hourlyRate) + overTimeTotal
        }
    }
}
print(overtime)
print(totalPay)

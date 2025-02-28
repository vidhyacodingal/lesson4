days = int(input("Enter the number of days"))
years = days//365
rem_days= days%365
months = days//30
rem_mdays= days%30
print("no of years in", days ,"is ", years , " year and ", rem_days , "days")
print("no of months in", days ,"is ", months , " months and ", rem_mdays , "days")
# take marks as input from user
print("Enter Marks Obtained in 4 Subjects out of 100: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
Spanish = int(input("hindi :"))

# Let's calculate the percentage of marks
sum = math+english+science+Spanish
print("sun of math,english,science and hindi",sum)

perc = (sum/400)*100

print("Percentage Mark = ",perc)

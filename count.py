amt = int(input("Enter the amount"))
note1 = amt//100
print("Number of 100 are", note1)
note2 = (amt%100)//50
print("Number of 50s are", note2)
note3 = (amt%50)//10
print("Number of 10s are", note3)
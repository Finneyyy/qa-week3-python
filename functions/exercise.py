def grade(name,final_exam):
    return f"Hi {name}, your final grade is: {final_exam}"

homework=int(input("Enter your homework score: "))/25    
assessment=int(input("Enter your assessment score: ")) /50
final_exam= (assessment+homework) /100

'''
if(final_exam >=80):
    print ("A")
elif(final_exam >=55):
    print("B")
elif(final_exam >=40):
    print("C")
elif(final_exam >=35):
    print("D")
else:
    print("You've failed.")
'''
print(grade(name="Eoin", final_exam=final_exam))
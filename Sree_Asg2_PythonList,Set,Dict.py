#-------- List (Creation, Modification and Access -----------------
#----- 1. List Creation

age_list = [23,19,25,27,32]
name_list = ["Abi","Kiran","Vasu","Riya","Hema"]
print("1.a) Age List :", age_list)
print("1.b) Name List :", name_list)

#----- 2. List Operations / Modifications
name_list.append("Yazhini")
print("2.a) Added Yazhini   :", (name_list))
age_list.insert(2,30)
print("2.b) Inserted Age    :", (age_list))
name_list.remove("Yazhini")
print("2.c) Removed Yazhini :", (name_list))
age_list.pop()
print("2.d) After Popped    :", (age_list))
age_list.extend([29,30,26])
print("2.e) Extented Age List :", (age_list))
age_list.sort(reverse=True)
print("2.f) Sorted Descending :", (age_list))
print("2.g) Maximum age :",max(age_list),"\n Minimum age :",min(age_list),
      "\n Sum of Age  :",sum(age_list))

#------ 3. Accessing List Elements
print("3.a) First Element :",(name_list[0]))
print("3.b) Last Element  :",(name_list[-1]))
print("3.c) Print Element :",(name_list[2:5:]))
name_list.reverse()
print("3.d) Reversed Element :", (name_list))


#----------- Dictionary (Creation, Modification and Access) ------------------

student_marks = {
    "Abi": 81,
    "Kiran": 92,
    "Vasu": 89,
    "Riya": 83,
    "Hema": 91
}
print("Students & Marks : ",student_marks)

print("Vasu Marks : ",student_marks["Vasu"])

#----- Adding new student 
student_marks.update({"Janani" : 80})
print("Students & Marks : ",student_marks)

#---- Update the mark of any one older student to 82
student_marks.update({"Abi" : 82})
print("Updated Students & Marks : ",student_marks)

#---- Print all keys, values, and key-value
print("Keys --: ",student_marks.keys())
print("Values --: ",student_marks.values())
print("Items --: ",student_marks.items())


#-----------  Sets (Operations) -----------------
my_set = {'a','e','i','o','u','a','a','i'}
print(my_set)

# my_set.update[4] = 's' ---- "ERROR"

#------ Create two sets 
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
print("set1 : ",set1)
print("set2 : ",set2)

#------ Union and Intersection two sets
print("Union : ",(set1 | set2))
print("Intersection : ",(set1 & set2))

#------------ (IF, ELIF, ELSE) ---------------
stu_na = input("Enter Student name : " )
stu_sc = int(input("Enter the Score out of 10 : "))
if stu_sc > 7 and stu_sc <= 10:
      print("Hi! " ,stu_na, "Your Score", stu_sc, "is Above average. " \
      "\n  Excellent performance! Keep up the good work")
elif stu_sc >= 4 and stu_sc <= 7 :
      print("Hi! " ,stu_na, "Your Score", stu_sc, "is Average. " \
      "\n  Good effort! Keep practicing, there's room for improvement")
elif stu_sc < 4 and stu_sc >= 0 :
      print("Hi! " ,stu_na, "Your Score", stu_sc, "is Below average . " \
      "\n  Need to improve your performance. Consistent practice will lead to better results")
else :
      print("Your Score is Invalid !")
##Start
first_dish = input("first dish name?\n")
first_price = int(input("What is the price of the dish?\n"))
second_dish = input("second dish name?\n")
second_price = int(input("What is the price of second the dish?\n"))
third_dish = input("third dish name?\n")
third_price = int(input("What is the price of the third dish?\n"))
original_price = first_price + second_price + third_price
## Customer info
name = input("What is your name\n")
student_status = input("Do you have a student ID(yes/no)\n")
is_student = 'yes' in student_status.lower()
order_time = int(input("When was the order made?\n"))

is_large = original_price >= 150000
large_discount = original_price*0.95*is_large
print(large_discount, "Large discount")
student_discount = original_price*0.85*is_student 
print(student_discount, "student discount")
happy_hour = order_time >= 14 and order_time <= 17
main_discount = student_discount * (student_discount >= happy_hour) + happy_hour * (happy_hour > student_discount)
print(main_discount, "Main discount")

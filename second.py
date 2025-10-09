##Start
first_dish = input("first dish name?\n")
first_price = int(input("What is the price of the dish?\n"))
how_many_first = int(input("How many meals?\n"))

second_dish = input("second dish name?\n")
second_price = int(input("What is the price of second the dish?\n"))
how_many_second = int(input("How many meals?\n"))

third_dish = input("third dish name?\n")
third_price = int(input("What is the price of the third dish?\n"))
how_many_third = int(input("How many meals?\n"))

original_price = how_many_first*first_price + how_many_second*second_price + how_many_third*third_price
## Customer info
name = input("What is your name\n")
student_status = input("Do you have a student ID(yes/no)\n")
is_student = 'yes' in student_status.lower()
order_time = int(input("When was the order made?\n"))

is_large = original_price >= 150000
large_discount = original_price*0.95*is_large
print(large_discount, "Large discount")
student_discount = original_price*0.85*is_student 
happy_hour = order_time >= 14 and order_time <= 17
main_discount = student_discount * (student_discount >= happy_hour) + happy_hour * (happy_hour > student_discount)
print(main_discount, "Main discount")

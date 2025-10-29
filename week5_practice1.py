names = ["Alice", "Bob", "Charlie", "David", "me"]
student_scores = [88, 92, 99, 95, 99]

def find_best_student(student_names, student_scores):
    highest_index = 1
    max_score = max(student_scores)
    for i in student_scores:
        if i == max_score:

            for j in range(highest_index-1,highest_index):
                ## For the top student
                student_scores = names[j:j+1]
                converter = "".join(student_scores)
                
                ## For tie
                student_scores.remove()
                another_max_score = max(student_scores)
                if max_score == another_max_score:
                    print("There's a tie")
                else:
                    print("There's a winner")
                ## For practice


            return print(f"Top student is: {converter}\nTop student in a tie is: nullpo\nResult for empty lists: nullpo")
        else:
            highest_index += 1
            continue
    return
find_best_student(names, student_scores)

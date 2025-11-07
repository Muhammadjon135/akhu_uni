employees = ["Alice", "Bob", "Charlie", "David"]
scores = [70, 95, 88, 74]
update_info = ["Alice", 72]
min_required_score = 75
high_perf_score = 90


unchanged_employess = employees[:]
unchanged_scores = scores[:]
def update_employee_score(employees, scores, employee_name, new_score):
    for i in range(len(employees)):
        if employee_name == employees[i]:
            scores[i] = new_score
            return True
        return False


def remove_underperforming(employees, scores, min_score): 
    for i in range(len(scores) - 1, -1, -1):
            if scores[i] < min_score:
                employees.pop(i)
                scores.pop(i)


def group_by_performance(employees, scores, high_performer_threshold):
    high_performers = []
    core_contributors = []
    counter = 0
    for score in scores:
        if score >= high_performer_threshold:
            high_performers.append(employees[counter])
        else:
            core_contributors.append(employees[counter]) 
        counter += 1
    return high_performers, core_contributors


def run_performance_review(initial_employees, initial_scores, employee_to_update, min_performance_score, high_performer_score):
    employees = []
    scores = []
    for i in range(len(initial_employees)):
        employees.append(initial_employees[i])
        scores.append(initial_scores[i])
    update_employee_score(employees, scores, employee_to_update[0], employee_to_update[1])
    remove_underperforming(employees, scores, min_performance_score)
    high_performers, core_contributors = group_by_performance(employees, scores, high_performer_score)
    return high_performers, core_contributors

high_performers, core_contributors = run_performance_review(employees, scores, update_info, min_required_score, high_perf_score)


print(f"\nhigh_performers: {high_performers}")
print(f"core_contributors: {core_contributors}\n")
print("Original lists unchanged:")
print(f"employees: {unchanged_employess}")
print(f"scores: {unchanged_scores}")

staff = [
    {'emp_id': 101, 'department': "Sales"},
    {'emp_id': 102, 'department': "IT"},
    {'emp_id': 103, 'department': "HR"}   
]

submitted = [101, 103, 500]
def create_staff_dict(staff_list):
    return {line['emp_id']: line['department'] for line in staff_list}

def audit_submissions(staff_dict, submitted_ids):
    submitted, staff_dict = set(submitted_ids), set(staff_dict)
    return (staff_dict - submitted), (submitted - staff_dict)

def format_reminders(staff_dict, missing_set):
    missing_set = list(missing_set)
    missing_set.sort()
    reminders = [f"REMINDER: Staff #{id} ({staff_dict[id]})" for id in missing_set]
    return reminders

staff_creation = create_staff_dict(staff)
missing, invalid = audit_submissions(staff_creation, submitted)
formatting_func = format_reminders(staff_creation, missing)
print(f"Missing Timesheets: {missing}")
print(f"Invalid IDs: {invalid}")
print(f"Report: {formatting_func}")

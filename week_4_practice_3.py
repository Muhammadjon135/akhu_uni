print(f"TIME CONVERTER AND SCHEDULER")
print(f"{"="*40}")
def hours_to_minutes(hours):
    return hours*60
def minutes_to_seconds(minutes):
    return minutes*60
def total_seconds(hours, minutes, seconds):
    total_of_seconds = hours*3600 + minutes*60 + seconds
    return total_of_seconds
def format_time(total_minutes):
    hours = total_minutes//60
    minutes = total_minutes%60
    return f"{hours} hours and {minutes} minutes"
def can_fit_task(available_hours, task_hours, task_minutes):
    return available_hours*60 > task_hours*60 + task_minutes
def schedule_summary(task_name, hours, minutes):
    pass
hours = int(input("Please enter hours: "))
minutes = hours_to_minutes(hours)

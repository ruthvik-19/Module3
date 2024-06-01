
# User input for current time in hours
current_time = int(input("What time is it right now(hour)? "))
# User inputs in how many hours they want the alarm to go off in
hours_until_alarm = int(input("How many hours do you want to wait for the alarm? "))

# Logic for calculatiing time when alarm goes off
total_hours = current_time + hours_until_alarm
time_of_alarm = total_hours % 24

print(time_of_alarm)
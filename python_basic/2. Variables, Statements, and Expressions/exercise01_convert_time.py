# enter time you want to convert
str_seconds = input('Please enter the number of seconds you want to convert: ')
total_seconds = int(str_seconds)

# calculate hours
hours = total_seconds // 3600

# calculate minutes
seconds_still_remaining = total_seconds % 3600
minutes = seconds_still_remaining // 60

# calculate seconds final remaining
seconds_final_remaining = seconds_still_remaining % 60

# print converted time
print('Hours:', hours, 'Minutes:', minutes, 'Seconds:', seconds_final_remaining)
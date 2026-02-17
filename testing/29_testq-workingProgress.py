


# code question 29
#A database contains user data uploads with varying submission times. To process the latest information first, a function is needed to identify the most recent upload time.
#
#Complete the Python function find_latest. The function should accept an unordered list of user upload time strings, convert each string value into a datetime object using the provided date_format pattern, and return the most recent upload time as a datetime object.
#
#Only the find_latest function will be graded for this assessment. The function should work for any patterned strings passed from a list to find_latest beyond the examples provided.
#
#Example: If the stored user upload values are
#
#['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
#
#the expected return is
#
#2023-12-16 11:20:00
#
#Example: If the stored user upload values are
#
#['12/20/2023 02:00 AM', '12/18/2023 10:30 AM', '12/16/2023 07:45 PM', '12/14/2023 04:15 PM']
#
#the expected return is
#
#2023-12-20 02:00:00
from datetime import datetime
#
def find_latest(submissions):
    # Specify a date format
    original_format = '%m/%d/%Y %I:%M %p'
    dates = [datetime.strptime(s, original_format) for s in submissions]
    latestDate = max([datetime.strftime(date, "%Y-%m-%d %H:%M:%S") for date in dates])
    return latestDate
    # Convert string values into datetime objects.
 #   for dateTimeString in submissions:
#     dateTimeObject = datetime.strptime(dateTimeString, original_format) 
    #convert_datetimeObject = dateTimeObject.strftime("%y-%m-%d %h:%m:%s")
#    finalResult = [i for i, dateAndTimes in submissions datetime.strptime(dateAndTimes, original_format)]
#    return finalResult 
    # Determine and return latest
#    return convert_datetimeObject 
# You may alter the code below to test your solution or print help documentation.
# Only the find_latest function will be graded for this assessment.

#indexes = [i for i, usage in enumerate(cpu_list) if usage > 90]
submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print(find_latest(submission_timestamps))
# help(datetime.strptime)
#---

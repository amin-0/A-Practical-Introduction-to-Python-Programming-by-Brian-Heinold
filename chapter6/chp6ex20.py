'''
Write a program that converts a time from one time zone to another. 
The user enters the time in the usual American way, such as 3:48pm or 11:26am. 
The first time zone the user enters is that of the original time and the second is the desired time zone. 
The possible time zones are Eastern, Central, Mountain, or Pacific.
Time: 11:48pm
Starting zone: Pacific
Ending zone: Eastern
2:48am
'''

#GEt user's input and convert them to lower case
time = input('Time: ').lower()
start = input('Starting zone: ').lower()
end = input('Ending zone: ').lower()

hour_min = time[:-2] # Obtain the hour and mins
hour = int(hour_min[:hour_min.index(':')]) # Obtain the hour and convert to integer
min = int(hour_min[hour_min.index(':')+1 :]) # Obtain minute and convert to integer
period = time[-2:] # Obtain period either am or pm

if period == 'pm': # Change the time to 24 hours format
    hour = hour + 12
elif period == 'am':
    pass
else:
    print('Invalid time zone !!!!!')

#Convert the hour based on the start and end time zones
if start == 'pacific':
    if end == 'mountain':
        hour = hour + 1
    elif end == 'central':
        hour = hour + 2
    elif end == 'eastern':
        hour = hour + 3

elif start == 'mountain':
    if end == 'pacific':
        hour = hour - 1
    elif end == 'central':
        hour = hour + 1
    elif end == 'eastern':
        hour = hour + 2

elif start == 'central':
    if end == 'pacific':
        hour = hour - 2
    elif end == 'mountain':
        hour = hour - 1
    elif end == 'eastern':
        hour = hour + 1

elif start == 'eastern':
    if end == 'pacific':
        hour = hour - 3
    elif end == 'mountain':
        hour = hour - 2
    elif end == 'central':
        hour = hour - 1

#Obtain the new time period after conversion
if hour >= 12:
    period = 'pm'
else:
    period = 'am'

# Obtain the new hour in a 12 hours format
if hour % 12 == 0:
    hour = 12
else:
    hour = hour % 12

#Print result
print(f'{hour}:{min}{period}')
def add_time(start_time, duration, start_day=''):
    start_time_list = (start_time.replace(':', ' ')).split(' ')
    start_day = start_day.title()
    start_hour = int(start_time_list[0])
    start_mins = int(start_time_list[1])
    am_pm = start_time_list[2]
    dur_list = duration.split(':')
    dur_hour = int(dur_list[0])
    dur_mins = int(dur_list[1])
    new_mins_tup = divmod((start_mins + dur_mins), 60)
    new_hour_tup = divmod((start_hour + dur_hour + new_mins_tup[0]), 12)
    


    if new_hour_tup[1] == 0:
        new_hour = str(new_hour_tup[1] + 12)
    else:
        new_hour = str(new_hour_tup[1])
    

    new_mins = str(new_mins_tup[1])
    if len(new_mins) == 1:
        new_mins = '0' + new_mins

    # Encode day of the week with dictionary:
    day_to_num = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    num_to_day = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    if start_day == '':
        if am_pm == 'AM':
            if new_hour_tup[0] % 2 == 0:
                new_am_pm = ' AM'
            else:
                new_am_pm = ' PM' 
            num_extra_days = str(new_hour_tup[0] // 2)
            if new_hour_tup[0] == 0:
                new_time = new_hour + ':' + new_mins + ' ' + am_pm
            elif new_hour_tup[0] == 1:
                new_time = new_hour + ':' + new_mins + ' PM'
            elif new_hour_tup[0] == 2:
                new_time = new_hour + ':' + new_mins + ' AM (next day)'
            elif new_hour_tup[0] == 3:
                new_time = new_hour + ':' + new_mins + ' PM (next day)'
            elif new_hour_tup[0] > 3:
                new_time = new_hour + ':' + new_mins + new_am_pm + ' (' + num_extra_days + ' days later)'
               
        elif am_pm == 'PM':
            if new_hour_tup[0] % 2 == 0:
                new_am_pm = ' PM'
            else:
                new_am_pm = ' AM'
            num_extra_days = str((new_hour_tup[0] // 2) + 1)
            if new_hour_tup[0] == 0:
                new_time = new_hour + ':' + new_mins + ' ' + am_pm
            if new_hour_tup[0] == 1:
                new_time = new_hour + ':' + new_mins + ' AM (next day)'
            if new_hour_tup[0] == 2:
                new_time = new_hour + ':' + new_mins + ' PM (next day)'
            elif new_hour_tup[0] > 2:
                new_time = new_hour + ':' + new_mins + new_am_pm + ' (' + num_extra_days + ' days later)'
            
        
    else:
        day_code = day_to_num[start_day]
        if am_pm == 'AM':
            if new_hour_tup[0] % 2 == 0:
                new_am_pm = ' AM'
            else:
                new_am_pm = ' PM' 
            new_day_code = (day_code + (new_hour_tup[0] // 2)) % 7
            if new_hour_tup[0] == 0:
                new_time = new_hour + ':' + new_mins + ' ' + am_pm + ',' + num_to_day[new_day_code]
            elif new_hour_tup[0] == 1:
                new_time = new_hour + ':' + new_mins + ' PM, ' + num_to_day[new_day_code]
            elif new_hour_tup[0] == 2:
                new_time = new_hour + ':' + new_mins + ' AM, ' + num_to_day[new_day_code] + ' (next day)'
            elif new_hour_tup[0] == 3:
                new_time = new_hour + ':' + new_mins + ' PM, '+ num_to_day[new_day_code] + ' (next day)'
            elif new_hour_tup[0] > 3:
                new_time = new_hour + ':' + new_mins + new_am_pm + ',' + num_to_day[new_day_code]
               
        elif am_pm == 'PM':
            if new_hour_tup[0] % 2 == 0:
                new_am_pm = ' PM'
            else:
                new_am_pm = ' AM'
            new_day_code = (day_code + ((new_hour_tup[0] + 1) // 2)) % 7
            
            num_extra_days = str((new_hour_tup[0] // 2) + 1)
            if new_hour_tup[0] == 0:
                new_time = new_hour + ':' + new_mins + ' ' + am_pm + ', ' + num_to_day[new_day_code]
            if new_hour_tup[0] == 1:
                new_time = new_hour + ':' + new_mins + ' AM, ' + num_to_day[new_day_code] + ' (next day)'
            if new_hour_tup[0] == 2:
                new_time = new_hour + ':' + new_mins + ' PM, ' + num_to_day[new_day_code] + ' (next day)'
            elif new_hour_tup[0] > 2:
                new_time = new_hour + ':' + new_mins + new_am_pm + ', ' + num_to_day[new_day_code] + ' (' + num_extra_days + ' days later)'

    return new_time

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'monDay'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))

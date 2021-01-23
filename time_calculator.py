def add_time(start, duration, day=None):
    days =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    convert = start_to_sec(start)
    convert1 = dur_to_sec(duration)
    final_sec = convert + convert1
    time_day = sec_to_time(final_sec) #[time, how many day after]
    
    day_later = ''
    if time_day[1] == 1:
        day_later = ' (next day)'
    elif time_day[1] >1:
        day_later = ' (' + str(time_day[1]) +' days later)'

    what_day = ''
    day_index = day_to_int(day, days)
    if day_index != None:
        for_day = int(time_day[1] + day_index) % 7
        what_day = ',' + ' ' + days[for_day].capitalize()

    new_time = time_day[0] + what_day + day_later
    return new_time

def add_zero(num):
    z = str(int(num))
    if len(z) == 1:
        z = '0' + str(num)
    return z
        
def day_to_int(day, days):
    if day != None:
        day = day.lower()
        for for_day in range(len(days)):
            if days[for_day] == day:
                di = for_day
                break
        return di
    

def start_to_sec(time):
    hour1 = time.split(':') #[11, 20 AM]
    min1 = hour1[1].split(' ')
    if min1[1] == "AM":
        if hour1[0] == '12':
            hour1[0] == '00'
    elif min1[1] == "PM":
        if hour1[0] != '12':
            hour1[0] = int(hour1[0]) + 12
    hour_to_sec = int(hour1[0]) * 3600
    min_to_sec = int(min1[0]) * 60 
    total_sec = hour_to_sec + min_to_sec
    return total_sec
    
def dur_to_sec(time1):
    hour_min = time1.split(':')
    hour_to_sec1 = int(hour_min[0]) * 3600
    min_to_sec1 = int(hour_min[1]) * 60 
    total_sec1 = hour_to_sec1 + min_to_sec1
    return total_sec1
    
def sec_to_time(final_sec):
    mode = 'AM'
    
    rem = final_sec % 3600
    cal_min = int(rem/60)
    cal_hour = int(final_sec /3600)
    total_days = int(cal_hour / 24)
    h24 = cal_hour % 24
    h12 = h24
    if h24 >= 12:
        mode = 'PM'
        if h24 > 12:
            h12 = h24 - 12
    elif h24 == 0:
        h12 = h24 + 12
    time = str(h12) + ':' + add_zero(cal_min) + ' ' + mode
    return (time, int(total_days))
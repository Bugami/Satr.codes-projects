def convert_time(time):
    """ Convert time from 12h and 24h format"""
    if 'am' in time:
        time = time[:5]
        if time[:2] == '12':
            return '0'+time[2:]
        else:
            return time
    elif 'pm' in time:
        time = time[:5]
        if time[:2] == '12':
            return time
        elif time[:2] in '10 11':
            t1 = int(time[:2])+12
            time=str(t1)+time[2:]
            return time
        else:
            t1 = int(time[0])+12
            time=str(t1)+time[1:]
            return time        
    else:
        if time[:2] in '13 14 15 16 17 18 19 20 21 22 23':
            t1 = int(time[:2]) - 12
            time = str(t1) + time[2:] + ' pm'
            return time
        elif time[:2] in '12':
            return time + " pm"
        elif time[0] in '0':
            return '12' + time[1:] + ' am'
        else:
            return time + ' am'
    pass

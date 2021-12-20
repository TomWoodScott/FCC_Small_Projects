def add_time(start, duration, day = None):

    day_di = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    if day is not None:
        day = str(day).lower()
        start_day = day_di[day]

    start_split = str(start).split(":")
    duration_split = str(duration).split(":")
    am_pm = start_split[1][-2:]
    days = 0

    dirty_time_hours = int(int(start_split[0])+int(duration_split[0]))
    dirty_time_minutes = int(start_split[1][:-3]) + int(duration_split[1])

    if dirty_time_minutes >= 60:
        dirty_time_hours += 1
        dirty_time_minutes -= 60

# N0 days
    if dirty_time_hours >= 24:
        while dirty_time_hours >= 24:
            dirty_time_hours -= 24
            days += 1

        if dirty_time_hours >= 12:
            dirty_time_hours -= 12

            if am_pm == 'PM':
                days += 1
                am_pm = f'AM ({days} days later)'
            else:
                if days != 1:
                    am_pm = f'PM ({days} days later)'
                else:
                    am_pm = f'PM (next day)'

        else:
            if days != 1:
                am_pm = f'{am_pm} ({days} days later)'
            else: am_pm = f'{am_pm} (next day)'

# Next day and fix AM/PM
# if gone through previous loop this on will be skipped
    if dirty_time_hours >= 12:
        dirty_time_hours -= 12
        if am_pm == 'PM':
            am_pm = 'AM (next day)'
            days += 1
        else:
            am_pm = 'PM'

    hours = dirty_time_hours
    minutes = dirty_time_minutes

    # fix midday bug and additional 0 for '-0:-0 xM'
    if len(str(minutes)) == 1:
        minutes = str(minutes).rjust(2, "0")
    if am_pm[:2] == 'PM':
        if hours == 12:
            hours = "12"
        elif hours == 0:
            hours = 12
    elif hours == 0:
        hours = "12"

    if day is not None:
        day_end = start_day + days
        while day_end > 7:
            day_end -= 7

        day_end = list(day_di.keys())[list(day_di.values()).index(day_end)].capitalize()
        am_pm_cont = am_pm[3:].strip()
        am_pm_ = am_pm[:3].strip()
        if am_pm_cont != '':
            return f'{hours}:{minutes} {am_pm_}, {day_end} {am_pm_cont}'
        else:
            return f'{hours}:{minutes} {am_pm_}, {day_end}'

    return f'{hours}:{minutes} {am_pm}'

# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.


def time_conversion(s):
    if s[0:2] == '12':
        return s[0:-2] if s[-2] == 'P' else '00' + s[2:-2]

    return s[0:-2] if s[-2] == 'A' else str(int(s[0:2]) + 12) + s[2:-2]

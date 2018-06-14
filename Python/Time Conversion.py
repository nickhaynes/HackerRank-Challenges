def timeConversion(s):
    i = s[-2]
    h = int(s[0:2])
    min = s[3:5]
    sec = s[6:8]
    if i == "P":
        if h < 12:
            h = h + 12
            hour = str(h)
        elif h == 12:
            hour = str(h)
    elif i == "A":
        if h == 12:
            hour = '00'
        elif h < 10:
            hour = '0' + str(h)
        else:
            hour = str(h)
    return hour + ':' + min + ':' + sec
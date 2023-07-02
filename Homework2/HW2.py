"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""

import datetime


def find(s):
    calendar_month = {'january': 1,
                      'february': 2,
                      'march': 3,
                      'april': 4,
                      'may': 5,
                      'june': 6,
                      'july': 7,
                      'august': 8,
                      'september': 9,
                      'october': 10,
                      'november': 11,
                      'december': 12
                      }
    x = datetime.datetime.now()
    c = x.strftime("%x")
    c1 = c.split("/")
    c_month = int(c1[0])
    c_date = int(c1[1])
    c_year = int(x.strftime("%Y"))
    s1 = s.split(",")
    s2 = s1[0].split()
    if len(s2) == 3:
        if s2[0].lower() in calendar_month.keys():
            month = calendar_month[s2[0].lower()]
            s_date = s2[1][:-1]
            if s_date.isdigit():
                date = int(s_date)
                if 1 <= date <= 31:
                    if s2[2].isdigit():
                        year = int(s2[2])
                        if year < c_year:
                            return f"{month}/{date}/{year}"
                        elif year == c_year:
                            if month < c_month:
                                return f"{month}/{date}/{year}"
                            elif month == c_month:
                                if date <= c_date:
                                    return f"{month}/{date}/{year}"

    else:
        exit()


f1 = open("parsedDates.txt", "w")
with open('inputDates.txt', 'r') as f:
    while True:
        b = f.readline()
        if b != '-1':
            result = find(b)
            if result:
                f1.write(result)
                f1.write("\n")
        else:
            break
f1.close()

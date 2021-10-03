from datetime import date


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
 
 
# To store number of days in all months from
# January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
 
# This function counts number of leap years
# before the given date
 
 
def countLeapYears(d):
 
    years = d.y
 
    # Check if the current year needs to be considered
    # for the count of leap years or not
    if (d.m <= 2):
        years -= 1
 
    # An year is a leap year if it is a multiple of 4,
    # multiple of 400 and not a multiple of 100.
    return int(years / 4) - int(years / 100) + int(years / 400)
 
 
# This function returns number of days between two
# given dates
def getDifference(dt1, dt2):
 
    # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'
 
    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d
 
    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
 
    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(dt1)
 
    # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'
 
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
 
    # return difference between two counts
    return (n2 - n1)
 


current_date = [ int(x) for x in str(date.today()).split('-') ]
 
ref_date = Date(1, 1, 2000)
current_date = Date(current_date[2], current_date[1], current_date[0])
test = Date(30, 8, 1956)
 
# print("Today is:", current_date)

D_difference_of_days = getDifference(ref_date, test)
print("No. of days from January 1, 2000:", D_difference_of_days, "days")


def calculate_f(planet):
  P_orbital_period = {
    'Mercury': 87.97,
    'Venus': 224.64,
    'Earth': 365.26,
    'Mars': 686.79,
    'Jupiter': 4332.80,
    'Saturn': 10759.7
  }

  r = (D_difference_of_days/P_orbital_period[planet])
  # print('r for', planet, 'is', r)

  if r >= 0:
    s = int(r) * -1
  else:
    s = int(str(int(r))[1:]) + 1
    # print('s for', planet, 'is', s)

  f = float(r) + float(s)
  # print('f for', planet, 'is', f)
  return float(str(f)[:4])

print('Earth: ', calculate_f('Earth'))
print('Venus: ', calculate_f('Venus'))



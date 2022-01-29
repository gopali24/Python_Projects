from numpy import dtype
import datetime as dt

def valid_date(y,m,d):
    correctDate = None
    try:
        newDate = dt.datetime(y,m,d)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate

def age_calc(y,m,d,y1,m1,d1):
    dt1 = dt.date(y1,m1,d1)
    dt2=dt.date(y,m,d)
    
    daysLeft = dt1-dt2
    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt=int(years)

    months=(years-yearsInt)*12
    monthsInt=int(months)

    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    print(f"Difference betwen the 2 dates is: {yearsInt} years {monthsInt} months {daysInt} days")

def find_greater(y,m,d,y1,m1,d1):
    dt1 = dt.date(y,m,d)
    dt2 = dt.date(y1,m1,d1)
    if dt1>dt2:
        age_calc(y1,m1,d1,y,m,d)
    else:
        age_calc(y,m,d,y1,m1,d1)


y,m,d = input("Enter first date in year month date format: ").strip().split()
y1,m1,d1 = input("Enter second date in year month date format: ").strip().split()
y=int(y)
m=int(m)
d=int(d)
y1=int(y1)
m1=int(m1)
d1=int(d1)
if valid_date(y,m,d) and valid_date(y1,m1,d1):
    # find_greater(y,m,d,y1,m1,d1)
    age_calc(y,m,d,y1,m1,d1)
else:
    print("Enter a valid date -_-")
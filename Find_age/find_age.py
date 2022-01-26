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

def age_calc(y,m,d):
    today = dt.datetime.now().date()
    dob=dt.date(y,m,d)
    if dob>today:
        print("Enter a valid date -_-")
    else:
        age = int((today-dob).days/365.25)
        if age!=0:
            print(f"Your age as of today is: {age} years.")
        else:
            daysLeft = today - dob
            years = ((daysLeft.total_seconds())/(365.242243600))
            years = abs(years)
            yearsInt=int(years)

            months=(years-yearsInt)*12
            months = abs(months)
            monthsInt=int(months)
            print(f"Yoour age as of today is: {monthsInt} months.")

y,m,d = input("Enter your Date of birth in year month date format: ").strip().split()
y=int(y)
m=int(m)
d=int(d)
if valid_date(y,m,d):
    age_calc(y,m,d)
else:
    print("Enter a valid date -_-")
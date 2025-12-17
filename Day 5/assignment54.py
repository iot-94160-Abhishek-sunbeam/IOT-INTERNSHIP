
import datetime as dt


current_date_time = dt.datetime.now()
print ("Current Date and Time =", current_date_time)


year = current_date_time.year
print("current year =", year)


month = current_date_time.month
print("current month =", month)


day = current_date_time.day     
print("current day =", day)


day = current_date_time.strftime("%A")
print("day of week =", day)
import datetime

date = datetime.datetime.now()
dayend = "th "
if date.day%10 == 1:
	dayend = "st "
elif date.day%10 == 2:
	dayend = "nd "
elif date.day%10 == 3:
	dayend = "rd "

first_half_date = date.strftime("%A, %B %d")
second_half_date = date.strftime("%Y at %I:%M %p")

print(first_half_date+dayend+second_half_date)

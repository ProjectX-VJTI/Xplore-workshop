# Datetime Module
# ---------------
# Supplies classes for manipulating dates and times.

import datetime

# 1. Getting Current Date and Time
# datetime.datetime represents both date (Y, M, D) and time (H, M, S, MS)

now = datetime.datetime.now()
print("Current Date & Time:")
print(now)                  # e.g., 2026-02-26 17:15:44.123456
print(now.year, now.month, now.day)

# 2. Creating Specific Dates
# datetime.date represents just the date (Year, Month, Day)

my_bday = datetime.date(2000, 5, 15)
print("\nSpecific Date:")
print(my_bday)              # 2000-05-15

# 3. Timedelta (Date Math)
# Represents the difference between two dates or times.
# You can use it to add or subtract days, weeks, etc.

today = datetime.date.today()
# Create a duration of 10 days
ten_days = datetime.timedelta(days=10)

future_date = today + ten_days
past_date = today - ten_days

print("\nTimedelta Math:")
print("Today:", today)
print("10 Days from now:", future_date)
print("10 Days ago:", past_date)

# Difference between two dates
time_lived = today - my_bday
print(f"Days since my birthday: {time_lived.days} days")

# 4. Formatting and Parsing Dates (strftime & strptime)
# strftime: String Format Time (Object to String)
# strptime: String Parse Time (String to Object)

# Formatting: Converting datetime object to a readable string
formatted_now = now.strftime("%A, %B %d, %Y - %I:%M %p")
print("\nFormatted Date (strftime):")
print(formatted_now)        # e.g., Thursday, February 26, 2026 - 05:15 PM

# Parsing: Converting string back to a datetime object
date_string = "25 December, 2026"
parsed_date = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("\nParsed Date (strptime):")
print(parsed_date)          # 2026-12-25 00:00:00
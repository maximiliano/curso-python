# help('datetime')
from datetime import date, datetime, timedelta

today = date.today()
now = datetime.now()

today.day
now.minute
today + timedelta(days=30)

from calendar import calendar, monthrange

calendar(2013)
monthrange(2013, 2)



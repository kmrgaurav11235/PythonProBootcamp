import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
print(year)
print(type(year))
print(f"{now.month} {now.weekday()} {now.hour}:{now.minute}")

date_of_birth = dt.datetime(year=1488, month=7, day=13, hour=14, minute=8)
print(date_of_birth)

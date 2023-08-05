import datetime

close = datetime.time(1, 0)
open = datetime.time(2, 0)
now = datetime.time(2, 0)


def method():
    return (close < open and (now >= open or now <= close)) or (open <= now <= close)


print(method())

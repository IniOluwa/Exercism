from datetime import timedelta


def add_gigasecond(day):
    Gs = timedelta(seconds=10**9)
    return day + Gs
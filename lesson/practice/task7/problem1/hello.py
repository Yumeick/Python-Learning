def f1(year):
    if year%4==0 or (year%400==0 and year%100!=0):
        return True
    else:
        return False
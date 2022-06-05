def solution(a, b):
    lst_day = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']
    lst_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    today = sum(lst_month[:a-1])+b

    return lst_day[today%7]
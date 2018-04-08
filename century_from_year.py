def centuryFromYear(year):
    if year in range (1, 2018):
        num = year%100
        century = (year-num)/100
        if num == 0:
            return century
        else:
            return century+1

centuryFromYear(2017)

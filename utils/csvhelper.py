def all_unique(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False


def isall_notnull(list):
    null = 0
    for item in list:
        if item == '':
            null = null + 1
    if null == 0:
        return True
    else:
        return False


def isall_null(list):
    notnull = 0
    for item in list:
        if item != '':
            notnull = notnull + 1
    if notnull == 0:
        return True
    else:
        return False


def isvalid_date(datestr):
    invalid_flag = 0
    if len(datestr) == 0:
        return True
    if len(datestr) != 8:
        invalid_flag = invalid_flag + 1

    year = int(datestr[0:4])
    month = int(datestr[4:6])
    day = int(datestr[6:])
    # print(year,month,day)

    if year < 1857 or year > 2030:
        invalid_flag = invalid_flag + 1

    if month > 12 or month == 0:
        invalid_flag = invalid_flag + 1

    if day > 31 or day == 0:
        invalid_flag = invalid_flag + 1

    if invalid_flag > 0:
        return False
    else:
        return True


def isvalid_datelist(list):
    valid_list = []
    for date in list:
        if isvalid_date(date):
            valid_list.append(date)
        else:
            print(date)

    if len(list) == len(valid_list):
        return True
    else:
        return False

# def isvalid_geo():
    #

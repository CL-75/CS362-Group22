##########
# Helper functions for my_datetime() function
##########

def get_str(month, day, yr):
    temp_date = str(month) + "-"

    if month < 10:
        temp_date = "0" + temp_date

    if day < 10:
        temp_date += "0"

    temp_date = temp_date + str(day) + "-" + str(yr)

    return temp_date

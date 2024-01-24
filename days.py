month = input("Enter a month: ")
day = int(input("Enter a day: "))
valid_months30days = ['April', 'June', 'September', 'November']
valid_months31days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
valid_months29days = ['February']

if month in valid_months31days and 1 <= day <= 31:
    if month == valid_months31days[0] and 1 <= day <= 31:
        print('Winter')
    elif month == valid_months31days[1] and 1 <= day <= 31:
        print('Winter')
    elif month == valid_months31days[2] and 1 <= day <= 31:
        print('Spring')
    elif month == valid_months31days[3] and 1 <= day <= 31:
        print('Spring')
    elif month == valid_months31days[4] and 1 <= day <= 31:
        print('Summer')
    elif month == valid_months31days[5] and 1 <= day <= 31:
        print('Autumn')
    elif month == valid_months31days[6] and 1 <= day <= 31:
        print('Autumn')
elif month in valid_months30days and 1 <= day <= 30:
    if month == valid_months30days[0] and 1 <= day <= 30:
        print('Spring')
    elif month == valid_months30days[1] and 21 <= day <= 30:
        print('Summer')
    elif month == valid_months30days[2] and 1 <= day <= 30:
        print('Spring')
    elif month == valid_months30days[3] and 1 <= day <= 30:
        print('Autumn')
elif month in valid_months29days and 1 <= day <= 29:
    if month == valid_months29days[0] and 1 <= day <= 29:
        print('Winter')
else:
    print('Invalid')

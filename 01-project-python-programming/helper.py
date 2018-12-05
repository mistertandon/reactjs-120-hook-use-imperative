CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

FILTER_DATA = { 'month':'month',
                'day':'day',
                'both':'both',
                'none':'none'}

MONTH_DATA = { 'jan':'January',
                'feb':'February',
                'mar':'March',
                'apr':'April',
                'may':'May',
                'jun':'June',
                'jul':'July',
                'aug':'August',
                'sep':'September',
                'oct':'October',
                'nov':'November',
                'dec':'December'}

DAY_DATA = {'0': 'sunday',
            '1': 'moday',
            '2': 'tuesday',
            '3': 'wednesday',
            '4': 'thursday',
            '5': 'friday',
            '6': 'saturday'}                

def get_user_city():
    while True:
        city_input = input('\nFor which city would you like to see data. Available cities are chicago, new york city, washington : \nType input : ')

        if city_input in CITY_DATA:
            city_val = city_input
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    return city_val


def get_user_filter():
    while True:
        filter_input = input('\nWould you like to filter the data by month, day, both or not at all.\nNote: Type "none" [all in lower case]\nAvailable options are [ month, day, both, none ]\nType input : ')

        if filter_input in FILTER_DATA:
            filter_val = filter_input
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    return filter_val


def get_month():
    while True:
        month_input = input('\nSelect month\n all => All, jan => January, feb => February, mar => March, apr => April, may => May, jun => June, jul => July, aug => August, sep => September, oct => October, nov => November, dec => December \n Note: Type jan to select January month\nType input : ')           

        if month_input in MONTH_DATA:
            month_val = MONTH_DATA[month_input]
            break
        else:
            print('You have entered incorrect option. Please try again...')

    return month_val


def get_day():
    while True:
        day_input = input('\nSelect day\n 0 => sunday, 1 => moday, 2 => tuesday, 3 => wednesday, 4 => thursday, 5 => friday, 6 => saturday\nNote: Type 6 to select saturday\nType input : ')

        if day_input in DAY_DATA:
            day_val = DAY_DATA[day_input]
            break
        else:
            print('You have entered incorrect option. Please try again...')

    return day_val
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

FILTER_DATA = { 'month':'month',
                'day':'day',
                'both':'both',
                'none':'none'}

MONTH_DATA = { 'all':'all',
                'jan':'January',
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
            '6': 'saturday',
            '7': 'all'}                

def get_user_city():
    while True:
        get_city = input('\nFor which city would you like to see data. Available cities are chicago, new york city, washington : \nType input : ')

        if get_city in CITY_DATA:
            city_val = get_city
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print('Selected city is: ', city_val)

    return city_val


def get_user_filter():
    while True:
        get_filter = input('\nWould you like to filter the data by month, day, both or not at all.\nNote: Type "none" [all in lower case]\nAvailable options are [ month, day, both, none ]\nType input : ')

        if get_filter in FILTER_DATA:
            filter_val = get_filter
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print('Selected filter option is: ', filter_val)

    return filter_val


def get_month():
    while True:
        get_month = input('\nSelect month\n all => All, jan => January, feb => February, mar => March, apr => April, may => May, jun => June, jul => July, aug => August, sep => September, oct => October, nov => November, dec => December \n Note: Type jan to select January month\nType input : ')           

        if get_month in MONTH_DATA:
            month_val = get_month
            break
        else:
            print('You have entered incorrect option. Please try again...')

    return MONTH_DATA[month_val]


def get_day():
    while True:
        get_day = input('\nSelect day\n 0 => sunday, 1 => moday, 2 => tuesday, 3 => wednesday, 4 => thursday, 5 => friday, 6 => saturday, 7 => all \nNote: Type 6 to select saturday\n')

        if get_day in DAY_DATA:
            day_val = get_day
            break
        else:
            print('You have entered incorrect option. Please try again...')

    return DAY_DATA[get_day]
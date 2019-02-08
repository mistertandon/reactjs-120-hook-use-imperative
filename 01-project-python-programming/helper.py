"""
CITY_DATA contains avaliable citites name in python dict
"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
FILTER_DATA contains available filter option
"""
FILTER_DATA = { 'month':'month',
                'day':'day',
                'both':'both',
                'none':'none'}

"""
MONTH_DATA contains list of months
"""

MONTH_DATA_REF = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

MONTH_DATA = {
    1: {
        'full_name': 'January',
        'value': 1
    },
    2: {
        'full_name': 'February',
        'value': 2
    },
    3: {
        'full_name': 'March',
        'value': 3
    },
    4: {
        'full_name': 'April',
        'value': 4
    },
    5: {
        'full_name': 'May',
        'value': 5
    },
    6: {
        'full_name': 'June',
        'value': 6
    },
    7: {
        'full_name': 'July',
        'value': 7
    },
    8: {
        'full_name': 'August',
        'value': 8
    },
    9: {
        'full_name': 'September',
        'value': 9
    },
    10: {
        'full_name': 'October',
        'value': 10
    },
    11: {
        'full_name': 'November',
        'value': 11
    },
    12: {
        'full_name': 'December',
        'value': 12
    }
}

"""
DAY_DATA_REF contains list of weekdays where monday has 0 value
"""
DAY_DATA_REF = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}


"""
DAY_DATA contains list of weekdays where monday has 0 value
"""
DAY_DATA = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: 'sunday'
}

"""
DAY_DATA contains list of weekdays where monday has 0 value
"""
USER_RESPONSE = {
    'no': 'No',
    'yes': 'Yes'
}


def display_raw_data_request():
    """
    Asks user if he would like to see raw lines of data.

    Returns:
        user_res (str) - User response
    """
    while True:
        user_res = input('\n Would you like to see raw lines of data\n Enter either yes OR no\n Type input : ')
        user_res_sanitized = user_res.lower()

        if user_res_sanitized in USER_RESPONSE.keys():
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    return user_res_sanitized


def get_user_city():
    """
    Asks user to provide input for city.

    Returns:
        city_val (str) - name of the city to analyze
    """
    while True:
        city_input = input('\n For which city would you like to see data. Available cities are chicago, new york city, washington\n Type input : ')
        city_input_sanitized = city_input.lower()

        if city_input_sanitized in CITY_DATA:
            city_val = city_input_sanitized
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print(' Selected city is: ', city_val)
    
    return city_val


def get_user_filter():
    """
    Asks user to provide filter option among available options i.e. month, day, both or none

    Return:
        filter_val (str) - filter value
    """
    while True:
        filter_input = input('\n Would you like to filter the data by month, day, both or not at all.\n Available options are [ month, day, both, none ]\n Type input : ')
        filter_input_sanitized = filter_input.lower()

        if filter_input_sanitized in FILTER_DATA:
            filter_val = filter_input_sanitized
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print(' Selected filter is: ', filter_val)

    return filter_val


def get_month():
    """
    Asks user to provide month value as a filter option

    Returns:
        month_val (str) - Month value based on which filter option would perform.
    """
    while True:
        month_input = input('\n Select month\n January, February, March, April, May, June, July, August, September, October, November, December\n Type input : ')
        month_input_sanitized = month_input.lower()

        if month_input_sanitized in MONTH_DATA_REF:
            month_val = MONTH_DATA_REF[month_input_sanitized]
            break
        else:
            print(' You have entered incorrect option. Please try again...')
    
    print(' Selected Month is: ', MONTH_DATA[month_val]['full_name'])

    return month_val


def get_day():
    """
    Asks user to provide day option, later would used as a filter.

    Returns:
        day_input (int) - weekday value based on which filter option would perform.
    """
    while True:
        day_input = input('\n Select day\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n Type input : ')
        day_input_sanitized = day_input.lower()

        if day_input_sanitized in DAY_DATA_REF:
            break
        else:
            print(' You have entered incorrect option. Please try again...')

    print(' Selected Day is: ', day_input_sanitized)

    return DAY_DATA_REF[day_input_sanitized]

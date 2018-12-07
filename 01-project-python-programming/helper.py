CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

FILTER_DATA = { 'month':'month',
                'day':'day',
                'both':'both',
                'none':'none'}

MONTH_DATA = { 1:{
                    'full_name':'January',
                    'value':1
                },
                2:{
                    'full_name':'February',
                    'value':2
                },
                3:{
                    'full_name':'March',
                    'value':3
                },
                4:{
                    'full_name':'April',
                    'value':4
                },
                5:{
                    'full_name':'May',
                    'value':5
                },
                6:{
                    'full_name':'June',
                    'value':6
                },
                7:{
                    'full_name':'July',
                    'value':7
                },
                8:{
                    'full_name':'August',
                    'value':8
                },
                9:{
                    'full_name':'September',
                    'value':9
                },
                10:{
                    'full_name':'October',
                    'value':10
                },
                11:{
                    'full_name':'November',
                    'value':11
                },
                12:{
                    'full_name':'December',
                    'value':12
                }
}

DAY_DATA = {0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday'}                

def get_user_city():
    while True:
        city_input = input('\nFor which city would you like to see data. Available cities are chicago, new york city, washington : \nType input : ')

        if city_input in CITY_DATA:
            city_val = city_input
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print('Selected city is: ', city_val)
    
    return city_val


def get_user_filter():
    while True:
        filter_input = input('\nWould you like to filter the data by month, day, both or not at all.\nNote: Type "none" [all in lower case]\nAvailable options are [ month, day, both, none ]\nType input : ')

        if filter_input in FILTER_DATA:
            filter_val = filter_input
            break
        else:
            print('\n You have entered incorrect option. Please try again...')

    print('Selected filter is: ', filter_val)

    return filter_val


def get_month():
    while True:
        month_input = int(input('\nSelect month\n1 => January, 2 => February, 3 => March, 4 => April, 5 => May, 6 => June, 7 => July, 8 => August, 9 => September, 10 => October, 11 => November, 12 => December \nNote: Type 1 to select January month\nType input : '))

        if month_input in MONTH_DATA:
            month_val = MONTH_DATA[month_input]['value']
            break
        else:
            print('You have entered incorrect option. Please try again...')
    
    print('Selected Month is: ', MONTH_DATA[month_input]['full_name'])

    return month_val


def get_day():
    while True:
        day_input = int(input('\nSelect day\n 0 => Monday, 1 => Tuesday, 2 => Wednesday, 3 => Thursday, 4 => Friday, 5 => Saturday, 6 => Sunday\nNote: Type 1 to select Tuesday\nType input : '))

        if day_input in DAY_DATA:
            day_val = DAY_DATA[day_input]
            break
        else:
            print('You have entered incorrect option. Please try again...')

    print('Selected Day is: ', day_val)

    return day_input
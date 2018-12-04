import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

FILTER_DATA = {
'month':'month',
'day':'day',
'both':'both',
'none':'none'
}

MONTH_DATA = {
'all':'all',
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
'dec':'December'
}

DAY_DATA = {
'0': 'sunday',
'1': 'moday',
'2': 'tuesday',
'3': 'wednesday',
'4': 'thursday',
'5': 'friday',
'6': 'saturday',
'7': 'all'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    get_city = get_filter = get_month = get_day = None

    while True:
        while True:
            get_city = input('\nFor which city would you like to see data. Available cities are chicago, new york city, washington : \nType input : ')

            if get_city in CITY_DATA:
                city_val = get_city
                break
            else:
                print('\n You have entered incorrect option. Please try again...')

        print('Selected city is: ', city_val)

        while True:
            get_filter = input('\nWould you like to filter the data by month, day, both or not at all.\n Note: Type "none" [all in lower case]\nAvailable options are [ month, day, both, none ]\nType input : ')

            if get_filter in FILTER_DATA:
                filter_val = get_filter
                break
            else:
                print('\n You have entered incorrect option. Please try again...')


        print('Selected filter option is: ', filter_val)

        while (True and (get_filter =='both' or get_filter =='month')):
            get_month = input('\nSelect month\n all => All, jan => January, feb => February, mar => March, apr => April, may => May, jun => June, jul => July, aug => August, sep => September, oct => October, nov => November, dec => December \n Note: Type jan to select January month\nType input : ')           

            if get_month in MONTH_DATA:
                month_val = get_month
                break
            else:
                print('You have entered incorrect option. Please try again...')

        if get_filter =='both' or get_filter =='month':
            print('Selected Month is: ', MONTH_DATA[month_val])

        while (True and (get_filter =='both' or get_filter =='day')):
            get_day = input('\nSelect day\n 0 => sunday, 1 => moday, 2 => tuesday, 3 => wednesday, 4 => thursday, 5 => friday, 6 => saturday, 7 => all \nNote: Type 6 to select saturday')

            if get_day in DAY_DATA:
                day_val = get_day
                break
            else:
                print('You have entered incorrect option. Please try again...')

        if get_filter =='both' or get_filter =='day':
            print('Selected Month is: ', DAY_DATA[day_val])

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

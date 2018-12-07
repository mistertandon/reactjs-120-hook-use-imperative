import time
import pandas as pd
import numpy as np
import helper
import sys
from datetime import datetime
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    month = day = 'all'
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = helper.get_user_city()

    # get user input for filetr type input
    filter_val = helper.get_user_filter()

    # get user input for month (all, january, february, ... , june)
    if filter_val =='both' or filter_val =='month':
        month = helper.get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_val =='both' or filter_val =='day':    
        day = helper.get_day()

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
    df = pd.read_csv(city + ".csv")

    df['Start Time'], df['End Time'] = pd.to_datetime(df['Start Time']), pd.to_datetime(df['End Time'])
    df['start_time_month'], df['end_time_month'] = df['Start Time'].dt.month, df['End Time'].dt.month
    df['start_time_weekday'], df['end_time_weekday'] = df['Start Time'].dt.weekday, df['End Time'].dt.weekday
    df['start_time_hour'], df['end_time_hour'] = df['Start Time'].dt.hour, df['End Time'].dt.hour
                     
    if month != 'all':
        df = df[(df['start_time_month'] == month) & (df['end_time_month'] == month)]

    if day != 'all':
        df = df[(df['start_time_weekday'] == day) & (df['end_time_weekday'] == day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month_max_value = df.groupby('start_time_month').agg({'start_time_weekday':'count'}).idxmax()['start_time_weekday']
    print('most common month : ', helper.MONTH_DATA[common_month_max_value]['full_name'])

    # display the most common day of week
    common_week_max_value = df.groupby('start_time_weekday').agg({'start_time_weekday':'count'}).idxmax()['start_time_weekday']
    print('most common weekday : ', helper.DAY_DATA[common_week_max_value])

    # display the most common start hour
    common_hour_max_value = df.groupby('start_time_hour').agg({'start_time_weekday':'count'}).idxmax()['start_time_weekday']
    print('most common start hour : ', common_hour_max_value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df.groupby('Start Station').agg({'Start Station':'count'}).idxmax()
    print('Most commonly used start station : ', common_start_station)

    # display most commonly used end station
    common_end_station = df.groupby('End Station').agg({'End Station':'count'}).idxmax()
    print('Most commonly used end station : ', common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_end_trip = df.groupby(['Start Station', 'End Station']).agg({'Start Station':'count'}).idxmax()
    print('Most frequent combination of start station and end station : ', common_start_end_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return


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
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        #df = load_data("chicago", 6, 'all')
        time_stats(df)
        
        station_stats(df)
        sys.exit()
        trip_duration_stats(df)
        user_stats(df)
        break
        #restart = input('\nWould you like to restart? Enter yes or no.\n')
        #if restart.lower() != 'yes':
        #    break


if __name__ == "__main__":
	main()

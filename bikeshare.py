import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
WEEKDAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('******US BIKESHARE DATA******\n')
    print('\nData provided by Motivate, a bike share system provider for many major cities in the United States.Randomly selected data for the first six months of 2017 are provided for three major cities in the US.\n')
    print('\nReady to explore some US bikeshare data?\nLet\'s get started!\n')
    # get user input for city (chicago, new york city, washington)
    city_choice = input(
        'Please choose a city:\n1)\'C\' or \'c\' for chicago.\n2)\'N\' or \'n\' for new york\n3)\'W\' or \'w\' city or washington?\n')
    # check if the city input is valid
    while city_choice.lower() not in ['c', 'n', 'w', '1', '2', '3']:
        city_choice = input(
            'The city you entered is not valid please enter one of the cities mentioned above.\n')
    # assign to city once the user has entered a valid city
    if city_choice.lower() in ['c', '1']:
        city = 'chicago'
    elif city_choice.lower() in ['n', '2']:
        city = 'new york city'
    elif city_choice.lower() in ['w', '3']:
        city = 'washington'
    print('\nYou have chosen to display the data for %s.\n' % city.title())
    # ask the user if he wants to apply get_filters
    apply_filters = input(
        'Before we explore the data, would you like to apply any filters? Enter yes or no\n')
    if apply_filters.lower() not in ['yes', 'y']:
        month = 'all'
        day = 'all'
        # return the function with no month or day filters
        return city, month, day

    # get user input for month (all, Jan, Feb, ... , june)
    month = input(
        '\nPlease choose a month: Jan, Feb, Mar, Apr, May, Jun or all if you don\'t wish to filter by month.\n')
    # check if the month input is valid
    while month.lower() not in MONTHS:
        month = input(
            '\nThe month you entered is not valid.\nPlease choose a month: Jan, Feb, Mar, Apr, May, Jun or all if you don\'t wish to filter by month.\n')
    # get user input for day of week
    day = input(
        '\nPlease choose a day: Mon, Tue, Wed, Thu, Fri, Sat, Sun or all if you don\'t wish to filter by day.\n')
    # chech that the user entered a valid day
    while day.lower() not in WEEKDAYS:
        day = input(
            '\nThe day you entered is not valid.\nPlease choose a day: Mon, Tue, Wed, Thu, Fri, Sat, Sun or all if you don\'t wish to filter by day.\n')

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
    # read cita data from .csv file
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time from str to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # filter data by month
    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['Start Time'].dt.month == month_index]
    # filter data by day
    if day != 'all':
        day_index = WEEKDAYS.index(day)
        df = df[df['Start Time'].dt.weekday == day_index]

    # drop NaN valuesto clean the data
    df = df.dropna(axis=0)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # get the trip datetime data
    trip_dt = df['Start Time'].dt

    # display the most common month
    try:
        most_month = trip_dt.month_name().mode()[0]
        print('The most common month is %s.\n' %
              most_month.title())
    except:
        print('Couldn\'t calculate the most common month.')

    # display the most common day of week
    try:
        most_day = trip_dt.day_name().mode()[0]
        print('The most common day of the week is %s.\n' % most_day.title())
    except:
        print('Couldn\'t calculate the most common day.')

    # display the most common start hour
    try:
        most_hour = trip_dt.hour.mode()[0]
        print('The most common start hour is %s:00.\n' % most_hour)
    except:
        print('Couldn\'t calculate the most common hour.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        most_start_station = df['Start Station'].value_counts().keys()[0]
        print('The most common start station is "%s".\n' % most_start_station)
    except:
        print('Couldn\'t calculate the most common start station.\n')
    # display most commonly used end station
    try:
        most_end_station = df['End Station'].value_counts().keys()[0]
        print('The most common end station is "%s".\n' % most_end_station)
    except:
        print('Couldn\'t calculate the most common end station.\n')
    # display most frequent combination of start station and end station trip
    try:
        df['routes'] = 'from "' + df['Start Station'] + \
            '" to "' + df['End Station'] + '"'
        most_route = df['routes'].value_counts().keys()[0]
        print('The most frequent combination of start station and end station trip is %s.\n' % most_route)
    except:
        print('Couldn\'t calculate the most common route between station.\n')

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        total_travel_time = float(df['Trip Duration'].sum())
        print('The total travel time is equals to %s.\n' %
              time.strftime('%j days, %-H hours, %-M minutes and %-S seconds', time.gmtime(total_travel_time)))
    except:
        print('Couldn\'t calculate total travel time.\n')

    # display mean travel time
    try:
        mean_travel_time = df['Trip Duration'].mean()
        print('The mean travel time is equals to %s.\n' %
              time.strftime('%H:%M:%S', time.gmtime(mean_travel_time)))
    except:
        print('Couldn\'t calculate mean travel time.\n')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('User Type information:\n')
        for i in range(user_types.size):
            print('%s of the users are %ss.\n' %
                  (user_types[i], user_types.keys()[i]))
    except:
        print('Couldn\'t get User type information.\n')

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nUser Gender Information:\n')
        for i in range(user_gender.size):
            print('%s of the users are %ss.\n' %
                  (user_gender[i], user_gender.keys()[i]))
    except:
        print('Couldn\'t get Gender Information.\n')
    # Display earliest, most recent, and most common year of birth
    try:
        year_of_birth = df['Birth Year'].astype(int)
        print('\nUser Age information:\n')
        print('The earliest year of birth is %s.\n' % int(year_of_birth.min()))
        print('The most recent year of birth is %s.\n' %
              int(year_of_birth.max()))
        print('The most common year of birth is %s.\n' %
              int(year_of_birth.mode()[0]))
    except:
        print('Couldn\'t get information about the users age.\n')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def show_raw_data(city):
    """ Displays the raw data for the user 5 rows at a time """
    #read the raw data without any filters or cleaning
    raw_data = pd.read_csv(CITY_DATA[city])
    show = input(
        '\nWould you like to see the raw data yourself? Enter yes or no.\n')
    start = 0
    end = 5
    while show.lower() in ['yes', 'y']:
        print('\n%s\n' % raw_data[start:end])
        print('-'*40)
        show = input(
            '\nWould you like to see 5 more rows of raw data? Enter yes or no.\n')
        start += 5
        end += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
    main()

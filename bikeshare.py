import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

WEEKDAYS = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Ready to explore some US bikeshare data?\n Let\'s get started\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        'Please choose a city: chicago, new york city or washington?\n')
    # check if the city input is valid
    while city not in CITY_DATA:
        city = input(
            "The city you entered is not valid please enter one of the cities mentioned above.\n")

    # get user input for month (all, january, february, ... , june)
    month = input(
        'Please choose a month: all, january, february, ... , june.\n')
    # check if the month input is valid
    while month not in MONTHS and month != 'all':
        month = input(
            'The month you entered is not valid please enter a month between january and june or all if you don\'t wish to filter by month\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        'Please choose a day: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n')

    while day not in WEEKDAYS and day != 'all':
        day = input(
            'The day you entered is not valid please enter a day between monday and sunday or all if you don\'t wish to filter by day\n')

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
        most_month = trip_dt.month.mode()[0]
        print('The most common month is %s.\n' %
              MONTHS[int(most_month)-1].title())
    except:
        print('Couldn\'t calculate the most common month.')

    # display the most common day of week
    try:
        most_day = trip_dt.weekday.mode()[0]
        print('The most common day of the week is %s.\n' %
              WEEKDAYS[int(most_day)].title())
    except:
        print('Couldn\'t calculate the most common day.')

    # display the most common start hour
    try:
        most_hour = trip_dt.hour.mode()[0]
        print('The most common start hour is %s.\n' %
              str(datetime.timedelta(hours=most_hour)))
    except:
        print('Couldn\'t calculate the most common hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    try:
        most_start_station = df['Start Station'].value_counts().keys()[0]
        print('The most common start station is %s ' % most_start_station)
    except:
        print('Couldn\'t calculate the most common start station')
    # display most commonly used end station
    try:
        most_end_station = df['End Station'].value_counts().keys()[0]
        print('The most common end station is %s ' % most_end_station)
    except:
        print('Couldn\'t calculate the most common end station')
    # display most frequent combination of start station and end station trip
    try:
        df['routes'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
        most_route = df['routes'].value_counts().keys()[0]
        print('The most frequent combination of start station and end station trip is %s' % most_route)
    except:
        print('Couldn\'t calculate the most common route between station')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    try:
        total_travel_time = float(df['Trip Duration'].sum())
        print('\nThe total travel time is equals to %s.' %
              str(datetime.timedelta(seconds=total_travel_time)))
    except:
        print('\nCouldn\'t calculate total travel time.\n')

    # display mean travel time
    try:
        mean_travel_time = df['Trip Duration'].mean()
        print('\nThe mean travel time is equals to %s.' %
              str(datetime.timedelta(seconds=mean_travel_time)))
    except:
        print('\nCouldn\'t calculate mean travel time.\n')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('User Type information: ')
        for i in range(user_types.size):
            print('%s of the users are %ss.' %
                  (user_types[i], user_types.keys()[i]))
    except:
        print('\nCouldn\'t get User type information.')

    # Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nUser Gender Information:')
        for i in range(user_gender.size):
            print('%s of the users are %ss.' %
                  (user_gender[i], user_gender.keys()[i]))
    except:
        print('\nCouldn\'t get Gender Information')
    # Display earliest, most recent, and most common year of birth
    try:
        year_of_birth = df['Birth Year'].astype(int)
        print('\nUser age information')
        print('The earliest year of birth is %s ' % int(year_of_birth.min()))
        print('The most recent year of birth is %s ' %
              int(year_of_birth.max()))
        print('The most common year of birth is %s ' %
              int(year_of_birth.mode()[0]))
    except:
        print('\nCouldn\'t get information about the year of birth')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def show_raw_data(city):
    """ Show the raw data for the user 5rows at a time """
    raw_data = pd.read_csv(CITY_DATA[city])
    show = input('\nWould you like to watch the raw data? Enter yes or no.\n')
    start = 0
    end = 5
    while show.lower() == 'yes':
        print(raw_data[start:end])
        show = input(
            '\nWould you like to see more raw data? Enter yes or no.\n')
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
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Would you like to see data from Chicago, New York city, or Washington? ")).lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = str(input("Please Choose Chicago, New York City, or Washington. ")).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("Which month would you like to see? ")).lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = str(input("Please January, February, March, April, May, June ,or All ")).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Which day? ")).lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']:
        day = str(
            input("Please Choose monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all ")).lower()

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Common Month: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most Common Day Of Week: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Most Common Start Hour Of Day: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Common End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station: " +
          (df['Start Station'] + "||" + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time(Seconds): ', int(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('Mean Travel Time(Seconds): ', int(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types in Data: ', df['User Type'].value_counts())

    if city == 'chicago' or city == 'new_york_city':
        # TO DO: Display counts of gender
        print("The count of user gender: ", df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year is: ", int(df['Birth Year'].min()))
        print("The most recent year is: ", int(df['Birth Year'].max()))
        print("The most common year is: ", int(df['Birth Year'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_raw_data(df):
    line = 0
    while True:
        view_raw_data = input("Would you like to see the raw data? 'Yes' or 'No' ").lower()
        if view_raw_data == "yes":
            print(df.iloc[line: line + 6])
            line += 6
        elif view_raw_data == "no":
            break
        else:
            print("Enter 'yes' or 'no'")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_raw_data(df)
        restart = input('\nWould you like to restart? Enter "y" for yes or "n" for no.\n').lower()
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
    main()
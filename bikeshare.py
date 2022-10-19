import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Select a city to analyse ( chicago, new york city, washington : )").lower()
    while city not in CITY_DATA.keys():
        print("Please Select a valid city")
        city = input("Select a city to analyse ( chicago, new york city, washington :) ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while True:
        month= input("select the month you want to check : (all, january, february, march, april , may, june)").lower()
        if month in months:
            break
        else:
            print("the month you select is out of our range, please select valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while True:
        day = input("select the day you want to check : (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)").lower()
        if day in days:
            break
        else:
            print("invalid, please select valid day")

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

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most Common Month is : ", common_month)

    # TO DO: display the most common day of week
    common_day = df["day"].mode()[0]
    print("The Most common day of the week is : " , common_day)

    # TO DO: display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("The most common start hour is : ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start startion"].mode()[0]
    print ("The most common Start Station is : " , common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print ("The most common End Station is : " , common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = (df['Start Station'] & ['End Station']).mode()[0]
    print ("The most frequent combination is : " , frequent_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip duration"].sum()
    print("The Total Trip Time is : ", total_travel_time)

    # TO DO: display mean travel time
    mean_travle_time = df["Trip duration"].mean()
    print("The Mean Trip Time is : ", mean_travle_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df["User Type"].value_counts()
    print("Counts if user type is : ", user_counts)


    # TO DO: Display counts of gender
    if city != "washington":
        print(df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df["Birth Year"].min())
    recent = int(df["Birth Year"].max())
    common = int(df["Birth Year"].mode())
    print("The earlist Year of birth is : ", earlist)
    print("The most recent Year of birth is : " , recent)
    print("The most common Year of birth is : " , common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
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

import pandas as pd

MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June'
}

def get_city():
    """
    Prompt the user to select a city for bikeshare analysis.

    Returns:
        str: The selected city name (Chicago, New York, or Washington).

    Usage:
        The function prompts the user to enter a city name as input (case-insensitive). It validates the input against a list of available cities (Chicago, New York, and Washington) and returns the selected city.

    Example:
        >>> city = get_city()
        Please select a city (Chicago, New York, or Washington): chicago
        >>> print(city)
        chicago
    """
    cities = ['chicago', 'new york', 'washington']
    while True:
        city = input("Please select a city (Chicago, New York, or Washington): ").lower()
        if city in cities:
            return city
        else:
            print("Invalid city. Please try again.")


def get_filter():
    """
    Ask the user if they want to filter the data by month, day, or not at all.
    """
    filter_choices = ['month', 'day', 'none']
    while True:
        filter_choice = input("Would you like to filter the data by month, day, or not at all? ").lower()
        if filter_choice in filter_choices:
            return filter_choice
        else:
            print("Invalid choice. Please try again.")

def get_month():
    """
    Ask the user to select a specific month.
    """
    while True:
        month = input("Please enter the month (1-6): ")
        if month.isdigit() and int(month) in range(1, 7):
            return int(month)
        else:
            print("Invalid month. Please try again.")

def get_day():
    """
    Ask the user to select a specific day.
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        day = input("Please enter the day (Monday, Tuesday, etc.): ").title()
        if day in days:
            return day
        else:
            print("Invalid day. Please try again.")

def display_data(df):
    """
    Ask the user if they want to see the raw data.
    Display 5 rows at a time if the user answers 'yes'.
    """
    start_idx = 0
    while True:
        display = input("Would you like to see the raw data? (yes or no): ").lower()
        if display == 'yes':
            print(df.iloc[start_idx:start_idx+5])
            start_idx += 5
            if start_idx >= len(df):
                print("No more data to display.")
                break
        elif display == 'no':
            break
        else:
            print("Invalid input. Please try again.")

def calculate_popular_times(df):
    """
    Calculate and display the popular times of travel.
    """
    print("1. Popular times of travel:")
    calculate_most_common_month(df)
    calculate_most_common_day(df)
    calculate_most_common_hour(df)

def calculate_most_common_month(df):
    """
    Calculate and display the most common month.
    """
    popular_month = df['Start Time'].dt.month.mode()[0]
    print("   Most common month:", MONTHS[popular_month])

def calculate_most_common_day(df):
    """
    Calculate and display the most common day of week.
    """
    popular_day = df['Start Time'].dt.day_name().mode()[0]
    print("   Most common day of week:", popular_day)

def calculate_most_common_hour(df):
    """
    Calculate and display the most common hour of day.
    """
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("   Most common hour of day:", popular_hour)

def calculate_popular_stations_trips(df):
    """
    Calculate and display the popular stations and trips.
    """
    print("2. Popular stations and trips:")
    calculate_most_common_start_station(df)
    calculate_most_common_end_station(df)
    calculate_most_common_trip(df)

def calculate_most_common_start_station(df):
    """
    Calculate and display the most common start station.
    """
    popular_start_station = df['Start Station'].mode()[0]
    print("   Most common start station:", popular_start_station)

def calculate_most_common_end_station(df):
    """
    Calculate and display the most common end station.
    """
    popular_end_station = df['End Station'].mode()[0]
    print("   Most common end station:", popular_end_station)

def calculate_most_common_trip(df):
    """
    Calculate and display the most common trip from start to end.
    """
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print("   Most common trip from start to end:", popular_trip)

def calculate_trip_duration(df):
    """
    Calculate and display the trip duration.
    """
    print("3. Trip duration:")
    calculate_total_travel_time(df)
    calculate_average_travel_time(df)

def calculate_total_travel_time(df):
    """
    Calculate and display the total travel time.
    """
    total_travel_time = df['Trip Duration'].sum()
    print("   Total travel time:", total_travel_time)

def calculate_average_travel_time(df):
    """
    Calculate and display the average travel time.
    """
    average_travel_time = df['Trip Duration'].mean()
    print("   Average travel time:", average_travel_time)

def calculate_user_info(df):
    """
    Calculate and display the user information.
    """
    print("4. User info:")
    calculate_user_type_counts(df)
    calculate_gender_counts(df)
    calculate_birth_year_info(df)

def calculate_user_type_counts(df):
    """
    Calculate and display the count of each user type.
    """
    user_type_counts = df['User Type'].value_counts()
    print("   Counts of each user type:")
    print(user_type_counts)

def calculate_gender_counts(df):
    """
    Calculate and display the count of each gender (if available).
    """
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("   Counts of each gender:")
        print(gender_counts)

def calculate_birth_year_info(df):
    """
    Calculate and display the earliest, most recent, and most common birth years (if available).
    """
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("   Earliest birth year:", earliest_birth_year)
        print("   Most recent birth year:", most_recent_birth_year)
        print("   Most common birth year:", most_common_birth_year)

def main():
    # Get user input
    city = get_city()
    filter_choice = get_filter()
    month = None
    day = None

    # Load the data
    filename = city.replace(" ", "_").lower() + ".csv"
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("Data file not found. Please make sure the file is in the correct directory.")
        return

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter the data based on user input
    if filter_choice == 'month':
        month = get_month()
        df = df[df['Start Time'].dt.month == month]
    elif filter_choice == 'day':
        day = get_day()
        df = df[df['Start Time'].dt.day_name() == day]

    # Calculate and display statistics
    calculate_popular_times(df)
    calculate_popular_stations_trips(df)
    calculate_trip_duration(df)
    calculate_user_info(df)

    # Display raw data if requested by the user
    display_data(df)

if __name__ == '__main__':
    main()

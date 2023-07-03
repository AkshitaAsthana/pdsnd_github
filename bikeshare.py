import pandas as pd

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June'
}

def get_city():
    """
    Prompt the user to select a city.
    """
    cities = ['chicago', 'new york', 'washington']
    while True:
        city_name = input("Please select a city (Chicago, New York, or Washington): ").lower()
        if city_name in cities:
            return city_name
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
        display_choice = input("Would you like to see the raw data? (yes or no): ").lower()
        if display_choice == 'yes':
            print(df.iloc[start_idx:start_idx+5])
            start_idx += 5
            if start_idx >= len(df):
                print("No more data to display.")
                break
        elif display_choice == 'no':
            break
        else:
            print("Invalid input. Please try again.")

def calculate_statistics(df):
    """
    Calculate and display the statistics based on the filtered data.
    """
    # 1. Popular times of travel
    print("1. Popular times of travel:")
    # Most common month
    popular_month = df['Start Time'].dt.month.mode()[0]
    print("   Most common month:", months[popular_month])

    # Most common day of week
    popular_day = df['Start Time'].dt.day_name().mode()[0]
    print("   Most common day of week:", popular_day)

    # Most common hour of day
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("   Most common hour of day:", popular_hour)

    # 2. Popular stations and trips
    print("2. Popular stations and trips:")
    # Most common start station
    popular_start_station = df['Start Station'].mode()[0]
    print("   Most common start station:", popular_start_station)

    # Most common end station
    popular_end_station = df['End Station'].mode()[0]
    print("   Most common end station:", popular_end_station)

    # Most common trip from start to end
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print("   Most common trip from start to end:", popular_trip)

    # 3. Trip duration
    print("3. Trip duration:")
    # Total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("   Total travel time:", total_travel_time)

    # Average travel time
    average_travel_time = df['Trip Duration'].mean()
    print("   Average travel time:", average_travel_time)

    # 4. User info
    print("4. User info:")
    # Count of each user type
    user_type_counts = df['User Type'].value_counts()
    print("   Counts of each user type:")
    print(user_type_counts)

    # Count of each gender (if available)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("   Counts of each gender:")
        print(gender_counts)

    # Earliest, most recent, and most common year of birth (if available)
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("   Earliest birth year:", earliest_birth_year)
        print("   Most recent birth year:", most_recent_birth_year)
        print("   Most common birth year:", most_common_birth_year)

def main():
    # Get user input
    city_name = get_city()
    filter_choice = get_filter()
    month = None
    day = None

    # Load the data
    filename = city_name.replace(" ", "_").lower() + ".csv"
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
    calculate_statistics(df)

    # Display raw data if requested by the user
    display_data(df)

if __name__ == '__main__':
    main()

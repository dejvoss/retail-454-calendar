from flask import render_template, Response
from app import app
from datetime import datetime, timedelta
import pandas as pd
from io import BytesIO


def is_leap_year(year):
    """Check if a given year is a leap year.

    Args:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year < 1582:
        return False
    elif year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def count_days_in_month(year, month):
    """Count the number of days in a given month.

    Args:
        year (int): The year for which the number of days is to be counted.
        month (int): The month for which the number of days is to be counted.

    Returns:
        int: The number of days in the given month.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and is_leap_year(year):
        return 29
    elif month == 2 and not is_leap_year(year):
        return 28
    else:
        return 0


def count_days_in_year(year):
    """Count the number of days in a given year.

    Args:
        year (int): The year for which the number of days is to be counted.

    Returns:
        int: The number of days in the given year.
    """
    days = 0
    for month in range(1, 13):
        days += count_days_in_month(year, month)
    return days


def count_weeks_in_year(year):
    """Count the number of weeks in a given year.

    Args:
        year (int): The year for which the number of weeks is to be counted.

    Returns:
        int: The number of weeks in the given year.
    """
    past_years_of_53_weeks = [2006, 2012, 2017, 2023]
    if year in past_years_of_53_weeks:
        return 53
    if max(past_years_of_53_weeks) > year > min(past_years_of_53_weeks):
        return 52
    if year < min(past_years_of_53_weeks):
        number_of_days_left = 0
        for year_nb in range(year, min(past_years_of_53_weeks), ):
            days_in_year = count_days_in_year(year_nb)
            number_of_days_left += days_in_year % 52 * 7
        if number_of_days_left >= 4:
            return 53
        else:
            return 52
    if year > max(past_years_of_53_weeks):
        number_of_days_left = 0
        for year_nb in range(max(past_years_of_53_weeks), year):
            days_in_year = count_days_in_year(year_nb)
            number_of_days_left += days_in_year % 52 * 7
        if number_of_days_left >= 4:
            return 53
        else:
            return 52


def get_first_sunday_of_february(year):
    """Get the first day of Sunday of February for a given year.

    Args:
        year (int): The year for which the first day of February is to be returned.

    Returns:
        int: The first day of February for the given year.
    """
    first_day_of_feb = datetime(year, 2, 1).weekday()
    return 7 - first_day_of_feb


def count_start_454year_date(year):
    """Count the date of the year when the 454 calendar starts.

    Args:
        year (int): The year for which the start day is to be counted.

    Returns:
        date: The date of the year when the 454 calendar starts.
    """
    first_sunday = get_first_sunday_of_february(year)
    if first_sunday <= 4:
        return datetime(year, 2, first_sunday)
    else:
        return datetime(year, 2, first_sunday) - timedelta(days=7)


def count_weeks_in_454_calendar(year):
    """Count the number of weeks in a given year for a 454 calendar.

    Args:
        year (int): The year for which the number of weeks is to be counted.

    Returns:
        int: The number of weeks in the given year.
    """
    year_start = count_start_454year_date(year)
    year_end = count_start_454year_date(year + 1)
    days_in_year = (year_end - year_start).days
    return days_in_year / 7


def generate_454_calendar(year):
    """Generate a calendar for a given year and return a string containing HTML code.

    Args:
        year (int): The year for which the calendar is to be generated.
        calendar_type (str): The type of calendar to be generated 454 or 455.
        month_start (int): The month in which the year starts.
        week_start (int): The day of the week on which the calendar starts.
        If, after laying out the entire 52-week calendar for any given year,
        there are four or more days left in January during the 53rd week, then a 53rd week is added

    Returns:
        str: The HTML code for the calendar.
    """
    nr_of_weeks = count_weeks_in_year(year)
    year_start = count_start_454year_date(year)
    year_end = count_start_454year_date(year + 1) - timedelta(days=1)
    date = year_start
    month_names = ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December', 'January']
    week_day_names = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    weeks = [[day for day in range(1, 8)] for _ in range(1, nr_of_weeks + 1)]
    calendar = pd.DataFrame(columns=['Date', 'Day', 'Weekday', 'Week of the Month', 'Month Name'])
    calendar['Date'] = pd.date_range(start=year_start, end=year_end, freq='D')
    calendar['Day'] = calendar['Date'].dt.day
    calendar['Weekday'] = calendar['Date'].dt.weekday
    calendar['Day Sequence'] = pd.Series(range(1, len(calendar['Date']) + 1))
    periods = [4, 5, 4] * 4 if nr_of_weeks == 52 else [4, 5, 4] * 3 + [4, 5, 5]
    week_nr = []
    month_series = []
    week_sequence = []
    weeks_counter = 0
    for idx, weeks in enumerate(periods):

        for week in range(1, weeks + 1):
            week_nr += [week] * 7
            week_sequence += [weeks_counter + week] * 7
        weeks_counter += weeks

        month_series += [month_names[idx]] * 7 * weeks
    calendar['Week of the Month'] = pd.Series(week_nr)
    calendar['Month Name'] = pd.Series(month_series)
    calendar['Week Sequence'] = pd.Series(week_sequence)
    calendar['Month Sequence'] = calendar['Month Name'].map(month_names.index) + 1
    calendar['Weekday'] = calendar['Weekday'].map(week_day_names)
    calendar['Calendar week'] = calendar['Date'].dt.isocalendar().week

    return calendar[['Date', 'Month Name', 'Day', 'Weekday', 'Calendar week', 'Week of the Month', 'Week Sequence',
                     'Month Sequence']]


@app.route('/')
@app.route('/<int:year>')
def home(year=None):
    if year is not None and (len(str(year)) != 4 or year < 1930):
        return render_template('404.html'), 404
    current_year = datetime.now().year
    if year is None:
        calendar_year = current_year
    else:
        calendar_year = year
    years = [year for year in range(current_year - 10, current_year + 10)]
    calendar = generate_454_calendar(calendar_year)
    months = []
    for month in calendar['Month Name'].unique():
        month_data = calendar[calendar['Month Name'] == month]
        month_obj = {'month': month, 'weeks': []}
        for week in month_data['Week Sequence'].unique():
            week_data = month_data[month_data['Week Sequence'] == week]
            calendar_week = week_data[week_data['Weekday'] == 'Wednesday']['Calendar week'].values[0]
            month_obj['weeks'].append({'week': week, 'calendar_week': calendar_week, 'days': week_data['Day'].tolist()})
        months.append(month_obj)
    return render_template(
        'index.html',
        years=years,
        chosen_year=calendar_year,
        months=months
    )


@app.route('/save_to_xlsx/<int:year>')
def save_to_excel(year):
    try:
        if len(str(year)) != 4 or year < 1930 or year is None:
            return render_template('404.html'), 404
        calendar = generate_454_calendar(year)
    except ValueError:
        return render_template('404.html'), 404

    calendar['Date'] = calendar['Date'].dt.date
    file = BytesIO()
    calendar.to_excel(file, index=False)
    file.seek(0)
    return Response(
        file,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-disposition": "attachment; filename={year}-454-calendar.xlsx".format(year=year)}
    )


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

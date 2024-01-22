import unittest
from app import routes
from datetime import datetime


class TestHelperFunctions(unittest.TestCase):
    def test_is_leap_year(self):
        lap_years = [2000, 2004, 2008, 2012, 2016, 2020]
        no_lap_years = [2001, 2002, 2003, 2005, 2006, 2007]
        lap_answers = []
        no_lap_answers = []
        for year in lap_years:
            lap_answers.append(routes.is_leap_year(year))
        for year in no_lap_years:
            no_lap_answers.append(routes.is_leap_year(year))

        assert all(lap_answers), "Not all lap years were correctly identified."
        assert not any(no_lap_answers), "Not all non-lap years were correctly identified."

    def test_count_days_in_month(self):
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_in_months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for month in range(1, 13):
            assert routes.count_days_in_month(2020, month) == days_in_months_leap[month - 1], \
                "Not all days in months were correctly counted."
            assert routes.count_days_in_month(2021, month) == days_in_months[month - 1], \
                "Not all days in months were correctly counted."

    def test_count_days_in_year(self):
        assert routes.count_days_in_year(2020) == 366, "Days in year were not correctly counted."
        assert routes.count_days_in_year(2021) == 365, "Days in year were not correctly counted."

    def test_get_first_sunday_of_february(self):
        assert routes.get_first_sunday_of_february(2020) == 2, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2021) == 7, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2008) == 3, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2009) == 1, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2010) == 7, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2011) == 6, "First Sunday of February was not correctly identified."
        assert routes.get_first_sunday_of_february(2012) == 5, "First Sunday of February was not correctly identified."

    def test_count_weeks_in_454_calendar(self):
        assert routes.count_weeks_in_454_calendar(2006) == 53, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2007) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2008) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2009) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2010) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2011) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2012) == 53, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2013) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2014) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2015) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2016) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2017) == 53, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2018) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2019) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2020) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2021) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2022) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2023) == 53, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2024) == 52, "Number of 454 weeks was not correctly counted."
        assert routes.count_weeks_in_454_calendar(2025) == 52, "Number of 454 weeks was not correctly counted."

    def test_count_start_454year_date(self):
        assert routes.count_start_454year_date(2020) == datetime(2020, 2, 2), \
            "Start date of 454 year was not correctly identified."
        assert routes.count_start_454year_date(2021) == datetime(2021, 1, 31), \
            "Start date of 454 year was not correctly identified."
        assert routes.count_start_454year_date(2022) == datetime(2022, 1, 30), \
            "Start date of 454 year was not correctly identified."
        assert routes.count_start_454year_date(2023) == datetime(2023, 1, 29), \
            "Start date of 454 year was not correctly identified."
        assert routes.count_start_454year_date(2024) == datetime(2024, 2, 4), \
            "Start date of 454 year was not correctly identified."
        assert routes.count_start_454year_date(2025) == datetime(2025, 2, 2), \
            "Start date of 454 year was not correctly identified."


if __name__ == '__main__':
    unittest.main()

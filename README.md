# 454 Retail Calendar

## Description

"454 Retail Calendar" is a Flask-based web application that allows users to generate a 4-5-4 retail calendar for a
selected year. The 4-5-4 retail calendar is widely used in the retail industry for tracking sales performance and
planning. The application enables the calendar to be generated in two formats: a printable PDF version and an Excel
spreadsheet format.
I have built that application to help me with my work as I could find many 4-5-4 calendar but all was in the printable
format and I needed to have it in Excel format to be able to use for calculations and for database purposes.

## Features

- Generate a 4-5-4 retail calendar for any selected year.
- Export the calendar in PDF format, ready for printing.
- Export the calendar in Excel format for further analysis and use.
- User-friendly interface for ease of use.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
   `git clone https://github.com/dejvoss/retail-454-calendar.git`
2. Navigate to the project directory:
   `cd calendar454`
3. Install required dependencies:
   `pip install -r requirements.txt`
4. Configure app:
    `export FLASK_APP=calendar454.py` or create .flaskenv file with `FLASK_APP=calendar454.py`
5. Run the application:
   `python calendar454.py`

## Usage

After launching the application, go to `http://localhost:5000` in your web browser. Select the year for which you want
to generate the calendar, and then choose the output format (PDF or Excel).

## Contribution

Contributions to the project are welcome. If you have ideas for new features or improvements, feel free to create new
issues or pull requests in the repository.

## License

This project is made available under the [MIT License](LICENSE).

## Contact

If you have any questions or would like to contact regarding the project, please email dev@deos.work


import unittest
from input import check_inp
import datetime

# Function to convert string to datetime


def convert(date_time):
    format = '%b %d %Y %I:%M%p'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format)

    return datetime_str


date_time = 'Dec 4 2018 10:07AM'

input_data = {
    "Open": 2.2,
    "High": 2.2,
    "Low": 3.3,
    "Close": 2.2,
    "Volume": 5,
    "Instrument": "HINDALCO",
    "Datetime": convert(date_time)
}


class TestInputData(unittest.TestCase):
    def test_open_high_low_close(self):
        # Test that the Open, High, Low, and Close values are decimal numbers
        self.assertTrue(isinstance(input_data['Open'], float))
        self.assertTrue(isinstance(input_data['High'], float))
        self.assertTrue(isinstance(input_data['Low'], float))
        self.assertTrue(isinstance(input_data['Close'], float))

    def test_volume(self):
        # Test that the volume value is an integer
        self.assertTrue(isinstance(input_data['Volume'], int))

    def test_instrument(self):
        # Test that the instrument value is a string
        self.assertTrue(isinstance(input_data['Instrument'], str))

    def test_datetime(self):
        # Test that the datetime value is a datetime object
        self.assertTrue(isinstance(input_data['Datetime'], datetime.datetime))


if __name__ == '__main__':
    unittest.main()

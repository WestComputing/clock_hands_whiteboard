import unittest
from clock_hands import find_smallest_angle

invalid_input_tests_disabled = dict(
    flag=False,
    reason="Invalid input tests are disabled--set to False to enable"
)


class ClockHandsTestCase(unittest.TestCase):
    test_data = [
        {
            "time": "12:30",
            "angle": 165.0
        },
        {
            "time": "3:30",
            "angle": 75.0
        },
        {
            "time": "3:15",
            "angle": 7.5
        },
        {
            "time": "4:50",
            "angle": 155.0
        },
        {
            "time": "9:00",
            "angle": 90.0
        },
        {
            "time": "12:00",
            "angle": 0.0
        },
    ]

    def test_01_isFloat(self):
        for datum in ClockHandsTestCase.test_data:
            result_type = type(find_smallest_angle(datum['time']))
            self.assertIs(result_type,
                          float,
                          f"Return type is {result_type}--should be float.")

    def test_02_isExpectedAngle(self):
        for datum in ClockHandsTestCase.test_data:
            expected_result = datum['angle']
            actual_result = find_smallest_angle(datum['time'])
            self.assertEqual(actual_result,
                             expected_result,
                             f"Wrong angle returned: {actual_result}"
                             f"--should be {expected_result}.")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_03_handles_missing_colon(self):
        actual_result = find_smallest_angle("1230")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_04_handles_missing_minutes(self):
        actual_result = find_smallest_angle("3:")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_05_handles_missing_hours(self):
        actual_result = find_smallest_angle(":59")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_06_handles_empty_string(self):
        actual_result = find_smallest_angle("")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_07_handles_numbers(self):
        actual_result = find_smallest_angle(2100)
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_08_handles_hour_lower_bound(self):
        actual_result = find_smallest_angle("00:00")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_09_handles_hours_upper_bound(self):
        actual_result = find_smallest_angle("13:37")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_10_handles_minutes_lower_bound(self):
        actual_result = find_smallest_angle("1:-1")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_0_handles_minutes_upper_bound(self):
        actual_result = find_smallest_angle("6:61")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")

    @unittest.skipIf(invalid_input_tests_disabled['flag'],
                     invalid_input_tests_disabled['reason'])
    def test_0_handles_out_of_bounds_hours_and_minutes(self):
        actual_result = find_smallest_angle("-1:100")
        self.assertIsNone(actual_result, f"Returned {actual_result}"
                                         f"--should be None")


if __name__ == '__main__':
    unittest.main()

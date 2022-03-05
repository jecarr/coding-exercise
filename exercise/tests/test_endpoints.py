import random

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

# Some request-types we are testing
GET = "get"
POST = "post"


def get_resp_content(response: HttpResponse):
    """Helper-method that, given a response, returns its content (decoded as it is of type bytes)."""
    return response.content.decode(response.charset)


class ExerciseTestSuite(TestCase):
    """The test-suite for this application."""

    def test_hello_world(self):
        """Tests the hello-world endpoint outputs the correct response."""
        # Get the response for the endpoint
        resp = self.client.get(reverse("hello"))
        # Check the response's content is equal to "Hello World"
        match = "Hello World".lower() == get_resp_content(resp).lower()
        self.assertTrue(match, "'Hello World' endpoint returned incorrect response or was phrased differently.")

    def test_join_words(self):
        """Tests the join-words endpoint outputs the expected concatenated string."""
        # The combinations we are testing; 1 test with words; 1 with numbers and words
        tests = [("To", "infinity"), ("A", 113)]
        for test_s1, test_s2 in tests:
            # Get the response for the endpoint
            resp = self.client.get(reverse("join_words", kwargs=dict(s1=test_s1, s2=test_s2)))
            # What we are expecting
            expected_output = str(test_s1) + "-" + str(test_s2)
            # Check the response's content is as expected
            match = expected_output == get_resp_content(resp)
            self.assertTrue(match, "Join-words endpoint did not return '{}'.".format(expected_output))

    def add_numbers_checker_success(self, number1, number2, error_msg_suffix=None, request_type=GET, request_data=None):
        """Helper-method to test successful outcomes of the add-numbers endpoint."""
        # Given two numbers, generate our expected output
        expected_output = float(number1) + float(number2)
        # Get endpoint's response for these numbers (dependent on request-type)
        if request_type == GET:
            resp = self.client.get(reverse("add_numbers", kwargs=dict(num1=number1, num2=number2)))
        elif request_type == POST:
            resp = self.client.post(reverse("add_numbers", kwargs=dict(num1=number1, num2=number2)), data=request_data)
        else:
            raise ValueError("add_numbers_checker_success() currently tests GETs and POSTs.")
        # Prepare error-message
        error_msg = "Response did not contain expected sum for {} + {} = {}".format(number1, number2, expected_output)
        error_msg = error_msg + (": {}".format(error_msg_suffix) if error_msg_suffix else ".")
        # Check assertion that the sum is as expected
        self.assertTrue(float(get_resp_content(resp)) == expected_output, error_msg)

    def test_add_numbers(self):
        """Tests the add-numbers endpoint returns the correct sum."""
        self.add_numbers_checker_success(random.randint(0, 9999), random.randint(0, 9999), "positive numbers")

    def test_add_numbers_invalid_numbers(self):
        """Tests the add-numbers endpoint returns the correct sum when non-numerical values are given."""
        # Send words to the add-numbers endpoint
        invalid1, invalid2 = "Phone", "home"
        resp = self.client.get(reverse("add_numbers", kwargs=dict(num1=invalid1, num2=invalid2)))
        # Confirm a bad-request status code and defined-message are returned
        self.assertEqual(resp.status_code, 400, "Add-numbers with words did not return a 400-response.")
        msg_found = "Non numerical value(s) supplied in url" in get_resp_content(resp)
        self.assertTrue(msg_found, "Add-numbers with words did not return expected error-message to user.")

    def test_add_numbers_with_decimals(self):
        """Tests the add-numbers endpoint returns the correct sum when decimal values are given."""
        # Generate two random decimals (add a random int so our test values aren't always less than 1)
        num1 = random.random() + random.randint(0, 100)
        num2 = random.random() + random.randint(0, 100)
        self.add_numbers_checker_success(num1, num2, "numbers with decimals")

    def test_add_numbers_with_negatives(self):
        """Tests the add-numbers endpoint returns the correct sum when negative values are given."""
        self.add_numbers_checker_success(random.randint(-9999, -1), random.randint(-9999, -1), "negative numbers")

    def test_add_numbers_ignore_post(self):
        """Tests the add-numbers endpoint returns the correct sum and ignores any POST arguments."""
        # Create some arguments to ignore that are greater than the numbers we want to sum (to see the difference)
        ignored_args = dict(num1=random.randint(1000, 2000), num2=random.randint(1000, 2000))
        self.add_numbers_checker_success(
            random.randint(0, 999),
            random.randint(0, 999),
            "ignore POST arguments",
            request_type=POST,
            request_data=ignored_args,
        )

    def test_add_numbers_with_recurring_decimals(self):
        """Tests the add-numbers endpoint returns the correct sum when recurring decimals are given."""
        self.add_numbers_checker_success(1 / 3, 3 / 4, "recurring decimals")

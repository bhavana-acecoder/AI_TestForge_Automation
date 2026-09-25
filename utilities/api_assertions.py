import json


class APIAssertions:
    """
    Common API Assertions.
    """

    @staticmethod
    def get_json(response):
        """
        Parse the response body as JSON.
        AutomationExercise returns JSON with a text/html content type,
        so the body is parsed from response.text.
        """
        return json.loads(response.text)

    @staticmethod
    def assert_status_code(response, expected_status):
        """
        Verify response status code.
        """
        assert response.status_code == expected_status, (
            f"Expected Status Code: {expected_status}, "
            f"Actual Status Code: {response.status_code}"
        )

    @staticmethod
    def assert_response_code(response, expected_code):
        """
        AutomationExercise always returns HTTP 200 and puts the real
        result code (200, 201, 400, 404, 405) in the 'responseCode' field.
        """
        APIAssertions.assert_status_code(response, 200)

        actual_code = APIAssertions.get_json(response)["responseCode"]

        assert actual_code == expected_code, (
            f"Expected responseCode: {expected_code}, "
            f"Actual responseCode: {actual_code}"
        )

    @staticmethod
    def assert_message(response, expected_message):
        """
        Verify the 'message' field in the response body.
        """
        actual_message = APIAssertions.get_json(response)["message"]

        assert actual_message == expected_message, (
            f"Expected message: {expected_message}, "
            f"Actual message: {actual_message}"
        )

    @staticmethod
    def assert_response_key(response, key):
        """
        Verify key exists in response.
        """
        data = response.json()

        assert key in data, (
            f"'{key}' not found in response."
        )

    @staticmethod
    def assert_response_value(response, key, expected_value):
        """
        Verify response value.
        """
        data = response.json()

        assert data[key] == expected_value, (
            f"Expected {key}={expected_value}, "
            f"Actual={data[key]}"
        )

    @staticmethod
    def assert_response_time(response, max_seconds):
        """
        Verify response time.
        """
        assert response.elapsed.total_seconds() < max_seconds, (
            f"Response took "
            f"{response.elapsed.total_seconds()} seconds."
        )

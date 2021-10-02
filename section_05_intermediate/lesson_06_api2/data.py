import requests

# Docs for this API: https://opentdb.com/api_config.php
URL = "https://opentdb.com/api.php"
AMOUNT_PARAM = "amount"
TYPE_PARAM = "type"
RESPONSE_RESULTS_KEY = "results"


def get_question_data(question_count=10, question_type="boolean"):
    # Query params
    parameters = {
        AMOUNT_PARAM: question_count,
        TYPE_PARAM: question_type,
    }

    # Call the Open Trivia API
    open_trivia_api_response = requests.get(url=URL, params=parameters)
    open_trivia_api_response.raise_for_status()

    # Parse the response
    open_trivia_api_response_data = open_trivia_api_response.json()
    return open_trivia_api_response_data[RESPONSE_RESULTS_KEY]


question_data = get_question_data()

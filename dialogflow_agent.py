import os
from google.cloud import dialogflow_v2beta1 as dialogflow
from config import *
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "weber-sbhu-ab7a0fd864b7.json"


def dialogflow_request(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PRODUCT_ID, SESSION_ID)

    text_input = dialogflow.TextInput(
        text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)

    query_input = dialogflow.QueryInput(text=text_input)
    response_new = session_client.detect_intent(
        request={"session": session, "query_input": query_input})

    return response_new.query_result.fulfillment_text

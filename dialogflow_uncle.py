import dialogflow
import os
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        data = {}
        data['fulfillment_text'] = response.query_result.fulfillment_text
        from google.protobuf.json_format import MessageToDict
     
        data['parameters'] = MessageToDict(response.query_result.parameters)
        # data['parameters'] = response.query_result.parameters
        data['fulfillment_messages'] = [str(i.text.text[0]) for i in response.query_result.fulfillment_messages]
        data['action'] = response.query_result.action
        return data

# if __name__ == "__main__":
#     ### enable google dialogflow api
#     ### firstly set GOOGLE_APPLICATION_CREDENTIALS=Credentials.json

    ## os.environ['DIALOGFLOW_PROJECT_ID'] = 'uncletut01-eqapks'
    ## os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Credentials.json'
#     i = 0
#     while(i<5):
#         message = input('please input some text :')
#         project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
#         res = detect_intent_texts(project_id, "1234", message, 'th')

#         print(res)
#         i += 1
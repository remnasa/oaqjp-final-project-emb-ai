# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

import requests
import json

def emotion_detector(text_to_analyse):
    """ This fucntion defines the URL for emotion analysis API,
    Creates the payload with the text to be analyzed, sets the headers, 
    makes the post request to the API with the payload and headers, 
    parses the response from the API, and provides the status code.
    """
    # Define the URL for the emotion analuysis API
    url = """https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"""

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=myobj, headers=header)

        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

        # Parse the response from the API
        formatted_response = response.json()

        emotion_prediction = formatted_response.get('emotionPredictions', {}).get('emotion', {})
        dominant_emotion = formatted_response.get('emotionPredictions', {}).get('dominant_emotion', "unknown")

        emotions = {}
        for emotion, score in emotion_prediction.items():
            emotions[emotion] = score
        
        emotions['dominant_emotion'] = dominant_emotion

        return emotions
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while making the request: {e}")
    
    except ValueError as ve:
        raise Exception(f"Error processing the response: {ve}")

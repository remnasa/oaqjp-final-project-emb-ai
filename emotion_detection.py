# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

import requests
import json

# Constants for API
API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
MODEL_ID = 'emotion_aggregated-workflow_lang_en_stock'


def emotion_detector(text_to_analyse, api_url=API_URL, model_id=MODEL_ID):
    """
    Detects emotions from a given text and extracts the dominant emotion.

    Args:
        text_to_analyse (str): The input text to analyze.
        api_url (str): The URL of the emotion detection API.
        model_id (str): The model ID for the API.

    Returns:
        dict: A dictionary containing the emotion scores and the dominant emotion.
    """
    # Create the request payload and headers
    payload = {"raw_document": {"text": text_to_analyse}}
    headers = {"grpc-metadata-mm-model-id": model_id}

    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=payload, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            formatted_response = response.json()

            # Safely extract emotion scores
            emotion_predictions = formatted_response.get('emotionPredictions', [])
            if emotion_predictions and isinstance(emotion_predictions, list):
                # Extract the first set of emotions
                emotion_data = emotion_predictions[0].get('emotion', {})

                # Extract all available emotions dynamically
                emotion_scores = {
                    key: value for key, value in emotion_data.items() if value is not None
                }

                # Find the dominant emotion
                dominant_emotion = max(
                    emotion_scores,
                    key=emotion_scores.get,
                    default=None,
                )

                # Return the detected emotions along with the dominant one
                return {**emotion_scores, 'dominant_emotion': dominant_emotion}

        # Return default values if no valid response
        return {
            'dominant_emotion': None
        }

    except requests.exceptions.RequestException as e:
        # Handle network-related errors or API issues
        print(f"An error occurred: {e}")
        return {
            'dominant_emotion': None
        }

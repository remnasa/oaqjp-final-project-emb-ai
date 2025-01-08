""" This was part of the Final Project Emotion Detector from the class
    Developing AI Applications with Python and Flask. 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
    This function takes the input text "textToAnalyze", passes it to the 
    emotion_detector function, and returns the detected emotions and dominant 
    emotion as a response. 

    Args:
        None (The text is retrieved from the URL query parameters.)

    Returns:
        str: A message indicating the detected emotions and the dominant emotion.
            Returns an error message if input is invalid. 
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (indicating invalid input)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Extract the label and score from the response
    all_emotions = {key: value for key, value in response.items() if key != 'dominant_emotion'}
    dom_emotion = response["dominant_emotion"]

    # Return the detected emotions along with the dominant one
    phrase = f"For the given statement, the system response is {all_emotions}.\
     The dominant emotion is {dom_emotion}."

    return phrase

@app.route("/")
def render_index_page():
    """
    Renders the index page where users can input text to be analysed by the emotion detector. 

    Returns:
        The rendered HTML content of the index page, 'index.html'.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

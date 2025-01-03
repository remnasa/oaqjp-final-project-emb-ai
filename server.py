from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"error": "Missing ;textToAnalyze' query parameter"}), 400
    
    try:

        # Pass the text to the emotion_detector function and store the response
        response = emotion_detector(text_to_analyze)

        all_emotions = {key: response[key] for key in response if key != 'dominant_emotion'}
        dom_emotion = response["dominant_emotion"]

        # Return the detected emotions along with the dominant one
        phrase = f"For the given statement, the system response is {all_emotions}. The dominant emotion is {dom_emotion}."
    
        return phrase

    except Exception as e:

        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
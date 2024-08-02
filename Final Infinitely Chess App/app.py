from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    logger.error("ANTHROPIC_API_KEY is not set in the environment variables")
else:
    # Initialize the Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

@app.route('/')
def sign_up():
    logger.info("Serving Sign Up page")
    return render_template('Sign Up.html')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sign_in')
def sign_in():
    return render_template('Sign In.html')

@app.route('/edit_profile')
def edit_profile():
    return render_template('Edit Profile.html')

@app.route('/profile')
def profile():
    return render_template('Profile1.html')

@app.route('/save', methods=['POST'])
def save_profile():
    # Here, you would process the form data and update the profile information
    name = request.form.get('name')
    username = request.form.get('username')
    bio = request.form.get('bio')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # Simulate saving the data (in reality, you would update the database)
    print(f'Updated profile - Name: {name}, Username: {username}, Bio: {bio}, Email: {email}, Phone: {phone}')

    # Redirect back to the profile or another page after saving
    return redirect(url_for('profile'))

@app.route('/practice')
def practice():
    return render_template('Practice.html')

# @app.route('/sign_up')
# def sign_up():
#     return render_template('Sign Up.html')

@app.route('/chat', methods=['POST'])
def chat():
    logger.info("Received POST request to /chat")
    data = request.json
    if not data or 'message' not in data:
        logger.error("No message provided in request")
        return jsonify({'error': 'No message provided'}), 400

    user_message = data['message']
    length = data.get('length', 'short')  # Default to medium if not provided
    humor = data.get('humor', False)  # Default to no humor if not provided
    logger.info(f"User message: {user_message}, Length: {length}, Humor: {humor}")

    try:
        # Prepare a chess-specific prompt with humor and length
        chess_prompt = (
            f"You are an AI assistant for a chess learning application called Infinitely Chess. "
            f"Provide a {'humorous and ' if humor else ''}helpful and informative response to the following chess-related question or statement: {user_message}. "
            f"The response should be {length} in length and well-formatted."
        )

        logger.info("Sending request to Anthropic API")
        # Send the message to Claude
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            system="You are a helpful AI assistant for a chess learning application called Infinitely Chess. Provide informative and engaging responses to chess-related queries.",
            messages=[
                {"role": "user", "content": chess_prompt}
            ]
        )

        # Extract the assistant's reply
        response = message.content[0].text

        # Format the response
        formatted_response = (
            
            f"{response}"
            f"<p>Anything else you would like to learn!</p>"
        )
        
        logger.info(f"Received response from API: {response[:100]}...")  # Log first 100 chars of response
        return jsonify({'response': formatted_response})
    except anthropic.APIError as e:
        logger.error(f"Anthropic API Error: {str(e)}")
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/test', methods=['GET'])
def test():
    logger.info("Test route accessed")
    return jsonify({'status': 'ok', 'message': 'Test route is working'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

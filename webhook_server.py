from dependencies.flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to log into a file
logging.basicConfig(filename='webhook.log', level=logging.INFO, format='%(asctime)s - %(message)s')


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get headers and body from the request
        headers = dict(request.headers)
        body = request.get_json() or request.data.decode('utf-8')

        # Log headers and body
        logging.info(f"Headers: {headers}")
        logging.info(f"Body: {body}")

        # Return 200 OK response
        return "Received", 200
    except Exception as e:
        logging.error(f"Error: {e}")
        return "Error", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    url_for,
)

from twilio.rest import Client

# Load "dotenv" files in order of precedence to set environment variables
load_dotenv()

app = Flask(__name__)
# Create secret key
app.secret_key = "ssssh don't tell anyone"
# get environment variable
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Create client object
client = Client()

def get_sent_messages():
    # Collecting the messages sent from the number
    messages = client.messages.list(from_=TWILIO_PHONE_NUMBER)
    return messages

def send_message(to, body):
    # Send text messages
    client.messages.create(
        to=to,
        body=body,
        from_=TWILIO_PHONE_NUMBER
    )

# Get index page
@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)    
    
@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender','Someone') # get the sender
    receiver = request.values.get('receiver','Someone') # get the receiver
    compliment = request.values.get('compliment','Wonderful') # get the compliment
    to =  request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'  
    send_message(to, body) 
    flash('Your message was sent successfully')
    return redirect(url_for('index')) # reopen to index.html 

if __name__ == '__main__':
    app.run(debug=True)    
  






from twilio.rest import Client

# Create new client
client = Client("###########","##############")

# Iterate through messages and see all message
for message in client.messages.list():
    print(message.body)

# Deleting the message
for message in client.message.list():
    print(f"Deleting messages: {message.body}")
    message.delete()

# Send new message
msg = client.messages.create(
    to = "+919860518###",
    from_ = "+19036231###",
    body= "Hello from Python..."
)    

print(f"new message created: {msg.sid}")

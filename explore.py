from twilio.rest import Client

# Create new client
client = Client("ACcc36e92e48f99e1dd6d6330fe40c244f","0d1f3c27f724c7ee63e0acc1d0eed0c0")

# Iterate through messages and see all message
#for message in client.messages.list():
#    print(message.body)

# Deleting the message
for message in client.message.list():
    print(f"Deleting messages: {message.body}")
    message.delete()

# Send new message
# msg = client.messages.create(
#     to = "+919860518381",
#     from_ = "+19036231488",
#     body= "Hello from Python..."
# )    

# print(f"new message created: {msg.sid}")
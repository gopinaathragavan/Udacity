"""
Twilio sms messaging facility
"""
# Download the twilio-python library from twilio.com/docs/libraries/python

from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "your_account_sid" # test credentials in use
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token" # test credentials in use

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+15005550007", # test number in use
    from_="+15005550007",
    body="")

print(message.sid)
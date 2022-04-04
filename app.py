from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

mesg = "".join(["Hello...it's me again\n" for i in range(5)])

send_msg = client.messages.create(to = my_cell, from = my_twilio, body = mesg)

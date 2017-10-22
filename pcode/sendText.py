from twilio.rest import Client

#Twilio account and auth token from twilio.com/user/account
account_sid ="ACdc356dc022e21ea1cff1851a19756fdf"
auth_token = "6834744afc84d24f9cd9e91cea4058df"
client = Client(account_sid,auth_token)

message = client.messages.create(body="Please. mercy", to="+4407472910230", from_="+441163263865")
print message.sid
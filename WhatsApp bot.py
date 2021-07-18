from twilio.rest import Client

def send(body_text, to_who = "+97252*******"):
    account_sid = 'AC7211f042a2ea4004fbf253955c411808'
    auth_token = '***********************'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body_text,
        to='whatsapp:' + to_who
    )
    print(message)

for i in range(1):
    send("פרטי האשראי נקלטו תודה על ביצוע הרכישה", '+97252*******')

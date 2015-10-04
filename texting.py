import private
import pymongo

def addNumber(number):
    client = pymongo.MongoClient()
	db = client.numbers
    db.insert_one({'number': number})
    client.close()

def sendTexts(message):
    client = pymongo.MongoClient()
    db = client.numbers
    account_sid = private.TWILIO_SID
    auth_token  = private.TWILIO_TOKEN
    twilioClient = TwilioRestClient(account_sid, auth_token)
    for number in db.find()
        message = twilioClient.messages.create(body=message, to=number['number'], from_=TWILIO_NUMBER)

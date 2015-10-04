import private
import pymongo
import twilio.rest

def addNumber(number):
    client = pymongo.MongoClient()
    db = client.numbers
    db.insert_one({'number': number})
    client.close()

def sendTexts(message):
    client = pymongo.MongoClient()
    db = client.numbers
    numbers = db.numbers
    account_sid = private.TWILIO_SID
    auth_token  = private.TWILIO_TOKEN
    twilioClient = twilio.rest.TwilioRestClient(account_sid, auth_token)
    for number in numbers.find():
        message = twilioClient.messages.create(body=message, to=number['number'], from_=TWILIO_NUMBER)

from twilio.rest import Client



if __name__ == '__main__':
	
	accout_sid = "AC14f37af1a6467ecefbc2a039d65ebc76"
	auth_token = "*********"#get from https://www.twilio.com/console/phone-numbers/incoming
	client = Client(accout_sid,auth_token)


	message = client.messages.create(to="+8618951105877", 
								 	 from_="+15155005763",
                                 	 body="Hello Colin!")
	print(message.sid)		


	call = client.calls.create(to="+8618951105877",
                           from_="+15155005763",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
	print(call.sid)
	
from datetime import datetime

def greet_user():
	""Greets the user according to the time of day""

	hour = datetime.now().hour

	if(hour >= 6) and (hour <12):
		speak =
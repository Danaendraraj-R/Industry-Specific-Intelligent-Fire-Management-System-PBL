import requests
import json
url = "https://www.fast2sms.com/dev/bulkV2"
my_data = {
	'sender_id': 'FSTSMS',
	'message': 'Alert Some abnormality is found is XYZ industry! Kindly Evacuvate from the place',
	'language': 'english',
	'route': 'p',
	'numbers': '9952356090'	
}
headers = {
	'authorization': 'o0azwVFNHOM5B3hrRxdenyU2cfZujqSpYEX7t8LAgJPb9kliWCugDvo1n0kcY8TGHOt3dIQwsKpLbAJU',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}
response = requests.request("POST",
							url,
							data = my_data,
							headers = headers)
returned_msg = json.loads(response.text)
print(returned_msg['message'])


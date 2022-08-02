import requests 

# https://your-heroku-app-name.herokuapp.com/predict
# http://127.0.0.1:5000
with open('test.pdf', 'rb') as f:
	resp = requests.post("https://flask-text-parser.herokuapp.com/plaintext", files={'file': f})

	print(resp.text)
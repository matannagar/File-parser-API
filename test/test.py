import requests 

# https://your-heroku-app-name.herokuapp.com/predict
# http://127.0.0.1:5000
with open('test.docx', 'rb') as f:
	resp = requests.post("http://127.0.0.1:5000/plaintext", files={'file': f})

	print(resp.text)
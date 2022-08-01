import requests 

# https://your-heroku-app-name.herokuapp.com/predict
# http://127.0.0.1:5000
resp = requests.post("https://flask-smsphishing.herokuapp.com/predict", data={'sms': 'you are a wizard!'})

print(resp.text)
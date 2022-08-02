# File-parser-API
Flask based API allowing users to send (PDF, Docx, doc, txt) files to retrieve clean text without any images, signs and so on...  

## How To Use

### Python example

```
import requests 

with open('test.pdf', 'rb') as f:
	resp = requests.post("https://flask-text-parser.herokuapp.com/plaintext", files={'file': f})

	print(resp.text)
```

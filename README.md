# File-parser-API
Flask based API allowing users to send files to retrieve clean text without any images, signs and so on...  
Create a post request, attach a file and you'll receive plain text.  

#### Allowed files
* PDF
* Docx
* doc
* txt

## How To Use

### Python example

```
import requests 

with open('test.pdf', 'rb') as f:
	resp = requests.post("https://file-parser-quzy.onrender.com/plaintext", files={'file': f})

	print(resp.text)
```

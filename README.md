# PyCaddy

A tiny Python module to manage uploading to [Caddy](https://caddyserver.com/) servers with the [upload extension](https://caddyserver.com/docs/upload).  
HMAC-SHA256 is supported as well.

### Example

```python
import pycaddy as caddy

try:
	with open(filePath, 'rb') as file:
		if key and secret:
			# with authentication
			link = caddy.upload(url, file, key, secret)
		else:
			# without authentication
			link = caddy.upload(url, file)
except Exception as e:
	print(str(e))

print('File uploaded at ' + link)
```

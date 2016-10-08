# PyCaddy

A tiny Python module to manage uploading to [Caddy](https://caddyserver.com/) servers with the [upload extension](https://caddyserver.com/docs/upload).  
HMAC-SHA256 is supported as well.

### Dependencies

- [Requests](http://python-requests.org/)

### Example

```python
import pycaddy as caddy

try:
	with open(filePath, 'rb') as file:
		if key and secret:
			# with authentication
			url = caddy.upload(url, file, key, secret)
		else:
			# without authentication
			url = caddy.upload(url, file)
except Exception as e:
	print(str(e))

print('File uploaded at ' + url)
```

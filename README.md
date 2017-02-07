# PyCaddy

A tiny Python module to manage uploading to [Caddy](https://caddyserver.com/) servers with the [upload extension](https://caddyserver.com/docs/upload).  
HMAC-SHA256 is supported as well.

### Example

```python
import pycaddy as caddy

# upload without authentication
link = caddy.upload(url, file_path)

# upload with authentication
link = caddy.upload(url, file_path, key, secret)

# provide the authentication directly
signature = caddy.SignatureAuth(key, secret)
link = caddy.upload(url, file_path, signature=signature)

print('File uploaded at ' + link)
```

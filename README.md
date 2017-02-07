# PyCaddy

A tiny Python module to manage uploading to [Caddy](https://caddyserver.com/) servers with the [upload extension](https://caddyserver.com/docs/upload).  
HMAC-SHA256 is supported as well.

### Example

```python
import pycaddy as caddy

# upload file without authentication
link = caddy.upload(url, file_path)

# upload file with authentication
link = caddy.upload(url, file_path, key, secret)

# provide the authentication directly
signature = caddy.SignatureAuth(key, secret)
link = caddy.upload(url, file_path, signature=signature)

# move file (new_path is relevant to the server)
caddy.move(url, new_path, signature=signature)

# delete file
caddy.delete(url, signature=signature)

# all of the methods only raise when there are errors
print('File uploaded at ' + link)
```

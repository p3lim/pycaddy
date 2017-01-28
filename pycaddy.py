import ntpath
import time
import hmac, hashlib, base64
import string, random

from .requests import requests

class SignatureAuth(requests.auth.AuthBase):
	def __init__(self, key, secret):
		self.auth_header = 'Signature keyId="%s",signature="%%s"' % key
		self.secret = secret

	def __call__(self, req):
		timestamp = str(int(time.time()))
		token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

		digest = hmac.new(self.secret.encode('utf-8'), (timestamp + token).encode('utf-8'), hashlib.sha256).digest()
		signature = base64.b64encode(digest).decode('utf-8')

		req.headers['Token'] = token
		req.headers['Timestamp'] = timestamp
		req.headers['Authorization'] = self.auth_header % signature

		return req

def upload(url, file_path, key=None, secret=None):
	file_name = ntpath.basename(file_path)

	with open(file_path, 'rb') as file:
		files = {str(file_name): file}

		if key and secret:
			res = requests.post(url, files=files, auth=SignatureAuth(key, secret))
		else:
			res = requests.post(url, files=files)

	res.raise_for_status()

	return res.url + file_name

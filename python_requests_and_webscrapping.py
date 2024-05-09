# -*- coding: utf-8 -*-
"""Python Requests and WebScrapping.ipynb
"""

#pip install requests

import requests
response  = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

response = requests.get('https://api.github.com')
response.content

response.text

response.encoding = 'utf-8' # Optional: requests infers this internally
response.text

response.json()

response.headers
response.headers['Content-Type']
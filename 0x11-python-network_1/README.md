To fetch internet resources and make HTTP requests in Python, you can use either the `urllib` package or the `requests` package. Here's a brief overview of both:

### Using `urllib`:

1. **Fetch Internet Resources:**
   ```python
   from urllib import request

   url = 'https://example.com'
   response = request.urlopen(url)
   html = response.read().decode('utf-8')
   ```

2. **Decode urllib Body Response:**
   You can use `decode('utf-8')` on the response to convert it to a string.

### Using `requests`:

1. **Install `requests`:**
   ```bash
   pip install requests
   ```

2. **Fetch Internet Resources:**
   ```python
   import requests

   url = 'https://example.com'
   response = requests.get(url)
   html = response.text
   ```

3. **Make HTTP GET Request:**
   ```python
   response = requests.get('https://api.example.com/data')
   ```

4. **Make HTTP POST/PUT/etc. Request:**
   ```python
   payload = {'key1': 'value1', 'key2': 'value2'}
   response = requests.post('https://api.example.com/post', data=payload)
   ```

5. **Fetch JSON Resources:**
   ```python
   response = requests.get('https://api.example.com/data.json')
   data = response.json()
   ```

6. **Manipulate Data from an External Service:**
   Once you have the data, you can manipulate it using Python's data manipulation libraries (e.g., `json`, `pandas`, etc.).

### Examples:

```python
# Using requests to fetch and manipulate JSON data
import requests

url = 'https://api.example.com/data.json'

# Fetch JSON resource
response = requests.get(url)
data = response.json()

# Manipulate data
for item in data['items']:
    print(item['name'])
```

Remember to handle exceptions and errors appropriately in a production setting. `requests` is a widely used library for making HTTP requests due to its simplicity and ease of use.

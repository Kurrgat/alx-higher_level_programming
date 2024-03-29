### Python - Network Basics:

1. **URL (Uniform Resource Locator):**
   - A URL is a reference or address used to access resources on the internet. It consists of various components like the scheme, domain, path, query parameters, and fragments.

2. **HTTP (Hypertext Transfer Protocol):**
   - HTTP is a protocol used for transmitting hypermedia documents, such as HTML. It is the foundation of data communication on the World Wide Web.

3. **Reading a URL:**
   - To read a URL in Python, you can use the `urllib.parse` module to parse and manipulate URLs.

4. **Scheme for an HTTP URL:**
   - The scheme in an HTTP URL is typically "http" or "https", indicating the protocol used for communication.

5. **Domain Name:**
   - A domain name is a human-readable address that points to a specific IP address on the internet.

6. **Sub-Domain:**
   - A sub-domain is a domain that is part of a larger domain. For example, "blog.example.com" is a sub-domain of "example.com."

7. **Port Number in a URL:**
   - Port numbers in a URL are specified after the domain, separated by a colon (e.g., `http://example.com:8080`).

8. **Query String:**
   - A query string is a part of the URL that contains key-value pairs separated by "&," used to pass data to a web server.

9. **HTTP Request:**
   - An HTTP request is a message sent by a client to request a specific action from a server. It consists of a request method, URL, headers, and an optional body.

10. **HTTP Response:**
    - An HTTP response is the message sent by a server to fulfill an HTTP request. It contains a status code, headers, and an optional body.

11. **HTTP Headers:**
    - HTTP headers provide additional information about the request or response. They include metadata such as content type, content length, etc.

12. **HTTP Message Body:**
    - The HTTP message body contains the actual data being sent in the request or response, such as the content of a web page.

13. **HTTP Request Method:**
    - HTTP request methods define the action to be performed for a given resource. Common methods include GET, POST, PUT, DELETE, etc.

14. **HTTP Response Status Code:**
    - HTTP status codes indicate the outcome of an HTTP request. Examples include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).

15. **HTTP Cookie:**
    - An HTTP cookie is a small piece of data stored on the client's computer by the web browser, often used for user authentication and session management.

16. **cURL Request:**
    - To make a request with cURL in Python, you can use the `subprocess` module or libraries like `requests` that provide a higher-level interface.

17. **Browser Request to google.com (Application Level):**
    - When you type "google.com" in your browser, it initiates an HTTP request to Google's servers. The server responds with an HTTP response containing the HTML, CSS, and JavaScript code that the browser renders to display the Google search page. This involves DNS resolution, TCP connection establishment, and the exchange of HTTP requests and responses.

# Python - Network #1

This project covers fetching web resources with `urllib` and `requests`.

## Tasks

### 0. What's my status? #0
`0-hbtn_status.py` fetches the ALU status page with `urllib` and prints the
body's type, raw bytes, and UTF-8 decoded text.

### 1. Response header value #0
`1-hbtn_header.py` prints the `X-Request-Id` header of a URL response using
`urllib`.

### 2. POST an email #0
`2-post_email.py` posts an email address as the `email` parameter with
`urllib` and prints the decoded response body.

### 3. Error code #0
`3-error_code.py` prints the body of a URL response, or `Error code:` followed
by the status code when `urllib` raises an HTTP error.

### 4. What's my status? #1
`4-hbtn_status.py` fetches the ALU status page with `requests` and prints the
body's type and content.

### 5. Response header value #1
`5-hbtn_header.py` prints the `X-Request-Id` response header using `requests`.

### 6. POST an email #1
`6-post_email.py` posts the `email` parameter with `requests` and prints the
response body.

### 7. Error code #1
`7-error_code.py` prints the response body, or `Error code:` and the status
code when the status is 400 or higher.

### 8. Search API
`8-json_api.py` posts a `q` letter to the search API and prints `[id] name`,
`No result`, or `Not a valid JSON`.

### 9. My GitHub!
`10-my_github.py` uses Basic Authentication with a personal access token to
print the authenticated GitHub user's id.

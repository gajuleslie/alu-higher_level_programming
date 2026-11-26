# Python - Network #0

This project introduces HTTP requests with `cURL` through small Bash scripts.

## Tasks

### 0. cURL body size
`0-body_size.sh` takes a URL, sends a request to it, and prints the size of the
response body in bytes.

### 1. cURL to the end
`1-body.sh` takes a URL, sends a GET request, and prints only the body of a
successful (200) response.

### 2. cURL method
`2-delete.sh` sends a DELETE request to the URL passed as an argument and prints
the response body.

### 3. cURL only methods
`3-methods.sh` sends an OPTIONS request to the URL passed as an argument and
prints the HTTP methods the server accepts.

### 4. cURL headers
`4-header.sh` sends a GET request with the `X-HolbertonSchool-User-Id: 98`
header and prints the response body.

### 5. cURL POST parameters
`5-post_params.sh` sends a POST request with `email=test@gmail.com` and
`subject=I will always be here for PLD`, then prints the response body.

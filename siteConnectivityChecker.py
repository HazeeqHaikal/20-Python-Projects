import urllib.request as urllib

print("This is a site connectivity checker program")
url = input("Enter URL: ")

def takeURL(url):
    print("Checking connectivity...")
    
    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    match response.getcode():
        case 200:
            print("Status code 200: OK")
        case 301:
            print("Status code 301: Moved Permanently")
        case 302:
            print("Status code 302: Found")
        case 303:
            print("Status code 303: See Other")
        case 304:
            print("Status code 304: Not Modified")
        case 307:
            print("Status code 307: Temporary Redirect")
        case 400:
            print("Status code 400: Bad Request")
        case 401:
            print("Status code 401: Unauthorized")
        case 403:
            print("Status code 403: Forbidden")
        case 404:
            print("Status code 404: Not Found")
        case 405:
            print("Status code 405: Method Not Allowed")
        case 408:
            print("Status code 408: Request Timeout")
        case 500:
            print("Status code 500: Internal Server Error")
        case 501:
            print("Status code 501: Not Implemented")
        case 502:
            print("Status code 502: Bad Gateway")
        case 503:
            print("Status code 503: Service Unavailable")
        case 504:
            print("Status code 504: Gateway Timeout")
        case _:
            print("Status code", response.getcode(), ": Unknown")

if __name__ == '__main__':
    takeURL(url)
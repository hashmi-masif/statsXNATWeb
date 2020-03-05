import urllib.request

# This file is used to check for network connection during testing
# If no network connection found the test depending on network will be skipped

def connect():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False
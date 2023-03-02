import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input("Give URL:")  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #Header
    print("Headers:")
    for header,value in response.headers.items():
        print(header,value,sep=":")
    print("\n")
    #Web Server
    web_server = response.headers.get("Server")
    print("Web Server:",web_server,end="\n\n")
    #Cookies
    cookies = response.cookies
    print("Cookies:\n",cookies)
    for cookie in cookies :
        expires = cookie.expires
        print("Cookies Expiration:",cookie.name,expires)
    #more(html)

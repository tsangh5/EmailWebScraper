from bs4 import BeautifulSoup
import requests
# Execute a web request
params = {}
headers = {}
letters = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', "V", 'W', 'X', 'Y', 'Z']
results=[]
emails=[]
for letter in letters:
    for i in range(1, 10):
        response = requests.get(f'https://www.hkicpa.org.hk/en/Membership/Find-a-CPA/Hong-Kong-CPA-Practice-Directory?pn={i}&pnsn={letter}&pnkw=', params=params, headers=headers)
        html = response.content.decode(response.encoding)
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all('a'):
            try:
                emails.append(link.get('href'))
            except:
                pass
for stuff in emails:
    if type(stuff) == str:
        if '@' in stuff:
            stuff = stuff.replace('mailto:', '')
            results.append(stuff)
print(results, len(results))

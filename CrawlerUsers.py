import requests,csv
from bs4 import BeautifulSoup

def writeFile (User):
	with open('RelatedUsers.csv', 'a') as f:
	    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
    	    writeit.writerow([User])

def getPages(User):
    pages = 2
    refpage = requests.get("http://www.flickr.com/people/" + User + "/contacts/?filter=&page=1").text
    soupp = BeautifulSoup (refpage,"html.parser")
    souppessoas = soupp.find('div',{'class','Results'})
    pessoas = souppessoas.text[1:-8]   # Taking the number of friends
    pages = int(pessoas.replace(',',''))/30 + 2        # +1 for an incomplete page and +1 for the loop limit be exclusive.
    return pages
    
#Taking the amount of this contact's friends
def getUsers(User):
    pages = getPages(User)
    writeFile(User)
    for i in range(1,pages):
        r = requests.get("http://www.flickr.com/people/" + User + "/contacts/?filter=&page=" + str(i))
        if(r.status_code==200):
            html = r.text
            soup = BeautifulSoup (html, "html.parser")
            table = soup.find('table',{'class':'PeopleResults'})
            for td in table.findAll('td',{'class':'Icon'}):
                href = td.find_next('a').get('href')
                Friend = href[8:-1]
                if("/" not in Friend): #To not get invalid values
                    writeFile(Friend)

        print i 
    
mainContact = "j0annie"
getUsers(mainContact)

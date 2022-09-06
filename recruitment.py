import pandas as pd 
import requests
from bs4 import BeautifulSoup

url = "https://courses.uit.edu.vn/user/index.php?id=9857&perpage=150"
login = "https://courses.uit.edu.vn/login/index.php"

with requests.Session() as s:
    s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    res = s.get(login)
    soup = BeautifulSoup(res.text,'html.parser')   
    payload = {i['name']:i.get('value','') for i in soup.select('input[name]')}         
    #what the above line does is parse the keys and valuse available in the login form
    payload['username'] = 20520688
    payload['password'] = 1753552030

    print(payload) #when you print this, you should see the required parameters within payload 

    s.post(login,data=payload)
    #as we have laready logged in, the login cookies are stored within the session
    #in our subsequesnt requests we are reusing the same session we have been using from the very beginning
    r = s.get(url).text
    #print(r.status_code)
    sourceF = open('web.xlxs', 'w')
    #print(r.text, file=sourceF)

#html_data = requests.get(url).text
soup1 = BeautifulSoup (r, 'lxml')
amazon_data = pd.DataFrame(columns=["Name", "Role", "Group", "Access"])

for row in soup1.find("tbody").find_all("tr"):
    col = row.find_all("th")
    name = col[0].text
    col = row.find_all("td")
    role = col[1].text
    group = col[2].text 
    access = col[3].text
    amazon_data = amazon_data.append({"Name":name, "Role":role, "Group":group, "Access":access}, ignore_index=True)
    
    # tmp = amazon_data
    # tmp.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    # amazon_data = pd.concat(tmp)
    
    #tmp.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    #amazon_data = pd.concat({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
    
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(amazon_data, file=sourceF)

#print(amazon_data, file=sourceF)
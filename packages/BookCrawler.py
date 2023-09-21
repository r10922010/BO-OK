import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}

"""
找書
target => 書名
"""
def searchbook(target):
    booksURL="https://search.books.com.tw/search/query/cat/all/key/"+target
    kingstoneURL="https://www.kingstone.com.tw/search/search?q="+target
    sanminURL="https://www.sanmin.com.tw/search/index/?ct=N&qu="+target+"&ls=SD"
    
    BOOKSbook=[]
    r = requests.get(booksURL)
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("ul.searchbook li.item")
    for s in sel:
        link=s.find('a').get('href')
        spl=link.split('/')
        if(not(spl[4][0]<='9' and spl[4][0]>='0') and not(spl[4][0]=='E')and not(spl[4][0]=='R')):
            continue
        name=s.find('a').get('title')
        img=s.find('a').find('img').get('data-original')
        img=img.split('&')[0]
        temp=s.find_all('a',rel='go_author')
        writer=""
        for i in temp:
            writer+=i.get('title')
            writer+=' '
        price=s.find('span',class_="price").find_all('b')[-1].string
        
        book={
                "List":[name,link,img,writer,int(price)]
            }
        BOOKSbook.append(book)
    
    r = requests.get(kingstoneURL,headers=header)
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("li.displayunit div.division1")
    basicURL="https://www.kingstone.com.tw"
    KINGSTONEbook=[]
    for s in sel:
        temp=s.find('span',class_='book').string
        if(temp.find("書")==-1):
            if(temp.find("雜誌")==-1):
                continue
        img=s.find('div',class_='coverbox').find('a').find('img').get('data-src')
        link=basicURL+s.find('a').get('href')
        name=s.find('a').find('img').get('title')
        writer=s.find('div',class_='basic2box').find('span')
        if(writer==None):
            writer=None
        else:
            temp=writer.find_all('a')
            writer=""
            for i in temp:
                writer+=i.string+' '
        
        price=s.find('div',class_='buymixbox').find_all('span')[-2].find('b').string
        book={
                "List":[name,link,img,writer,int(price)]
            }
        KINGSTONEbook.append(book)
    
    
    basicURL="https://www.sanmin.com.tw"
    SANMINbook=[]
    r = requests.get(sanminURL)
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("div.ProductView div.condition")
    for s in sel:
        img=s.find('div',class_='resultBooksImg').find('a').find('img').get('original')
        name=s.find('h3').find('a').text
        name=name.split('.')[-1]

        link=basicURL+s.find('div',class_='resultBooksImg').find('a').get('href')
        if(s.find('span',class_='ProdAu')==None):
            continue
        
        temp=s.find('span',class_='ProdAu').find_all('a')
        writer=""
        for i in temp:
            writer+=i.string+' '
        price=s.find('span',class_='price')
        if price==None:
            price=s.find('div',class_="resultBooksLayout").find('p').string
            price=price.replace(' ','')
            price=price.replace('\n','')
            price=price.replace('\r','')
            price=price.replace('\xa0','')
            price=price[3:-1]
        else:
            price=price.string
        
        book={
                "List":[name,link,img,writer,int(price)]
            }
        SANMINbook.append(book)
      #  print(book['List'][2])
    return [BOOKSbook,KINGSTONEbook,SANMINbook]



def getSANMINrank():
    basicURL="https://www.sanmin.com.tw"
    
    books=[]
    for i in range(3):#如果要抓少一點改這邊 1次=20本
        r = requests.get(basicURL+"/promote/top/?pi="+str(i+1)) 
        soup = BeautifulSoup(r.text,"html.parser") 
        sel = soup.find('div',id='normal-list').select("div.condition")
        for s in sel:
            img=s.find("img").get('original')
            link=basicURL+s.find("div",class_='resultBooksInfor').find("a").get('href')
            listwriter=s.find("p",class_='author').find('span',class_='green13').find_all('a')
            temp=""
            for j in listwriter:
                temp+=j.string+' '
                temp= temp.replace('\n','')
                temp= temp.replace('   ','')
            writer=temp
            price=s.find("div",class_='resultBooksLayout').find('span',class_='price').string
            name=s.find('h3').find('a').string
            name=name.split('.')[-1]
            book={
                "List":[name,link,img,writer,int(price)]
            }
            books.append(book)
    return books

def getKINGSTONErank():
    basicURL="https://www.kingstone.com.tw"
    r = requests.get("https://www.kingstone.com.tw/bestseller/best/book",headers=header) 
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("div.proMain li.modProList") 

    books=[]
    
    for s in sel:
        temp=s.find("div",class_="modProPic")
        img=temp.find("img").get('data-src')
        link=temp.find('a').get("href")
        link=link.split('?')[0]
        link=basicURL+link
        name=temp.find("img").get('alt')
        writer=s.find("div",class_="modProAuthor").find('a').string
        price=s.find_all('b')[-1].string
        book={
            "List":[name,link,img,writer,int(price)]
        }

        books.append(book)

    return books

def getBOOKSrank():
    r = requests.get("https://www.books.com.tw/web/sys_hourstop/home?loc=P_0022_more_001") 
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("div.clearfix li.item")
    books=[]
    for s in sel:
        link=s.find("h4").find("a").get('href').split('?')[0]
        spl=link.split('/')
        if(not(spl[4][0]<='9' and spl[4][0]>='0') and not(spl[4][0]=='E')and not(spl[4][0]=='R')):
            continue

        img=s.find("img").get('src').split('&')[0]
        name=s.find("h4").find("a").string
        writer=s.find("ul").find("li").find("a")
        if(writer==None):
            writer=None
        else:
            writer=writer.string

        list_price=s.find("ul").find("li",class_="price_a").find_all("b")
        price=list_price[-1].string
        book={
            "List":[name,link,img,writer,int(price)]
        }
        books.append(book)
    return books

"""
爬新書
"""
def newbook():
    r = requests.get("https://www.books.com.tw/web/sys_newtopb/books/")
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("div.clearfix li.item")
    BOOKSbook=[]
    for s in sel:
        link=s.find("h4").find("a").get('href').split('?')[0]
        spl=link.split('/')
        if(not(spl[4][0]<='9' and spl[4][0]>='0') and not(spl[4][0]=='E')and not(spl[4][0]=='R')):
            continue

        img=s.find("img").get('src').split('&')[0]
        name=s.find("h4").find("a").string
        writer=s.find("ul").find("li").find("a")
        if(writer==None):
            writer=None
        else:
            writer=writer.string

        list_price=s.find("ul").find("li",class_="price_a").find_all("b")
        price=list_price[-1].string
        book={
            "List":[name,link,img,writer,int(price)]
        }
        BOOKSbook.append(book)

    basicURL="https://www.kingstone.com.tw"
    r = requests.get("https://www.kingstone.com.tw/BestSeller/news/book",headers=header) 
    soup = BeautifulSoup(r.text,"html.parser") 
    sel = soup.select("div.proMain li.modProList") 

    KINGSTONEbook=[]
    
    for s in sel:
        temp=s.find("div",class_="modProPic")
        img=temp.find("img").get('data-src')
        link=temp.find('a').get("href")
        if (link.find("book")==-1):
            continue
        link=link.split('?')[0]
        link=basicURL+link
        name=temp.find("img").get('alt')
        writer=s.find("div",class_="modProAuthor").find('a').string
        price=s.find_all('b')[-1].string
        book={
            "List":[name,link,img,writer,int(price)]
        }
        KINGSTONEbook.append(book)



    basicURL="https://www.sanmin.com.tw"    
    SANMINbook=[]
    for i in range(1):#如果要抓少一點改這邊 1次=20本
        r = requests.get(basicURL+"/promote/hotbook/?id=00&vs=grid&pi="+str(i+1)+"&vs=list") 
        soup = BeautifulSoup(r.text,"html.parser") 
        sel = soup.find('div',id='normal-list').select("div.condition")
        for s in sel:
            img=s.find("img").get('original')
            link=basicURL+s.find("div",class_='resultBooksInfor').find("a").get('href')
            listwriter=s.find("p",class_='author').find('span',class_='green13').find_all('a')
            temp=""
            for j in listwriter:
                temp+=j.string+' ' 
                temp= temp.replace('\n','')
                temp= temp.replace('   ','')
            writer=temp
            price=s.find("div",class_='resultBooksLayout').find('span',class_='price').string
            name=s.find('h3').find('a').string
            name=name.split('.')[-1]
            name=name.split('－')[-1]

            book={
                "List":[name,link,img,writer,int(price)]
            }
            SANMINbook.append(book)


    return [BOOKSbook,KINGSTONEbook,SANMINbook]
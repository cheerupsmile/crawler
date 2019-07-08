import urllib.request
from bs4 import BeautifulSoup



def main():
    list_href = []
    list_content = []
  
    url =  ##########################url수정하기############ 
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    for href in soup.find_all("div",class_="mfn_inner"):#####테그와 class
        list_href.append("########url앞부분 주소 넣기#########"+href.find('a')["href"])

    for i in range(0, len(list_href)):
        url = list_href[i]
        source_code = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source_code, "html.parser")

        list_content.append(soup.find('div',class_="text_area").get_text())

    print(list_href)
    print(list_content)


if __name__ == "__main__":
    main()

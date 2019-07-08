import urllib.request
from bs4 import BeautifulSoup



def main():
    print("href 출력해보기")

    list_href = []

    url = ""#####################수정
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")


    # href 모두 수집하여 list_href에 저장
    for i in range(3,23):
        #목록 하나에 들어가는 링크갯수 수정
        
        list_href.append(soup.find_all("span",class_="tit")[i].find("a")['href'])

    print(list_href)


if __name__ == "__main__":
    main()

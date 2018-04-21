# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import urllib.request
import urllib.parse
import datetime
from bs4 import BeautifulSoup


class NewsCrawler :    
    def __init__(self, keyword, date) :
        self.keyword = keyword
        self.date = date

        fullURL_meta = 'https://openapi.naver.com/v1/search/news.xml?sort=date&start=%d&display=%d'
        fullURL = fullURL_meta%(1,1)
        """
        defaultURL = 'https://openapi.naver.com/v1/search/news.xml?'
        sort = 'sort=date'
        start = '&start=1'
        display = '&display=1'
        """
        # 사용자에게 검색어를 입력받아 quote_plus 함수로 UTF-8 타입에 맞도록 변환시켜 줍니다.
        self.query = '&query=' + urllib.parse.quote_plus(str(keyword))  
        fullURL = fullURL+ self.query
        self.headers = {
            'Host' : 'openapi.naver.com',
            'User-Agent' : 'curl/7.43.0',
            'Accept' : '*/*',
            'Content-Type' : 'application/xml',
            'X-Naver-Client-Id' : '96DwyVJz0WexhFhU6uk3',
            'X-Naver-Client-Secret' : 'uvTcTSqHxm'
        }
        # HTTP 요청을 하기 전에 헤더 정보를 이용해 request 객체를 생성합니다. urllib 모듈에서 헤더 정보를 서버에 전달할 때 사용하는 대표적인 방법입니다.
        req = urllib.request.Request(fullURL, headers=self.headers)
        # 생성된 request객체를 uplopen함수의 인수로 전달합니다. 이렇게 되면 헤더 정보를 포함하여 서버에게 HTTP 요청을 하게 됩니다.
        f = urllib.request.urlopen(req)
        resultXML = f.read()
        xmlsoup = BeautifulSoup(resultXML, 'html.parser')
        self.total = int(xmlsoup.total.get_text(strip=True))
    def getTotal(self):
        return self.total
    def getInfo(self):
        return self.keyword, self.total

if __name__ == "__main__" :
    nc = NewsCrawler("황종국 강원도 고성군","19990101")
    print(nc.getTotal())
    print(nc.getInfo())


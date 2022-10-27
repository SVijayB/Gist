import requests
from bs4 import BeautifulSoup


class InShort:
    __category = None

    def __init__(self, category='all'):
        # dict to hold category wise DB offset
        self.__Categories = {
            "all": None,
            "national": None,
            "business": None,
            "sports": None,
            "world": None,
            "politics": None,
            "technology": None,
            "startup": None,
            "entertainment": None,
            "miscellaneous": None,
            "hatke": None,
            "science": None,
            "automobile": None
        }
        self.__content = {
            "all": [],
            "national": [],
            "business": [],
            "sports": [],
            "world": [],
            "politics": [],
            "technology": [],
            "startup": [],
            "entertainment": [],
            "miscellaneous": [],
            "hatke": [],
            "science": [],
            "automobile": []

        }
        if category in self.__Categories.keys():
            self.__category = category
            self.__initial_get()
        else:
            raise Exception(f"Invalid Category {category}")

    # private method
    def __initial_get(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
        }
        s = requests.Session()
        s.headers = headers
        self.__s = s
        query = "" if self.__category == "all" else self.__category
        print(f"requesting url :https://www.inshorts.com/en/read/{query}")
        r = s.get(f"https://www.inshorts.com/en/read/{query}")
        if r.status_code == 200:
            response = r.text
            offset = response.split("min_news_id = \"")[1].split("\"")[0]
            self.__Categories[self.__category] = offset
            content = self.__to_json(r, caller=1)
            self.__content[self.__category] = content
        else:
            raise Exception(f"Check Connection,request status code : {r.status_code}")

    def __to_json(self, r, caller=2):
        json_list = []
        if caller == 2:
            new_cards = BeautifulSoup(r.json()['html'], 'lxml').findAll(class_='news-card')
        else:
            new_cards = BeautifulSoup(r.text, 'lxml').findAll(class_='news-card')
        for card in new_cards:
            try:
                headline = card.find(class_="news-card-title").find('span').text
            except Exception:
                headline = None
            try:
                image_url = card.find(class_="news-card-image")['style'].split("'")[1]
            except Exception:
                image_url = None
            try:
                url = 'https://www.inshorts.com' + card.find(class_="news-card-title").find('a').get('href')
            except Exception:
                url = None
            try:
                author = card.find(class_="author").text
            except Exception:
                author = None
            try:
                date = card.find(clas="date").text
            except Exception:
                date = None
            try:
                time = card.find(class_="time").text
            except:
                time = None
            try:
                content = card.find(class_="news-card-content").find('div').text
            except Exception:
                content = None
            try:
                full_article_link = card.find(class_="read-more").find('a').get('href')
            except Exception:
                full_article_link = None

            data = {
                'title': headline,
                'imageUrl': image_url,
                'url': url,
                'author': author,
                'date': date,
                'time': time,
                'content': content,
                'readMoreUrl': full_article_link
            }

            json_list.append(data)
        return json_list

    # public method
    def is_valid_category(self, category):
        if category in self.__Categories.keys():
            return True
        else:
            return False

    def get_more(self, category='all'):

        # check if valid category
        if not self.is_valid_category(category):
            raise Exception(f"Invalid Category")
        else:
            self.__category = category

        if self.__Categories[self.__category] is None:
            self.__initial_get()
        else:
            curr_category_offset = self.__Categories[self.__category]
            post_data = f"category=&news_offset={curr_category_offset}"
            r = self.__s.post("https://inshorts.com/en/ajax/more_news", data=post_data)
            if r.status_code == 200:
                curr_category_offset = r.json()['min_news_id']
                self.__Categories[self.__category] = curr_category_offset
                content = self.__to_json(r)
                self.__content[self.__category] += content
            else:
                raise Exception(f"Connection failed with request status code : {r.status_code}")

    def __str__(self):
        return str(self.__content)

    def __len__(self):
        pass

    def get_curr_category(self):
        return self.__category

    def get_content(self, category='all'):
        if not self.is_valid_category(category):
            raise Exception(f"Invalid Category")
        else:
            return self.__content[category]

    def get_all(self):
        return self.__content

    # get db offset value by category
    def get_offset(self,category='all'):
        if not self.is_valid_category(category):
            raise Exception(f"Invalid Category")
        else:
            return self.__Categories[category]

    def get_all_offset(self):
        return self.__Categories


obj = InShort("all")
obj.get_more()
obj.get_more("entertainment")
print(obj.get_offset("entertainment"))
print(obj.get_all_offset())
obj.get_more("sports")
print(obj.get_offset("sports"))
print(obj.get_all_offset())

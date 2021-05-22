import re

import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []

    authors = [author.text for author in parser.body.findAll("a", {"class": "hnuser"})]

    comments = [i for i in parser.body.find_all("a") if "item?id=" in i.attrs["href"]]
    comments = [
        i.text for i in comments if (re.match("\d+\scomment", i.text) or i.text == "discuss")
    ]
    comments = [int(i[: i.find("\xa0")]) if not "discuss" in i else 0 for i in comments]

    scores = [
        int(i.text[: i.text.find(" ")]) for i in parser.body.find_all("span", {"class": "score"})
    ]

    links = [link for link in parser.body.findAll("a", {"class": "storylink"})]
    links = [link.attrs["href"] for link in links]

    titles = [i.text for i in parser.body.find_all("a", {"class": "storylink"})]

    assert len(authors) == len(comments) == len(scores) == len(links) == len(titles)

    for i in range(len(authors)):
        dic = {
            "title": titles[i],
            "author": authors[i],
            "url": links[i],
            "comments": comments[i],
            "points": scores[i],
        }
        news_list.append(dic)

    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    url = parser.body.find("a", {"class": "morelink"}).attrs["href"]
    return url


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

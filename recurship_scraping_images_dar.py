from requests import get
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import time


def scrapPage(url, imgs, links):
    response = get(url)

    # Parsing the site using lxml
    soup = BeautifulSoup(response.text, 'lxml')

    # make a list of all the links on the page
    for t in soup.select("h2.entry-title"):
        links.append((t.text, t.a['href']))
    # print(links)

    # loop to traverse to each link
    for next_url in links:
        article = get(next_url[1])
        tomatoSoup = BeautifulSoup(article.text, 'lxml')

        # list of all the image links on a page
        img_links = []
        # find every image src and append them in the list
        # (not getting data-src because that's the alternative/duplicate)
        for i in tomatoSoup.select("img"):
            img_links.append(i['src'])

        # add the corresponding links in the dictionary with the article name
        imgs[next_url[0]] = img_links


def main():
    t1 = time.time()
    imgs = {}
    links = []

    url = "http://recurship.com/"
    scrapPage(url, imgs, links)

    pages_to_scrap = 2  # max pages on the site are 5
    for i in range(2, pages_to_scrap+1):
        url = f"http://recurship.com/page/{i}/"
        scrapPage(url, imgs, links)

    # print(imgs)

    # printing the dictionary in a more readable format
    for data in imgs:
        print(data, ': \n')
        for links in imgs[data]:
            print(links)
        print('\n')

    print(f"Time taken in scraping and printing: {time.time()- t1}")


if __name__ == "__main__":
    main()

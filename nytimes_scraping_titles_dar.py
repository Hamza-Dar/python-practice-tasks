from requests import get
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer


def main():
    url = "https://www.nytimes.com/"

    # .css-debyuq:last-child > .e1voiwgp0
    # .css-debyuq
    # balancedHeadline

    response = get(url)
    # print(response.text[:500])

    # Parsing the site using lxml
    soup = BeautifulSoup(response.text, 'lxml')

    # class for the article titles
    divs = soup.select('.e1voiwgp0')

    # total divs with this class attribute
    print(len(divs), '\n')

    # print each title
    for h in divs:
        print(h.text)


if __name__ == "__main__":
    main()

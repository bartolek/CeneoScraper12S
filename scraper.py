#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL strony z opiniami
url = "https://www.ceneo.pl/85910996#tab=reviews"

#pobranie kodu HTML strony
page_respons = requests.get(url)
page_tree = BeautifulSoup(page_respons.text, "html.parser")

#wydobycie z kodu HTML fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych dla pojedynczej opinii
for opinion in opinions:

    opinion_id = opinion["data-entry-id"]
    author = opinion.find("div", "reviewer-name-line").string
    recomendation = opinion.find("div", "product-review-summary").find("em").string
    stars = opinion.find("span","review-score-count").string
    try:
        purchased = opinion.find("div", "product-review-pz").string
    except IndexError:
        purchased = None
    dates = opinion.finf("span", "review-time").find_all("time").
    review_date = dates.pop()["datetime"]
    try:
        purchase_date = dates.pop()["datetime"]
    except IndexError:
        purchase_date = None


    usefull = opinion.find("button", "vote-yes").find("span").string
    useless = opinion.find("button", "vote-no").find("span").string
    content = opinion.find("p", "product-review-body").get_text()

    try:
        pros = opinion.find("div", "pros-cell").find("ul").get_text()
    except IndexError:
        pros = None

    try:
        cons = opinion.find("div", "pros-cell").find("ul").get_text()
    except IndexError:
        cons = None


## Etap 2 - pobieranie skłądowych wszystkich opinii z pojedynczej strony
-zapisanie składowych opinii w złożonej strukturze danych
## Etap 3 
- przechodenie po stronach z opiniami
- eksport opinii do pliku (.csv lub .xlsx lub .json)


import bs4
import requests

def wikiRequest(string):

    print ("Search Wikipedia about.... " + string)

    req = requests.get("https://pt.wikipedia.org/wiki/"+ string)

    if req is not None:
        page = bs4.BeautifulSoup(req.text, 'html.parser')

        title = page.select("#firstHeading")[0].text
        paragraphs = page.select("p")
        intro = '\n'.join([ para.text for para in paragraphs[0:10]])
        return intro

        # print(title)
        # print (intro)

# wikiRequest('cavalo')
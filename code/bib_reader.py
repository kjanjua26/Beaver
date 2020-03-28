'''
    This is the main utility function that takes the title and returns the bibtex citation.
'''
from bs4 import BeautifulSoup
import requests, os
from urllib.request import Request, urlopen

class Parser:
    '''
        The parser class for scrapping the Google Scholar. 
        Since there is no official API, we write the scrapping part.
        # Arguments:
            When the object of Parser class is created, it accepts the name of the paper.
        # Returns:
            It returns the bibtex reference for the paper.
    '''
    def __init__(self, paper_name):
        self.paper_name = paper_name

    def read_page(self, base_url):
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
        req = Request(base_url, headers=header)
        webpage = urlopen(req).read()
        return BeautifulSoup(webpage, 'html.parser')

    def get_cluster_and_bib_id(self):
        base_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=' + str('+'.join(self.paper_name.split(' '))) + '&oq='
        page = self.read_page(base_url)
        cluster_id = list(page.find_all('a', attrs={'class': 'gs_nph'}))
        bib_id = page.find_all('a', attrs={'class': 'gs_or_nvi'})
        if len(bib_id) > 0:
            bib_id = str(bib_id[0]).split('q=cache:')[-1].split(':scholar')[0]
        else:
            print('Google Blocking!')
        cluster_id = str(cluster_id[-1]).split('&')[0].split('?cluster=')[-1]
        return (cluster_id, bib_id)
    
    def recover_bib(self):
        _, bib_id = self.get_cluster_and_bib_id()
        base_bib_url = 'https://scholar.google.com/scholar?q=info:{}:scholar.google.com/&output=cite&scirp=0&hl=en'.format(bib_id)
        page = self.read_page(base_bib_url)
        bib_data = page.find_all('a', attrs={'class': 'gs_citi'})
        print(str(bib_data[0]).split(''))


if __name__ == "__main__":
    p1 = Parser("Deep Latent Space Learning for Cross modal Mapping of Audio and Visual Signals")
    p1.recover_bib()
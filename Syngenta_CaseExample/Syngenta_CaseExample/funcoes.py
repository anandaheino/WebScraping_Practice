from urllib.request import urlopen
from bs4 import BeautifulSoup

def abre_e_scrap(url):
    """Esta função abre o url dado como parâmetro e retorna a 'sopa de html'.
    Parâmetro: url
    Retorno: uma sopa de html da página."""

    html = urlopen(url)
    scrap = BeautifulSoup(html, 'html.parser')
    return scrap


def find_links_in_cards(scrap, class_card):
    """ Função que recebe a sopa e a string dos cards,
    passa por todos esses cards e retorna os links contidos neles.
    Parâmetros:
    * scrap: página html obtida através do BeautifulSoup
    * class_card: qual a str correspondente ao card a ser encontrado
    Retorno: uma lista contendo os links contidos em cada card."""

    cards = scrap.find_all('div', {'class': class_card})

    links = []

    for link in cards:
        link = link.a['href']
        links.append(link)

    return links
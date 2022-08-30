from dataclasses import asdict

from utils.config import Imobiliaria
from utils.csv_util import write_csv
from utils.pages import Selectors, card_data, cards


def _scrap_pagination():
    ...


def _scrap_without_pagination(selectors: Selectors, imobiliaria: Imobiliaria):
    imoveis = []

    for card in cards(imobiliaria.search_url, imobiliaria.css.cards):
        data = card_data(card, selectors, imobiliaria.base_url)
        data |= {'imobiliaria': imobiliaria.name}
        imoveis.append(data)

    return imoveis


def scrap(imobiliaria: Imobiliaria) -> None:
    selectors = Selectors(**asdict(imobiliaria.css))

    if imobiliaria.pagination:
        imoveis = _scrap_pagination()
    else:
        imoveis = _scrap_without_pagination(selectors, imobiliaria)

    write_csv(imobiliaria.name, imoveis)

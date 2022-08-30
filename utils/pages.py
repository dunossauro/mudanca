from dataclasses import dataclass
from csv import Error
from httpx import Client
from parsel import Selector

from .headers import headers

client = Client(headers=headers, timeout=None)


@dataclass
class Selectors:
    href: str
    title: str
    desc: str
    price: str
    base_url: str


def cards(content_url: str, cards_selector: str) -> list[Selector]:
    response = client.get(content_url)
    if (code := response.status_code) != 200:
        raise Error(f'Request Error {code} - {content_url}')
    sel = Selector(response.text)
    return sel.css(cards_selector)


def card_page(
    card: Selector, selector: str, base_url: str
) -> tuple[Selector, str]:
    card_url: str = card.css(selector).get()
    final_url = f'{base_url}{card_url}'
    response = client.get(final_url)
    sel = Selector(response.text)
    return sel, final_url


def card_title(page, selector) -> str:
    return page.css(selector).get()


def card_desc(page, selector) -> str:
    return page.css(selector).get()


def card_price(page, selector) -> str:
    return page.css(selector).get()


def card_data(card: Selector, selectors: Selectors) -> dict[str, str]:
    card_sel, url = card_page(card, selectors.href, selectors.base_url)
    title = card_title(card_sel, selectors.title)
    price = card_price(card_sel, selectors.price)
    desc = card_desc(card_sel, selectors.desc)

    return {'titulo': title, 'descricao': desc, 'preco': price, 'url': url}

from utils.pages import cards, card_data, Selectors
from utils.config import Imobiliarias

imobiliarias = Imobiliarias.from_yaml_file('imobiliarias.yaml')

for imobiliaria in imobiliarias.imobiliarias:
    css = imobiliaria.css

    selectors = Selectors(
        base_url=imobiliaria.base_url,
        href=css.href,
        title=css.title,
        price=css.price,
        desc=css.desc
    )

    for card in cards(imobiliaria.search_url, css.cards):
        print(card_data(card, selectors))

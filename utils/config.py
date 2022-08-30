from dataclasses import dataclass
from dataclass_wizard import YAMLWizard


@dataclass
class CSS:
    href: str
    title: str
    desc: str
    price: str
    cards: str


@dataclass
class Imobiliaria:
    nome: str
    base_url: str
    search_url: str
    css: CSS
    pagination: bool = False


@dataclass
class Imobiliarias(YAMLWizard):
    imobiliarias: list[Imobiliaria]

from utils.config import Imobiliarias
from utils.scrap import scrap

imobiliarias = Imobiliarias.from_yaml_file('imobiliarias.yaml')

for imobiliaria in imobiliarias.imobiliarias:
    scrap(imobiliaria)

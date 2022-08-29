"""
Arquivo base para não ter que iniciar os imports e estrutura básica todas as vezes.
"""

from parsel import Selector
from httpx import Client

from utils.headers import headers
from utils.csv_utils import write_csv

base_url = ''
url = ''

client = Client(headers=headers, timeout=None)


resultado = []

# loop


write_csv('...', resultado)

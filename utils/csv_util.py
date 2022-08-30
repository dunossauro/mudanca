from csv import DictWriter


def write_csv(
    imobiliaria: str,
    vals: list[dict[str, str]],
    fieldnames: list[str] = ['titulo', 'descricao', 'preco', 'url'],
):
    with open(f'data/{imobiliaria}.csv', 'w', encoding='utf-8') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(vals)

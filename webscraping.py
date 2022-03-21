from bs4 import BeautifulSoup as BS
import pandas as pd
import requests
import re

###############################˜#################################
########################## WEBSCRAPING #########################
################################################################

# page = requests.get('https://www.fundamentus.com.br/ultimos-resultados.php')
# print(page.status_code)

# Se der 403, verificar autorizações que estão no cabeçado de solicitação. Como:
# Inpecionar -> Network -> refresh page -> últimos resultados -> header
# Botão direito no "últimos resultados" -> copy -> copy as curl
# Procura no google um site que converte curl to python (https://curlconverter.com/)
# Faz a conversão e cola os dados do header no código

headers = {
    "authority": "www.fundamentus.com.br",
    "cache-control": "max-age=0",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://www.fundamentus.com.br/",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "PHPSESSID=b35b6f7e4375de4017926983c7b3c3b9; __utma=138951332.603349871.1645791453.1645791453.1645791453.1; __utmc=138951332; __utmz=138951332.1645791453.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _fbp=fb.2.1645791452965.1662452217; __gads=ID=da6343ddcbcb1019-22825324cb7b007f:T=1645791453:RT=1645791453:S=ALNI_MbwgrZR2JVeAIbqnFdd3Cdxwtha3A; __cf_bm=B_MY59FPh103xQNjwUMyd1dMabrsX2r4AsOmg7wCmi8-1645791455-0-AXVuJvcPFqziuSDjQT1PxlmxuVZylJtEHL7/tQYbfC1YyjV3HQd1MlWDgIxOZ928IQckWjnXzh5frVauVz8rqkrshCPLKdLbivXDplu6uZDiehJ9IsasC84fkO4LX4rZRQ==; __utmb=138951332.2.10.1645791453",
}
page = requests.get(
    "https://www.fundamentus.com.br/ultimos-resultados.php", headers=headers
)

print(page.status_code)

# Get page content in a better format:
source_page = BS(page.content, "html.parser")

# Filter by tag using regex, [:-1] eliminates the last value
links = source_page.find_all("a", attrs={"href": re.compile("detalhes.php")})[:-1]


# Retorna o primeiro elemento
# print(links[0])

# Retorna o texto dentro de <a> TEXTO <\a>
# print(links[0].text)

# Retorna o link desejado em formato json
# print(links[0].attrs['href'])

# Para pegar todos os links desejados e salvar em json, usar a função anônima lambda (funciona como um for)
links = list(map(lambda x: x.attrs["href"], links))
# print(links)

# interar cada link na variável
def details(link):
    print(f"O código está pegando o link: {link}")
    headers = {
        "authority": "www.fundamentus.com.br",
        "cache-control": "max-age=0",
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": "https://www.fundamentus.com.br/",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "PHPSESSID=b35b6f7e4375de4017926983c7b3c3b9; __utma=138951332.603349871.1645791453.1645791453.1645791453.1; __utmc=138951332; __utmz=138951332.1645791453.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _fbp=fb.2.1645791452965.1662452217; __gads=ID=da6343ddcbcb1019-22825324cb7b007f:T=1645791453:RT=1645791453:S=ALNI_MbwgrZR2JVeAIbqnFdd3Cdxwtha3A; __cf_bm=B_MY59FPh103xQNjwUMyd1dMabrsX2r4AsOmg7wCmi8-1645791455-0-AXVuJvcPFqziuSDjQT1PxlmxuVZylJtEHL7/tQYbfC1YyjV3HQd1MlWDgIxOZ928IQckWjnXzh5frVauVz8rqkrshCPLKdLbivXDplu6uZDiehJ9IsasC84fkO4LX4rZRQ==; __utmb=138951332.2.10.1645791453",
    }
    page_data = requests.get(
        "https://www.fundamentus.com.br/{}".format(link), headers=headers
    )
    source_page_data = BS(page_data.content, "html.parser")
    # Pega somente as tabelas
    tables = source_page_data.find_all("table")
    tables_data = {}
    for i in range(0, len(tables)):
        label = tables[i].find_all("td", attrs={"class": "label"})
        data = tables[i].find_all("td", attrs={"class": "data"})
        tables_data.update(
            dict(
                zip(
                    list(map(lambda x: x.text.replace("?", ""), label)),
                    list(map(lambda x: x.text.replace("\n", ""), data)),
                )
            )
        )
    return tables_data


data_acoes = []
for i in links:
    data_acoes.append(details(i))
print(len(data_acoes))
# print(data_acoes)


################################################################
######################## ANÁLISE DOS DADOS ######################
################################################################

import plotly.express as px

df = pd.DataFrame(data_acoes)
df.head()

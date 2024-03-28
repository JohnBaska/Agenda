import requests
from bs4 import BeautifulSoup

class Informacoes():
    def Estados (self):
        url = 'https://www.todamateria.com.br/estados-do-brasil/' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        estados = soup.find_all('tbody') #qual parte do site vc quer?
        estados = soup.find_all('td')
        self.estados = []
        j = 0

        for i in range(len(estados)):
            if i % 3 == 0:
                self.estados.insert(j, estados[i].get_text())
                j += 1
    
    def Cidades_MG (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Minas_Gerais_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()[0:len(informacoes_tabela[i].get_text()) - 1]
                self.cidades.insert(j, cidade)
                j += 1
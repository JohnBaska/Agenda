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
    
    def Cidades_AC (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Acre_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_AL (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Alagoas_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_AP (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_AM (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amazonas_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_BA (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_da_Bahia_por_popula%C3%A7%C3%A3o_(2022)' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 6 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_CE (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Cear%C3%A1_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_ES (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Esp%C3%ADrito_Santo_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_GO (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Goi%C3%A1s_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_MA (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Maranh%C3%A3o_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_MT (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Mato_Grosso_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 4 == 2:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_MS (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Mato_Grosso_do_Sul_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        cidade = ""
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
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
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_PA (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Par%C3%A1_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_PB (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_da_Para%C3%ADba_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_PR (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Paran%C3%A1_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_PE (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Pernambuco_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_PI (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Piau%C3%AD_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 6 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_RJ (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Rio_de_Janeiro_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_RN (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Rio_Grande_do_Norte_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 4 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_RS (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Rio_Grande_do_Sul_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_RO (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Rond%C3%B4nia_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_RR (self): #erro
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Roraima_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 6 == 2:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_SC (self): #erro
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Santa_Catarina_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        cidade = ""
        
        for i in range(len(informacoes_tabela)):
            if i % 4 == 1:
                cidade = informacoes_tabela[i].get_text()
                self.cidades.insert(j, cidade)
                j += 1
    def Cidades_SP (self): #erro
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_S%C3%A3o_Paulo_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find_all('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela[1].find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_SE (self):
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Sergipe_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
    def Cidades_TO (self): #erro
        url = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Tocantins_por_popula%C3%A7%C3%A3o' #site de onde irá vir o texto

        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" } #pesquise no seu navegador my user agent

        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        tabela = soup.find('tbody') #qual parte do site vc quer?
        informacoes_tabela = tabela.find_all('td')
        self.cidades = []
        j = 0
        for i in range(len(informacoes_tabela)):
            if i % 3 == 1:
                self.cidades.insert(j, informacoes_tabela[i].get_text())
                j += 1
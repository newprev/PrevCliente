import requests as http


class IntegracaoRepository:

    def __init__(self):
        self.urlBase = 'https://'

    def getCep(self, numCep):
        url = self.urlBase + f'viacep.com.br/ws/{numCep}/json/'
        try:
            response: http.Response = http.get(url)

            if response.status_code == 200:
                if response.text != "" and 'erro' not in response.json().keys():
                    return response.json()
                else:
                    return dict()
            else:
                return dict()
        except http.exceptions.ConnectionError:
            mensagem = {'erro': 'Falta de conexão com a internet.'}
            return mensagem

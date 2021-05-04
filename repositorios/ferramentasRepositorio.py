import requests

from modelos.tetosPrevModelo import TetosPrevModelo


class ApiFerramentas:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/explorer-api/'

    def getAllTetosPrevidenciarios(self, id:int =None):
        url = self.baseUrl + 'tetosPrev/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            listaTetos = [TetosPrevModelo().fromDict(teto) for teto in response.json()]
        else:
            print('Deu erro')
            print(f"response.url: {response.url}")
            print(f"response.text: {response.text}")
            print(f"response.content: {response.content}")



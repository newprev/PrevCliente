import requests

class ApiFerramentas:

    def __init__(self):
        self.baseUrl = 'http://localhost:8000/explorer-api/'

    def getAllTetosPrevidenciarios(self, id:int =None):
        url = self.baseUrl + 'tetosPrev/'
        response = requests.get(url)

        if 199 < response.status_code < 400:
            print(f"response.url: {response.url}")

            i = 0
            for teto in response.json():
                print(teto)
                i += 1
                if i > 5:
                    break
        else:
            print('Deu erro')
            print(f"response.url: {response.url}")
            print(f"response.text: {response.text}")
            print(f"response.content: {response.content}")



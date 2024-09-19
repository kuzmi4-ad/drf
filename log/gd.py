import requests


class GD:
    def load(id):
        URL = "https://docs.google.com/uc?export=download"
        session = requests.Session()

        response = session.get(URL, params={'id': id}, stream=True)
        return response

        # token = GD.get_confirm_token(response)

        # if token:
        #     params = {'id': id, 'confirm': token}
        #     response = session.get(URL, params=params, stream=True)
        #     return response

    def get_confirm_token(response):
        print(response.headers)
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value

        return None

    def save(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

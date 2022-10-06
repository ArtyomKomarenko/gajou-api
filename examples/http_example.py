import logging

from requests import Session

from src.gajou_api.http import BaseHTTP


# Example based on public API https://pokeapi.co

# backend class collects all API routes and passes one session to all of them
class Backend:
    def __init__(self, host, schema='https'):
        self.base_url = f'{schema}://{host}'
        self.session = Session()

        self.pokemon = PokemonAPI(self.session, self.base_url)


# API class should be inherited from BaseHTTP
class PokemonAPI(BaseHTTP):
    def list(self):
        url = '/api/v2/pokemon'
        rs = self.get(url, skip_body=True)  # there is way to skip response body if it consists from a lot of info
        return rs

    def by_name(self, name):
        url = f'/api/v2/pokemon/{name}'
        rs = self.get(url)
        return rs


if __name__ == '__main__':
    # logger configuration to demonstrate "out-of-the-box" logs
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='[%(levelname)s] %(asctime)s  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # simple example of using
    backend = Backend('pokeapi.co')
    pokemons = backend.pokemon.list()
    ditto = backend.pokemon.by_name('ditto')

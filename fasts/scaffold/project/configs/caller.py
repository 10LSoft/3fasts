import httpx

from configs.envs import get_server_config

configs = get_server_config()


class Caller:
    '''
    This class is responsible for making HTTP requests to the server. The main
    goal is to provide a simple interface for making GET, POST, PUT, and
    DELETE requests to the server. In the future, it can be extended to support
    some other HTTP methods.
    '''

    def __init__(self, url: str, method: str = 'GET'):
        self.url = self.__formating_url(url)
        self.client = httpx.AsyncClient()
        self.method = method.upper()
        self.methods_manager = {
            'GET': self.client.get,
            'POST': self.client.post,
            'PUT': self.client.put,
            'DELETE': self.client.delete
        }

    def __formating_url(self, url: str) -> str:
        '''
        This method intends to format the URL to be used in the request. If
        host and port are not present in URL, then the caller will accept that
        the passed URL value is the complete URL, else, the Caller will format
        the URL to an internal URL.
        '''
        port = configs.get('port', 8000)
        host = configs.get('host', 'localhost')
        print(host, port, url)

        if host not in url:
            new_url = f'http://{host}:{port}{url}'
            print(new_url)
            return new_url

        return self.url

    async def call(self):
        '''
        This method is responsible for making the HTTP request to the server.
        '''
        if self.method not in self.methods_manager:
            raise ValueError(f'Method {self.method} is not supported.')

        try:
            response = await self.methods_manager[self.method](self.url)
            response.raise_for_status()

            return response.json()
        except httpx.RequestError as e:
            print(f'An error occurred while requesting {e.request.url}: {e}')
        except httpx.HTTPStatusError as e:
            print(
                f'Error response {e.response.status_code} while '
                'requesting {e.request.url}: {e}'
            )
        finally:
            await self.client.aclose()

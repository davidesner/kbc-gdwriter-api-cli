""""
Entry point for the Storage API client.
"""


from gdwriterapi.tables import Tables
from gdwriterapi.dimensions import DateDimensions

class Client:
    """
    Storage API Client.
    """

    def __init__(self, api_domain, config_id, token):
        """
        Initialise a client.

        Args:
            api_domain (str): The domain on which the API sits. eg.
                "https://connection.keboola.com".
            token (str): A storage API key.
        """
        self.root_url = api_domain
        self._token = token


        self.tables = Tables(self.root_url, config_id, self.token)
        self.date_dimension = DateDimensions(self.root_url, config_id, self.token)

    @property
    def token(self):
        return self._token
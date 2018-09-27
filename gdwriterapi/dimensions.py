from gdwriterapi.base import Endpoint


class DateDimensions(Endpoint):
    """
    Buckets Endpoint
    """
    def __init__(self, root_url, config_id, token):
        """
        Create a DateDimensions endpoint.

        Args:
            root_url (:obj:`str`): The base url for the API.
            token (:obj:`str`): A storage API key.
        """
        super().__init__(root_url, 'date-dimensions', config_id, token)

    def list(self):
        """
        List all dimensions accessible by token.

        Args:
            include (list): Properties to list (attributes, columns, buckets)
        Returns:
            response_body: The parsed json from the HTTP response.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        return self._get(self.base_url)

    def detail(self, dimension_id):
        """
        Retrieves information about a given dimension.

        Args:
            dimension_id (str): The id of the dimension.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        if not isinstance(dimension_id, str) or dimension_id == '':
            raise ValueError("Invalid dimension_id '{}'.".format(dimension_id))
        url = '{}/{}'.format(self.base_url, dimension_id)
        return self._get(url)

    def delete(self, dimension_id):
        """
        Delete a dimension referenced by ``dimension_id``.

        Args:
            dimension_id (str): The id of the dimension to be deleted.
        """
        if not isinstance(dimension_id, str) or dimension_id == '':
            raise ValueError("Invalid dimension_id '{}'.".format(dimension_id))
        url = '{}/{}'.format(self.base_url, dimension_id)
        self._delete(url)

    def create(self, dimension):
        
        return self._post(self.base_url, data=dimension)
    

    def update(self, name, dimensionJson):
        url = '{}/{}'.format(self.base_url, name)
        return self._patch(url, data=dimensionJson)

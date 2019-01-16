"""
Manages calls to the Storage API relating to tables

Full documentation `here`.

.. _here:
    http://docs.keboola.apiary.io/#reference/tables/
"""
from gdwriterapi.base import Endpoint


class Tables(Endpoint):
    """
    Buckets Endpoint
    """
    def __init__(self, root_url, config_id, token):
        """
        Create a Tables endpoint.

        Args:
            root_url (:obj:`str`): The base url for the API.
            token (:obj:`str`): A storage API key.
            config_id (:obj:`str`): GD Writer config id.
            
        """
        super().__init__(root_url, 'tables', config_id, token)

    def list(self, include=None):
        """
        List all tables accessible by token.

        Args:
            include (list): Properties to list (attributes, columns, buckets)
        Returns:
            response_body: The parsed json from the HTTP response.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        params = {'include': ','.join(include)} if include else {}
        return self._get(self.base_url, params=params)

    def detail(self, table_id, include=None):
        """
        Retrieves information about a given table.

        Args:
            table_id (str): The id of the table.

        Raises:
            requests.HTTPError: If the API request fails.
        """
        params = {'include': ','.join(include)} if include else {}
        if not isinstance(table_id, str) or table_id == '':
            raise ValueError("Invalid table_id '{}'.".format(table_id))
        url = '{}/{}'.format(self.base_url, table_id)
        return self._get(url, params=params)

    def delete(self, table_id):
        """
        Delete a table referenced by ``table_id``.

        Args:
            table_id (str): The id of the table to be deleted.
        """
        if not isinstance(table_id, str) or table_id == '':
            raise ValueError("Invalid table_id '{}'.".format(table_id))
        url = '{}/{}'.format(self.base_url, table_id)
        self._delete(url)

    def deleteFromProject(self, table_id, pid):
        """
        Delete a table referenced by ``table_id` from GD project `pid`. Safe way to delete single table from GD project. 
        Table definition in configuration is kept.

        Args:
            table_id (str): The id of the table to be deleted.
        """
        projectsUrl = self.base_url.replace('tables', 'projects')
        if not isinstance(table_id, str) or table_id == '':
            raise ValueError("Invalid table_id '{}'.".format(table_id))
        if not isinstance(pid, str) or pid == '':
            raise ValueError("Invalid project_id '{}'.".format(pid))
        
        url = '{}/{}/datasets/{}'.format(projectsUrl, pid, table_id)
        self._delete(url)

    def create(self, table):
        
        return self._post(self.base_url, data=table)
    

    def update(self, tableId, tableJson):
        url = '{}/{}'.format(self.base_url, tableId)
        return self._patch(url, data=tableJson)

import json


class ConfigDuplicator:
    def __init__(self, client_from, client_to):
        """
        Initialise a client.

        Args:
            client_from (gdwriterapi.client): Client object for source Writer configuration.
            client_to (gdwriterapi.client): Client object for destination Writer configuration.
            
        """

        self.client_from = client_from
        self.client_to = client_to        
        
        
    def migrateTables(self):
        """
        Super simple method, getting all table config objects and updating/creating them in the destination configuration.
        Includes all attributes, even the ones that are not updateble => API service will ignore them.
            
        """
        tables = self.client_from.tables.list(['columns'])
        if len(tables) > 0:
            for table in tables:
                self.client_to.tables.update(table['tableId'], json.dumps(table))
        else:
            print("No tables to migrate!")
            return
        print(len(tables) + " Tables migrated!")
    def migrateDateDimension(self):
        """
        Super simple method, getting all date dimensions from source config and updating/creating them in the destination configuration.
        Includes all attributes, even the ones that are not updateble => API service will ignore them.
            
        """
        dims = self.client_from.date_dimension.list()
        if len(dims) > 0:
            for dimension in dims:
                self.client_to.date_dimension.update(dimension['name'], json.dumps(dimension))
        else:
            print("No dimensions to migrate!")
            return
        print(len(dims) + " Date Dimensions migrated!")
            
        
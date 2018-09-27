from gdwriterapi.client import Client
from gdwriterapi.config_duplicator import ConfigDuplicator
import plac





def main(from_config, from_token, to_config, to_token, syrup_url_from = 'https://syrup.keboola.com', syrup_url_to= 'https://syrup.keboola.com'):
    """
    Simple CMD to migrate GD writer config (tables, dimensions) from one config to another.
    
    """
    from_client  =  Client(syrup_url_from, from_config, from_token)
    to_client  =  Client(syrup_url_to, to_config, to_token)
    
    duplicator = ConfigDuplicator(from_client, to_client)
    
    print('Migrating tables from config: ' + from_config + ' to: ' + to_config)
    try:
        duplicator.migrateTables()
    except Exception as err:
        print("Failed to migrate the tables: {0}".format(err))
        exit()
    
    print('Migrating date dimensions from config: ' + from_config + ' to: ' + to_config)    
    try:    
        duplicator.migrateDateDimension()
    except Exception as err:
        print("Failed to migrate the dimensions: {0}".format(err))
        exit()
        




if __name__ == '__main__':
    plac.call(main)
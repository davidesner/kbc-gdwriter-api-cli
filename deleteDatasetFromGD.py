from gdwriterapi.client import Client
from gdwriterapi.config_duplicator import ConfigDuplicator
import plac





def main(config, token, table_id, project_id, syrup_url = 'https://syrup.keboola.com'):
    """
    Simple CMD to delete dataset from GD. Keeps the KBC table config. Useful to prevent fullload when deleting one object.
    
    """
    client  =  Client(syrup_url, config, token)    

    print('Deleting dataset : ' + table_id + ' from GD project: ' + project_id)
    try:
        client.tables.deleteFromProject(table_id, project_id)
    except Exception as err:
        print("Failed to delete dataset: {0}".format(err))
        exit()





if __name__ == '__main__':
    plac.call(main)
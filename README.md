
# kbc-gdwriter-api-cli
Simple client Keboola GoodData writer API https://keboolagooddatawriterv2.docs.apiary.io/

## Usage:
```
usage: duplicateConfig.py [-h]
                          from_config from_token to_config to_token
                          [syrup_url_from] [syrup_url_to]

positional arguments:
  from_config
  from_token
  to_config
  to_token
  syrup_url_from  [https://syrup.keboola.com]
  syrup_url_to    [https://syrup.keboola.com]
```
**Migrate one GD Writer config (tables, dimensions) to another:** 

	- using default syrup URL (US Region https://syrup.keboola.com)
```python
python duplicateConfig.py source_config_id source_token dest_config_id dest_token
```
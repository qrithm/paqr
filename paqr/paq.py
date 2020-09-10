from paqr import qpr
import os
import yaml


class InvalidPaq(Exception):
    "Raise this error if paq is invalid"
    pass


def paq_memory_is_valid(memory: str) -> bool:
    """ TODO: validate the memory specified in paq.yaml is valid """
    return True


def validate_paq(paq_dir: str) -> dict:
    """ Checks that the paq at paq_dir is valid. Raises InvalidPaq Exception if not. """
    config_path = os.path.join(paq_dir, 'paq.yaml')
    if not os.path.isfile(config_path):
        raise InvalidPaq(
            "Paq directories must contain a paq.yaml file to be valid")
    f = open(config_path, 'r')
    config = yaml.load(f, Loader=yaml.FullLoader)
    if 'name' not in config.keys():
        raise InvalidPaq("The paq file must contain a name field")
    if 'memory' not in config.keys():
        logging.warn(
            "The key 'memory' should be specified in your paq.yaml file. Using default value of 2048M for now. You should change this!")
        config['memory'] = '2048M'
    if qpr.name_is_available(config['name']) is not True:
        raise InvalidPaq(
            "The name {} is already in use. Please select a new name".format(paq_name))
    if paq_memory_is_valid(config['memory']) is not True:
        raise InvalidPaq(
            "The memory specified: {} is not valid. Please use a valid memory")
    return config

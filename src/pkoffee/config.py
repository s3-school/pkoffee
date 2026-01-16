import yaml
from pathlib import Path


def load_config(config_file):
    """
    Load configuration from a YAML file.
    Parameters
    ----------
    config_file : str
        Path to the YAML configuration file.
    Returns
    -------
    dict
        Dictionary containing the configuration parameters.
    """

    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config

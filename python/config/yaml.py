from pathlib import Path

import yaml


class Config(object):
    def __init__(self, location: str):
        self.config_location = location
        loader = yaml.safe_load(open(location, 'rb').read())
        self.root_directory = loader["root_directory"]

    def get_root_location(self) -> Path:
        return Path(self.root_directory)

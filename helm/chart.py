from pathlib import Path
from yaml import YAMLObject
from typing import Tuple

class HelmChart:
    '''Used for operations on a Helm chart'''
    def __init__(self, path: Path):
        self.path = path

class Values(YAMLObject):
    
    def __init__(self, path: Path):
        self.path = path
    
    @property
    def argument(self) -> Tuple[str, str]:
        return ('--values', self.path)

    def __str__(self):
        return self.path

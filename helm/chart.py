from pathlib import Path
from yaml import YAMLObject
from typing import Tuple

class HelmChart:
    '''Used for operations on a Helm chart'''
    def __init__(self, path: Path):
        self.path = path

class Values(YAMLObject):
    '''Expanded upon casting to string to be provided to Helm
    
    either to a --values {PATH} ...'''
    
    def __init__(self, path: Path):
        self.path = path
    
    def __str__(self) -> Tuple[str, str]:
        return ('--values', self.path)

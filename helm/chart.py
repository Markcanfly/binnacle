from pathlib import Path
from yaml import YAMLObject

class HelmChart:
    '''Used for operations on a Helm chart'''
    def __init__(self, path: Path):
        self.path = path

class Values(YAMLObject):
    '''Expanded upon casting to string to be provided to Helm
    
    either to a --values {PATH} or a --set {VALUE1} ...'''

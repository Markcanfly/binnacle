from yaml import YAMLObject
from typing import Any
from deepdiff import DeepDiff
from enum import Enum

class DiffFormat(str, Enum):
    JSON = 'json'
    YAML = 'yaml'
    GIT  = 'git'

class K8SObject(YAMLObject):
    # TODO store the filename
    def differences(self, other: 'K8SObject'):
        return DeepDiff(self, other)

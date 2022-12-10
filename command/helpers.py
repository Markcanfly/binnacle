from enum import Enum
from deepdiff import Delta
import yaml
from pprint import pprint
from helm.k8s import DiffFormat

def print_differences(delta: Delta, diff_format: DiffFormat='json') -> None:
    if diff_format == DiffFormat.JSON:
        print_json(delta)
    elif diff_format == DiffFormat.YAML:
        print_yaml(delta)
    elif diff_format == DiffFormat.GIT:
        print_git(delta)
    else:
        raise KeyError(f'Unknown diff print format "{diff_format}". Use one of {", ".join(e.value for e in DiffFormat)}')

def print_json(delta: Delta) -> None:
    pprint(delta)

def print_yaml(delta: Delta) -> None:
    yaml.safe_dump([dict(c) for c in delta])

def print_git(delta: Delta)  -> None:
    raise NotImplementedError()

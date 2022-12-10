from helm.chart import HelmChart, Values
from helm.helmbin import Helm
from helm.k8s import K8SObject
from typing import List
from deepdiff import DeepDiff, Delta
from command.helpers import DiffFormat, print_differences

def regression(helm: Helm, old: HelmChart, new: HelmChart, values: List[Values], format: DiffFormat=DiffFormat.YAML) -> List[Delta]:
    differences = []
    for value in values:
        old_objects: List[K8SObject] = helm.template(old, [value])
        new_objects: List[K8SObject] = helm.template(old, [value])
        differences.append(DeepDiff(old_objects, new_objects))
    
    print_differences(differences, diff_format=format)

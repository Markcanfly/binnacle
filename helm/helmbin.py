from pathlib import Path
import shutil
import subprocess
from typing import List, Dict, TextIO
from helm.chart import HelmChart, Values
from helm.k8s import K8SObject
import yaml

ExitCode = int

class HelmError(BaseException): pass

class Helm:
    '''Wrapper to run helm commands'''
    def __init__(self, helm_binary: Path = 'helm'):
        self.path = shutil.which(helm_binary)
        if self.path is None:
            raise ValueError('Cannot find helm executable')
    
    def operation(self, opname: str, *params) -> TextIO:
        'Perform a generic operation'
        run: subprocess.CompletedProcess = subprocess.run([self.path, opname, *params], capture_output=True)
        if run.returncode != 0:
            raise HelmError(f'Helm returned exit code {run.returncode}. Error output:\n{run.stdout}\n{run.stderr}')
        return run.stdout
    
    def lint(self, chart: HelmChart) -> bool:
        '''Check if the linter catches an error
        
        Returns True if an error is found, otherwise False'''
        try:
            self.operation('lint', chart.path)
        except HelmError as e:
            print(f'Invalid chart found in {chart.path}, cannot run regression')
            raise e
    
    def template(self, chart: HelmChart, values: List[Values] = None) -> List[K8SObject]:
        if values is None: values = []
        stdout = self.operation('template', chart.path, *[v.argument for v in values]) 
        # Remove --values from here and create it in the Values class
        return [o for o in yaml.safe_load_all(stdout)]

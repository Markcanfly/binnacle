import unittest
import command.regression
from pathlib import Path
from typing import List
from deepdiff import Delta
from helm.helmbin import Helm
import helm.chart

def regression(old: str, new: str, values: List[str]) -> List[Delta]:
    path = Path('test/resources/charts')
    old_chart = helm.chart.HelmChart(path/old)
    new_chart = helm.chart.HelmChart(path/new)
    res_path = Path('test/resources/values')
    values = [helm.chart.Values(res_path/p) for p in values]
    return command.regression.regression(Helm(), old_chart, new_chart, values)

class TestRegression(unittest.TestCase):
    
    def test_no_change(self):
        self.assertEqual([{}], regression('old', 'old', []))

    def test_chart_change(self):
        d = regression('old', 'new', [])
        name_change = d[0]['values_changed']["root[0]['metadata']['name']"]
        self.assertEqual('cat', name_change['old_value'])
        self.assertEqual('dog', name_change['new_value'])

    def test_value_change(self):
        d = regression('old', 'new', [])
        image_version = d[0]['values_changed']["root[0]['spec']['containers'][0]['image']"]
        # New chart uses a value for the version instead of hardcoding it
        self.assertEqual('nginx:1.14.2', image_version['new_value'])

if __name__ == '__main__':
    unittest.main()

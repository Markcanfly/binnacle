import unittest
import command.regression
from pathlib import Path
from typing import List
from deepdiff import Delta
from helm.helmbin import Helm
import helm.chart

def regression(old: Path, new: Path, values: List[helm.chart.Values]) -> List[Delta]:
    path = Path('test/resources/charts')
    old_chart = helm.chart.HelmChart(path/old)
    new_chart = helm.chart.HelmChart(path/new)
    helm_bin = Helm()
    return command.regression.regression(helm_bin, old_chart, new_chart, values)

class TestRegression(unittest.TestCase):
    
    def test_no_change(self):
        self.assertEqual([{}], regression('old', 'old', []))

if __name__ == '__main__':
    unittest.main()

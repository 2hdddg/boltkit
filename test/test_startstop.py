import unittest
import shutil
import tempfile
import os

from boltkit.controller import install, start, stop

class StartStopTestCase(unittest.TestCase):
    def setUp(self):
        self._root = tempfile.mkdtemp(prefix='neo4j')
        self._home = install(['-v', '-e', '4.0', self._root])
        os.chdir(self._home)

    def tearDown(self):
        if self._home:
            shutil.rmtree(self._home)

    def test_startALot(self):
        args = ['-v', '-t 10', self._home]
        for x in range(0, 10):
            start(args)
            stop()


if __name__ == '__main__':
    unittest.main()


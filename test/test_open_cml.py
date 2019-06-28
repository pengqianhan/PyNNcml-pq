import unittest
import torchrain as tr


class TestOpenCML(unittest.TestCase):
    def test_load(self):
        link_list = tr.read_open_cml_dataset('/data/projects/torch_rain/data/open_cml.p')
        [self.assertTrue(isinstance(d, tr.Link)) for d in link_list]
        self.assertTrue(len(link_list) == 20)

    def test_file_exception(self):
        pickle_path = '/bla/bla'
        with self.assertRaises(Exception) as context:
            link_list = tr.read_open_cml_dataset(pickle_path)
        self.assertTrue('The input path: ' + pickle_path + ' is not a file' == str(context.exception))
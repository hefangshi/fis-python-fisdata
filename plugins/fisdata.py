import os
import re

class FisData():
    root = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../../'))
    reg = re.compile('^[\\\/]template')

    def get_datatype(self):
        raise NotImplementedError("datatype error")

    def get_data(self, template_path):
        raise NotImplementedError("datatype error")

    def get_datafile_path(self, template_path, extension):
        if template_path.find(self.root) != 0:
            raise AssertionError("template_path should in root path")
        data_path = self.reg.sub('test', template_path[len(self.root):])
        fname,fext = os.path.splitext(data_path)
        return os.path.normpath(os.path.join(self.root, fname + extension))


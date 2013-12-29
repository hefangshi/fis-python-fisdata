from fisdata import FisData
import os

class FisPy(FisData):
    def get_datatype(self):
        return 'python'

    def get_data(self, template_path):
        data_path = self.get_datafile_path(template_path, '.py')
        if os.path.exists(data_path) == False:
            return False
        script_locals = dict()
        execfile(data_path, {}, script_locals)
        return script_locals['fis_data']


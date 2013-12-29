from fisdata import FisData
import json
import os

class FisJson(FisData):
    def get_datatype(self):
        return 'json'

    def get_data(self, template_path):
        data_path = self.get_datafile_path(template_path, '.json')
        if os.path.exists(data_path) == False:
            return False
        with open(data_path, "r") as file:
            data = file.read()
            try:
                data = json.loads(data)
            except:
                data = False
        return data

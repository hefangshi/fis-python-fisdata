class FisDataManager():
    data_handlers = {}

    @classmethod
    def register(self, data_handler):
        self.data_handlers[data_handler.get_datatype()] = data_handler

    @classmethod
    def get_data(self, data_type, template_path):
        if data_type not in self.data_handlers.keys():
            data_type = 'python'
        data_handler = self.data_handlers[data_type]
        data = data_handler.get_data(template_path)
        return data

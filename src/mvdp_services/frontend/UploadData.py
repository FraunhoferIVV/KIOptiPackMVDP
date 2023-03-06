class UploadData:

    def __init__(self, data_file, file_type, data_delimiter, decimal_delimiter, material_ID):
        self.data_file = data_file
        self.file_type = file_type
        self.data_delimiter = data_delimiter
        self.decimal_delimiter = decimal_delimiter
        if material_ID != 'no':
            self.material_ID = material_ID
        else:
            self.material_ID = None

    def get_delimiter(self):
        if self.decimal_delimiter == 'point':
            return '.'
        if self.decimal_delimiter == 'comma':
            return ','
        return None

    def get_sep(self):
        if self.dataDelimiter == 'comma':
            return ','
        if self.dataDelimiter == 'semicolon':
            return ';'
        return None
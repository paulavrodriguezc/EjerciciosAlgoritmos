class Section:
    def __init__(self, name, writers):
        self.name=name
        self.writers=writers
class Writer(Section):
    def __init__(self, name, writers, writer_name, writer_id):
        super().__init__(name, writers)
        self.writer_name=writer_name
        self.writer_id=writer_id
class Chief(Writer):
    def __init__(self, name, writers, writer_name, writer_id, chief_status):
        super().__init__(name, writers, writer_name, writer_id)
        self.chief_status=chief_status
class Article:
    def __init__(self, title, summary, body, num_images, creation_date, writer):
        self.title=title
        self.summary=summary
        self.body=body
        self.num_images=num_images
        self.creation_date=creation_date
        self.writer=writer
        self.publish_date=None
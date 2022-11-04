from Periodico.Artículos import Article
import random
class Writer:
    def __init__(self, writer_name, writer_id):
        self.writer_name=writer_name
        self.writer_id=writer_id
    def write_article(self):
        print("The process of writing an article has begun.")
        article=Article(input("Title: "), input("Summary: "), input("Body: "), input("Number of images: "), input("Date of creation: "))
        print("The article has been written.")
        return article
class Chief(Writer):
    def __init__(self, writer_name, writer_id, writers):
        super().__init__(writer_name, writer_id)
        self.writers=writers
    def supervise(self):
        print("Chief supervising. All good.")
    def choose_article(self, article):
        if random.random()>0.5:
            print(f"The article {article.title} has been aproved.")
        else:
            print(f"The article {article.title} has not been aproved.")
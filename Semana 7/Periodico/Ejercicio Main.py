from Periodico.Secciones import Section
from Periodico.Redactores import Writer,Chief
def get_writers_sports():
    return [Writer("Paula",28327724), Writer("Mauricio",29548761), Writer("Andreina",29555421), Writer("Mariana",30456821), Writer("Anabella",30487691)]
def process_articles(section):
    print("The sports section has begun its work.")
    for writer in section.chief.writers:
        print(f"The writer in question is {writer.writer_name}.")
        article=writer.write_article()
        print(f"The chief of the section is {section.chief.writer_name}.")
        section.chief.choose_article(article)
def main():
    chief_writer_sports=Chief("Antonio",22975412,get_writers_sports)
    section_sports=Section(chief_writer_sports, "Sports")
    process_articles(section_sports)
main()
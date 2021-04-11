class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = new_content

    def change_author(self, new_authpr):
        self.author = new_authpr

    def rename(self, new_title):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)

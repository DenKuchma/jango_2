from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=120)
#     year_of_public = models.DateField()
#     coast = models.IntegerField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
#
#     def __str__(self):
#         return self.title
#


# class Authors(models.Model):
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name
#
#
# class Books(models.Model):
#     title = models.CharField(max_length=120)
#     year_of_public = models.DateField()
#     coast = models.IntegerField()
#     author = models.ManyToManyField(Authors)
#
#     def __str__(self):
#         return self.title
#
#
# class Library(models.Model):
#     library_man = models.CharField(max_length=120)
#     books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookss', unique=True)
#
#     def __str__(self):
#         return self.library_man



class Bloger(models.Model):
    name = models.CharField(max_length=36)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Publicate(models.Model):
    title_of_blog = models.CharField(max_length=64)
    text_of_blog = models.CharField(max_length=128)
    bloger = models.ForeignKey(Bloger, on_delete=models.CASCADE, related_name='blogers')

    def __str__(self):
        return self.title_of_blog


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Publicate, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('dz.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.CharField(max_length=64)

    def __str__(self):
        return "{} by {}".format(self.text, self.user)



class Like(models.Model):
    username = models.CharField(max_length=64)
    article = models.ForeignKey(Publicate, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "By user {} to article {}".format(self.username, self.article.id)



class Disike(models.Model):
    username = models.CharField(max_length=64)
    article = models.ForeignKey(Publicate, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "By user {} to article {}".format(self.username, self.article.id)
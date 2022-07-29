from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='Publish name')
    website = models.URLField(help_text='web site address')
    email = models.EmailField(help_text='email')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text='book title')
    publication_date = models.DateField(verbose_name='Date of publication of the book')
    isbn = models.CharField(max_length=20, help_text='ISBN book number')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # relationship many to one
    contributor = models.ManyToManyField('Contributor', through='BookContributor')
    cover = models.ImageField(null=True, blank=True, upload_to="book_covers/")
    sample = models.FileField(null=True, blank=True, upload_to="book_samples/")

    def __str__(self):
        return "{} - ({})". format(self.title, self.isbn)


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text='contributor first name')
    last_name = models.CharField(max_length=50, help_text='contributor last name')
    email = models.EmailField(help_text='contributor email')

    def __str__(self):
        return self.first_name


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Contributor role", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="review text")
    rating = models.IntegerField(help_text="Stars")
    date_created = models.DateTimeField(auto_now_add=True, help_text="created date review")
    date_edited = models.DateTimeField(null=True, help_text="edited date review")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="book review")

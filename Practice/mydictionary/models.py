from django.db import models

# Create your models here.
class ZhDict(models.Model):
    zh_meaning = models.TextField()

class DeDict(models.Model):
    de_meaning = models.TextField()

class EnDict(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField()
    synonyms = models.TextField()
    antonym = models.TextField()
    repeat = models.BooleanField()
    hard = models.IntegerField()
    ch_meaning = models.ForeignKey(ZhDict, on_delete=models.PROTECT)
    ge_meaning = models.ForeignKey(DeDict, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.word}: {self.meaning}, synonyms: {self.synonyms}; antonym: {self.antonym}; ch: {self.ch_meaning}; ge: {self.ge_meaning}"

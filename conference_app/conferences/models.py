from django.db import models

# a.Konferencija – turi datą nuo-iki, pavadinimą, [sukūrimo
# ir modifikavimo datos (auto_now, auto_now_add)]

class Conference(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length = 100)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title


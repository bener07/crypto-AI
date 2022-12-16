from django.db import models

# Create your models here.


class coins(models.Model):
    coin_name = models.CharField(("Coin name"), max_length=255)
    price = models.FloatField(("Price"))
    date = models.DateField(("Date "), null=True, blank=True)
    time = models.TimeField(("Time"), auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.coin_name


    def add_coin(coin_name, price):
        if coins.objects.filter(coin_name=coin_name.upper()):
            raise KeyError('Impossible to add coin, already in database')
        return coins.objects.create(coin_name=coin_name.upper(), price=price)
    

    def remove_coin(coin_name):
        return coins.objects.delete(coin_name=coin_name.upper())


    def current_coins():
        return coins.objects.all()
    

    def update_price(c_name, price):
        return coins.objects.filter(coin_name=c_name).update(price=price)



class test_model(models.Model):
    text = models.TextField(("Text: "))
    name = models.CharField(("What's your name? "), max_length=50)

    class Meta:
        verbose_name = ("test_model")
        verbose_name_plural = ("test_models")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("test_model_detail", kwargs={"pk": self.pk})
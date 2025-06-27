from django.db import models

# 夜市模型
class NightMarket(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.city})"

    class Meta:
        db_table = 'night_markets'

# 攤販模型
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    night_market = models.ForeignKey(NightMarket, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=15, null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} at {self.night_market.name}"

    class Meta:
        db_table = 'vendors'

# 美食模型
class Food(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.vendor.name})"

    class Meta:
        db_table = 'foods'
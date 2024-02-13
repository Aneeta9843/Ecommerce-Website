from django.db import models
from apps.user.models import User
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    class Meta(object):
        db_table= 'order'

    user = models.ForeignKey(
        User, related_name= 'related_order_user', on_delete=models.CASCADE
    )
    customer_name = models.CharField(
        'Customer Name', max_length=255, null=False, blank=False
    )
    address = models.CharField(
        'Address', max_length=255, null=False, blank=False
    )
    pin_code = models.CharField(
        'Pin Code', max_length=255, null=False, blank=False
    )
    building_type = models.CharField(
        'Building Type', max_length=255, null=True, blank=True
    )
    city = models.CharField(
        'City', max_length=255, null=False, blank=False
    )
    state = models.CharField(
        'State', max_length=255, null=False, blank=False
    )
    total_price = models.FloatField(
        'Total Price', null=False, blank=False
    )
    total_qty = models.IntegerField(
        'Total Quantity', null=False, blank=False
    )
    created_at = models.DateTimeField(
        'Creation Date', blank=True, default= timezone.now
    )

    @property
    def order_items(self):
        return self.related_order.all()


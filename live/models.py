from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# # class Profile(models.Model):
# #     name = models.CharField(max_length=35)
# #     item_code = models.CharField(max_length=30, unique=True)
# #     item_cod_desc = models.CharField(max_length=64)
# #     link = models.CharField(max_length=512)
# #     level = models.SmallIntegerField(default=0)
# #     status = models.BooleanField(default=1)
# #     # The following field is temporal
# #     P0 = 'P0'
# #     P1 = 'P1'
# #     P2 = 'P2'
# #     P3 = 'P3'
# #     P4 = 'P4'
# #     P99 = 'P99'
# #     LOCATION_TO_CHOICE = [
# #         (P0, 'QA'),
# #         (P1, 'FCT -> QA'),
# #         (P2, 'FCT -> Burn In -> QA'),
# #         (P3, 'FCT -> Production -> Burn In -> QA'),
# #         (P4, 'Production -> Burn In -> QA'),
# #         (P99, 'NA'),
# #     ]
# #     location = models.CharField(max_length=2, choices=LOCATION_TO_CHOICE, default=P0)
    
    
# #     def __str__(self):
# #         return f"{self.item_code} | {self.item_cod_desc} | {self.level}"

class Product(models.Model):
    so_line = models.CharField(max_length=14)
    customer_no = models.CharField(max_length=15)
    sales_order_no = models.CharField(max_length=7)
    customer_name = models.CharField(max_length=50)
    linekey = models.CharField(max_length=6)
    item_code = models.CharField(max_length=30)
    item_cod_desc = models.CharField(max_length=64)
    so_header = models.DateField()
    prom_date = models.DateField()
    clear_date = models.DateField()
    exp_date_i = models.DateField()
    exp_date_f = models.DateField()
    qty = models.IntegerField()
    qty_shipped = models.IntegerField()
    unit_price = models.CharField(max_length=20, default="0")
    production_notes = models.CharField(max_length=512)
    qty_on_hand = models.IntegerField()
    rma_number = models.IntegerField()
    drop_ship = models.CharField(max_length=2)
    comments = models.CharField(max_length=512, blank=True)
    active = models.BooleanField(default=1)
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_id", default=0)
    #The following fields are only temporal
    notes = models.CharField(max_length=512, blank=True)
    notes_deprecated = models.CharField(max_length=512, blank=True)
    steps = models.IntegerField(default=100)
    prgr = models.IntegerField(default=0)
    NEW = 'NEW'
    KITTING = 'KITTING'
    WAITING = 'WAITING'
    KITTED = 'KITTED'
    TESTING = 'FCT in PROGRESS'
    ONHOLD = 'ON HOLD'
    BUILDING = 'BUILDING'
    PASS = 'FCT PASSED'
    BURNIN = 'BURN-IN'
    QA = 'QA'
    SHIPPING = 'SHIPPING'
    NA = 'NAN'
    STATUS_TO_CHOICE = [
        (NEW, 'NEW'),
        (KITTING, 'KITTING'),
        (WAITING, 'WAITING'),
        (KITTED, 'KITTED'),
        (TESTING, 'FCT in PROGRESS'),
        (ONHOLD, 'ON HOLD'),
        (BUILDING, 'BUILDING'),
        (PASS, 'FCT PASSED'),
        (BURNIN, 'BURN-IN'),
        (QA, 'QA'),
        (SHIPPING, 'SHIPPING'),
        (NA, 'NA'),
    ]
    status = models.CharField(max_length=32, choices=STATUS_TO_CHOICE, default=NEW)

    #Profile
    P0 = 'P0'
    P1 = 'P1'
    P2 = 'P2'
    P3 = 'P3'
    P4 = 'P4'
    P5 = 'P5'
    P97 = 'P97'
    P98 = 'P98'
    P99 = 'P99'
    PROFILE_TO_CHOICE = [
        (P0, 'QA'),
        (P1, 'FCT -> QA'),
        (P2, 'FCT -> Burn In -> QA'),
        (P3, 'FCT -> Production -> Burn In -> QA'),
        (P4, 'Production -> Burn In -> QA'),
        (P5, 'Burn In -> QA'),
        (P97, 'SHIPPING'),
        (P98, 'ON-HOLD'),
        (P99, 'NA'),
    ]
    profile = models.CharField(max_length=3, choices=PROFILE_TO_CHOICE, default=P0)

    class Meta:
        ordering = ("exp_date_f", )

    def __str__(self):
        return f"{self.so_line} {self.customer_name} {self.item_code} {self.item_cod_desc} {self.exp_date_f} {self.qty} {self.comments}"

# # class Comment(models.Model):
# #     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
# #     detail = models.CharField(max_length=64)
# #     date = models.DateField()
# #     status = models.BooleanField(default=1)
# #     def __str__(self):
# #         return f"{self.id} {self.profile_id} {self.detail} {self.date} {self.status}"

# # class Status(models.Model):
# #     name = models.CharField(max_length=25)
# #     description = models.CharField(max_length=50)
# #     def __str__(self):
# #         return f"{self.id} {self.name} {self.description}"

# # class Log(models.Model):
# #     product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_log")
# #     status_id = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status")
# #     date = models.DateField()
# #     def __str__(self):
# #         return f"{self.id} {self.product_id} {self.status_id} {self.date}"


# # class Location(models.Model):
# #     name = models.CharField(max_length=25)
# #     x = models.SmallIntegerField(default=0)
# #     y = models.SmallIntegerField(default=0)
# #     z = models.SmallIntegerField(default=0)
# #     status = models.BooleanField(default=1)
# #     def __str__(self):
# #         return f"{self.name}"



# # class Profile_Location(models.Model):
# #     profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile")
# #     location_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_profile")
# #     step = models.SmallIntegerField()
# #     def __str__(self):
# #         return f"{self.profile_id} {self.location_id} {self.step}"

# # class Location_User(models.Model):
# #     location_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_user")
# #     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
# #     def __str__(self):
# #         return f"{self.location_id} {self.user_id}"


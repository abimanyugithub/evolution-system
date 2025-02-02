import uuid
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.forms import ValidationError
from applications.mapping.models import Provinsi, KabupatenKota, Kecamatan, KelurahanDesa
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique identifier
    code = models.CharField(max_length=20)  # unique=True memastikan bahwa tidak ada dua entri
    name = models.CharField(max_length=255) 
    zone = models.CharField(max_length=255)
    # capacity = models.PositiveIntegerField(blank=True, null=True) # Kapasitas maksimum warehouse
    capacity = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)  # Nama manajer gudang
    current_inventory = models.PositiveIntegerField(default=0)  # Jumlah inventaris saat ini
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Alamat Baris 1')
    address_line2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Alamat Baris 2')
    province = models.ForeignKey(Provinsi, on_delete=models.CASCADE, blank=True, null=True)
    regency = models.ForeignKey(KabupatenKota, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, blank=True, null=True)
    village = models.ForeignKey(KelurahanDesa, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name='Alamat Email')
    phone_number = models.CharField(
        max_length=15,  # Adjust the length as needed
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        blank=True,  # Set to False if the phone number is required
        null=True    # Set to False if the phone number cannot be null
    )
    # phone_number = PhoneNumberField(blank=True)
    def clean(self):
        # Jika active True, periksa apakah code sudah ada
        if self.active:
            if Warehouse.objects.exclude(pk=self.pk).filter(code=self.code, active=True).exists():
                raise ValidationError(f'The code "{self.code}" must be unique when active.')

    def __str__(self):
        return f"{self.code} ({self.name})"
    

    class Meta:
        ordering = ['code']
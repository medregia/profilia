from django.db import models

class BusinessData(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('Proprietorship', 'Proprietorship'),
        ('Partnership', 'Partnership'),
        ('Private Limited', 'Private Limited'),
        ('LLP', 'LLP'),
        ('Franchise', 'Franchise'),
        ('Cooperative Society', 'Cooperative Society'),
    ]

    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES)

    # Common fields
    business_name = models.CharField(max_length=100)
    pan = models.CharField(max_length=10, blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)

    # Proprietorship
    proprietor_name = models.CharField(max_length=100, blank=True, null=True)

    # Partnership
    partnership_name = models.CharField(max_length=100, blank=True, null=True)
    partners = models.JSONField(blank=True, null=True)  # List of partner details (name, PAN, contact, etc.)

    # Private Limited
    cin = models.CharField(max_length=21, blank=True, null=True)
    directors = models.JSONField(blank=True, null=True)  # List of director details (name, PAN, DIN, etc.)

    # LLP
    llpin = models.CharField(max_length=7, blank=True, null=True)

    # Franchise
    franchise_name = models.CharField(max_length=100, blank=True, null=True)
    parent_company_name = models.CharField(max_length=100, blank=True, null=True)
    franchise_agreement_number = models.CharField(max_length=50, blank=True, null=True)
    franchise_duration = models.IntegerField(blank=True, null=True)  # Duration in months/years
    parent_company_representative_name = models.CharField(max_length=100, blank=True, null=True)
    parent_company_representative_contact = models.CharField(max_length=15, blank=True, null=True)

    # Cooperative Society
    society_name = models.CharField(max_length=100, blank=True, null=True)
    members = models.JSONField(blank=True, null=True)  # List of member details (name, PAN, role, etc.)

    # Common contact and address details
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    registered_address = models.TextField()
    shop_address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.business_name} ({self.business_type})"

from django.db import models

# Create your models here.
class Invoice(models.Model):
    
    comments = models.TextField(max_length=3000, default='',
                                blank=True, null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False,
                                    blank=True, null=True)
    name = models.CharField('Customer Name', max_length=120, default='',
                             blank=True, null=True)
    amount_with_tax = models.CharField(max_length=120, default='',blank=True,null=True)
    amount_without_tax = models.CharField(max_length=120, default='',blank=True,null=True)
    type_of_sales = models.CharField(max_length=120, default='',blank=True,null=True)
    
    phone_number = models.CharField(max_length=120, default='',
                                    blank=True, null=True)
    
    
    
    
    total = models.IntegerField(default='0', blank=True,
                                null=True)
    balance = models.IntegerField(default='0', blank=True,
                                  null=True)
    timestamp = models.DateTimeField(auto_now_add=True,
                                     auto_now=False)
    
    last_updated = models.DateTimeField(auto_now_add=False,
                                        auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
            ('Receipt', 'Receipt'),
            ('Proforma Invoice', 'Proforma Invoice'),
            ('Invoice', 'Invoice'),
        )
    invoice_type = models.CharField(max_length=50, default='',
                                    blank=True, null=True, choices=invoice_type_choice)
    


    def __unicode__(self):
        return self.invoice_number
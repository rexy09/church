from django.db import models
from datetime import date

# Create your models here.


class ChurchMember(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    birth_date = models.DateField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    nida = models.CharField(max_length=50, unique=True, null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    work_phone = models.CharField(
        max_length=15, unique=True, blank=True, null=True)
    email = models.EmailField(
        max_length=254, unique=True, blank=True, null=True)
    address = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='member_photos', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["full_name"]
        verbose_name = 'Church Member'
        verbose_name_plural = 'Church Members'

    def __str__(self):
        return "{0} - {1}".format(self.id, self.full_name)

    def get_absolute_url(self):
        return ('')
    
    @property
    def current_year_total_contribution(self):
        total = self.church_contribution.filter(
            contribution_date__year=date.today().year).aggregate(total=models.Sum('amount'))['total']
        if total:
            return total
        else:
            return 0


class MemberContribution(models.Model):
    member = models.ForeignKey(
        ChurchMember, related_name='church_contribution', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    contribution_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-pk"]
        verbose_name = 'Member Contribution'
        verbose_name_plural = 'Member Contributions'

    def __str__(self):
        return self.member.full_name


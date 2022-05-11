from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title ="Nyankumbu Parish"
admin.site.index_title = "Nyankumbu Parish"
admin.site.site_header = 'Nyankumbu Parish'


admin.site.register(ChurchMember)
admin.site.register(MemberContribution)

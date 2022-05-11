from django import forms
from .models import *


class ChurchMemberForm(forms.ModelForm):
    
    class Meta:
        model = ChurchMember
        fields = "__all__"


class MemberContributionForm(forms.ModelForm):

    class Meta:
        model = MemberContribution
        fields = "__all__"

from django.shortcuts import render, redirect
from .models import ChurchMember, MemberContribution
from .forms import ChurchMemberForm, MemberContributionForm
from django.db.models import Sum

# Create your views here.


def index(request, *args, **kwargs):
    members = ChurchMember.objects.all()
    contributions = MemberContribution.objects.all()

    context = {
        'members': members,
        'contributions': contributions,
    }
    return render(request, 'index.html', context)


def list_church_members(request, *args, **kwargs):
    members = ChurchMember.objects.all().annotate(rank=Sum('church_contribution__amount')).order_by('-rank')
    context = {
        'members': members,
    }
    return render(request, 'list_church_members.html', context)


def add_church_member(request, *args, **kwargs):
    if request.method == 'POST':
        form = ChurchMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parish:list_church_members')
        else:
            print(form.errors)
    else:
        form = ChurchMemberForm()
    context = {
        'form': form,
    }
    return render(request, 'add_church_member.html', context)


def edit_church_member(request, *args, **kwargs):
    member = ChurchMember.objects.get(id=kwargs.get('id'))
    if request.method == 'POST':
        form = ChurchMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('parish:list_church_members')
        else:
            print(form.errors)
    else:
        form = ChurchMemberForm(instance=member)
    context = {
        'form': form,
    }
    return render(request, 'edit_church_member.html', context)


def delete_church_member(request, *args, **kwargs):
    obj = ChurchMember.objects.get(id=kwargs.get('id'))

    if request.method == 'POST':
        obj.delete()
        return redirect('parish:list_church_members')

    context = {
        'obj': obj,
    }
    return render(request, 'delete_church_member.html', context)


def view_church_member(request, *args, **kwargs):
    obj = ChurchMember.objects.get(id=kwargs.get('id'))

    context = {
        'obj': obj,
    }
    return render(request, 'view_church_member.html', context)

def list_member_contributions(request, *args, **kwargs):
    contributions = MemberContribution.objects.all()
    context = {
        'contributions': contributions,
    }
    return render(request, 'list_member_contributions.html', context)


def add_member_contribution(request, *args, **kwargs):
    # Initializingi member id in contribution form 
    if kwargs.get('id'):
        member = ChurchMember.objects.get(id=kwargs.get('id'))
        
    if request.method == 'POST':
        form = MemberContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parish:list_member_contributions')
        else:
            print(form.errors)
    else:
        if kwargs.get('id'):
            form = MemberContributionForm(
                initial={'member': member})
        else:
            form = MemberContributionForm()
    context = {
        'form': form,
    }
    return render(request, 'add_member_contribution.html', context)


def edit_member_contribution(request, *args, **kwargs):
    member = MemberContribution.objects.get(id=kwargs.get('id'))

    if request.method == 'POST':
        form = MemberContributionForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('parish:list_member_contributions')
        else:
            print(form.errors)
    else:
        form = MemberContributionForm(instance=member)
        
    context = {
        'form': form,
    }
    return render(request, 'edit_member_contribution.html', context)


def delete_member_contribution(request, *args, **kwargs):
    obj = MemberContribution.objects.get(id=kwargs.get('id'))

    if request.method == 'POST':
        obj.delete()
        return redirect('parish:list_member_contributions')

    context = {
        'obj': obj,
    }
    return render(request, 'delete_member_contribution.html', context)

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import ArepUserCreationForm
from .forms import CountryForm, MemberForm, ContactForm, FederationForm, BranchForm, MemberEditForm
from django.db import transaction
from membership.models import Branch, Member, Country, Federation
from datetime import datetime
from collections import Counter
import json

def index(request):
    title = "Nos membres, notre force"
    return render(request,"membership/home.html",{
        "title":title
    })

def listMembers(request):
    listTitle = "Member list"
    memberList = Member.objects.all
    return render(request,"membership/member-list.html",{
        'title':listTitle,
        'user':request.user,
        'memberz':memberList
    })

def editMember(request,member_id):
    member = get_object_or_404(Member,id=member_id)
    if request.method == "POST":
        member_form = MemberEditForm(request.POST,instance=member)
        contact_form = ContactForm(request.POST,instance=member.contact)
        if member_form.is_valid() and contact_form.is_valid():
            with transaction.atomic():
                contact = contact_form.save()
                contact.save()
                member = member_form.save()
                member.contact=contact
                member.last_change_date = datetime.now()
                member.save()
                return redirect(f"/membership/edit-member-success/{member.id}")
    else:
        member_form = MemberEditForm(instance=member)
        contact_form = ContactForm(instance=member.contact)
    return render(request,"membership/edit-member.html",{
        "title":f"Modifier le profil pour le membre \"{member.first_name} {member.name}\"",
        "member_form":member_form,
        "contact_form":contact_form
    })

def editMemberSuccess(request,member_id):
    member = get_object_or_404(Member,id=member_id)
    return render(request, "membership/edit-member-success.html/",{
        "title":f"Le profil du membre {member.first_name} {member.name} a été modifié.",
        "member":member
    })

def memberCharts(request):
    pageTitle = "Statistiques des membres"
    memberz = Member.objects.all()

    age_data = [(0 if member.age is None else member.age) for member in memberz]
    federation_data = [member.branch.federation.name for member in memberz]
    federation_counter = Counter(federation_data)
    sex_list = [member.sex for member in memberz]
    sex_counter = Counter(sex_list)
    sex_data = list(sex_counter.items())
    context = {
        "members":memberz,
        "title":pageTitle,
        "age_data":age_data,
        "federation_labels":list(federation_counter.keys()),
        "federation_counts":list(federation_counter.values()),
        "sex_data":sex_data,
        "sex_list":sex_list,
        "sex_counter":json.dumps(sex_counter),
        "sex_labels":list(sex_counter.keys()),
        "sex_counts":list(sex_counter.values())
    }
    return render(request, "membership/part/member-charts-bis.html",
                  context)

def charts(request):
    pageTitle = "Statistiques"
    #memberChartsPage = memberCharts(request)
    return render(request,"membership/charts.html",{
        "title":pageTitle,
     #   "included_html":memberChartsPage
    })

def memberDetail(request,member_id):
    member = get_object_or_404(Member,id=member_id)
    return render(request,"membership/member-detail.html",{
        "title":f"Données membre: {member.first_name} {member.name} {member.postname}",
        "member":member
    })

def listCountries(request):
    listTitle = "Country list"
    countryList = Country.objects.all
    return render(request,"membership/country-list.html",{
        'title':listTitle,
        'user':request.user,
        'countriez':countryList
    })

def listFederations(request):
    listTitle = "Liste des fédérations"
    federationList = Federation.objects.all
    return render(request,"membership/federation-list.html",{
        'title':listTitle,
        'user':request.user,
        'federationz':federationList
    })

def listBranchesByFederation(request, federation_id):
    federation = get_object_or_404(Federation,id=federation_id)
    listTitle = "Branch list for federation "+str(federation_id)
    branchList = federation.branches.all()
    return render(request,"membership/branch-list-by-federation-id.html",{
        'title':listTitle,
        'user':request.user,
        'branchez':branchList,
        'federation':federation
    })

def listMembersByBranch(request, branch_id):
    branch = get_object_or_404(Branch,id=branch_id)
    listTitle = "Liste des adhésions via l'antenne "+branch.name
    memberList = branch.members.all()
    return render(request,"membership/member-list-by-branch-id.html",{
        'title':listTitle,
        'user':request.user,
        'memberz':memberList,
        'branch':branch
    })

def addMember(request):
    if request.method == "POST":
        user_form = ArepUserCreationForm(request.POST)
        member_form = MemberForm(request.POST)
        contact_form = ContactForm(request.POST)
        if user_form.is_valid() and member_form.is_valid() and contact_form.is_valid():
            with transaction.atomic():
                contact = contact_form.save()
                contact.save()
                user = user_form.save()
                user.save()
                member = member_form.save()
                member.user=user
                member.contact=contact
                member.registration_start_date = datetime.now()
                member.save()
                return redirect(f"/membership/add-member-success/{member.id}")
    else:
        member_form = MemberForm()
        contact_form = ContactForm()
        user_form = ArepUserCreationForm()

    return render(
        request, "membership/add-member.html",{
        "title":"Ajout nouveau membre",
        "member_form":member_form,
        "contact_form":contact_form,
        "user_form" : user_form
    }) 

def addMemberSuccess(request,member_id):
    newMember = get_object_or_404(Member,id=member_id)
    return render(request, "membership/add-member-success.html",{
        "title":f"Le membre {newMember.first_name} {newMember.name} est bien enregistré.",
        "member":newMember
    })

def addBranchToFederation(request,federation_id):
    federation = get_object_or_404(Federation,id=federation_id)
    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        if(branch_form.is_valid()):
            with transaction.atomic():
                branch = branch_form.save()
                branch.federation = federation
                branch.save()
                return redirect(f"/membership/add-branch-success/{branch.id}")
    else:
        branch_form = BranchForm()

    return render(request,"membership/add-branch.html",{
        "title":f"Nouvelle branche pour la fédération \"{federation.name}\"",
        "branch_form":branch_form
    })

def addBranchSuccess(request,branch_id):
    newBranch = get_object_or_404(Branch,id=branch_id)
    return render(request,"membership/add-branch-success.html",{
        "branch":newBranch,
        "title":f"La branche \"{newBranch.name}\" de la fédération \"{newBranch.federation.name}\" a été créée avec succès."
    })

def addCountry(request):
    if request.method == "POST":
        country_form = CountryForm(request.POST)
        if(country_form.is_valid()):
            with transaction.atomic():
                country = country_form.save()
                return redirect(f"/membership/add-country-success/{country.code}")
    else:
        country_form = CountryForm()

    return render(request,"membership/add-country.html",{
        "title":"Nouveau pays",
        "country_form":country_form
    })

def addCountrySuccess(request,country_code):
    newCountry = get_object_or_404(Country,code=country_code)
    return render(request,"membership/add-country-success.html",{
        "branch":newCountry,
        "title":f"Le pays \"{newCountry.name}\" a été créée avec succès."
    })
def addFederation(request):
    if request.method == "POST":
        federation_form = FederationForm(request.POST)
        if(federation_form.is_valid()):
            with transaction.atomic():
                federation = federation_form.save()
                return redirect(f"/membership/add-federation-success/{federation.id}")
    else:
        federation_form = FederationForm()

    return render(request,"membership/add-federation.html",{
        "title":"Nouvelle fédération",
        "federation_form":federation_form
    })

def addFederationSuccess(request,federation_id):
    newFederation = get_object_or_404(Federation,id=federation_id)
    return render(request,"membership/add-federation-success.html",{
        "federation":newFederation,
        "title":f"La fédération \"{newFederation.name}\" a été créée avec succès."
    })

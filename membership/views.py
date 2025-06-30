from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import ArepUserCreationForm
from .forms import MemberForm, ContactForm, FederationForm, BranchForm
from django.db import transaction
from membership.models import Branch, Member, Country, Federation

def index(request):
    title = "AREP, notre pilier"
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

def listCountries(request):
    listTitle = "Country list"
    countryList = Country.objects.all
    return render(request,"membership/country-list.html",{
        'title':listTitle,
        'user':request.user,
        'countriez':countryList
    })

def listFederations(request):
    listTitle = "Federation list"
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
                user = user_form.save()
                member = member_form.save()
            return redirect("membership/add-member-success")
    else:
        member_form = MemberForm()
        contact_form = ContactForm()
        user_form = ArepUserCreationForm()

    return render(
        request, "membership/add-member.html",{
        "title":"Ajout nouveau membre",
        "member_form":member_form,
        "contact_form":contact_form,
        "user_form" : user_form,
    }) 

def addMemberSuccess(request,member_id):
    newMember = get_object_or_404(Member,id=member_id)
    return render("membership/add-member-success",{
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

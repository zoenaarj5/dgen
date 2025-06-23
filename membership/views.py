from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

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

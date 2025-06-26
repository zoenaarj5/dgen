from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("add-member/",views.addMember,name="addMember"),
    path("add-member-success/",views.addMemberSuccess,name="addMemberSuccess"),
    path("add-federation/",views.addFederation,name="addFederation"),
    path("add-federation-success/<int:federation_id>",views.addFederationSuccess,name="addFederationSuccess"),
    path("members/",views.listMembers,name="listMembers"),
    path("countries/",views.listCountries,name="listCountries"),
    path("federations/",views.listFederations,name="listFederations"),
    path("federations/<int:federation_id>/branches/",views.listBranchesByFederation,name="listBranchesByFederationId"),
    path("branches/<int:branch_id>/members/",views.listMembersByBranch,name="listMembersByBranchId"),
]
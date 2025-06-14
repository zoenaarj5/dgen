from rest_framework import serializers
from .models import Country,Permission,Role,Federation,Branch,PersonType,MemberTitle,MemberStatus,Grade,Contact,Member

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class PermissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class FederationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Federation
        fields = '__all__'

class BranchSerializer (serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class PersonTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = '__all__'

class MemberTitleSerializer (serializers.ModelSerializer):
    class Meta:
        model = MemberTitle
        fields = '__all__'
    
class MemberStatusSerializer (serializers.ModelSerializer):
    class Meta:
        model = MemberStatus
        fields = '__all__'

class GradeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
    

class ContactSerializer (serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class MemberSerializer (serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


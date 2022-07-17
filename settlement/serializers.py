from wsgiref import validate
from homepage.models import Homepage
from homepage.serializers import HomepageSerializer
from rest_framework import serializers
from settlement.models import MainOp, OtherOp, PostAdmitComa, PreAdmitComa, Settlement

class MainOpSerializer(serializers.ModelSerializer):
    op_time = serializers.ListField(
        child = serializers.CharField()
    )
    anaesthesia_time = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = MainOp
        fields = (
            'name',
            'code',
            'anaesthesia_type',
            'operator_name',
            'operator_code',
            'anaesthetist_name',
            'anaesthetist_code',
            'op_time',
            'anaesthesia_time',
        )
class OtherOpSerializer(serializers.ModelSerializer):
    op_time = serializers.ListField(
        child = serializers.CharField()
    )
    anaesthesia_time = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = OtherOp
        fields = (
            'name',
            'code',
            'anaesthesia_type',
            'operator_name',
            'operator_code',
            'anaesthetist_name',
            'anaesthetist_code',
            'op_time',
            'anaesthesia_time',
        )
class PreAdmitComaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreAdmitComa
        fields = (
            'days',
            'hrs',
            'mins',
        )
class PostAdmitComaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAdmitComa
        fields = (
            'days',
            'hrs',
            'mins',
        )

class SettlementSerializer(serializers.ModelSerializer):
    homepage_id = serializers.CharField(max_length=100)
    pre_admit_coma = PreAdmitComaSerializer(many=False)
    post_admit_coma = PostAdmitComaSerializer(many=False)
    main_ops = MainOpSerializer(many=True)
    other_ops = OtherOpSerializer(many=True)

    present_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    work_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    contact_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    admit_specialty = serializers.ListField(
        child = serializers.CharField()
    )
    trans_specialty = serializers.ListField(
        child = serializers.CharField()
    )
    release_specialty = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = Settlement
        fields = (
            "homepage_id",
            "list_sn",
            "org_name",
            "org_code",

            "case_num",
            "name",
            "age",
            "nationality",
            "ethnicity",
            "id_type",
            "id_card_num",
            "profession",
            "present_addr1",
            "present_addr2",
            "work_addr1",
            "work_addr2",
            "work_phone",
            "work_zip",
            "contact_name",
            "contact_relation",
            "contact_addr1",
            "contact_addr2",
            "contact_phone",
            "newborn_birth_weight",
            "admit_path",
            "admit_specialty",
            "trans_specialty",
            "release_time",
            "release_specialty",
            "hosp_duration",
            "head_injury_check",
            "pre_admit_coma",
            "post_admit_coma",
            "release_type",
            "cont_hosp_check",
            "cont_hosp_plan",

            "physician_name",
            "nurse_ic_name",

            "main_ops",
            "other_ops",
        )

    def create(self, validated_data): # data -> obj
        print('serializer')
        print('validated_data:',validated_data)
        homepage_id = validated_data.pop('homepage_id')
        pre_admit_coma_data = validated_data.pop('pre_admit_coma')
        post_admit_coma_data = validated_data.pop('post_admit_coma')

        main_ops_data = validated_data.pop('main_ops')
        other_ops_data = validated_data.pop('other_ops')
        homepage = Homepage.objects.get(id=homepage_id)
        settlement = Settlement.objects.create(homepage=homepage, **validated_data)
        PreAdmitComa.objects.create(settlement=settlement, **pre_admit_coma_data)
        PostAdmitComa.objects.create(settlement=settlement, **post_admit_coma_data)
        for main_op_data in main_ops_data:
            MainOp.objects.create(settlement=settlement, **main_op_data)
        for other_op_data in other_ops_data:
            OtherOp.objects.create(settlement=settlement, **other_op_data)


        return settlement
    
    def update(self, instance, validated_data):
        print('SettlementSerializer.update()')
        instance.list_sn = validated_data.get('list_sn', instance.list_sn)
        instance.org_name = validated_data.get('org_name', instance.org_name)
        instance.org_code = validated_data.get('org_code', instance.org_code)
        
        instance.case_num = validated_data.get('case_num', instance.case_num)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
        instance.id_type = validated_data.get('id_type', instance.id_type)
        instance.id_card_num = validated_data.get('id_card_num', instance.id_card_num)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.present_addr1 = validated_data.get('present_addr1', instance.present_addr1)
        instance.present_addr2 = validated_data.get('present_addr2', instance.present_addr2)
        instance.work_addr1 = validated_data.get('work_addr1', instance.work_addr1)
        instance.work_addr2 = validated_data.get('work_addr2', instance.work_addr2)
        instance.work_phone = validated_data.get('work_phone', instance.work_phone)
        instance.work_zip = validated_data.get('work_zip', instance.work_zip)
        instance.contact_name = validated_data.get('contact_name', instance.contact_name)
        instance.contact_relation = validated_data.get('contact_relation', instance.contact_relation)
        instance.contact_addr1 = validated_data.get('contact_addr1', instance.contact_addr1)
        instance.contact_addr2 = validated_data.get('contact_addr2', instance.contact_addr2)
        instance.contact_phone = validated_data.get('contact_phone', instance.contact_phone)
        instance.newborn_birth_weight = validated_data.get('newborn_birth_weight', instance.newborn_birth_weight)
        instance.newborn_admit_weight = validated_data.get('newborn_admit_weight', instance.newborn_admit_weight)
        instance.admit_path = validated_data.get('admit_path', instance.admit_path)
        instance.admit_specialty = validated_data.get('admit_specialty', instance.admit_specialty)
        instance.trans_specialty = validated_data.get('trans_specialty', instance.trans_specialty)
        instance.release_time = validated_data.get('release_time', instance.release_time)
        instance.release_specialty = validated_data.get('release_specialty', instance.release_specialty)
        instance.hosp_duration = validated_data.get('hosp_duration', instance.hosp_duration)
        instance.head_injury_check = validated_data.get('head_injury_check', instance.head_injury_check)
        instance.pre_admit_coma = validated_data.get('pre_admit_coma', instance.pre_admit_coma)
        instance.post_admit_coma = validated_data.get('post_admit_coma', instance.post_admit_coma)
        instance.release_type = validated_data.get('release_type', instance.release_type)
        instance.cont_hosp_check = validated_data.get('cont_hosp_check', instance.cont_hosp_check)
        
        instance.physician_name = validated_data.get('physician_name', instance.physician_name)
        instance.nurse_ic_name = validated_data.get('nurse_ic_name', instance.nurse_ic_name)
        
        pre_admit_coma_data = validated_data.pop('pre_admit_coma')
        pre_admit_coma = instance.pre_admit_coma
        pre_admit_coma.days = pre_admit_coma_data.get('days', pre_admit_coma.days)
        pre_admit_coma.hrs = pre_admit_coma_data.get('days', pre_admit_coma.hrs)
        pre_admit_coma.mins = pre_admit_coma_data.get('days', pre_admit_coma.mins)
        pre_admit_coma.save()

        post_admit_coma_data = validated_data.pop('post_admit_coma')
        post_admit_coma = instance.post_admit_coma
        post_admit_coma.days = post_admit_coma_data.get('days', post_admit_coma.days)
        post_admit_coma.hrs = post_admit_coma_data.get('days', post_admit_coma.hrs)
        post_admit_coma.mins = post_admit_coma_data.get('days', post_admit_coma.mins)
        post_admit_coma.save()

        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        print('ret:',ret)
        # ret['username'] = ret['username'].lower()
        return ret
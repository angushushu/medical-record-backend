from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Charge, Homepage, MainDiag, OtherDiag, Op, LesionReason, Pathology, PostAdmitComa, PreAdmitComa

class MainDiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDiag
        fields = (
            'release',
            'code',
            'condition',
        )
class LesionReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LesionReason
        fields = (
            'description',
            'code',
        )
class PathologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathology
        fields = (
            'description',
            'code',
            'number',
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
class OtherDiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDiag
        fields = (
            'release',
            'code',
            'condition',
        )
class OpSerializer(serializers.ModelSerializer):
    wound_healing_lvl = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = Op
        fields = (
            'code',
            'date',
            'level',
            'name',
            'operator',
            'assis1',
            'assis2',
            'wound_healing_lvl',
            'anaesthesia_type',
            'anaesthetist',
        )
class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = (
            'total',
            'self_pay',
            'general_service',
            'general_operation',
            'general_nursing',
            'general_other',
            'pathologic_diag',
            'lab_diag',
            'scan_diag',
            'clinic_diag',
            'non_operational',
            'operational',
            'clinic_physic',
            'anaesthesia',
            'operation',
            'recover',
            'traditional_treat',
            'western_med',
            'antibio_med',
            'traditional_patent_drug',
            'traditional_herb',
            'blood',
            'proteins',
            'globulins',
            'coagulation',
            'cytokine',
            'examine_supplies',
            'treat_supplies',
            'operation_supplies',
            'other',
        )
class HomepageSerializer(serializers.ModelSerializer):
    main_diag = MainDiagSerializer(many=False)
    lesion_reason = LesionReasonSerializer(many=False)
    pathology = PathologySerializer(many=False)
    pre_admit_coma = PreAdmitComaSerializer(many=False)
    post_admit_coma = PostAdmitComaSerializer(many=False)
    charge = ChargeSerializer(many=False)
    other_diags = OtherDiagSerializer(many=True)
    ops = OpSerializer(many=True)
    id = -1
    parent_birthplace = serializers.ListField(
        child = serializers.CharField()
    )
    birthplace = serializers.ListField(
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
    present_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    registered_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    work_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    contact_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = Homepage
        fields = (
            "id", #
            "org_name",
            "org_code",
            "main_diag",
            "lesion_reason",
            "pathology",
            "pre_admit_coma",
            "post_admit_coma",
            "other_diags",
            "ops",
            "charge",

            "purchase_method",
            "health_card",
            "admit_cnt",
            "case_num",
            "name",
            "gender",
            "birthday",
            "age",
            "nationality",
            "newborn_check",
            "newborn_birth_weight",
            "newborn_admit_weight",
            "birthplace",
            "parent_birthplace",
            "ethnicity",
            "id_type",
            "id_num",
            "id_card_num",
            "passport_num",
            "officer_num",
            "profession",
            "marriage_stat",
            "present_addr1",
            "present_addr2",
            "present_phone",
            "present_zip",
            "registered_addr1",
            "registered_addr2",
            "registered_zip",
            "work_addr1",
            "work_addr2",
            "work_phone",
            "work_zip",
            "contact_name",
            "contact_relation",
            "contact_other_description",
            "contact_addr1",
            "contact_addr2",
            "contact_phone",
            "admit_path",
            "admit_time",
            "admit_specialty",
            "admit_sickroom",
            "trans_specialty",
            "release_time",
            "release_specialty",
            "release_sickroom",
            "hosp_duration",
            "diagnosis",
            "disease_code",

            "od_release",
            "od_code",
            "od_condition",
            "drug_allergy_check",
            "drug_allergy",
            "necropsy_check",
            "blood_group",
            "rh",
            "director",
            "chief",
            "physician_ic",
            "resident",
            "nurse_ic",
            "refresher",
            "trainee",
            "coder",
            "record_quality",
            "qc_doctor",
            "qc_nurse",
            "qc_date",
            "release_type",
            "accept_hosp_2",
            "accept_hosp_3",
            "cont_hosp_check",
            "cont_hosp_plan",
            "head_injury_check",
        )
    def create(self, validated_data):
        print('validated_data:',validated_data)
        # print('in create()')
        
        main_diag_data = validated_data.pop('main_diag')
        lesion_reason_data = validated_data.pop('lesion_reason')
        pathology_data = validated_data.pop('pathology')
        pre_admit_coma_data = validated_data.pop('pre_admit_coma')
        post_admit_coma_data = validated_data.pop('post_admit_coma')
        other_diags_data = validated_data.pop('other_diags')
        ops_data = validated_data.pop('ops')
        charge_data = validated_data.pop('charge')
        # print('main_diag_data:', main_diag_data)
        # print('diags_data:',other_diags_data)
        # print('ops_data:',ops_data)
        print('admit_specialty:',validated_data['admit_specialty'])
        print('trans_specialty:',validated_data['trans_specialty'])
        print('release_specialty:',validated_data['release_specialty'])
        print('type:',type(validated_data['release_specialty']))
                
        homepage = Homepage.objects.create(**validated_data)
        MainDiag.objects.create(homepage=homepage, **main_diag_data)
        LesionReason.objects.create(homepage=homepage, **lesion_reason_data)
        Pathology.objects.create(homepage=homepage, **pathology_data)
        PreAdmitComa.objects.create(homepage=homepage, **pre_admit_coma_data)
        PostAdmitComa.objects.create(homepage=homepage, **post_admit_coma_data)
        Charge.objects.create(homepage=homepage, **charge_data)
        for other_diag_data in other_diags_data:
            OtherDiag.objects.create(homepage=homepage, **other_diag_data)
        for op_data in ops_data:
            Op.objects.create(homepage=homepage, **op_data)
        
        return homepage
    
    def update(self, instance, validated_data):
        print('HomepageSerializer.update()')
        # print('validated_data[org_name]:', validated_data['org_name'])
        # 更新字段 未完待续
        instance.org_code = validated_data.get('org_code', instance.org_code)
        instance.org_name = validated_data.get('org_name', instance.org_name)
        instance.purchase_method = validated_data.get('purchase_method', instance.purchase_method)
        instance.health_card = validated_data.get('health_card', instance.health_card)
        instance.admit_cnt = validated_data.get('admit_cnt', instance.admit_cnt)
        instance.case_num = validated_data.get('case_num', instance.case_num)
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.age = validated_data.get('age', instance.age)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.newborn_check = validated_data.get('newborn_check', instance.newborn_check)
        instance.newborn_birth_weight = validated_data.get('newborn_birth_weight', instance.newborn_birth_weight)
        # "nationality",
        # "newborn_check",
        # "newborn_birth_weight",
        # "newborn_admit_weight",
        # "birthplace",
        # "parent_birthplace",
        # "ethnicity",
        # "id_type",
        # "id_num",
        # "id_card_num",
        # "passport_num",
        # "officer_num",
        # "profession",
        # "marriage_stat",
        # "present_addr1",
        # "present_addr2",
        # "present_phone",
        # "present_zip",
        # "registered_addr1",
        # "registered_addr2",
        # "registered_zip",
        # "work_addr1",
        # "work_addr2",
        # "work_phone",
        # "work_zip",
        # "contact_name",
        # "contact_relation",
        # "contact_other_description",
        # "contact_addr1",
        # "contact_addr2",
        # "contact_phone",
        # "admit_path",
        # "admit_time",
        # "admit_specialty",
        # "admit_sickroom",
        # "trans_specialty",
        # "release_time",
        # "release_specialty",
        # "release_sickroom",
        # "hosp_duration",
        # "diagnosis",
        # "disease_code",

        # "od_release",
        # "od_code",
        # "od_condition",
        # "drug_allergy_check",
        # "drug_allergy",
        # "necropsy_check",
        # "blood_group",
        # "rh",
        # "director",
        # "chief",
        # "physician_ic",
        # "resident",
        # "nurse_ic",
        # "refresher",
        # "trainee",
        # "coder",
        # "record_quality",
        # "qc_doctor",
        # "qc_nurse",
        # "qc_date",
        # "release_type",
        # "accept_hosp_2",
        # "accept_hosp_3",
        # "cont_hosp_check",
        # "cont_hosp_plan",
        # "head_injury_check",
        
        main_diag_data = validated_data.pop('main_diag')
        print('new main_diag_data:',main_diag_data)
        main_diag = instance.main_diag
        main_diag.release = main_diag_data.get('release', main_diag.release)
        main_diag.code = main_diag_data.get('code', main_diag.code)
        main_diag.condition = main_diag_data.get('condition', main_diag.condition)
        main_diag.save()
        
        other_diags_data = validated_data.pop('other_diags')
        print('new other_diag_data:',other_diags_data)
        print(instance.other_diags)
        OtherDiag.objects.filter(homepage=instance).delete()
        for other_diag_data in other_diags_data:
            OtherDiag.objects.create(homepage=instance, **other_diag_data)
        
        ops_data = validated_data.pop('ops')
        print('new ops_data:', ops_data)
        print(instance.other_diags)
        Op.objects.filter(homepage=instance).delete()
        for op_data in ops_data:
            Op.objects.create(homepage=instance, **op_data)
        
        lesion_reason_data = validated_data.pop('lesion_reason')
        print('new lesion_reason_data:',lesion_reason_data)
        lesion_reason = instance.lesion_reason
        lesion_reason.description = lesion_reason_data.get('description', lesion_reason.description)
        lesion_reason.code = lesion_reason_data.get('code', lesion_reason.code)
        lesion_reason.save()

        pathology_data = validated_data.pop('pathology')
        print('new pathology_data:',pathology_data)
        pathology = instance.pathology
        pathology.description = pathology_data.get('description', pathology.description)
        pathology.code = pathology_data.get('code', pathology.code)
        pathology.number = pathology_data.get('number', pathology.number)
        pathology.save()

        post_admit_coma_data = validated_data.pop('post_admit_coma')
        print('new post_admit_coma_data:',post_admit_coma_data)
        post_admit_coma = instance.post_admit_coma
        post_admit_coma.days = post_admit_coma_data.get('days', post_admit_coma.days)
        post_admit_coma.hrs = post_admit_coma_data.get('hrs', post_admit_coma.hrs)
        post_admit_coma.mins = post_admit_coma_data.get('mins', post_admit_coma.mins)
        post_admit_coma.save()

        pre_admit_coma_data = validated_data.pop('pre_admit_coma')
        print('new pre_admit_coma_data:',pre_admit_coma_data)
        pre_admit_coma = instance.pre_admit_coma
        pre_admit_coma.days = pre_admit_coma_data.get('days', pre_admit_coma.days)
        pre_admit_coma.hrs = pre_admit_coma_data.get('hrs', pre_admit_coma.hrs)
        pre_admit_coma.mins = pre_admit_coma_data.get('mins', pre_admit_coma.mins)
        pre_admit_coma.save()

        charge_data = validated_data.pop('charge')
        print('new charge_data:',charge_data)
        charge = instance.charge
        charge.total = charge_data.get('total', charge.total)
        charge.self_pay = charge_data.get('self_pay', charge.self_pay)
        charge.general_service = charge_data.get('general_service', charge.general_service)
        charge.general_operation = charge_data.get('general_operation', charge.general_operation)
        charge.general_nursing = charge_data.get('general_nursing', charge.general_nursing)
        charge.general_other = charge_data.get('general_other', charge.general_other)
        charge.pathologic_diag = charge_data.get('pathologic_diag', charge.pathologic_diag)
        charge.lab_diag = charge_data.get('lab_diag', charge.lab_diag)
        charge.scan_diag = charge_data.get('scan_diag', charge.scan_diag)
        charge.clinic_diag = charge_data.get('clinic_diag', charge.clinic_diag)
        charge.non_operational = charge_data.get('non_operational', charge.non_operational)
        charge.operational = charge_data.get('operational', charge.operational)
        charge.clinic_physic = charge_data.get('clinic_physic', charge.clinic_physic)
        charge.anaesthesia = charge_data.get('anaesthesia', charge.anaesthesia)
        charge.operation = charge_data.get('operation', charge.operation)
        charge.recover = charge_data.get('recover', charge.recover)
        charge.traditional_treat = charge_data.get('traditional_treat', charge.traditional_treat)
        charge.western_med = charge_data.get('western_med', charge.western_med)
        charge.antibio_med = charge_data.get('antibio_med', charge.antibio_med)
        charge.traditional_patent_drug = charge_data.get('traditional_patent_drug', charge.traditional_patent_drug)
        charge.traditional_herb = charge_data.get('traditional_herb', charge.traditional_herb)
        charge.blood = charge_data.get('blood', charge.blood)
        charge.proteins = charge_data.get('proteins', charge.proteins)
        charge.globulins = charge_data.get('globulins', charge.globulins)
        charge.coagulation = charge_data.get('coagulation', charge.coagulation)
        charge.cytokine = charge_data.get('cytokine', charge.cytokine)
        charge.examine_supplies = charge_data.get('examine_supplies', charge.examine_supplies)
        charge.treat_supplies = charge_data.get('treat_supplies', charge.treat_supplies)
        charge.operation_supplies = charge_data.get('operation_supplies', charge.operation_supplies)
        charge.other = charge_data.get('other', charge.other)
        charge.save()

        instance.save()
        return instance

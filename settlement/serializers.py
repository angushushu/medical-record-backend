from wsgiref import validate
# from attr import fields

# from cv2 import validateDisparity
from homepage.models import Homepage
from homepage.serializers import HomepageSerializer
from rest_framework import serializers
from settlement.models import BedFee, CUUsage, DiagFee, DiagInfo, ExamFee, GeneralDiagFee, LabTestFee, MainDiag, MainDisease, MainOp, MedMaterialFee, NursingFee, OpFee, OtherDiag, OtherFee, OtherOp, MainSymp, PostAdmitComa, PreAdmitComa, RegistrationFee, Settlement, SpecialFee, TotalFee, TraditionalPatentFee, TraditionalRelease, TraditionalTabletFee, Transfusion, TreatFee, VentilatorDuration, WesternRelease, WesternMedFee

class BedFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class DiagFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class ExamFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class LabTestFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class TreatFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class OpFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class NursingFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursingFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class MedMaterialFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedMaterialFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class WesternMedFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WesternMedFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class TraditionalTabletFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalTabletFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class TraditionalPatentFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalPatentFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class GeneralDiagFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralDiagFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class RegistrationFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class OtherFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class SpecialFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )
class TotalFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalFee
        fields = (
            'amount',
            'A',
            'B',
            'self_pay',
            'other'
        )

class TransfusionSerializer(serializers.ModelSerializer):
    blood_type = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = Transfusion
        fields = (
            'blood_type',
            'blood_volume',
            'volume_unit',
        )
class CUUsageSerializer(serializers.ModelSerializer):
    time = serializers.ListField(
        child = serializers.CharField()
    )
    class Meta:
        model = CUUsage
        fields = (
            'CU_type',
            'time',
            'total_hr',
            'total_min'
        )

class MainSympSerializer(serializers.ModelSerializer):
    # owner = serializers.IntegerField(required=False) # testing
    class Meta:
        model = MainSymp
        fields = (
            'diag',
            'disease_code',
            'admit_condition'
        )
    # def get_validation_exclusions(self):
    #     exclusions = super(MainSymSerializer, self).get_validation_exclusions()
    #     return exclusions + ['owner']
class MainDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDisease
        fields = (
            'diag',
            'disease_code',
            'admit_condition'
        )
class OtherDiagSerializer(serializers.ModelSerializer):
    # owner = serializers.IntegerField(required=False)
    class Meta:
        model = OtherDiag
        fields = (
            'diag',
            'disease_code',
            'admit_condition'
        )
    def to_representation(self, instance):
        print('HELLO OTHERDIAG')
        print('other_diag', instance)
        ret = super().to_representation(instance)
        print('other_diag rep:', ret)
        return ret
class MainDiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDiag
        fields = (
            'diag',
            'disease_code',
            'admit_condition'
        )
    def to_representation(self, instance):
        print('HELLO MAINDIAG')
        print('main_diag', instance)
        ret = super().to_representation(instance)
        print('main_diag rep:', ret)
        return ret
class TraditionalReleaseSerializer(serializers.ModelSerializer):
    main_disease = MainDiseaseSerializer()
    # main_symps = MainSympSerializer(many=True, required=False)
    main_symps = MainSympSerializer(many=True)
    class Meta:
        model = TraditionalRelease
        fields = (
            'main_disease',
            'main_symps'
        )
class WesternReleaseSerializer(serializers.ModelSerializer):
    # main_diag = MainDiagSerializer(many=False)
    main_diag = MainDiagSerializer()
    # other_diags = OtherDiagSerializer(many=True, required=False)
    other_diags = OtherDiagSerializer(many=True)
    class Meta:
        model = WesternRelease
        fields = (
            'main_diag',
            'other_diags'
        )
    def to_representation(self, instance):
        print('HELLO WORLD')
        print('western_release', instance)
        ret = super().to_representation(instance)
        print('rep:', ret)
        return ret
class DiagInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagInfo
        fields = (
            'disease_name',
            'disease_code',
            'op_name',
            'op_code'
        )

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
class VentilatorDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentilatorDuration
        fields = (
            'days',
            'hrs',
            'mins',
        )
# class NewBornAdmitTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewBornAdmitType
#         fields = (
#             'value' # value key 在view中加入
#         )

class SettlementSerializer(serializers.ModelSerializer):
    homepage_id = serializers.CharField(max_length=100)
    heal_type = serializers.ListField(
        child = serializers.CharField()
    )
    present_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    work_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    contact_addr1 = serializers.ListField(
        child = serializers.CharField()
    )
    diag_specialty = serializers.ListField(
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
    # w_emergency_diag = serializers.ListField(
    #     child = serializers.CharField()
    # )
    # t_emergency_diag = serializers.ListField(
    #     child = serializers.CharField()
    # )
    settle_duration = serializers.ListField(
        child = serializers.CharField()
    )
    diag_info = DiagInfoSerializer(many=True)
    western_release = WesternReleaseSerializer(many=False)
    traditional_release = TraditionalReleaseSerializer(many=False)
    main_ops = MainOpSerializer(many=True)
    other_ops = OtherOpSerializer(many=True)
    ventilator_duration = VentilatorDurationSerializer(many=False)
    pre_admit_coma = PreAdmitComaSerializer(many=False)
    post_admit_coma = PostAdmitComaSerializer(many=False)
    CU_usage = CUUsageSerializer(many=True)
    transfusion = TransfusionSerializer(many=True)
    bed_fee = BedFeeSerializer(many=False)
    diag_fee = DiagFeeSerializer(many=False)
    exam_fee = ExamFeeSerializer(many=False)
    lab_test_fee = LabTestFeeSerializer(many=False)
    treat_fee = TreatFeeSerializer(many=False)
    op_fee = OpFeeSerializer(many=False)
    nursing_fee = NursingFeeSerializer(many=False)
    med_material_fee = MedMaterialFeeSerializer(many=False)
    western_med_fee = WesternMedFeeSerializer(many=False)
    traditional_tablet_fee = TraditionalTabletFeeSerializer(many=False)
    traditional_patent_fee = TraditionalPatentFeeSerializer(many=False)
    general_diag_fee = GeneralDiagFeeSerializer(many=False)
    registration_fee = RegistrationFeeSerializer(many=False)
    other_fee = OtherFeeSerializer(many=False)
    special_fee = SpecialFeeSerializer(many=False)
    total_fee = TotalFeeSerializer(many=False)
    # newborn_admit_type = NewBornAdmitTypeSerializer(many=True)
    newborn_admit_type = serializers.JSONField()
    class Meta:
        model = Settlement
        fields = (
            "homepage_id",
            "list_sn",
            "org_name",
            "org_code",
            "settlement_lvl",
            "settlement_num",
            "case_num",
            "report_time",
            "name",
            "gender", #
            "birthday", #
            "age",
            "nationality",
            "age_in_day",
            "ethnicity",
            "id_type",
            "id_card_num",
            "passport_num",
            "officer_num",
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
            "settlement_type",
            "special_person_type",
            "settlement_loc",
            "newborn_check",
            "newborn_admit_type",
            "newborn_birth_weight",
            "newborn_admit_weight",
            "diag_specialty",
            "diag_date",
            "diag_info",
            "hosp_reason",
            "admit_path",
            "heal_type",
            "admit_time",
            "admit_specialty",
            "trans_specialty",
            "release_time",
            "release_specialty",
            "hosp_duration",
            "w_emergency_diag",
            "t_emergency_diag",
            "w_disease_code",
            "t_disease_code",
            "western_release",
            "traditional_release",
            "diag_cnt",
            "main_ops",
            "other_ops",
            "op_cnt",
            "ventilator_duration",
            "head_injury_check",
            "pre_admit_coma",
            "post_admit_coma",
            "CU_usage",
            "transfusion",
            "special_care_days",
            "l1_care_days",
            "l2_care_days",
            "l3_care_days",
            "release_type",
            "accept_hosp_2",
            "accept_hosp_3",
            "cont_hosp_check",
            "cont_hosp_plan",

            "physician_name",
            "physician_code",
            "nurse_ic_name",
            "nurse_ic_code",
            "biz_sn",
            "bill_code",
            "bill_num",
            "settle_duration",
            "bed_fee",
            "diag_fee",
            "exam_fee",
            "lab_test_fee",
            "treat_fee",
            "op_fee",
            "nursing_fee",
            "med_material_fee",
            "western_med_fee",
            "traditional_tablet_fee",
            "traditional_patent_fee",
            "general_diag_fee",
            "registration_fee",
            "other_fee",
            "special_fee",
            "total_fee",
            "insurance_pay",
            "staff_subsidy",
            "residence_insurance",
            "public_servant_subsidy",
            "health_aid_pay",
            "enterprise_supp",
            "biz_insurance",
            "partial_self_purchase",
            "self_purchase",
            "account_pay",
            "cash_pay",
            "payment_type",
            "designated_med_report_unit",
            "designated_med_report_person",
            "health_insurance_org",
            "health_insurance_org_code",
            "health_insurance_person",
            "health_insurance_person_code",
        )

    def to_representation(self, instance):
        print('settlement_to_rep')
        # print('settlement.westernrelease:', WesternReleaseSerializer(instance.western_release).data)
        ret = super().to_representation(instance)
        # print('settlement @to_representation:', ret)
        # ret['username'] = ret['username'].lower()
        return ret

    def create(self, validated_data): # data -> obj
        print('@settlementSerializer.create()')
        print('validated_data:',validated_data)
        homepage_id = validated_data.pop('homepage_id')

        western_release_data = None
        main_diag_data = None
        other_diags_data = None
        traditional_release_data = None
        main_disease_data = None
        main_symps_data = None
        # western release
        if 'western_release' in validated_data.keys():
            print('there is western_release')
            western_release_data = validated_data.pop('western_release')
            print('western_release_data:',western_release_data)
            main_diag_data = western_release_data['main_diag']
            if 'other_diags' in western_release_data.keys():
                other_diags_data = western_release_data['other_diags']
            else:
                other_diags_data = []
        else:
            print('there is no western_release')
        # traditional release
        if 'traditional_release' in validated_data.keys():
            print('there is traditional_lease')
            traditional_release_data = validated_data.pop('traditional_release')
            print('traditional_release_data:',traditional_release_data)
            main_disease_data = traditional_release_data['main_disease']
            if 'main_symps' in traditional_release_data.keys():
                main_symps_data = traditional_release_data['main_symps']
            else:
                main_symps_data = []
        else:
            print('there is no western_release')
        main_ops_data = validated_data.pop('main_ops')
        other_ops_data = validated_data.pop('other_ops')
        ventilator_duration_data = validated_data.pop('ventilator_duration')
        pre_admit_coma_data = validated_data.pop('pre_admit_coma')
        post_admit_coma_data = validated_data.pop('post_admit_coma')
        CU_usages_data = validated_data.pop('CU_usage')
        transfusions_data = validated_data.pop('transfusion')
        bed_fee_data = validated_data.pop('bed_fee')
        diag_fee_data = validated_data.pop('diag_fee')
        exam_fee_data = validated_data.pop('exam_fee')
        lab_test_fee_data = validated_data.pop('lab_test_fee')
        treat_fee_data = validated_data.pop('treat_fee')
        op_fee_data = validated_data.pop('op_fee')
        nursing_fee_data = validated_data.pop('nursing_fee')
        med_material_fee_data = validated_data.pop('med_material_fee')
        western_med_fee_data = validated_data.pop('western_med_fee')
        traditional_tablet_fee_data = validated_data.pop('traditional_tablet_fee')
        traditional_patent_fee_data = validated_data.pop('traditional_patent_fee')
        general_diag_fee_data = validated_data.pop('general_diag_fee')
        registration_fee_data = validated_data.pop('registration_fee')
        other_fee_data = validated_data.pop('other_fee')
        special_fee_data = validated_data.pop('special_fee')
        total_fee_data = validated_data.pop('total_fee')
        print('creating diag info')
        diag_infos_data = validated_data.pop('diag_info')
        print('test1')
        homepage = Homepage.objects.get(id=homepage_id)
        print('test2')
        settlement = Settlement.objects.create(homepage=homepage, **validated_data)
        
        print('diag_infos_data:',diag_infos_data)
        for diag_info_data in diag_infos_data:
            print('  diag_info_data:', diag_info_data)
            DiagInfo.objects.create(settlement=settlement, **diag_info_data)
        
        print('creating western_release')
        # western release
        if western_release_data:
            western_release = WesternRelease.objects.create(settlement=settlement)
            if main_diag_data:
                MainDiag.objects.create(western_release=western_release, **main_diag_data)
            if other_diags_data:
                for other_diag_data in other_diags_data:
                    OtherDiag.objects.create(western_release=western_release, **other_diag_data)
        # traditional release
        if traditional_release_data:
            traditional_release = TraditionalRelease.objects.create(settlement=settlement)
            if main_disease_data:
                MainDisease.objects.create(traditional_release=traditional_release, **main_disease_data)
            if main_symps_data:
                for main_symp_data in main_symps_data:
                    MainSymp.objects.create(traditional_release=traditional_release, **main_symp_data)
        for main_op_data in main_ops_data:
            MainOp.objects.create(settlement=settlement, **main_op_data)
        for other_op_data in other_ops_data:
            OtherOp.objects.create(settlement=settlement, **other_op_data)
        VentilatorDuration.objects.create(settlement=settlement, **ventilator_duration_data)
        PreAdmitComa.objects.create(settlement=settlement, **pre_admit_coma_data)
        PostAdmitComa.objects.create(settlement=settlement, **post_admit_coma_data)
        for CU_usage_data in CU_usages_data:
            CUUsage.objects.create(settlement=settlement, **CU_usage_data)
        for transfusion_data in transfusions_data:
            Transfusion.objects.create(settlement=settlement, **transfusion_data)
        BedFee.objects.create(settlement=settlement, **bed_fee_data)
        DiagFee.objects.create(settlement=settlement, **diag_fee_data)
        ExamFee.objects.create(settlement=settlement, **exam_fee_data)
        LabTestFee.objects.create(settlement=settlement, **lab_test_fee_data)
        TreatFee.objects.create(settlement=settlement, **treat_fee_data)
        OpFee.objects.create(settlement=settlement, **op_fee_data)
        NursingFee.objects.create(settlement=settlement, **nursing_fee_data)
        MedMaterialFee.objects.create(settlement=settlement, **med_material_fee_data)
        WesternMedFee.objects.create(settlement=settlement, **western_med_fee_data)
        TraditionalTabletFee.objects.create(settlement=settlement, **traditional_tablet_fee_data)
        TraditionalPatentFee.objects.create(settlement=settlement, **traditional_patent_fee_data)
        GeneralDiagFee.objects.create(settlement=settlement, **general_diag_fee_data)
        RegistrationFee.objects.create(settlement=settlement, **registration_fee_data)
        OtherFee.objects.create(settlement=settlement, **other_fee_data)
        SpecialFee.objects.create(settlement=settlement, **special_fee_data)
        TotalFee.objects.create(settlement=settlement, **total_fee_data)
        return settlement
    
    def update(self, instance, validated_data):
        print('@SettlementSerializer.update()')
        instance.list_sn = validated_data.get('list_sn', instance.list_sn)
        instance.org_name = validated_data.get('org_name', instance.org_name)
        instance.org_code = validated_data.get('org_code', instance.org_code)
        instance.settlement_lvl = validated_data.get('settlement_lvl', instance.settlement_lvl)
        instance.settlement_num = validated_data.get('settlement_num', instance.settlement_num)
        instance.case_num = validated_data.get('case_num', instance.case_num)
        instance.report_time = validated_data.get('report_time', instance.report_time)
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.age = validated_data.get('age', instance.age)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.age_in_day = validated_data.get('age_in_day', instance.age_in_day)
        instance.ethnicity = validated_data.get('ethnicity', instance.ethnicity)
        instance.id_type = validated_data.get('id_type', instance.id_type)
        instance.id_card_num = validated_data.get('id_card_num', instance.id_card_num)
        instance.passport_num = validated_data.get('passport_num', instance.passport_num)
        instance.officer_num = validated_data.get('officer_num', instance.officer_num)
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
        instance.settlement_type = validated_data.get('settlement_type', instance.settlement_type)
        instance.special_person_type = validated_data.get('special_person_type', instance.special_person_type)
        instance.settlement_loc = validated_data.get('settlement_loc', instance.settlement_loc)
        instance.newborn_check = validated_data.get('newborn_check', instance.newborn_check)
        instance.newborn_admit_type = validated_data.get('newborn_admit_type', instance.newborn_admit_type)
        instance.newborn_birth_weight = validated_data.get('newborn_birth_weight', instance.newborn_birth_weight)
        instance.newborn_admit_weight = validated_data.get('newborn_admit_weight', instance.newborn_admit_weight)
        instance.diag_specialty = validated_data.get('diag_specialty', instance.diag_specialty)
        instance.diag_date = validated_data.get('diag_date', instance.diag_date)
        # instance.diag_info = validated_data.get('diag_info', instance.diag_info)
        instance.hosp_reason = validated_data.get('hosp_reason', instance.hosp_reason)
        print('hosp_reason changed to',instance.hosp_reason)
        instance.admit_path = validated_data.get('admit_path', instance.admit_path)
        instance.heal_type = validated_data.get('heal_type', instance.heal_type)
        instance.admit_time = validated_data.get('admit_time', instance.admit_time)
        instance.admit_specialty = validated_data.get('admit_specialty', instance.admit_specialty)
        instance.trans_specialty = validated_data.get('trans_specialty', instance.trans_specialty)
        instance.release_time = validated_data.get('release_time', instance.release_time)
        instance.release_specialty = validated_data.get('release_specialty', instance.release_specialty)
        instance.hosp_duration = validated_data.get('hosp_duration', instance.hosp_duration)
        instance.w_emergency_diag = validated_data.get('w_emergency_diag', instance.w_emergency_diag)
        instance.t_emergency_diag = validated_data.get('t_emergency_diag', instance.t_emergency_diag)
        print('t_emergency_diag in validated_data:', validated_data['t_emergency_diag'])
        instance.w_disease_code = validated_data.get('w_disease_code', instance.w_disease_code)
        instance.t_disease_code = validated_data.get('t_disease_code', instance.t_disease_code)
        # instance.western_release = validated_data.get('western_release', instance.western_release)
        # instance.traditional_release = validated_data.get('traditional_release', instance.traditional_release)
        instance.diag_cnt = validated_data.get('diag_cnt', instance.diag_cnt)
        # main_ops
        # other_ops
        instance.op_cnt = validated_data.get('op_cnt', instance.op_cnt)
        # ventilator_duration
        instance.head_injury_check = validated_data.get('head_injury_check', instance.head_injury_check)
        # instance.pre_admit_coma = validated_data.get('pre_admit_coma', instance.pre_admit_coma)
        # instance.post_admit_coma = validated_data.get('post_admit_coma', instance.post_admit_coma)
        # CU_usage
        # transfusion
        instance.special_care_days = validated_data.get('special_care_days', instance.special_care_days)
        print('validated_data[l1_care_days]:', validated_data['l1_care_days'])
        instance.l1_care_days = validated_data.get('l1_care_days', instance.l1_care_days)
        print('l1_care_days changed to:',instance.l1_care_days)
        instance.l2_care_days = validated_data.get('l2_care_days', instance.l2_care_days)
        instance.l3_care_days = validated_data.get('l3_care_days', instance.l3_care_days)
        instance.release_type = validated_data.get('release_type', instance.release_type)
        instance.accept_hosp_2 = validated_data.get('accept_hosp_2', instance.accept_hosp_2)
        instance.accept_hosp_3 = validated_data.get('accept_hosp_3', instance.accept_hosp_3)
        instance.cont_hosp_check = validated_data.get('cont_hosp_check', instance.cont_hosp_check)
        instance.cont_hosp_plan = validated_data.get('cont_hosp_plan', instance.cont_hosp_plan)
        
        instance.physician_name = validated_data.get('physician_name', instance.physician_name)
        instance.physician_code = validated_data.get('physician_code', instance.physician_code)
        instance.nurse_ic_name = validated_data.get('nurse_ic_name', instance.nurse_ic_name)
        instance.nurse_ic_code = validated_data.get('nurse_ic_code', instance.nurse_ic_code)
        instance.biz_sn = validated_data.get('biz_sn', instance.biz_sn)
        instance.bill_code = validated_data.get('bill_code', instance.bill_code)
        instance.bill_num = validated_data.get('bill_num', instance.bill_num)
        instance.settle_duration = validated_data.get('settle_duration', instance.settle_duration)

        instance.insurance_pay = validated_data.get('insurance_pay', instance.insurance_pay)
        instance.staff_subsidy = validated_data.get('staff_subsidy', instance.staff_subsidy)
        instance.residence_insurance = validated_data.get('residence_insurance', instance.residence_insurance)
        instance.public_servant_subsidy = validated_data.get('public_servant_subsidy', instance.public_servant_subsidy)
        instance.health_aid_pay = validated_data.get('health_aid_pay', instance.health_aid_pay)
        instance.enterprise_supp = validated_data.get('enterprise_supp', instance.enterprise_supp)
        instance.biz_insurance = validated_data.get('biz_insurance', instance.biz_insurance)
        instance.partial_self_purchase = validated_data.get('partial_self_purchase', instance.partial_self_purchase)
        instance.self_purchase = validated_data.get('self_purchase', instance.self_purchase)
        instance.account_pay = validated_data.get('account_pay', instance.account_pay)
        instance.cash_pay = validated_data.get('cash_pay', instance.cash_pay)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.designated_med_report_unit = validated_data.get('designated_med_report_unit', instance.designated_med_report_unit)
        instance.designated_med_report_person = validated_data.get('designated_med_report_person', instance.designated_med_report_person)
        instance.health_insurance_org = validated_data.get('health_insurance_org', instance.health_insurance_org)
        instance.health_insurance_org_code = validated_data.get('health_insurance_org_code', instance.health_insurance_org_code)
        instance.health_insurance_person = validated_data.get('health_insurance_person', instance.health_insurance_person)
        instance.health_insurance_person_code = validated_data.get('health_insurance_person_code', instance.health_insurance_person_code)

        # diag_info
        diag_infos_data = None
        DiagInfo.objects.filter(settlement=instance).delete() # 如果更新一个空DiagInfo会出问题吗？
        if 'diag_info' in validated_data.keys():
            print('there is diag_info')
            diag_infos_data = validated_data.pop('diag_info')
            for diag_info_data in diag_infos_data:
                DiagInfo.objects.create(settlement=instance, **diag_info_data)
        else:
            print('there is no diag_info')


        # western_release
        western_release_data = None
        main_diag_data = None
        other_diags_data = None
        traditional_release_data = None
        main_disease_data = None
        main_symps_data = None
        WesternRelease.objects.filter(settlement=instance).delete()
        TraditionalRelease.objects.filter(settlement=instance).delete()
        # western release
        if 'western_release' in validated_data.keys():
            print('there is western_release')
            western_release_data = validated_data['western_release']
            western_release = WesternRelease.objects.create(settlement=instance)
            print('western_release_data:',western_release_data)
            main_diag_data = western_release_data['main_diag']
            print('main_diag_data:',main_diag_data)
            main_diag = MainDiag.objects.create(western_release=western_release, **main_diag_data)
            print('created main_diag:',main_diag)
            if 'other_diags' in western_release_data.keys():
                other_diags_data = western_release_data['other_diags']
                print('other_diags_data:',other_diags_data)
                for other_diag_data in other_diags_data:
                    OtherDiag.objects.create(western_release=western_release, **other_diag_data) # 如果没有，前端改[]
            western_release.save()
        else:
            print('there is no western_release')
        # if western_release_data:
        #     western_release = WesternRelease.objects.create(settlement=settlement)
        #     if main_diag_data:
        #         MainDiag.objects.create(western_release=western_release, **main_diag_data)
        #     if other_diags_data:
        #         for other_diag_data in other_diags_data:
        #             OtherDiag.objects.create(western_release=western_release, **other_diag_data)
        # traditional_release
        if 'traditional_release' in validated_data.keys():
            print('there is traditional_lease')
            traditional_release_data = validated_data.pop('traditional_release')
            traditional_release = TraditionalRelease.objects.create(settlement=instance)
            print('traditional_release_data:',traditional_release_data)
            main_disease_data = traditional_release_data['main_disease']
            MainDisease.objects.create(traditional_release=traditional_release, **main_disease_data)
            if 'main_symps' in traditional_release_data.keys():
                main_symps_data = traditional_release_data['main_symps']
                for main_symp_data in main_symps_data:
                    MainSymp.objects.create(traditional_release=traditional_release, **main_symp_data)
        else:
            print('there is no traditional_release')
        # if traditional_release_data:
        #     traditional_release = TraditionalRelease.objects.create(settlement=settlement)
        #     if main_disease_data:
        #         MainDisease.objects.create(traditional_release=traditional_release, **main_disease_data)
        #     if main_symps_data:
        #         for main_symp_data in main_symps_data:
        #             MainSymp.objects.create(traditional_release=traditional_release, **main_symp_data)

        # main_ops
        main_ops_data = validated_data.pop('main_ops')
        MainOp.objects.filter(settlement=instance).delete()
        for main_op_data in main_ops_data:
            MainOp.objects.create(settlement=instance, **main_op_data)
        # other_ops
        other_ops_data = validated_data.pop('other_ops')
        OtherOp.objects.filter(settlement=instance).delete()
        for other_op_data in other_ops_data:
            OtherOp.objects.create(settlement=instance, **other_op_data)
        # ventilator_duration
        ventilator_duration_data = validated_data.pop('ventilator_duration')
        ventilator_duration = instance.ventilator_duration
        ventilator_duration.days = ventilator_duration_data.get('days', ventilator_duration.days)
        ventilator_duration.hrs = ventilator_duration_data.get('hrs', ventilator_duration.hrs)
        ventilator_duration.mins = ventilator_duration_data.get('mins', ventilator_duration.mins)
        ventilator_duration.save()

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
        # CU_usage
        CU_usages_data = validated_data.pop('CU_usage')
        CUUsage.objects.filter(settlement=instance).delete()
        for CU_usage_data in CU_usages_data:
            print('a CU_usage_data:', CU_usage_data)
            CUUsage.objects.create(settlement=instance, **CU_usage_data)
        # transfusion
        transfusions_data = validated_data.pop('transfusion')
        Transfusion.objects.filter(settlement=instance).delete()
        for transfusion_data in transfusions_data:
            Transfusion.objects.create(settlement=instance, **transfusion_data)
        
        # newborn_admit_type
        # newborn_admit_types_data = validated_data.pop('newborn_admit_type')
        # NewBornAdmitType.objects.filter(settlement=instance).delete()
        # for newborn_admit_type_data in newborn_admit_types_data:
        #     NewBornAdmitType.objects.create(settlement=instance, **newborn_admit_type_data)

        # bed_fee
        bed_fee_data = validated_data.pop('bed_fee')
        bed_fee = instance.bed_fee
        bed_fee.amount = bed_fee_data.get('amount', bed_fee.amount)
        bed_fee.A = bed_fee_data.get('A', bed_fee.A)
        bed_fee.B = bed_fee_data.get('B', bed_fee.B)
        bed_fee.self_pay = bed_fee_data.get('self_pay', bed_fee.self_pay)
        bed_fee.other = bed_fee_data.get('other', bed_fee.other)
        bed_fee.save()
        # diag_fee
        diag_fee_data = validated_data.pop('diag_fee')
        diag_fee = instance.diag_fee
        diag_fee.amount = diag_fee_data.get('amount', diag_fee.amount)
        diag_fee.A = diag_fee_data.get('A', diag_fee.A)
        diag_fee.B = diag_fee_data.get('B', diag_fee.B)
        diag_fee.self_pay = diag_fee_data.get('self_pay', diag_fee.self_pay)
        diag_fee.other = diag_fee_data.get('other', diag_fee.other)
        diag_fee.save()
        # exam_fee
        exam_fee_data = validated_data.pop('exam_fee')
        exam_fee = instance.exam_fee
        exam_fee.amount = exam_fee_data.get('amount', exam_fee.amount)
        exam_fee.A = exam_fee_data.get('A', exam_fee.A)
        exam_fee.B = exam_fee_data.get('B', exam_fee.B)
        exam_fee.self_pay = exam_fee_data.get('self_pay', exam_fee.self_pay)
        exam_fee.other = exam_fee_data.get('other', exam_fee.other)
        exam_fee.save()
        # lab_test_fee
        lab_test_fee_data = validated_data.pop('lab_test_fee')
        lab_test_fee = instance.lab_test_fee
        lab_test_fee.amount = lab_test_fee_data.get('amount', lab_test_fee.amount)
        lab_test_fee.A = lab_test_fee_data.get('A', lab_test_fee.A)
        lab_test_fee.B = lab_test_fee_data.get('B', lab_test_fee.B)
        lab_test_fee.self_pay = lab_test_fee_data.get('self_pay', lab_test_fee.self_pay)
        lab_test_fee.other = lab_test_fee_data.get('other', lab_test_fee.other)
        lab_test_fee.save()
        # treat_fee
        treat_fee_data = validated_data.pop('treat_fee')
        treat_fee = instance.treat_fee
        treat_fee.amount = treat_fee_data.get('amount', treat_fee.amount)
        treat_fee.A = treat_fee_data.get('A', treat_fee.A)
        treat_fee.B = treat_fee_data.get('B', treat_fee.B)
        treat_fee.self_pay = treat_fee_data.get('self_pay', treat_fee.self_pay)
        treat_fee.other = treat_fee_data.get('other', treat_fee.other)
        treat_fee.save()
        # op_fee
        op_fee_data = validated_data.pop('op_fee')
        op_fee = instance.op_fee
        op_fee.amount = op_fee_data.get('amount', op_fee.amount)
        op_fee.A = op_fee_data.get('A', op_fee.A)
        op_fee.B = op_fee_data.get('B', op_fee.B)
        op_fee.self_pay = op_fee_data.get('self_pay', op_fee.self_pay)
        op_fee.other = op_fee_data.get('other', op_fee.other)
        op_fee.save()
        # nursing_fee
        nursing_fee_data = validated_data.pop('nursing_fee')
        nursing_fee = instance.nursing_fee
        nursing_fee.amount = nursing_fee_data.get('amount', nursing_fee.amount)
        nursing_fee.A = nursing_fee_data.get('A', nursing_fee.A)
        nursing_fee.B = nursing_fee_data.get('B', nursing_fee.B)
        nursing_fee.self_pay = nursing_fee_data.get('self_pay', nursing_fee.self_pay)
        nursing_fee.other = nursing_fee_data.get('other', nursing_fee.other)
        nursing_fee.save()
        # med_material_fee
        med_material_fee_data = validated_data.pop('med_material_fee')
        med_material_fee = instance.med_material_fee
        med_material_fee.amount = med_material_fee_data.get('amount', med_material_fee.amount)
        med_material_fee.A = med_material_fee_data.get('A', med_material_fee.A)
        med_material_fee.B = med_material_fee_data.get('B', med_material_fee.B)
        med_material_fee.self_pay = med_material_fee_data.get('self_pay', med_material_fee.self_pay)
        med_material_fee.other = med_material_fee_data.get('other', med_material_fee.other)
        med_material_fee.save()
        # western_med_fee
        western_med_fee_data = validated_data.pop('western_med_fee')
        western_med_fee = instance.western_med_fee
        western_med_fee.amount = western_med_fee_data.get('amount', western_med_fee.amount)
        western_med_fee.A = western_med_fee_data.get('A', western_med_fee.A)
        western_med_fee.B = western_med_fee_data.get('B', western_med_fee.B)
        western_med_fee.self_pay = western_med_fee_data.get('self_pay', western_med_fee.self_pay)
        western_med_fee.other = western_med_fee_data.get('other', western_med_fee.other)
        western_med_fee.save()
        # traditional_tablet_fee
        traditional_tablet_fee_data = validated_data.pop('traditional_tablet_fee')
        traditional_tablet_fee = instance.traditional_tablet_fee
        traditional_tablet_fee.amount = traditional_tablet_fee_data.get('amount', traditional_tablet_fee.amount)
        traditional_tablet_fee.A = traditional_tablet_fee_data.get('A', traditional_tablet_fee.A)
        traditional_tablet_fee.B = traditional_tablet_fee_data.get('B', traditional_tablet_fee.B)
        traditional_tablet_fee.self_pay = traditional_tablet_fee_data.get('self_pay', traditional_tablet_fee.self_pay)
        traditional_tablet_fee.other = traditional_tablet_fee_data.get('other', traditional_tablet_fee.other)
        traditional_tablet_fee.save()
        # traditional_patent_fee
        traditional_patent_fee_data = validated_data.pop('traditional_patent_fee')
        traditional_patent_fee = instance.traditional_patent_fee
        traditional_patent_fee.amount = traditional_patent_fee_data.get('amount', traditional_patent_fee.amount)
        traditional_patent_fee.A = traditional_patent_fee_data.get('A', traditional_patent_fee.A)
        traditional_patent_fee.B = traditional_patent_fee_data.get('B', traditional_patent_fee.B)
        traditional_patent_fee.self_pay = traditional_patent_fee_data.get('self_pay', traditional_patent_fee.self_pay)
        traditional_patent_fee.other = traditional_patent_fee_data.get('other', traditional_patent_fee.other)
        traditional_patent_fee.save()
        # general_diag_fee
        general_diag_fee_data = validated_data.pop('general_diag_fee')
        general_diag_fee = instance.general_diag_fee
        general_diag_fee.amount = general_diag_fee_data.get('amount', general_diag_fee.amount)
        general_diag_fee.A = general_diag_fee_data.get('A', general_diag_fee.A)
        general_diag_fee.B = general_diag_fee_data.get('B', general_diag_fee.B)
        general_diag_fee.self_pay = general_diag_fee_data.get('self_pay', general_diag_fee.self_pay)
        general_diag_fee.other = general_diag_fee_data.get('other', general_diag_fee.other)
        general_diag_fee.save()
        # registration_fee
        registration_fee_data = validated_data.pop('registration_fee')
        registration_fee = instance.registration_fee
        registration_fee.amount = registration_fee_data.get('amount', registration_fee.amount)
        registration_fee.A = registration_fee_data.get('A', registration_fee.A)
        registration_fee.B = registration_fee_data.get('B', registration_fee.B)
        registration_fee.self_pay = registration_fee_data.get('self_pay', registration_fee.self_pay)
        registration_fee.other = registration_fee_data.get('other', registration_fee.other)
        registration_fee.save()
        # other_fee
        other_fee_data = validated_data.pop('other_fee')
        other_fee = instance.other_fee
        other_fee.amount = other_fee_data.get('amount', other_fee.amount)
        other_fee.A = other_fee_data.get('A', other_fee.A)
        other_fee.B = other_fee_data.get('B', other_fee.B)
        other_fee.self_pay = other_fee_data.get('self_pay', other_fee.self_pay)
        other_fee.other = other_fee_data.get('other', other_fee.other)
        other_fee.save()
        # special_fee
        special_fee_data = validated_data.pop('special_fee')
        special_fee = instance.special_fee
        special_fee.amount = special_fee_data.get('amount', special_fee.amount)
        special_fee.A = special_fee_data.get('A', special_fee.A)
        special_fee.B = special_fee_data.get('B', special_fee.B)
        special_fee.self_pay = special_fee_data.get('self_pay', special_fee.self_pay)
        special_fee.other = special_fee_data.get('other', special_fee.other)
        special_fee.save()
        # total_fee
        total_fee_data = validated_data.pop('total_fee')
        total_fee = instance.total_fee
        total_fee.amount = total_fee_data.get('amount', total_fee.amount)
        total_fee.A = total_fee_data.get('A', total_fee.A)
        total_fee.B = total_fee_data.get('B', total_fee.B)
        total_fee.self_pay = total_fee_data.get('self_pay', total_fee.self_pay)
        total_fee.other = total_fee_data.get('other', total_fee.other)
        total_fee.save()

        instance.save()
        return instance

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        print('ret:',ret)
        # ret['username'] = ret['username'].lower()
        return ret
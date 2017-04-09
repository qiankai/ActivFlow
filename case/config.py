from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from models import CaseBaseInfo


content_type = ContentType.objects.get_for_model(CaseBaseInfo)

Permission.objects.create(codename='CAN_SE_CASE_CONFIRM',name='se confirm case',content_type=content_type)
Permission.objects.create(codename='CAN_SALE_OPEN_CASE',name='sales open case',content_type=content_type)
Permission.objects.create(codename='CAN_OPEN_CASE',name='approve open case',content_type=content_type)

# -*- coding: utf-8 -*-
#

from django.urls import path
from rest_framework_bulk.routes import BulkRouter

from .. import api


app_name = 'orgs'
router = BulkRouter()

router.register(r'orgs', api.OrgViewSet, 'org')
router.register(r'org-member-relation', api.OrgMemberRelationBulkViewSet, 'org-member-relation')

urlpatterns = [
    path('orgs/current/', api.CurrentOrgDetailApi.as_view(), name='current-org-detail'),
]

urlpatterns += router.urls

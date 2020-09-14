from rest_framework import pagination
from django.conf import settings

class MythCasterPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = settings.REST_FRAMEWORK.get('MAX_PAGE_SIZE', 1000)

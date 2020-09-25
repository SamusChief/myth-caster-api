""" Settings for the Django Rest Framework """
REST_FRAMEWORK = {
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'common.paginators.MythCasterPagination',
    'PAGE_SIZE': 100,
    'MAX_PAGE_SIZE': 1000,
    # Filtering, General Search, Ordering
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'common.permissions.IsOwnerOrEditor'
    ]
}

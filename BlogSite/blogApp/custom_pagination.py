from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'items_per_page'
    page_query_param = 'page'
    max_page_size = 100  # Default maximum page size

    def get_page_size(self, request):
        """
        Get the number of items per page from the request query parameters.
        """
        return int(request.query_params.get(self.page_size_query_param, self.max_page_size))

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset according to the custom pagination parameters.
        """
        self.page_size = self.get_page_size(request)

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        """
        Return a paginated-style response with custom pagination metadata.
        """
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()

        return Response({
            'pagination': {
                'next': next_url,
                'previous': previous_url,
                'count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
                'current_page': self.page.number,
                'results': data,
            }
        })

import pytest

from data_engineering.common.views.base import PaginatedListView


def test_paginated_list_view_get_fields_required(app_with_db):
    with app_with_db.test_request_context():
        with pytest.raises(NotImplementedError):
            PaginatedListView().dispatch_request()

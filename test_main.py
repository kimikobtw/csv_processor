import pytest
from main import filter_data, aggregate_data

@pytest.fixture
def sample_data():
    return [
        {'name': 'iphone', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
    ]

def test_filter(sample_data):
    assert len(filter_data(sample_data, 'brand=apple')) == 1

def test_aggregate(sample_data):
    assert aggregate_data(sample_data, 'rating=avg')['avg'] == 4.85
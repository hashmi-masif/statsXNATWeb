import pytest
from src import check_network, dataFormatter

data_formatter = dataFormatter.Formatter()

def test_stats():

    # If connected to network then should return a list
    data = data_formatter.stats()

    if(check_network.connect()):
        assert type(data) == list
        assert len(data) == 9
    else:
        assert data == None
import pytest
from statsXNAT import dataFetcher, check_network

data_fetcher = dataFetcher.Fetcher('testUser', 'testPassword', 'https://central.xnat.org')    # Object of the Fetcher class


def test_get_projects():

    out = data_fetcher.get_projects()
    if(check_network.connect()):
        assert str(type(out)) == "<class 'pyxnat.core.jsonutil.JsonTable'>"
    else:
        assert out == None


def test_get_subjects():

    out = data_fetcher.get_subjects()
    if(check_network.connect()):
        assert str(type(out)) == "<class 'pyxnat.core.jsonutil.JsonTable'>"
    else:
        assert out == None


def test_get_experiments():

    out = data_fetcher.get_experiments()
    if(check_network.connect()):
        assert str(type(out)) == "<class 'pyxnat.core.jsonutil.JsonTable'>"
    else:
        assert out == None
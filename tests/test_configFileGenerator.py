import pytest
from src import configFileGenerator, check_network
import os.path

config_object = configFileGenerator.ConfigFileGenerator()

# Function for testing the name and password entered 
def test_name_and_pass():

    data = config_object.name_and_pass('testUser','testPassword')

    assert config_object.name == 'testUser'
    assert config_object.password == 'testPassword'

    if(check_network.connect()):
        assert type(data) == list
    else:
        assert out == None

# Function for testing the file generated is present in
# correct location with expected name
def test_generator():

    # config_object have the attributes from the above test function
    # thus config_object will use those attributes to generate the file
    data = config_object.generator()  

    if(check_network.connect()):
        assert type(data) == list
    else:
        assert out == None

    assert os.path.exists('../ConfigFile/central.cfg')

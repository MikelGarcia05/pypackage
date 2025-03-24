# package imports
from samplemod.module import Human


def test_human():
    jon_snow = Human(name="Jon Snow el nieves")
    assert isinstance(jon_snow, Human) == True

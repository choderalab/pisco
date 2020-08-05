import pytest


def test_ported_function():
    import pisco
    import os
    from pisco.data.utils.protein_net_parser import read_records
    from pisco.data.utils.protein_net_parser_to_raw import read_record
    f_handle = open(
        os.path.dirname(pisco.data.__file__) + '/protein_net_example.txt',
        'r',
    )

    _dict = read_record(
        f_handle,
        20,
    )

    assert isinstance(_dict, dict)

def test_import():
    import pisco
    pisco.data.datasets

@pytest.fixture
def example_ds():
    import pisco
    ds = pisco.data.collections.protein_net_example()
    return ds

def test_protein_net_example_init(example_ds):
    example_ds

def test_protein_net_example_iter(example_ds):
    list(example_ds)

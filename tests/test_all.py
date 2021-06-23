from AutocadProject.utils import files


def test_open_dxf():
    assert type(files.open_dxf_file()) == list

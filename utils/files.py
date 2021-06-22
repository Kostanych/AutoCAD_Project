import comtypes.client


def open_dxf_file(filename="testfile") -> list:
    """
    Opens DXF file by given name.
    :param filename: name of DXF file
    :return: list with all drawing data
    """
    dxf_file = open(filename + '.dxf', 'r')
    dxf = list(dxf_file)
    dxf_file.close()

    # we can cut \n if we need
    # dxf = [st.rstrip() for st in dxf]
    return dxf


def make_dxf_file(activedoc, filename: str = "testfile"):
    """
    Makes DXF file.
    :param activedoc:
    :param filename: name of DXF file
    :return: none
    """
    filename = filename
    sset = activedoc.SelectionSets.Add('SSET')
    activedoc.Export(filename, 'DXF', sset)

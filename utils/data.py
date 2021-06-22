from traceback import print_exc

import pandas as pd


def get_dim_info(dxf: list):
    """
    Extracts dimensions data from a dxf file.

    :param dxf: list with data from DXF file
    :return: Dataframes with all dimensions data
    """
    # Looking for lines in dxf file containing dimensions data
    entities, dimensions = [], []
    for i, element in enumerate(dxf):
        # Number of entities in dxf file
        if element == 'AcDbEntity\n':
            entities.append(i)
        # Number of dimensions in dxf file
        elif element == 'AcDbDimension\n':
            dimensions.append(i + 1)
    print(f'Objects at the drawing: {len(entities)}\n Dimensions : {len(dimensions)}')

    df_dimensions = pd.DataFrame()

    # Extracting data from dxf
    start_X, end_X, start_Y, end_Y, text_X, text_Y, dim_line_X, dim_line_Y = '', '', '', '', '', '', '', ''
    try:
        for ent in dimensions:
            # print('Dimension data:')
            for pos, line in enumerate(dxf[ent:]):
                if line == ' 13\n':
                    start_X = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'1st point X : {dxf[ent+pos+1]}')
                elif line == ' 23\n':
                    end_X = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'1st point Y : {dxf[ent+pos+1]}')
                elif line == ' 14\n':
                    start_Y = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'2nd point X : {dxf[ent+pos+1]}')
                elif line == ' 24\n':
                    end_Y = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'2nd point Y: {dxf[ent+pos+1]}')
                elif line == ' 11\n':
                    text_X = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'Text coord X: {dxf[ent+pos+1]}')
                elif line == ' 21\n':
                    text_Y = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'Text coord Y: {dxf[ent+pos+1]}')
                elif line == ' 10\n':
                    dim_line_X = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'Dimension line X: {dxf[ent+pos+1]}')
                elif line == ' 20\n':
                    dim_line_Y = float((dxf[ent + pos + 1]).rstrip())
                    # print(f'Dimension line Y: {dxf[ent+pos+1]}')

                elif (dxf[ent + pos] == 'AcDbEntity\n') or (dxf[ent + pos] == 'ENDSEC\n'):
                    break
            df_dimensions = df_dimensions.append({'start_X': start_X, 'end_X': end_X,
                                                  'start_Y': start_Y, 'end_Y': end_Y,
                                                  'text_X': text_X, 'text_Y': text_Y,
                                                  'dim_line_X': dim_line_X, 'dim_line_Y': dim_line_Y},
                                                 ignore_index=True)
            df_dimensions = df_dimensions[['start_X', 'end_X', 'start_Y', 'end_Y',
                                           'text_X', 'text_Y', 'dim_line_X', 'dim_line_Y']]

    except Exception as e:
        print_exc()
    return df_dimensions, entities, dimensions

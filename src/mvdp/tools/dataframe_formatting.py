from pandas import DataFrame


def fill_tree_dataframe(dataframe: DataFrame):
    """
    fills the missing entries from the previous ones
    :param: parameters: dataframe to fill
    :return: dataframe with full names
    """
    # create a dictionary to fill with data
    fill_table = dict()
    # each key represents a dataframe column
    for attr in list(dataframe):
        fill_table[attr] = list()
    # fill the dictionary with data
    for index, row in dataframe.iterrows():
        for attr in list(dataframe):
            table_entry = row[attr]
            if table_entry == '-':  # missing entry
                # copy the last filled value for the attribute
                table_entry = fill_table[attr][-1]
            fill_table[attr].append(table_entry)
    return DataFrame.from_dict(fill_table)


def reformat_parameters(parameters: DataFrame):
    """
    prepares the parameters dataframe for the uploading
    :return: dataframe with 2 columns:
        'Parameter': tree structured parameter names
        'ParValue': values for the parameters
    """
    # check if parameters have already been reformatted
    par_columns = list(parameters.columns)
    if len(par_columns) == 2 and 'Parameter' in par_columns and 'ParValue' in par_columns:
        return parameters

    # get rid of the tree structure
    parameters = fill_tree_dataframe(parameters)

    # unite parameters to tree parameters
    tree_parameters = {
        "Parameter": [],
        "ParValue": []
    }
    for index, row in parameters.iterrows():
        merged_param = ""
        for attr in list(parameters):
            if attr == 'Value':
                tree_parameters['ParValue'].append(row[attr])
            else:  # one of the parameters, that have to be merged
                merged_param += "::" + row[attr]
        tree_parameters['Parameter'].append(merged_param)
    return DataFrame.from_dict(tree_parameters)


from fastiot.msg.thing import Thing


class TableThing(Thing):
    """ Data model wrapper for Thing. Additionaly saves dataframes configuration """
    df_type: str
    """ Type of dataframe from an experiment table """
    df_index: int
    """ Dataframe index, which enables dataframe reconstruction """


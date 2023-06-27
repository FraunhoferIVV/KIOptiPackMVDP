from typing import Union

import pandas as pd
import requests as rq


class DataSpaceDownloader:
    """ Helper to access assets provided by the data provider service of the MVDP

    You may use the tool like the following:

    >>> loader = DataSpaceDownloader("http://motiv.kioptipack.ivv-dd.fhg.de/data_provider")
    >>> asset = loader.get_asset_as_df("Full")
    """

    def __init__(self, url):
        """

        :param url: URL of the server, should usually start with http:// and end before the last /
        """
        self.url_ = url

    def _retrieve_asset(self, asset_name) -> rq.Response:
        """ Actual retrieving. May be extended later… """
        source = self.url_ + '/assets/' + asset_name
        response = rq.get(source)

        if response.status_code != 200:
            raise RuntimeError(f"Could not fetch data, got error code {response.status_code} and "
                               f"message `{response.text}`.")

        return response

    def get_asset_as_df(self, asset_name: str) -> pd.DataFrame:
        """
        Retrieves an asset from the data provider as DataFrame

        :param asset_name: Name of the asset to retrieve
        :return: DataFrame with the asset values if asset is formatted in proper record style
        """
        response = self._retrieve_asset(asset_name)
        return pd.read_json(response.text, orient='records')

    def get_asset_as_raw_json(self, asset_name) -> str:
        """ Returns the named asset as raw string to be evaluated later """

        return self._retrieve_asset(asset_name).text

    def get_asset_as_json(self, asset_name, **kwargs) -> Union[list, dict]:
        """ Return the named asset as python primitives convert from the json document

        You may provide additional keyword arguments to passed to :func:`json.load`.
        See the official documentation at https://docs.python.org/3/library/json.html#json.load for explanation.
        """
        return self._retrieve_asset(asset_name).json(**kwargs)

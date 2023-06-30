import unittest

from mvdp.data_space_downloader.data_space_downloader import DataSpaceDownloader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        loader = DataSpaceDownloader("http://motiv.kioptipack.ivv-dd.fhg.de/data_provider")
        asset = loader.get_asset_as_df("Full")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

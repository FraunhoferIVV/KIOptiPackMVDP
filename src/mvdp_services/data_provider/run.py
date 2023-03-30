import logging

from mvdp_services.data_provider.data_provider_service import DataProviderService

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    DataProviderService.main()



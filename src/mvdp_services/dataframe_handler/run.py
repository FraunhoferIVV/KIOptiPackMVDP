import logging

from mvdp_services.dataframe_handler.dataframe_handler_service import DataframeHandlerService

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    DataframeHandlerService.main()

import logging
from mvdp_services.frontend.frontend_service import FrontendService

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    FrontendService.main()

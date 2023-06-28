#!/bin/bash

if [[ ! -d "${PWD}/src" ]]; then
  echo "You must start this script from the project root, so that 'misc/create_management_api_client.sh' is working!"
  exit 1
fi

docker run --rm -v "${PWD}:/local" \
         openapitools/openapi-generator-cli generate \
           -i /local/misc/management-api.yml -g python  -o /local/src --skip-validate-spec \
           --additional-properties "library=asyncio,packageName=mvdp.edc_management_client,generateSourceCodeOnly=true"

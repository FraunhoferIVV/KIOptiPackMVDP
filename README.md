# Minimum viable data space participant (MVDP) for project »KIOptiPack«

This repository is part of the project »KIOptipack« sponsored by the German Federal Ministry for Economic Affairs and 
Climate Action.
The project goal is to provide and apply digital tools with artificial intelligence to the whole chain of plastic 
recycling from granules to ready to use (consumer) packaging. You can find more about this project on the project’s 
website at https://ki-hub-kunststoffverpackungen.de/ki-opti-pack/

Scope of this repository to provide minium working examples to upload and share data in the common data space. 
The core connection between participants will be using the [Eclipse Data Space Connector](https://github.com/eclipse-edc).

<img style="display: inline"; height="84" src="https://ki-hub-kunststoffverpackungen.de/typo3conf/ext/gi_base/Resources/Themes/Dgt/Images/bundesministerium-logo_klein.jpg">
<img style="display: inline"; height="84" src="https://www.fona.de/cms/img/BMBF_FONA_Logo_de.svg">
<img style="display: inline"; height="84" src="https://ki-hub-kunststoffverpackungen.de/typo3conf/ext/gi_base/Resources/Themes/KiHubKunststoff/Images/KI-Logo-web.png">

## License

Copyright 2022 Fraunhofer IVV, Dresden and contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Repository structure

This project is based on the [FastIoT Framework](https://github.com/FraunhoferIVV/fastiot) and also uses some of its 
[core services](https://fastiot.readthedocs.io/en/latest/services.html#core-services)
Therefore it is recommended to have a short glimpse at the [FastIoT Documentation](https://fastiot.readthedocs.io/).

The project itself therefore also is conform to the [set FastIoT structure}(https://fastiot.readthedocs.io/en/latest/architecture/02-project-structure.html).

The code is located at [src](./src), where you find the [microservices](./src/mvdp_services), a very few 
[tests](./src/mvdp_tests) and a [library](./src/mvdp). 
The library may be installed in your projects for example to use the EDC REST Client or some tools to interact with 
the REST APIs provided by this service.

## Getting started

The code and especially the FastIoT Framework have only been tested on Linux systems so far, so no guarantee for any other os.
If you want to start the message broker for the service you must have Docker running on your system.

### Setup this project

1. Clone the repository (`git clone https://github.com/FraunhoferIVV/KIOptiPackMVDP.git`) and change into the new path (`cd KIOptiPackMVDP`)
2. Create a virtual environment (`python -m venv venv`) using at least Python 3.9 and activate it (`source venv/bin/activate`)
3. Install all required packages with `pip install -r requirements/requirements.all.txt`. 
   This will make working easier than just the minimal packages in `requirements.txt`.
4. To build the services install FastIoT in developer mode: `pip install fastiot[dev]`.
5. When working with PyCharm set the `src`-Directory as "Sources Root" (Right click on the the src-directory and close the bottom select "mark as -> Sources Root")

### Build FastIoT core services

To spin up all services it is recommended to have access to the FastIoT Services either a docker registry or simply locally on your computer:
1. Clone FastIoT to your computer (`git clone https://github.com/FraunhoferIVV/fastiot.git`) and change it this path (`cd fastiot`)
2. Create a virtual environment (`python -m venv venv`) using at least Python 3.9 and activate it (`source venv/bin/activate`)
3. Install the needed requirements with `pip install -r requirements/requirements.dev.txt`
4. Add the `src`-directory to your Python search path: `export PYTHONPATH="$(pwd)/src:$PYTHONPATH"`
5. Build the provided services to have them available locally: `bin/fiot build`

### Spinning up local deployments and services

Within the command line for this project you may start everything needed using the deployment `integration_test`.

1. Generate the docker-compose file and the configuration using `fiot config integration_test` 
   Hint: When leaving out the `integration_test` it will create configurations for all services. 
2. Run `fiot start integration_test` to start the infrastructure services and some FastIoT core services build in the previous section.

You now have a nats.io message broker for the services to interact. A MongoDB can store data (for integration test deployment only in a Ramdisk!).
The ObjectStorage Service stores data arriving via the message broker in the database.
The nats_logger will simply print out message going over the broker to help you debugging and see something :-)

You can now start any service using its `run.py` or the `xx_service.py` file.
It will read all environment variables from the integration test deployment and thus easily connect to broker, database and co.

ENJOY!
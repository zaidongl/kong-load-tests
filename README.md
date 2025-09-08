# Kong AI Gateway Load Tests
This repository contains load tests for Kong AI Gateway using Locust. It includes a mock LLM server to simulate LLM responses and Locust test scripts to perform load testing on the gateway and the mock LLM server directly.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Load Test Components](#load-test-components)
- [Build docker image on local machine](#build-docker-image-on-local-machine)
- [Run components using Docker](#run-components-using-docker)
- [Configure Kong AI Gateway for Load Testing](#configure-kong-ai-gateway-for-load-testing)
- [Running Load Tests](#running-load-tests)
- [Example Load Test Scenarios](#example-load-test-scenarios)

## Prerequisites
- Docker Desktop installed on your local machine
- Kong AI Gateway instance (can be a trial version https://cloud.konghq.com/us/gateway-manager/)
- Basic knowledge of Docker and Locust
- Familiarity with Kong AI Gateway configuration

## Load Test Components
1. **mock-llm**: A mock LLM server that simulates responses from a real LLM. It is built using Openresty and Lua.
2. **locust-tests**: Locust test scripts that define user behavior for load testing the Kong AI Gateway and the mock LLM server directly.
3. **kong-ai-gateway**: The Kong AI Gateway instance that will be tested.

## Build docker image on local machine
<h3> mock-llm: </h3>

```bash
cd mock_llm
docker build -t kong-load-tests/mock-llm:latest .
```

<h3> locust-tests: </h3>

```bash
cd locust_tests
docker build -t kong-load-tests/locust-tests:latest .
```

## Run components using Docker

<h3>1. Create a custom network for the containers to communicate</h3>
```bash
docker network create mynet
```

<h3>2. Run mock-llm: </h3>
```bash
docker run --network mynet --name mock-llm -p 8080:8080 kong-load-tests/mock_llm:latest
```

<h3>3. Run ai-gateway: </h3>
* Go to https://cloud.konghq.com/us/gateway-manager/
* Go to control plane (Create one if you don't have)
* Configure a data plane node
* copy the docker run command line and add arguments "--network mynet --name ai-gateway" after "docker run"
* Run the command line in your terminal to create the kong ai-gateway container

<h3>4. Run locust-tests: </h3>

Locust web UI for gateway will be available at http://localhost:8089
```bash
docker run --network mynet --name gateway-locust -p 8089:8089 kong-load-tests/locust-tests:latest "-f /home/locust/locustfiles/gateway_user.py"
```

Locust web UI for direct mock LLM will be available at http://localhost:8090
```bash
docker run --network mynet --name direct-mock-locust -p 8090:8089 kong-load-tests/locust-tests:latest "-f /home/locust/locustfiles/direct_llm_mock_user.py"
```

## Configure Kong AI Gateway for Load Testing
1. Log in to your Kong AI Gateway instance.
2. Create a new Service with routes and plugins defined in json files in the `kong-ai-gateway` folder.

## Running Load Tests
### Load Test against Gateway
1. Open the Locust web UI for the gateway at http://localhost:8089 for load tests against gateway.
2. Enter the number of users to simulate and the spawn rate.
3. Enter "http://kong-ai-gateway:8000" as the host URL.
4. Start the test and monitor the results.

### Load Test against Mock LLM Directly
1. Open the Locust web UI for the gateway at http://localhost:8090 for load tests against mock llm directly.
2. Enter the number of users to simulate and the spawn rate.
3. Enter "http://mock-llm:8000" as the host URL.
4. Start the test and monitor the results.

## Example Load Test Scenarios
### 1000 users sending requests to the Kong AI Gateway with a spawn rate of 10 users per second.
<img src="docs/images/gateway-load-tests-1000 users-stats.png" alt="gateway_1000_users" width="600"/>
<br>
<img src="docs/images/gateway-load-tests-1000 users-chart.png" alt="gateway_1000_users" width="600"/>

### 1000 users sending requests to the LLM Mock with a spawn rate of 10 users per second.
<img src="docs/images/mock-llm-load-tests-1000 users-stats.png" alt="mock_llm_1000_users" width="600"/>


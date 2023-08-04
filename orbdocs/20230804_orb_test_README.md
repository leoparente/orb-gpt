# Integration Tests
This directory contains integration tests that can be run through the UI and/or API


Here's what you'll need to do in order to run these tests:
- Setup your python environment
- Configure the test settings
- Run behave

## Setup your Python environment

<b>You need to have python >= 3.8 installed</b> 

Create a virtual environment: `python3 -m venv name_of_virtualenv`

Activate your virtual environment: `source name_of_virtualenv/bin/activate`

Install the required libraries: `pip install -r requirements.txt`


Scenarios with @mocked_interface tag requires tcpreplay to replay PCAP files into mock interface. Open VSwitch is used to create a virtual switch that export Flow Metrics (Sflow/NetFlow/IPFIX). You can install it using the following command:

`sudo apt -y install tcpreplay openvswitch-switch openvswitch-common`

### Additional configuration of your Python environment for UI tests
- Install Google Chrome :
```
$ sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
$ sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
$ sudo apt-get -y update
$ sudo apt-get -y install google-chrome-stable
```

- Install ChromeDriver
```
$ wget https://chromedriver.storage.googleapis.com/$(google-chrome --product-version)/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/bin/chromedriver
$ sudo chown root:root /usr/bin/chromedriver
$ sudo chmod +x /usr/bin/chromedriver
```

## Test settings
Create the test config file from the template: `cp test_config.ini.tpl test_config.ini`.

Then fill in the correct values:

- **email**:
  - Mandatory!
  - Orb user's email
- **password**:
  - Mandatory!
  - Orb user's password
- **orb_address**:
  - Mandatory!
  - URL of the Orb deployment. Do NOT include the protocol (`https://`, `http://` or `mqtt://`).
- **prometheus_username**
  - Mandatory!
  - Your Grafana Cloud Prometheus username
- **prometheus_key**
  - Mandatory!
  - Your Grafana Cloud API Key. Be sure to grant the key a role with metrics push privileges
- **remote_prometheus_endpoint**
  - Mandatory!
  - base URL to send Prometheus metrics to Grafana Cloud> `(ex. prometheus-prod-10-prod-us-central-0.grafana.net)`
- **verify_ssl**:
  - Bool
  - When it is False, replaces HTTPS connections with HTTP and disables SSL certificate validation in MQTT connections.
  - Default value: `True`
- **is_credentials_registered**:
  - Bool
  - If false, register an account with credentials (email and password) used
  - Default value: `True`
- **agent_docker_image**:
  - Docker image of the orb agent.
  - Default value: `orbcommunity/orb-agent`
- **agent_docker_tag**:
  - Tag of the Orb agent docker image.
  - Default value: `latest`
- **orb_agent_interface**:
  - Network interface that will be used by pktvisor when running the Orb agent.
  - Default value: `mock`
- **headless**:
  - Bool
  - Referred to UI tests. If True, run chromedriver in headless mode
  - Default value: `true`
- **include_otel_env_var**:
  - Bool
  - If true, use the environmental variable "ORB_OTEL_ENABLE" on agent provisioning commands
  - Default value: `false`
- **enable_otel**:
  - Bool
  - Value to be used in variable "ORB_OTEL_ENABLE". Note that `include_otel_env_var` parameter must be `true` if this variable is true.
  - Default value: `true`
- **use_orb_live_address_pattern**:
  - Bool
  - If true, uses orb_address as base to api and mqtt address using orb.live pattern. If false, requires you to add the corresponding addresses.
  - Default value: `true`
- **backend_type**:
  - Str
  - Sink backend type
  - Default value: `prometheus`
- **orb_cloud_api_address**:
  - Required if `use_orb_live_address_pattern` is false
  - URL of the Orb deployment API. Obs: You MUST include the protocol.
- **orb_cloud_mqtt_address**:
  - Required if `use_orb_live_address_pattern` is false
  - URL of the Orb deployment mqtt. Obs: You MUST include the protocol and the port.


## List scenarios to be performed

You can easily check the scenarios that will be executed considering the chosen tag by executing dry-run.

For example, run the command below to check scenarios belonging to the smoke test suite:
> behavex -t=@smoke --dry-run

Run the command below to check scenarios belonging to the sanity test suite:
> behavex -t=@sanity --dry-run


## Run behave
Simply run `behave`, optionally passing the feature file as follows:

```sh
$ behave --include agentsProvider.feature
```
Output:
```text
@agents
Feature: agent provider # features/agentsProvider.feature:2
  Scenario: Provision agent                                                  # features/agentsProvider.feature:4
    Given that the user is logged in on orb account                                         # features/steps/users.py:10 1.031s
    When a new agent is created                                              # features/steps/control_plane_agents.py:18 1.032s
    And the agent container is started                                       # features/steps/local_agent.py:10 0.217s
    Then the agent status in Orb should be online                            # features/steps/control_plane_agents.py:24 2.556s
    And the container logs should contain the message "sending capabilities" # features/steps/local_agent.py:26 0.023s
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m4.858s

```

## Run behave using parallel process
 
You can use [behavex](https://github.com/hrcorval/behavex) to run the scenarios using multiprocess by simply run:

Examples:

> behavex -t @\<TAG\> --parallel-processes=2 --parallel-schema=scenario

> behavex -t @\<TAG\> --parallel-processes=5 --parallel-schema=feature

Running smoke tests:

> behavex -t=@smoke --parallel-processes=8 --parallel-scheme=scenario


## Test execution reports
[behavex](https://github.com/hrcorval/behavex) provides a friendly HTML test execution report that contains information related to test scenarios, execution status, execution evidence and metrics. A filters bar is also provided to filter scenarios by name, tag or status.

It should be available at the following path:

<output_folder>/report.html

## Clean your environment

After running the tests, clean up your environment by running the command:

> behavex -t=@cleanup --parallel-processes=10 --parallel-scheme=scenario

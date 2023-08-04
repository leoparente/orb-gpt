# orb-gpt

Built with [OpenAI](https://github.com/openai/openai-python), [LangChain](https://github.com/langchain-ai/langchain) and based on [PrivateGPT](https://github.com/imartinez/privateGPT). 

Be aware that in order to run this project a `OPENAI_API_KEY` is required. Therefore, it requires a OpenAI account with Payment Method registered. You can check OpenAI Pricing [here](https://openai.com/pricing#language-models).
## Environment Setup

Install conda on [Linux](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html), [Windows](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) or [macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html).

Create and Activate
```shell
conda create -n orbgpt
conda activate orbgpt
```

Install all requirements
```shell
pip install -r requirements.txt
```

export your `OPENAI_API_KEY`.
```shell
export OPENAI_API_KEY="..."
```
## Regenerate tokens

If you update the files in `orbdocs/` you need to rerun
```shell
python ingest.py
```

## Run the Chat
```shell
python orbgpt.py
```


### Chat Sample
````
(orbgpt) leoparente@PC ~/git/orb-gpt (main) $ python orbgpt.py 
Chat with ORB docs!

Question:
what is orb and pktvisor?
OrbGPT:
Orb and pktvisor are two open source tools developed by NS1 Labs. They were created to address the challenge of real-time edge visibility and deep network observability in large, distributed edge environments.

pktvisor is a tool designed to analyze and extract information from massive streams of global DNS traffic, which can reach millions of queries per second. It helps identify and respond to malicious activities like DDoS attacks in real-time.

Orb, on the other hand, is an open source tool based on IoT principles. It provides a user interface (UI), application programming interface (API), and agent communications to orchestrate agents and their policies. Orb allows you to manage and reprogram fleets of pktvisors in real-time, enhancing the functionality of pktvisor by adding critical capabilities for collecting and sinking agent output.

In summary, pktvisor focuses on real-time analysis of network traffic at the edge, while Orb provides a global orchestration layer to dynamically adjust observability strategies across a fleet of pktvisors and collect data on a second-to-second basis.

Question:
can you create a orb policy with a pcap input and a dns v2 handler and a net handler in yaml format? 
OrbGPT:
To create an Orb policy with a pcap input, a DNS v2 handler, and a net handler in YAML format, you can use the following configuration:

```yaml
handlers:
  modules:
    handler_dns_1:
      type: dns
      version: 2
    handler_net_1:
      type: net
input:
  input_type: pcap
  tap: ethernet
  filter:
    bpf: 'port 53'
kind: collection
```

In this configuration, we have defined two handlers: `handler_dns_1` of type `dns` with version 2, and `handler_net_1` of type `net`. The input is set to `pcap` with the tap `ethernet`, and the filter is set to capture packets on port 53 (DNS).

Please note that you may need to adjust the tap configuration (`iface`) in the `visor` section and the agent address (`address`) in the `orb` section according to your specific setup.

Question:
quit

Exiting Chat... See ya!
````
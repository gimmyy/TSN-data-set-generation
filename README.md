# TSN-data-set-generation
This repository provides the data set generation tool for TSN scheduling algorithm evaluation. You can use it to generate testing topologies and flows according to customized requirements.

# Run
generate_flow_topo.py

# Command
python3 generate_flow_topo.py

# Notes
please consider citing our paper if you use the code：《Towards Distributed Flow Scheduling in IEEE 802.1Qbv Time-Sensitive
Networks》.

@article{10.1145/3676848,
author = {Guo, Miao and He, Shibo and Gu, Chaojie and Guo, Xiuzhen and Chen, Jiming and Gao, Tao and Wang, Tongtong},
title = {Towards Distributed Flow Scheduling in IEEE 802.1Qbv Time-Sensitive Networks},
year = {2024},
issue_date = {September 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {20},
number = {5},
issn = {1550-4859},
url = {https://doi.org/10.1145/3676848},
doi = {10.1145/3676848},
abstract = {Flow scheduling plays a pivotal role in enabling Time-Sensitive Networking (TSN) applications. Current flow scheduling mainly adopts a centralized scheme, posing challenges in adapting to dynamic network conditions and scaling up for larger networks. To address these challenges, we first thoroughly analyze the flow scheduling problem and find the inherent locality nature of time scheduling tasks. Leveraging this insight, we introduce the first distributed framework for IEEE 802.1Qbv TSN flow scheduling. In this framework, we further propose a multi-agent flow scheduling method by designing Deep Reinforcement Learning (DRL)-based route and time agents for route and time planning tasks. The time agents are deployed on field devices to schedule flows in a distributed way. Evaluations in dynamic scenarios validate the effectiveness and scalability of our proposed method. It enhances the scheduling success rate by 20.31\% compared to state-of-the-art methods and achieves substantial cost savings, reducing transmission costs by 410\texttimes{} in large-scale networks. Additionally, we validate our approach on edge devices and a TSN testbed, highlighting its lightweight nature and ease of deployment.},
journal = {ACM Trans. Sen. Netw.},
month = {jul},
articleno = {104},
numpages = {30},
keywords = {Time-sensitive networking, distributed scheduling, deep reinforcement learning}
}

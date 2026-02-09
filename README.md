# Awesome LLM-RLVR [🔥📜]
[![Auto Update Papers](https://github.com/smiles724/Awesome-LLM-RLVR/actions/workflows/arxiv-update.yml/badge.svg)](https://github.com/smiles724/Awesome-LLM-RLVR/actions/workflows/arxiv-update.yml)

<div align="center">
  <a href="https://github.com/smiles724/Awesome-LLM-RLVR/stargazers"><img src="https://img.shields.io/github/stars/smiles724/Awesome-LLM-RLVR?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/smiles724/Awesome-LLM-RLVR/network/members"><img src="https://img.shields.io/github/forks/smiles724/Awesome-LLM-RLVR?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/smiles724/Awesome-LLM-RLVR/graphs/contributors"><img src="https://img.shields.io/github/contributors/smiles724/Awesome-LLM-RLVR?style=for-the-badge" alt="Contributors"></a>
  <a href="https://github.com/smiles724/Awesome-LLM-RLVR/blob/main/LICENSE"><img src="https://img.shields.io/github/license/smiles724/Awesome-LLM-RLVR?style=for-the-badge" alt="MIT License"></a>
</div>

>  A curated list of research papers, tools, datasets, and frameworks for **Reinforcement Learning with Verifiable Rewards (RLVR)** in Large Language Models (LLMs).  
> Inspired by the intersection of alignment, reasoning, and self-improvement in foundation models.  

Contributions welcome! See [contributing guidelines](#contributing) below.

<details>
  <summary>🗂️ Table of Contents</summary>
  <ol>
    <li><a href="#motivation">🌟 Motivation</a></li>
    <li><a href="#auto-fetched-recent-papers">🔄 Auto-Fetched Recent Papers</a></li>
    <li><a href="#core-papers">🧠 Core Papers</a></li>
    <li><a href="#unsupervised-rlvr">🔍 Unsupervised RLVR</a></li>
    <li><a href="#entropy-in-rlvr">📉 Entropy in RLVR</a></li>
    <li><a href="#rlvr-analysis">🧪 RLVR Analysis</a></li>
    <li><a href="#mllm">🖼️ Multimodal LLM</a></li>
    <li><a href="#evaluation">📏 Evaluation Issue</a></li>
    <li><a href="#blogs">📰 Awesome Blogs about RLVR</a></li>
    <li><a href="#toolkits-and-libraries">🛠️ Toolkits and Libraries</a></li>
    <li><a href="#star">⭐ Star History</a></li>
    <li><a href="#contributing">🤝 Contributing</a></li>
    <li><a href="#license">🧾 License</a></li>
  </ol>
</details>

---

<h2 id="motivation">🌟 Motivation</h2>

RLVR is a rapidly evolving paradigm for aligning LLMs through **external reward verification**, **self-consistency**, and **bootstrap learning**, enabling models to improve reasoning capabilities without relying heavily on human supervision.

---

### 🔄 Auto-Fetched Recent Papers
- **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images** <2026-02-06>  
  *Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak*. [[Paper]](https://arxiv.org/abs/2602.06965v1)
- **Back to Basics: Revisiting Exploration in Reinforcement Learning for LLM Reasoning via Generative Probabilities** <2026-02-06>  
  *Pengyi Li, Elizaveta Goncharova, Andrey Kuznetsov, Ivan Oseledets*. [[Paper]](https://arxiv.org/abs/2602.05281v2)
- **Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling** <2026-02-06>  
  *Kate Sanders, Nathaniel Weir, Sapana Chaudhary, Kaj Bostrom, Huzefa Rangwala*. [[Paper]](https://arxiv.org/abs/2602.06795v1)
- **F-GRPO: Don't Let Your Policy Learn the Obvious and Forget the Rare** <2026-02-06>  
  *Daniil Plyusov, Alexey Gorbatovski, Boris Shaposhnikov, Viacheslav Sinii, Alexey Malakhov, Daniil Gavrilov*. [[Paper]](https://arxiv.org/abs/2602.06717v1)
- **Evaluating and Enhancing the Vulnerability Reasoning Capabilities of Large Language Models** <2026-02-06>  
  *Li Lu, Yanjie Zhao, Hongzhou Rao, Kechi Zhang, Haoyu Wang*. [[Paper]](https://arxiv.org/abs/2602.06687v1)
- **dUltra: Ultra-Fast Diffusion Language Models via Reinforcement Learning** <2026-02-06>  
  *Shirui Chen, Jiantao Jiao, Lillian J. Ratliff, Banghua Zhu*. [[Paper]](https://arxiv.org/abs/2512.21446v2)
- **POINTS-GUI-G: GUI-Grounding Journey** <2026-02-06>  
  *Zhongyin Zhao, Yuan Liu, Yikun Liu, Haicheng Wang, Le Tian, Xiao Zhou, Yangxiu You, Zilin Yu, Yang Yu, Jie Zhou*. [[Paper]](https://arxiv.org/abs/2602.06391v1)
- **CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs** <2026-02-06>  
  *Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.03048v3)
- **B-GRPO: Unsupervised Speech Emotion Recognition based on Batched-Group Relative Policy Optimization** <2026-02-06>  
  *Yingying Gao, Shilei Zhang, Runyan Yang, Zihao Cui, Junlan Feng*. [[Paper]](https://arxiv.org/abs/2602.06290v1)
- **VowelPrompt: Hearing Speech Emotions from Text via Vowel-level Prosodic Augmentation** <2026-02-06>  
  *Yancheng Wang, Osama Hanna, Ruiming Xie, Xianfeng Rui, Maohao Shen, Xuedong Zhang, Christian Fuegen, Jilong Wu, Debjyoti Paul, Arthur Guo, Zhihong Lei, Ozlem Kalinli, Qing He, Yingzhen Yang*. [[Paper]](https://arxiv.org/abs/2602.06270v1)
- **$f$-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment** <2026-02-05>  
  *Rajdeep Haldar, Lantao Mei, Guang Lin, Yue Xing, Qifan Song*. [[Paper]](https://arxiv.org/abs/2602.05946v1)
- **Anchored Policy Optimization: Mitigating Exploration Collapse Via Support-Constrained Rectification** <2026-02-05>  
  *Tianyi Wang, Long Li, Hongcan Guo, Yibiao Chen, Yixia Li, Yong Wang, Yun Chen, Guanhua Chen*. [[Paper]](https://arxiv.org/abs/2602.05717v1)
- **Rewards as Labels: Revisiting RLVR from a Classification Perspective** <2026-02-05>  
  *Zepeng Zhai, Meilin Chen, Jiaxuan Zhao, Junlang Qian, Lei Shen, Yuan Lu*. [[Paper]](https://arxiv.org/abs/2602.05630v1)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** <2026-02-05>  
  *Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu*. [[Paper]](https://arxiv.org/abs/2602.05548v1)
- **A Unified Framework for Rethinking Policy Divergence Measures in GRPO** <2026-02-05>  
  *Qingyuan Wu, Yuhui Wang, Simon Sinong Zhan, Yanning Dai, Shilong Deng, Sarra Habchi, Qi Zhu, Matthias Gallé, Chao Huang*. [[Paper]](https://arxiv.org/abs/2602.05494v1)
- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** <2026-02-05>  
  *Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He*. [[Paper]](https://arxiv.org/abs/2601.09361v2)
- **Length-Unbiased Sequence Policy Optimization: Revealing and Controlling Response Length Variation in RLVR** <2026-02-05>  
  *Fanfan Liu, Youyang Yin, Peng Shi, Siqi Yang, Zhixiong Zeng, Haibo Qiu*. [[Paper]](https://arxiv.org/abs/2602.05261v1)
- **EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization** <2026-02-05>  
  *Kevin Han, Yuhang Zhou, Mingze Gao, Gedi Zhou, Serena Li, Abhishek Kumar, Xiangjun Fan, Weiwei Li, Lizhu Zhang*. [[Paper]](https://arxiv.org/abs/2602.05165v1)
- **Beyond Correctness: Rewarding Faithful Reasoning in Retrieval-Augmented Generation** <2026-02-04>  
  *Zhichao Xu, Zongyu Wu, Yun Zhou, Aosong Feng, Kang Zhou, Sangmin Woo, Kiran Ramnath, Yijun Tian, Xuan Qi, Weikang Qiu, Lin Lee Cheong, Haibo Ding*. [[Paper]](https://arxiv.org/abs/2510.13272v2)
- **Extending RLVR to Open-Ended Tasks via Verifiable Multiple-Choice Reformulation** <2026-02-04>  
  *Mengyu Zhang, Siyu Ding, Weichong Yin, Yu Sun, Hua Wu*. [[Paper]](https://arxiv.org/abs/2511.02463v3)
- **Thickening-to-Thinning: Reward Shaping via Human-Inspired Learning Dynamics for LLM Reasoning** <2026-02-04>  
  *Wenze Lin, Zhen Yang, Xitai Jiang, Pony Ma, Gao Huang*. [[Paper]](https://arxiv.org/abs/2602.04265v1)
- **The Invisible Leash: Why RLVR May or May Not Escape Its Origin** <2026-02-04>  
  *Fang Wu, Weihao Xuan, Ximing Lu, Mingjie Liu, Yi Dong, Zaid Harchaoui, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2507.14843v4)
- **Monitorability as a Free Gift: How RLVR Spontaneously Aligns Reasoning** <2026-02-03>  
  *Zidi Xiong, Shan Chen, Himabindu Lakkaraju*. [[Paper]](https://arxiv.org/abs/2602.03978v1)
- **Learning Query-Specific Rubrics from Human Preferences for DeepResearch Report Generation** <2026-02-03>  
  *Changze Lv, Jie Zhou, Wentao Zhao, Jingwen Xu, Zisu Huang, Muzhao Tian, Shihan Dou, Tao Gui, Le Tian, Xiao Zhou, Xiaoqing Zheng, Xuanjing Huang, Jie Zhou*. [[Paper]](https://arxiv.org/abs/2602.03619v1)
- **Learning to Reason Faithfully through Step-Level Faithfulness Maximization** <2026-02-03>  
  *Runquan Gui, Yafu Li, Xiaoye Qu, Ziyan Liu, Yeqiu Cheng, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.03507v1)
- **Beyond Variance: Prompt-Efficient RLVR via Rare-Event Amplification and Bidirectional Pairing** <2026-02-03>  
  *Xin Sheng, Jiaxin Li, Yujuan Pang, Ran Peng, Yong Ma*. [[Paper]](https://arxiv.org/abs/2602.03452v1)
- **Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards** <2026-02-03>  
  *Hieu Trung Nguyen, Bao Nguyen, Wenao Ma, Yuzhi Zhao, Ruifeng She, Viet Anh Nguyen*. [[Paper]](https://arxiv.org/abs/2602.01601v2)
- **MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning** <2026-02-03>  
  *Shengyuan Liu, Liuxin Bao, Qi Yang, Wanting Geng, Boyun Zheng, Chenxin Li, Wenting Chen, Houwen Peng, Yixuan Yuan*. [[Paper]](https://arxiv.org/abs/2602.03320v1)
- **Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration** <2026-02-03>  
  *Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Dongchun Xie, Hanhui Li, Yiwei Wang, Xiaodan Liang, Jing Tang*. [[Paper]](https://arxiv.org/abs/2508.13755v5)
- **Self-Hinting Language Models Enhance Reinforcement Learning** <2026-02-03>  
  *Baohao Liao, Hanze Dong, Xinxing Xu, Christof Monz, Jiang Bian*. [[Paper]](https://arxiv.org/abs/2602.03143v1)
- **Test-time Recursive Thinking: Self-Improvement without External Feedback** <2026-02-03>  
  *Yufan Zhuang, Chandan Singh, Liyuan Liu, Yelong Shen, Dinghuai Zhang, Jingbo Shang, Jianfeng Gao, Weizhu Chen*. [[Paper]](https://arxiv.org/abs/2602.03094v1)
- **Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text** <2026-02-02>  
  *Ximing Lu, David Acuna, Jaehun Jung, Jian Hu, Di Zhang, Shizhe Diao, Yunheng Zou, Shaokun Zhang, Brandon Cui, Mingjie Liu, Hyunwoo Kim, Prithviraj Ammanabrolu, Jan Kautz, Yi Dong, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2601.22975v2)
- **Proof-RM: A Scalable and Generalizable Reward Model for Math Proof** <2026-02-02>  
  *Haotong Yang, Zitong Wang, Shijia Kang, Siqi Yang, Wenkai Yu, Xu Niu, Yike Sun, Yi Hu, Zhouchen Lin, Muhan Zhang*. [[Paper]](https://arxiv.org/abs/2602.02377v1)
- **Think Dense, Not Long: Dynamic Decoupled Conditional Advantage for Efficient Reasoning** <2026-02-02>  
  *Keqin Peng, Yuanxin Ouyang, Xuebo Liu, Zhiliang Tian, Ruijian Han, Yancheng Yuan, Liang Ding*. [[Paper]](https://arxiv.org/abs/2602.02099v1)
- **Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification** <2026-02-02>  
  *Yiju Guo, Tianyi Hu, Zexu Sun, Yankai Lin*. [[Paper]](https://arxiv.org/abs/2601.21244v2)
- **Grad2Reward: From Sparse Judgment to Dense Rewards for Improving Open-Ended LLM Reasoning** <2026-02-02>  
  *Zheng Zhang, Ao Lu, Yuanhao Zeng, Ziwei Shan, Jinjin Guo, Lufei Li, Yexin Li, Kan Ren*. [[Paper]](https://arxiv.org/abs/2602.01791v1)
- **The Multiple Ticket Hypothesis: Random Sparse Subnetworks Suffice for RLVR** <2026-02-02>  
  *Israel Adewuyi, Solomon Okibe, Vladmir Ivanov*. [[Paper]](https://arxiv.org/abs/2602.01599v1)
- **A Relative-Budget Theory for Reinforcement Learning with Verifiable Rewards in Large Language Model Reasoning** <2026-02-02>  
  *Akifumi Wachi, Hirota Kinoshita, Shokichi Takakura, Rei Higuchi, Taiji Suzuki*. [[Paper]](https://arxiv.org/abs/2602.01523v1)
- **GOPO: Policy Optimization using Ranked Rewards** <2026-02-01>  
  *Kyuseong Choi, Dwaipayan Saha, Woojeong Kim, Anish Agarwal, Raaz Dwivedi*. [[Paper]](https://arxiv.org/abs/2602.03876v1)
- **End-to-End Agentic RAG System Training for Traceable Diagnostic Reasoning** <2026-02-01>  
  *Qiaoyu Zheng, Yuze Sun, Chaoyi Wu, Weike Zhao, Pengcheng Qiu, Yongguo Yu, Kun Sun, Jian Zhang, Yanfeng Wang, Ya Zhang, Weidi Xie*. [[Paper]](https://arxiv.org/abs/2508.15746v2)
- **Probing RLVR training instability through the lens of objective-level hacking** <2026-02-01>  
  *Yiming Dong, Kun Fu, Haoyu Li, Xinyuan Zhu, Yurou Liu, Lijing Shao, Jieping Ye, Zheng Wang*. [[Paper]](https://arxiv.org/abs/2602.01103v1)
- **SetPO: Set-Level Policy Optimization for Diversity-Preserving LLM Reasoning** <2026-02-01>  
  *Chenyi Li, Yuan Zhang, Bo Wang, Guoqing Ma, Wei Tang, Haoyang Huang, Nan Duan*. [[Paper]](https://arxiv.org/abs/2602.01062v1)
- **DISPO: Enhancing Training Efficiency and Stability in Reinforcement Learning for Large Language Model Mathematical Reasoning** <2026-02-01>  
  *Batuhan K. Karaman, Aditya Rawal, Suhaila Shakiah, Mohammad Ghavamzadeh, Mingyi Hong, Arijit Biswas, Ruida Zhou*. [[Paper]](https://arxiv.org/abs/2602.00983v1)
- **Agentic Policy Optimization via Instruction-Policy Co-Evolution** <2026-01-31>  
  *Han Zhou, Xingchen Wan, Ivan Vulić, Anna Korhonen*. [[Paper]](https://arxiv.org/abs/2512.01945v2)
- **Resource-Efficient Reinforcement for Reasoning Large Language Models via Dynamic One-Shot Policy Refinement** <2026-01-31>  
  *Yunjian Zhang, Sudong Wang, Yang Li, Peiran Xu, Conghao Zhou, Xiaoyue Ma, Jianing Li, Yao Zhu*. [[Paper]](https://arxiv.org/abs/2602.00815v1)
- **Adaptive Ability Decomposing for Unlocking Large Reasoning Model Effective Reinforcement Learning** <2026-01-31>  
  *Zhipeng Chen, Xiaobo Qin, Wayne Xin Zhao, Youbin Wu, Ji-Rong Wen*. [[Paper]](https://arxiv.org/abs/2602.00759v1)
- **Learning Reasoning Reward Models from Expert Demonstration via Inverse Reinforcement Learning** <2026-01-31>  
  *Claudio Fanconi, Nicolás Astorga, Mihaela van der Schaar*. [[Paper]](https://arxiv.org/abs/2510.01857v2)
- **Agentic Reward Modeling: Verifying GUI Agent via Online Proactive Interaction** <2026-01-31>  
  *Chaoqun Cui, Jing Huang, Shijing Wang, Liming Zheng, Qingchao Kong, Zhixiong Zeng*. [[Paper]](https://arxiv.org/abs/2602.00575v1)
- **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs** <2026-01-31>  
  *Md Tanvirul Alam, Aritran Piplai, Ionut Cardei, Nidhi Rastogi, Peter J Worth*. [[Paper]](https://arxiv.org/abs/2602.00513v1)
- **LLMs as High-Dimensional Nonlinear Autoregressive Models with Attention: Training, Alignment and Inference** <2026-01-31>  
  *Vikram Krishnamurthy*. [[Paper]](https://arxiv.org/abs/2602.00426v1)
- **Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning** <2026-01-30>  
  *Yang Zhou, Sunzhu Li, Shunyu Liu, Wenkai Fang, Kongcheng Zhang, Jiale Zhao, Jingwen Yang, Yihe Zhou, Jianwei Lv, Tongya Zheng, Hengtong Lu, Wei Chen, Yan Xie, Mingli Song*. [[Paper]](https://arxiv.org/abs/2508.16949v6)
- **Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text** <2026-01-30>  
  *Ximing Lu, David Acuna, Jaehun Jung, Jian Hu, Di Zhang, Shizhe Diao, Yunheng Zou, Shaokun Zhang, Brandon Cui, Mingjie Liu, Hyunwoo Kim, Prithviraj Ammanabrolu, Jan Kautz, Yi Dong, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2601.22975v1)
- **MulFeRL: Enhancing Reinforcement Learning with Verbal Feedback in a Multi-turn Loop** <2026-01-30>  
  *Xuancheng Li, Haitao Li, Yujia Zhou, YiqunLiu, Qingyao Ai*. [[Paper]](https://arxiv.org/abs/2601.22900v1)
- **Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings** <2026-01-30>  
  *Safal Shrestha, Minwu Kim, Aadim Nepal, Anubhav Shrestha, Keith Ross*. [[Paper]](https://arxiv.org/abs/2505.13718v3)
- **Metis-SPECS: Decoupling Multimodal Learning via Self-distilled Preference-based Cold Start** <2026-01-30>  
  *Kun Chen, Peng Shi, Haibo Qiu, Zhixiong Zeng, Siqi Yang, Wenji Mao, Lin Ma*. [[Paper]](https://arxiv.org/abs/2510.25801v3)
- **Sharpness-Guided Group Relative Policy Optimization via Probability Shaping** <2026-01-30>  
  *Tue Le, Linh Ngo Van, Trung Le*. [[Paper]](https://arxiv.org/abs/2511.00066v3)
- **Learn More with Less: Uncertainty Consistency Guided Query Selection for RLVR** <2026-01-30>  
  *Hao Yi, Yulan Hu, Xin Li, Sheng Ouyang, Lizhong Ding, Yong Liu*. [[Paper]](https://arxiv.org/abs/2601.22595v1)
- **SSL: Sweet Spot Learning for Differentiated Guidance in Agentic Optimization** <2026-01-30>  
  *Jinyang Wu, Changpeng Yang, Yuhao Shen, Fangzhi Xu, Bolin Ni, Chonghua Liao, Yuchen Liu, Hongzhen Wang, Shuai Nie, Shuai Zhang, Haoran Luo, Jiaming Xu*. [[Paper]](https://arxiv.org/abs/2601.22491v1)
- **HeaPA: Difficulty-Aware Heap Sampling and On-Policy Query Augmentation for LLM Reinforcement Learning** <2026-01-30>  
  *Weiqi Wang, Xin Liu, Binxuan Huang, Hejie Cui, Rongzhi Zhang, Changlong Yu, Shuowei Jin, Jingfeng Yang, Qingyu Yin, Zhengyang Wang, Zheng Li, Yifan Gao, Priyanka Nigam, Bing Yin, Lihong Li, Yangqiu Song*. [[Paper]](https://arxiv.org/abs/2601.22448v1)
- **Prepare Reasoning Language Models for Multi-Agent Debate with Self-Debate Reinforcement Learning** <2026-01-29>  
  *Chenxi Liu, Yanshuo Chen, Ruibo Chen, Tianyi Xiong, Tong Zheng, Heng Huang*. [[Paper]](https://arxiv.org/abs/2601.22297v1)
- **ViSurf: Visual Supervised-and-Reinforcement Fine-Tuning for Large Vision-and-Language Models** <2026-01-29>  
  *Yuqi Liu, Liangyu Chen, Jiazhen Liu, Mingkang Zhu, Zhisheng Zhong, Bei Yu, Jiaya Jia*. [[Paper]](https://arxiv.org/abs/2510.10606v3)
- **Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification** <2026-01-29>  
  *Yiju Guo, Tianyi Hu, Zexu Sun, Yankai Lin*. [[Paper]](https://arxiv.org/abs/2601.21244v1)
- **Do Reasoning Models Enhance Embedding Models?** <2026-01-29>  
  *Wun Yu Chan, Shaojin Chen, Huihao Jing, Kwun Hang Lau, Elton Chun-Chai Li, Zihao Wang, Haoran Li, Yangqiu Song*. [[Paper]](https://arxiv.org/abs/2601.21192v1)
- **Llama-3.1-FoundationAI-SecurityLLM-Reasoning-8B Technical Report** <2026-01-28>  
  *Zhuoran Yang, Ed Li, Jianliang He, Aman Priyanshu, Baturay Saglam, Paul Kassianik, Sajana Weerawardhena, Anu Vellore, Blaine Nelson, Neusha Javidnia, Arthur Goldblatt, Fraser Burch, Avi Zohary, Assaf Eisenman, Mahdi Sabbaghi, Supriti Vijay, Rahim Dharssi, Dhruv Kedia, Kojin Oshiba, Yaron Singer, Amin Karbasi*. [[Paper]](https://arxiv.org/abs/2601.21051v1)
- **Solver-in-the-Loop: MDP-Based Benchmarks for Self-Correction and Behavioral Rationality in Operations Research** <2026-01-28>  
  *Ruicheng Ao, David Simchi-Levi, Xinshang Wang*. [[Paper]](https://arxiv.org/abs/2601.21008v1)
- **Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning** <2026-01-28>  
  *Minwu Kim, Safal Shrestha, Keith Ross*. [[Paper]](https://arxiv.org/abs/2601.20829v1)
- **Reinforcement Learning via Self-Distillation** <2026-01-28>  
  *Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta, Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, Andreas Krause*. [[Paper]](https://arxiv.org/abs/2601.20802v1)
- **P2S: Probabilistic Process Supervision for General-Domain Reasoning Question Answering** <2026-01-28>  
  *Wenlin Zhong, Chengyuan Liu, Yiquan Wu, Bovin Tan, Changlong Sun, Yi Wang, Xiaozhong Liu, Kun Kuang*. [[Paper]](https://arxiv.org/abs/2601.20649v1)
- **Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation** <2026-01-28>  
  *Yanqi Dai, Yuxiang Ji, Xiao Zhang, Yong Wang, Xiangxiang Chu, Zhiwu Lu*. [[Paper]](https://arxiv.org/abs/2601.20614v1)
- **Ranking-aware Reinforcement Learning for Ordinal Ranking** <2026-01-28>  
  *Aiming Hao, Chen Zhu, Jiashu Zhu, Jiahong Wu, Xiangxiang Chu*. [[Paper]](https://arxiv.org/abs/2601.20585v1)
- **RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation** <2026-01-28>  
  *Sunzhu Li, Jiale Zhao, Miteto Wei, Huimin Ren, Yang Zhou, Jingwen Yang, Shunyu Liu, Kaike Zhang, Wei Chen*. [[Paper]](https://arxiv.org/abs/2601.08430v2)
- **Endogenous Reprompting: Self-Evolving Cognitive Alignment for Unified Multimodal Models** <2026-01-28>  
  *Zhenchen Tang, Songlin Yang, Zichuan Wang, Bo Peng, Yang Li, Beibei Dong, Jing Dong*. [[Paper]](https://arxiv.org/abs/2601.20305v1)
- **Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning** <2026-01-28>  
  *Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang*. [[Paper]](https://arxiv.org/abs/2512.19920v3)
- **Rewarding Intellectual Humility Learning When Not To Answer In Large Language Models** <2026-01-27>  
  *Abha Jha, Akanksha Mahajan, Ashwath Vaithinathan Aravindan, Praveen Saravanan, Sai Sailaja Policharla, Sonal Chaturbhuj Gehlot*. [[Paper]](https://arxiv.org/abs/2601.20126v1)
- **Coupled Variational Reinforcement Learning for Language Model General Reasoning** <2026-01-27>  
  *Xueru Wen, Jie Lou, Yanjiang Liu, Hongyu Lin, Ben He, Xianpei Han, Le Sun, Yaojie Lu, Debing Zhang*. [[Paper]](https://arxiv.org/abs/2512.12576v2)
- **DiVE-k: Differential Visual Reasoning for Fine-grained Image Recognition** <2026-01-27>  
  *Raja Kumar, Arka Sadhu, Ram Nevatia*. [[Paper]](https://arxiv.org/abs/2511.18305v2)
- **Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward** <2026-01-26>  
  *Peter Chen, Xiaopeng Li, Ziniu Li, Wotao Yin, Xi Chen, Tianyi Lin*. [[Paper]](https://arxiv.org/abs/2512.16912v3)
- **From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation** <2026-01-26>  
  *Yuxin Jiang, Yufei Wang, Qiyuan Zhang, Xingshan Zeng, Liangyou Li, Jierun Chen, Chaofan Tao, Haoli Bai, Lifeng Shang*. [[Paper]](https://arxiv.org/abs/2601.18533v1)
- **PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR** <2026-01-26>  
  *James Burgess, Jan N. Hansen, Duo Peng, Yuhui Zhang, Alejandro Lozano, Min Woo Sun, Emma Lundberg, Serena Yeung-Levy*. [[Paper]](https://arxiv.org/abs/2601.18207v1)
- **When Sharpening Becomes Collapse: Sampling Bias and Semantic Coupling in RL with Verifiable Rewards** <2026-01-26>  
  *Mingyuan Fan, Weiguang Han, Daixin Wang, Cen Chen, Zhiqiang Zhang, Jun Zhou*. [[Paper]](https://arxiv.org/abs/2601.15609v2)
- **SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data** <2026-01-25>  
  *Wenkai Fang, Shunyu Liu, Yang Zhou, Kongcheng Zhang, Tongya Zheng, Kaixuan Chen, Mingli Song, Dacheng Tao*. [[Paper]](https://arxiv.org/abs/2505.20347v2)
- **Not All Steps are Informative: On the Linearity of LLMs' RLVR Training** <2026-01-25>  
  *Tianle Wang, Zhongyuan Wu, Shenghao Jin, Hao Xu, Wei Chen, Ning Miao*. [[Paper]](https://arxiv.org/abs/2601.04537v2)
- **Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning** <2026-01-25>  
  *Sanghwan Bae, Jiwoo Hong, Min Young Lee, Hanbyul Kim, JeongYeon Nam, Donghyun Kwak*. [[Paper]](https://arxiv.org/abs/2504.03380v2)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal** <2026-01-24>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v2)
- **VaseVQA: Multimodal Agent and Benchmark for Ancient Greek Pottery** <2026-01-24>  
  *Jinchao Ge, Tengfei Cheng, Biao Wu, Zeyu Zhang, Shiya Huang, Judith Bishop, Gillian Shepherd, Meng Fang, Ling Chen, Yang Zhao*. [[Paper]](https://arxiv.org/abs/2509.17191v2)
- **Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning** <2026-01-23>  
  *Massimiliano Pronesti, Anya Belz, Yufang Hou*. [[Paper]](https://arxiv.org/abs/2601.17223v1)
- **Reasoning Promotes Robustness in Theory of Mind Tasks** <2026-01-23>  
  *Ian B. de Haan, Peter van der Putten, Max van Duijn*. [[Paper]](https://arxiv.org/abs/2601.16853v1)
- **PhysProver: Advancing Automatic Theorem Proving for Physics** <2026-01-22>  
  *Hanning Zhang, Ruida Wang, Rui Pan, Wenyuan Wang, Bingxu Meng, Tong Zhang*. [[Paper]](https://arxiv.org/abs/2601.15737v1)
- **Your Group-Relative Advantage Is Biased** <2026-01-22>  
  *Fengkai Yang, Zherui Chen, Xiaohan Wang, Xiaodong Lu, Jiajun Chai, Guojun Yin, Wei Lin, Shuai Ma, Fuzhen Zhuang, Deqing Wang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2601.08521v2)
- **Can LLM Infer Risk Information From MCP Server System Logs?** <2026-01-22>  
  *Jiayi Fu, Yuansen Zhang, Yinggui Wang*. [[Paper]](https://arxiv.org/abs/2511.05867v3)
- **DARL: Encouraging Diverse Answers for General Reasoning without Verifiers** <2026-01-21>  
  *Chongxuan Huang, Lei Lin, Xiaodong Shi, Wenping Hu, Ruiming Tang*. [[Paper]](https://arxiv.org/abs/2601.14700v1)
- **LightOnOCR: A 1B End-to-End Multilingual Vision-Language Model for State-of-the-Art OCR** <2026-01-20>  
  *Said Taghadouini, Adrien Cavaillès, Baptiste Aubertin*. [[Paper]](https://arxiv.org/abs/2601.14251v1)
- **ICPO: Illocution-Calibrated Policy Optimization for Multi-Turn Conversation** <2026-01-20>  
  *Zhebo Wang, Xiaohu Mu, Zijie Zhou, Mohan Li, Wenpeng Xing, Dezhang Kong, Meng Han*. [[Paper]](https://arxiv.org/abs/2601.15330v1)
- **Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning** <2026-01-19>  
  *Duygu Nur Yaldiz, Evangelia Spiliopoulou, Zheng Qi, Siddharth Varia, Srikanth Doss, Nikolaos Pappas*. [[Paper]](https://arxiv.org/abs/2601.13284v1)
- **Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective** <2026-01-19>  
  *Zhezheng Hao, Hong Wang, Haoyang Liu, Jian Luo, Jiarui Yu, Hande Dong, Qiang Lin, Can Wang, Jiawei Chen*. [[Paper]](https://arxiv.org/abs/2510.10150v2)
- **Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models** <2026-01-19>  
  *Runxuan Liu, Xianhao Ou, Xinyan Ma, Jiyuan Wang, Jiafeng Liang, Jiaqi Li, Tao He, Zheng Chu, Rongchuan Mu, Zekun Wang, Baoxin Wang, Dayong Wu, Ming Liu, Shijin Wang, Guoping Hu, Bing Qin*. [[Paper]](https://arxiv.org/abs/2601.12995v1)
- **Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping** <2026-01-18>  
  *Miao Peng, Weizhou Shen, Nuo Chen, Chenliang Li, Ming Yan, Jia Li*. [[Paper]](https://arxiv.org/abs/2601.12465v1)
- **Aletheia: What Makes RLVR For Code Verifiers Tick?** <2026-01-17>  
  *Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych*. [[Paper]](https://arxiv.org/abs/2601.12186v1)
- **Post-Training as Reweighting: A Stochastic View of Reasoning Trajectories in Language Models** <2026-01-17>  
  *Dake Bu, Wei Huang, Andi Han, Atsushi Nitanda, Bo Xue, Qingfu Zhang, Hau-San Wong, Taiji Suzuki*. [[Paper]](https://arxiv.org/abs/2511.07368v2)
- **AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training** <2026-01-17>  
  *Zhiyuan Li, Yuan Wu, Yi Chang*. [[Paper]](https://arxiv.org/abs/2601.11864v1)
- **Reasoning Promotes Robustness in Theory of Mind Tasks** <2026-01-23>  
  *Ian B. de Haan, Peter van der Putten, Max van Duijn*. [[Paper]](https://arxiv.org/abs/2601.16853v1)
- **PhysProver: Advancing Automatic Theorem Proving for Physics** <2026-01-22>  
  *Hanning Zhang, Ruida Wang, Rui Pan, Wenyuan Wang, Bingxu Meng, Tong Zhang*. [[Paper]](https://arxiv.org/abs/2601.15737v1)
- **Your Group-Relative Advantage Is Biased** <2026-01-22>  
  *Fengkai Yang, Zherui Chen, Xiaohan Wang, Xiaodong Lu, Jiajun Chai, Guojun Yin, Wei Lin, Shuai Ma, Fuzhen Zhuang, Deqing Wang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2601.08521v2)
- **When Sharpening Becomes Collapse: Sampling Bias and Semantic Coupling in RL with Verifiable Rewards** <2026-01-22>  
  *Mingyuan Fan, Weiguang Han, Daixin Wang, Cen Chen, Zhiqiang Zhang, Jun Zhou*. [[Paper]](https://arxiv.org/abs/2601.15609v1)
- **Can LLM Infer Risk Information From MCP Server System Logs?** <2026-01-22>  
  *Jiayi Fu, Yuansen Zhang, Yinggui Wang*. [[Paper]](https://arxiv.org/abs/2511.05867v3)
- **DARL: Encouraging Diverse Answers for General Reasoning without Verifiers** <2026-01-21>  
  *Chongxuan Huang, Lei Lin, Xiaodong Shi, Wenping Hu, Ruiming Tang*. [[Paper]](https://arxiv.org/abs/2601.14700v1)
- **LightOnOCR: A 1B End-to-End Multilingual Vision-Language Model for State-of-the-Art OCR** <2026-01-20>  
  *Said Taghadouini, Adrien Cavaillès, Baptiste Aubertin*. [[Paper]](https://arxiv.org/abs/2601.14251v1)
- **ICPO: Illocution-Calibrated Policy Optimization for Multi-Turn Conversation** <2026-01-20>  
  *Zhebo Wang, Xiaohu Mu, Zijie Zhou, Mohan Li, Wenpeng Xing, Dezhang Kong, Meng Han*. [[Paper]](https://arxiv.org/abs/2601.15330v1)
- **Balancing Classification and Calibration Performance in Decision-Making LLMs via Calibration Aware Reinforcement Learning** <2026-01-19>  
  *Duygu Nur Yaldiz, Evangelia Spiliopoulou, Zheng Qi, Siddharth Varia, Srikanth Doss, Nikolaos Pappas*. [[Paper]](https://arxiv.org/abs/2601.13284v1)
- **Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective** <2026-01-19>  
  *Zhezheng Hao, Hong Wang, Haoyang Liu, Jian Luo, Jiarui Yu, Hande Dong, Qiang Lin, Can Wang, Jiawei Chen*. [[Paper]](https://arxiv.org/abs/2510.10150v2)
- **Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models** <2026-01-19>  
  *Runxuan Liu, Xianhao Ou, Xinyan Ma, Jiyuan Wang, Jiafeng Liang, Jiaqi Li, Tao He, Zheng Chu, Rongchuan Mu, Zekun Wang, Baoxin Wang, Dayong Wu, Ming Liu, Shijin Wang, Guoping Hu, Bing Qin*. [[Paper]](https://arxiv.org/abs/2601.12995v1)
- **Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping** <2026-01-18>  
  *Miao Peng, Weizhou Shen, Nuo Chen, Chenliang Li, Ming Yan, Jia Li*. [[Paper]](https://arxiv.org/abs/2601.12465v1)
- **Aletheia: What Makes RLVR For Code Verifiers Tick?** <2026-01-17>  
  *Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych*. [[Paper]](https://arxiv.org/abs/2601.12186v1)
- **Post-Training as Reweighting: A Stochastic View of Reasoning Trajectories in Language Models** <2026-01-17>  
  *Dake Bu, Wei Huang, Andi Han, Atsushi Nitanda, Bo Xue, Qingfu Zhang, Hau-San Wong, Taiji Suzuki*. [[Paper]](https://arxiv.org/abs/2511.07368v2)
- **AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training** <2026-01-17>  
  *Zhiyuan Li, Yuan Wu, Yi Chang*. [[Paper]](https://arxiv.org/abs/2601.11864v1)
- **Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning** <2026-01-16>  
  *Hongye Cao, Zhixin Bai, Ziyue Peng, Boyan Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao*. [[Paper]](https://arxiv.org/abs/2512.04359v3)
- **Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs** <2026-01-16>  
  *Lecheng Yan, Ruizhe Li, Guanhua Chen, Qing Li, Jiahui Geng, Wenxi Li, Vincent Wang, Chris Lee*. [[Paper]](https://arxiv.org/abs/2601.11061v1)
- **Many Minds from One Model: Bayesian-Inspired Transformers for Population Diversity** <2026-01-15>  
  *Diji Yang, Yi Zhang*. [[Paper]](https://arxiv.org/abs/2512.25063v2)
- **Better LLM Reasoning via Dual-Play** <2026-01-15>  
  *Zhengxin Zhang, Chengyu Huang, Aochong Oliver Li, Claire Cardie*. [[Paper]](https://arxiv.org/abs/2511.11881v3)
- **Dual-Uncertainty Guided Policy Learning for Multimodal Reasoning** <2026-01-15>  
  *Rui Liu, Dian Yu, Tong Zheng, Runpeng Dai, Zongxia Li, Wenhao Yu, Zhenwen Liang, Linfeng Song, Haitao Mi, Pratap Tokekar, Dong Yu*. [[Paper]](https://arxiv.org/abs/2510.01444v2)
- **Future-as-Label: Scalable Supervision from Real-World Outcomes** <2026-01-14>  
  *Benjamin Turtel, Paul Wilczewski, Danny Franklin, Kris Skothiem*. [[Paper]](https://arxiv.org/abs/2601.06336v2)
- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** <2026-01-14>  
  *Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He*. [[Paper]](https://arxiv.org/abs/2601.09361v1)
- **Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following** <2026-01-13>  
  *Yirong Zeng, Yufei Liu, Xiao Ding, Yutai Hou, Yuxian Wang, Haonan Song, Wu Ning, Dandan Tu, Qixun Zhang, Bibo Cai, Yuxiang He, Ting Liu*. [[Paper]](https://arxiv.org/abs/2601.04954v2)
- **JudgeRLVR: Judge First, Generate Second for Efficient Reasoning** <2026-01-13>  
  *Jiangshan Duo, Hanyu Li, Hailin Zhang, Yudong Wang, Sujian Li, Liang Zhao*. [[Paper]](https://arxiv.org/abs/2601.08468v1)
- **RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation** <2026-01-13>  
  *Sunzhu Li, Jiale Zhao, Miteto Wei, Huimin Ren, Yang Zhou, Jingwen Yang, Shunyu Liu, Kaike Zhang, Wei Chen*. [[Paper]](https://arxiv.org/abs/2601.08430v1)
- **The End of Reward Engineering: How LLMs Are Redefining Multi-Agent Coordination** <2026-01-13>  
  *Haoran Su, Yandong Sun, Congjia Yu*. [[Paper]](https://arxiv.org/abs/2601.08237v1)
- **ICPO: Intrinsic Confidence-Driven Group Relative Preference Optimization for Efficient Reinforcement Learning** <2026-01-13>  
  *Jinpeng Wang, Chao Li, Ting Ye, Mengyuan Zhang, Wei Liu, Jian Luan*. [[Paper]](https://arxiv.org/abs/2511.21005v5)
- **Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning** <2026-01-12>  
  *Wei Fang, James Glass*. [[Paper]](https://arxiv.org/abs/2601.07782v1)
- **Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?** <2026-01-12>  
  *Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash*. [[Paper]](https://arxiv.org/abs/2506.19467v3)
- **SPEC-RL: Accelerating On-Policy Reinforcement Learning with Speculative Rollouts** <2026-01-12>  
  *Bingshuai Liu, Ante Wang, Zijun Min, Liang Yao, Haibo Zhang, Yang Liu, Xu Han, Peng Li, Anxiang Zeng, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2509.23232v3)
- **Reward Modeling from Natural Language Human Feedback** <2026-01-12>  
  *Zongqi Wang, Rui Wang, Yuchuan Wu, Yiyao Yu, Pinyi Zhang, Shaoning Sun, Yujiu Yang, Yongbin Li*. [[Paper]](https://arxiv.org/abs/2601.07349v1)
- **Segmental Advantage Estimation: Enhancing PPO for Long-Context LLM Training** <2026-01-12>  
  *Xue Gong, Qi Yi, Ziyuan Nan, Guanhua Huang, Kejiao Li, Yuhao Jiang, Ruibin Xiong, Zenan Xu, Jiaming Guo, Shaohui Peng, Bo Zhou*. [[Paper]](https://arxiv.org/abs/2601.07320v1)
- **ReasonTabQA: A Comprehensive Benchmark for Table Question Answering from Real World Industrial Scenarios** <2026-01-12>  
  *Changzai Pan, Jie Zhang, Kaiwen Wei, Chenshuo Pan, Yu Zhao, Jingwang Huang, Jian Yang, Zhenhe Wu, Haoyang Zeng, Xiaoyan Gu, Weichao Sun, Yanbo Zhai, Yujie Mao, Zhuoru Jiang, Jiang Zhong, Shuangyong Song, Yongxiang Li, Zhongjiang He*. [[Paper]](https://arxiv.org/abs/2601.07280v1)
- **Thinking with Deltas: Incentivizing Reinforcement Learning via Differential Visual Reasoning Policy** <2026-01-11>  
  *Shujian Gao, Yuan Wang, Jiangtao Yan, Zuxuan Wu, Yu-Gang Jiang*. [[Paper]](https://arxiv.org/abs/2601.06801v1)
- **GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO** <2026-01-11>  
  *Shubhashis Roy Dipta, Khairul Mahbub, Nadia Najjar*. [[Paper]](https://arxiv.org/abs/2601.06767v1)
- **Plasticity vs. Rigidity: The Impact of Low-Rank Adapters on Reasoning on a Micro-Budget** <2026-01-10>  
  *Zohaib Khan, Omer Tafveez, Zoha Hayat Bhatti*. [[Paper]](https://arxiv.org/abs/2601.06677v1)
- **Revisiting Entropy in Reinforcement Learning for Large Reasoning Models** <2026-01-10>  
  *Renren Jin, Pengzhi Gao, Yuqi Ren, Zhuowen Han, Tongxuan Zhang, Wuwei Huang, Wei Liu, Jian Luan, Deyi Xiong*. [[Paper]](https://arxiv.org/abs/2511.05993v2)
- **IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck** <2026-01-09>  
  *Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, Yu Kang*. [[Paper]](https://arxiv.org/abs/2601.05870v1)
- **Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR** <2026-01-09>  
  *Abdelaziz Bounhar, Hadi Abdine, Evan Dufraisse, Ahmad Chamma, Amr Mohamed, Dani Bouch, Michalis Vazirgiannis, Guokan Shang*. [[Paper]](https://arxiv.org/abs/2511.01937v2)
- **From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation** <2026-01-09>  
  *Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu*. [[Paper]](https://arxiv.org/abs/2601.05787v1)
- **Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR** <2026-01-09>  
  *Zijun Min, Bingshuai Liu, Ante Wang, Long Zhang, Anxiang Zeng, Haibo Zhang, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2601.05607v1)
- **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** <2026-01-09>  
  *Xinping Zhao, Shouzheng Huang, Yan Zhong, Xinshuo Hu, Meishan Zhang, Baotian Hu, Min Zhang*. [[Paper]](https://arxiv.org/abs/2507.15586v5)
- **Reinforced Efficient Reasoning via Semantically Diverse Exploration** <2026-01-08>  
  *Ziqi Zhao, Zhaochun Ren, Jiahong Zou, Liu Yang, Zhiwei Xu, Xuri Ge, Zhumin Chen, Xinyu Ma, Daiting Shi, Shuaiqiang Wang, Dawei Yin, Xin Xin*. [[Paper]](https://arxiv.org/abs/2601.05053v1)
- **Character-R1: Enhancing Role-Aware Reasoning in Role-Playing Agents via RLVR** <2026-01-08>  
  *Yihong Tang, Kehai Chen, Xuefeng Bai, Benyou Wang, Zeming Liu, Haifeng Wang, Min Zhang*. [[Paper]](https://arxiv.org/abs/2601.04611v1)
- **Not All Steps are Informative: On the Linearity of LLMs' RLVR Training** <2026-01-08>  
  *Tianle Wang, Zhongyuan Wu, Shenghao Jin, Hao Xu, Wei Chen, Ning Miao*. [[Paper]](https://arxiv.org/abs/2601.04537v1)
- **Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification** <2026-01-08>  
  *Rui Sun, Yifan Sun, Sheng Xu, Li Zhao, Jing Li, Daxin Jiang, Cheng Hua, Zuo Bai*. [[Paper]](https://arxiv.org/abs/2601.03948v2)
- **Rate or Fate? RLV$^\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards** <2026-01-07>  
  *Ali Rad, Khashayar Filom, Darioush Keivan, Peyman Mohajerin Esfahani, Ehsan Kamalinejad*. [[Paper]](https://arxiv.org/abs/2601.04411v1)
- **Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models** <2026-01-07>  
  *Wei Wu, Liyi Chen, Congxi Xiao, Tianfu Wang, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu, Hui Xiong*. [[Paper]](https://arxiv.org/abs/2601.03969v1)
- **Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning** <2026-01-07>  
  *Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du*. [[Paper]](https://arxiv.org/abs/2601.03823v1)
- **ETR: Outcome-Guided Elastic Trust Regions for Policy Optimization** <2026-01-07>  
  *Shijie Zhang, Kevin Zhang, Zheyuan Gu, Xiang Guo, Rujun Guo, Shaoyu Liu, Guanjun Jiang, Xiaozhao Wang*. [[Paper]](https://arxiv.org/abs/2601.03723v1)
- **Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning** <2026-01-16>  
  *Hongye Cao, Zhixin Bai, Ziyue Peng, Boyan Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao*. [[Paper]](https://arxiv.org/abs/2512.04359v3)
- **Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs** <2026-01-16>  
  *Lecheng Yan, Ruizhe Li, Guanhua Chen, Qing Li, Jiahui Geng, Wenxi Li, Vincent Wang, Chris Lee*. [[Paper]](https://arxiv.org/abs/2601.11061v1)
- **Many Minds from One Model: Bayesian-Inspired Transformers for Population Diversity** <2026-01-15>  
  *Diji Yang, Yi Zhang*. [[Paper]](https://arxiv.org/abs/2512.25063v2)
- **Better LLM Reasoning via Dual-Play** <2026-01-15>  
  *Zhengxin Zhang, Chengyu Huang, Aochong Oliver Li, Claire Cardie*. [[Paper]](https://arxiv.org/abs/2511.11881v3)
- **Dual-Uncertainty Guided Policy Learning for Multimodal Reasoning** <2026-01-15>  
  *Rui Liu, Dian Yu, Tong Zheng, Runpeng Dai, Zongxia Li, Wenhao Yu, Zhenwen Liang, Linfeng Song, Haitao Mi, Pratap Tokekar, Dong Yu*. [[Paper]](https://arxiv.org/abs/2510.01444v2)
- **Future-as-Label: Scalable Supervision from Real-World Outcomes** <2026-01-14>  
  *Benjamin Turtel, Paul Wilczewski, Danny Franklin, Kris Skothiem*. [[Paper]](https://arxiv.org/abs/2601.06336v2)
- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** <2026-01-14>  
  *Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He*. [[Paper]](https://arxiv.org/abs/2601.09361v1)
- **Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following** <2026-01-13>  
  *Yirong Zeng, Yufei Liu, Xiao Ding, Yutai Hou, Yuxian Wang, Haonan Song, Wu Ning, Dandan Tu, Qixun Zhang, Bibo Cai, Yuxiang He, Ting Liu*. [[Paper]](https://arxiv.org/abs/2601.04954v2)
- **Your Group-Relative Advantage Is Biased** <2026-01-13>  
  *Fengkai Yang, Zherui Chen, Xiaohan Wang, Xiaodong Lu, Jiajun Chai, Guojun Yin, Wei Lin, Shuai Ma, Fuzhen Zhuang, Deqing Wang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2601.08521v1)
- **JudgeRLVR: Judge First, Generate Second for Efficient Reasoning** <2026-01-13>  
  *Jiangshan Duo, Hanyu Li, Hailin Zhang, Yudong Wang, Sujian Li, Liang Zhao*. [[Paper]](https://arxiv.org/abs/2601.08468v1)
- **RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation** <2026-01-13>  
  *Sunzhu Li, Jiale Zhao, Miteto Wei, Huimin Ren, Yang Zhou, Jingwen Yang, Shunyu Liu, Kaike Zhang, Wei Chen*. [[Paper]](https://arxiv.org/abs/2601.08430v1)
- **The End of Reward Engineering: How LLMs Are Redefining Multi-Agent Coordination** <2026-01-13>  
  *Haoran Su, Yandong Sun, Congjia Yu*. [[Paper]](https://arxiv.org/abs/2601.08237v1)
- **ICPO: Intrinsic Confidence-Driven Group Relative Preference Optimization for Efficient Reinforcement Learning** <2026-01-13>  
  *Jinpeng Wang, Chao Li, Ting Ye, Mengyuan Zhang, Wei Liu, Jian Luan*. [[Paper]](https://arxiv.org/abs/2511.21005v5)
- **Beyond Single-Shot: Multi-step Tool Retrieval via Query Planning** <2026-01-12>  
  *Wei Fang, James Glass*. [[Paper]](https://arxiv.org/abs/2601.07782v1)
- **Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?** <2026-01-12>  
  *Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash*. [[Paper]](https://arxiv.org/abs/2506.19467v3)
- **SPEC-RL: Accelerating On-Policy Reinforcement Learning with Speculative Rollouts** <2026-01-12>  
  *Bingshuai Liu, Ante Wang, Zijun Min, Liang Yao, Haibo Zhang, Yang Liu, Xu Han, Peng Li, Anxiang Zeng, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2509.23232v3)
- **Reward Modeling from Natural Language Human Feedback** <2026-01-12>  
  *Zongqi Wang, Rui Wang, Yuchuan Wu, Yiyao Yu, Pinyi Zhang, Shaoning Sun, Yujiu Yang, Yongbin Li*. [[Paper]](https://arxiv.org/abs/2601.07349v1)
- **Segmental Advantage Estimation: Enhancing PPO for Long-Context LLM Training** <2026-01-12>  
  *Xue Gong, Qi Yi, Ziyuan Nan, Guanhua Huang, Kejiao Li, Yuhao Jiang, Ruibin Xiong, Zenan Xu, Jiaming Guo, Shaohui Peng, Bo Zhou*. [[Paper]](https://arxiv.org/abs/2601.07320v1)
- **ReasonTabQA: A Comprehensive Benchmark for Table Question Answering from Real World Industrial Scenarios** <2026-01-12>  
  *Changzai Pan, Jie Zhang, Kaiwen Wei, Chenshuo Pan, Yu Zhao, Jingwang Huang, Jian Yang, Zhenhe Wu, Haoyang Zeng, Xiaoyan Gu, Weichao Sun, Yanbo Zhai, Yujie Mao, Zhuoru Jiang, Jiang Zhong, Shuangyong Song, Yongxiang Li, Zhongjiang He*. [[Paper]](https://arxiv.org/abs/2601.07280v1)
- **Thinking with Deltas: Incentivizing Reinforcement Learning via Differential Visual Reasoning Policy** <2026-01-11>  
  *Shujian Gao, Yuan Wang, Jiangtao Yan, Zuxuan Wu, Yu-Gang Jiang*. [[Paper]](https://arxiv.org/abs/2601.06801v1)
- **GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO** <2026-01-11>  
  *Shubhashis Roy Dipta, Khairul Mahbub, Nadia Najjar*. [[Paper]](https://arxiv.org/abs/2601.06767v1)
- **Plasticity vs. Rigidity: The Impact of Low-Rank Adapters on Reasoning on a Micro-Budget** <2026-01-10>  
  *Zohaib Khan, Omer Tafveez, Zoha Hayat Bhatti*. [[Paper]](https://arxiv.org/abs/2601.06677v1)
- **Revisiting Entropy in Reinforcement Learning for Large Reasoning Models** <2026-01-10>  
  *Renren Jin, Pengzhi Gao, Yuqi Ren, Zhuowen Han, Tongxuan Zhang, Wuwei Huang, Wei Liu, Jian Luan, Deyi Xiong*. [[Paper]](https://arxiv.org/abs/2511.05993v2)
- **IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck** <2026-01-09>  
  *Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, Yu Kang*. [[Paper]](https://arxiv.org/abs/2601.05870v1)
- **Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR** <2026-01-09>  
  *Abdelaziz Bounhar, Hadi Abdine, Evan Dufraisse, Ahmad Chamma, Amr Mohamed, Dani Bouch, Michalis Vazirgiannis, Guokan Shang*. [[Paper]](https://arxiv.org/abs/2511.01937v2)
- **From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation** <2026-01-09>  
  *Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu*. [[Paper]](https://arxiv.org/abs/2601.05787v1)
- **Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR** <2026-01-09>  
  *Zijun Min, Bingshuai Liu, Ante Wang, Long Zhang, Anxiang Zeng, Haibo Zhang, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2601.05607v1)
- **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** <2026-01-09>  
  *Xinping Zhao, Shouzheng Huang, Yan Zhong, Xinshuo Hu, Meishan Zhang, Baotian Hu, Min Zhang*. [[Paper]](https://arxiv.org/abs/2507.15586v5)
- **Reinforced Efficient Reasoning via Semantically Diverse Exploration** <2026-01-08>  
  *Ziqi Zhao, Zhaochun Ren, Jiahong Zou, Liu Yang, Zhiwei Xu, Xuri Ge, Zhumin Chen, Xinyu Ma, Daiting Shi, Shuaiqiang Wang, Dawei Yin, Xin Xin*. [[Paper]](https://arxiv.org/abs/2601.05053v1)
- **Character-R1: Enhancing Role-Aware Reasoning in Role-Playing Agents via RLVR** <2026-01-08>  
  *Yihong Tang, Kehai Chen, Xuefeng Bai, Benyou Wang, Zeming Liu, Haifeng Wang, Min Zhang*. [[Paper]](https://arxiv.org/abs/2601.04611v1)
- **Not All Steps are Informative: On the Linearity of LLMs' RLVR Training** <2026-01-08>  
  *Tianle Wang, Zhongyuan Wu, Shenghao Jin, Hao Xu, Wei Chen, Ning Miao*. [[Paper]](https://arxiv.org/abs/2601.04537v1)
- **Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification** <2026-01-08>  
  *Rui Sun, Yifan Sun, Sheng Xu, Li Zhao, Jing Li, Daxin Jiang, Cheng Hua, Zuo Bai*. [[Paper]](https://arxiv.org/abs/2601.03948v2)
- **Rate or Fate? RLV$^\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards** <2026-01-07>  
  *Ali Rad, Khashayar Filom, Darioush Keivan, Peyman Mohajerin Esfahani, Ehsan Kamalinejad*. [[Paper]](https://arxiv.org/abs/2601.04411v1)
- **Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models** <2026-01-07>  
  *Wei Wu, Liyi Chen, Congxi Xiao, Tianfu Wang, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu, Hui Xiong*. [[Paper]](https://arxiv.org/abs/2601.03969v1)
- **Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning** <2026-01-07>  
  *Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du*. [[Paper]](https://arxiv.org/abs/2601.03823v1)
- **ETR: Outcome-Guided Elastic Trust Regions for Policy Optimization** <2026-01-07>  
  *Shijie Zhang, Kevin Zhang, Zheyuan Gu, Xiang Guo, Rujun Guo, Shaoyu Liu, Guanjun Jiang, Xiaozhao Wang*. [[Paper]](https://arxiv.org/abs/2601.03723v1)
- **Think Outside the Policy: In-Context Steered Policy Optimization** <2026-01-07>  
  *Hsiu-Yuan Huang, Chenming Tang, Weijie Liu, Clive Bai, Saiyong Yang, Yunfang Wu*. [[Paper]](https://arxiv.org/abs/2510.26519v2)
- **DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search** <2026-01-07>  
  *Fang Wu, Weihao Xuan, Heli Qi, Ximing Lu, Aaron Tu, Li Erran Li, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2509.25454v3)
- **The Invisible Leash: Why RLVR May or May Not Escape Its Origin** <2026-01-07>  
  *Fang Wu, Weihao Xuan, Ximing Lu, Mingjie Liu, Yi Dong, Zaid Harchaoui, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2507.14843v3)
- **UltraLogic: Enhancing LLM Reasoning through Large-Scale Data Synthesis and Bipolar Float Reward** <2026-01-06>  
  *Yile Liu, Yixian Liu, Zongwei Li, Yufei Huang, Xinhua Feng, Zhichao Hu, Jinglu Hu, Jianfeng Yan, Fengzong Lian, Yuhong Liu*. [[Paper]](https://arxiv.org/abs/2601.03205v1)
- **Do Not Step Into the Same River Twice: Learning to Reason from Trial and Error** <2026-01-06>  
  *Chenming Tang, Hsiu-Yuan Huang, Weijie Liu, Clive Bai, Saiyong Yang, Yunfang Wu*. [[Paper]](https://arxiv.org/abs/2510.26109v3)
- **Evaluating Parameter Efficient Methods for RLVR** <2025-12-30>  
  *Qingyu Yin, Yulun Wu, Zhennan Shen, Sunbowen Li, Zhilin Wang, Yanshu Li, Chak Tou Leong, Jiale Kang, Jinjin Gu*. [[Paper]](https://arxiv.org/abs/2512.23165v2)
- **OpenSIR: Open-Ended Self-Improving Reasoner** <2025-12-30>  
  *Wai-Chung Kwan, Joshua Ong Jun Leang, Pavlos Vougiouklis, Jeff Z. Pan, Marco Valentino, Pasquale Minervini*. [[Paper]](https://arxiv.org/abs/2511.00602v2)
- **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** <2025-12-28>  
  *Ken Huang, Jerry Huang*. [[Paper]](https://arxiv.org/abs/2512.23760v1)
- **No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping** <2025-12-27>  
  *Thanh-Long V. Le, Myeongho Jeon, Kim Vu, Viet Lai, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2509.21880v2)
- **Search Self-play: Pushing the Frontier of Agent Capability without Supervision** <2025-12-26>  
  *Hongliang Lu, Yuhang Wen, Pengyu Cheng, Ruijin Ding, Jiaqi Guo, Haotian Xu, Chutian Wang, Haonan Chen, Xiaoxi Jiang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2510.18821v2)
- **StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion** <2025-12-26>  
  *Yutong Wu, Di Huang, Ruosi Wan, Yue Peng, Shijie Shang, Chenrui Cao, Lei Qi, Rui Zhang, Zidong Du, Jie Yan, Xing Hu*. [[Paper]](https://arxiv.org/abs/2508.04440v3)
- **AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning in LLMs** <2025-12-25>  
  *Xiang Feng, Wentao Jiang, Zengmao Wang, Yong Luo, Pingbo Xu, Baosheng Yu, Hua Jin, Bo Du, Jing Zhang*. [[Paper]](https://arxiv.org/abs/2504.02404v3)
- **Rethinking Sample Polarity in Reinforcement Learning with Verifiable Rewards** <2025-12-25>  
  *Xinyu Tang, Yuliang Zhan, Zhixun Li, Wayne Xin Zhao, Zhenduo Zhang, Zujie Wen, Zhiqiang Zhang, Jun Zhou*. [[Paper]](https://arxiv.org/abs/2512.21625v1)
- **Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning** <2025-12-25>  
  *Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang*. [[Paper]](https://arxiv.org/abs/2512.19920v2)
- **IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck** <2026-01-09>  
  *Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, Yu Kang*. [[Paper]](https://arxiv.org/abs/2601.05870v1)
- **Shorter but not Worse: Frugal Reasoning via Easy Samples as Length Regularizers in Math RLVR** <2026-01-09>  
  *Abdelaziz Bounhar, Hadi Abdine, Evan Dufraisse, Ahmad Chamma, Amr Mohamed, Dani Bouch, Michalis Vazirgiannis, Guokan Shang*. [[Paper]](https://arxiv.org/abs/2511.01937v2)
- **From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation** <2026-01-09>  
  *Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu*. [[Paper]](https://arxiv.org/abs/2601.05787v1)
- **SPEC-RL: Accelerating On-Policy Reinforcement Learning via Speculative Rollouts** <2026-01-09>  
  *Bingshuai Liu, Ante Wang, Zijun Min, Liang Yao, Haibo Zhang, Yang Liu, Anxiang Zeng, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2509.23232v2)
- **Orchestrating Tokens and Sequences: Dynamic Hybrid Policy Optimization for RLVR** <2026-01-09>  
  *Zijun Min, Bingshuai Liu, Ante Wang, Long Zhang, Anxiang Zeng, Haibo Zhang, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2601.05607v1)
- **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** <2026-01-09>  
  *Xinping Zhao, Shouzheng Huang, Yan Zhong, Xinshuo Hu, Meishan Zhang, Baotian Hu, Min Zhang*. [[Paper]](https://arxiv.org/abs/2507.15586v5)
- **Reinforced Efficient Reasoning via Semantically Diverse Exploration** <2026-01-08>  
  *Ziqi Zhao, Zhaochun Ren, Jiahong Zou, Liu Yang, Zhiwei Xu, Xuri Ge, Zhumin Chen, Xinyu Ma, Daiting Shi, Shuaiqiang Wang, Dawei Yin, Xin Xin*. [[Paper]](https://arxiv.org/abs/2601.05053v1)
- **Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following** <2026-01-08>  
  *Yirong Zeng, Yufei Liu, Xiao Ding, Yutai Hou, Yuxian Wang, Haonan Song, Wu Ning, Dandan Tu, Qixun Zhang, Bibo Cai, Yuxiang He, Ting Liu*. [[Paper]](https://arxiv.org/abs/2601.04954v1)
- **Character-R1: Enhancing Role-Aware Reasoning in Role-Playing Agents via RLVR** <2026-01-08>  
  *Yihong Tang, Kehai Chen, Xuefeng Bai, Benyou Wang, Zeming Liu, Haifeng Wang, Min Zhang*. [[Paper]](https://arxiv.org/abs/2601.04611v1)
- **Not All Steps are Informative: On the Linearity of LLMs' RLVR Training** <2026-01-08>  
  *Tianle Wang, Zhongyuan Wu, Shenghao Jin, Hao Xu, Wei Chen, Ning Miao*. [[Paper]](https://arxiv.org/abs/2601.04537v1)
- **Trade-R1: Bridging Verifiable Rewards to Stochastic Environments via Process-Level Reasoning Verification** <2026-01-08>  
  *Rui Sun, Yifan Sun, Sheng Xu, Li Zhao, Jing Li, Daxin Jiang, Cheng Hua, Zuo Bai*. [[Paper]](https://arxiv.org/abs/2601.03948v2)
- **Rate or Fate? RLV$^\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards** <2026-01-07>  
  *Ali Rad, Khashayar Filom, Darioush Keivan, Peyman Mohajerin Esfahani, Ehsan Kamalinejad*. [[Paper]](https://arxiv.org/abs/2601.04411v1)
- **Anti-Length Shift: Dynamic Outlier Truncation for Training Efficient Reasoning Models** <2026-01-07>  
  *Wei Wu, Liyi Chen, Congxi Xiao, Tianfu Wang, Qimeng Wang, Chengqiang Lu, Yan Gao, Yi Wu, Yao Hu, Hui Xiong*. [[Paper]](https://arxiv.org/abs/2601.03969v1)
- **Step Potential Advantage Estimation: Harnessing Intermediate Confidence and Correctness for Efficient Mathematical Reasoning** <2026-01-07>  
  *Fei Wu, Zhenrong Zhang, Qikai Chang, Jianshu Zhang, Quan Liu, Jun Du*. [[Paper]](https://arxiv.org/abs/2601.03823v1)
- **ETR: Outcome-Guided Elastic Trust Regions for Policy Optimization** <2026-01-07>  
  *Shijie Zhang, Kevin Zhang, Zheyuan Gu, Xiang Guo, Rujun Guo, Shaoyu Liu, Guanjun Jiang, Xiaozhao Wang*. [[Paper]](https://arxiv.org/abs/2601.03723v1)
- **Think Outside the Policy: In-Context Steered Policy Optimization** <2026-01-07>  
  *Hsiu-Yuan Huang, Chenming Tang, Weijie Liu, Clive Bai, Saiyong Yang, Yunfang Wu*. [[Paper]](https://arxiv.org/abs/2510.26519v2)
- **DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search** <2026-01-07>  
  *Fang Wu, Weihao Xuan, Heli Qi, Ximing Lu, Aaron Tu, Li Erran Li, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2509.25454v3)
- **The Invisible Leash: Why RLVR May or May Not Escape Its Origin** <2026-01-07>  
  *Fang Wu, Weihao Xuan, Ximing Lu, Mingjie Liu, Yi Dong, Zaid Harchaoui, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2507.14843v3)
- **UltraLogic: Enhancing LLM Reasoning through Large-Scale Data Synthesis and Bipolar Float Reward** <2026-01-06>  
  *Yile Liu, Yixian Liu, Zongwei Li, Yufei Huang, Xinhua Feng, Zhichao Hu, Jinglu Hu, Jianfeng Yan, Fengzong Lian, Yuhong Liu*. [[Paper]](https://arxiv.org/abs/2601.03205v1)
- **Do Not Step Into the Same River Twice: Learning to Reason from Trial and Error** <2026-01-06>  
  *Chenming Tang, Hsiu-Yuan Huang, Weijie Liu, Clive Bai, Saiyong Yang, Yunfang Wu*. [[Paper]](https://arxiv.org/abs/2510.26109v3)
- **Many Minds from One Model: Bayesian Transformers for Population Intelligence** <2025-12-31>  
  *Diji Yang, Yi Zhang*. [[Paper]](https://arxiv.org/abs/2512.25063v1)
- **Evaluating Parameter Efficient Methods for RLVR** <2025-12-30>  
  *Qingyu Yin, Yulun Wu, Zhennan Shen, Sunbowen Li, Zhilin Wang, Yanshu Li, Chak Tou Leong, Jiale Kang, Jinjin Gu*. [[Paper]](https://arxiv.org/abs/2512.23165v2)
- **OpenSIR: Open-Ended Self-Improving Reasoner** <2025-12-30>  
  *Wai-Chung Kwan, Joshua Ong Jun Leang, Pavlos Vougiouklis, Jeff Z. Pan, Marco Valentino, Pasquale Minervini*. [[Paper]](https://arxiv.org/abs/2511.00602v2)
- **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** <2025-12-28>  
  *Ken Huang, Jerry Huang*. [[Paper]](https://arxiv.org/abs/2512.23760v1)
- **No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping** <2025-12-27>  
  *Thanh-Long V. Le, Myeongho Jeon, Kim Vu, Viet Lai, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2509.21880v2)
- **Search Self-play: Pushing the Frontier of Agent Capability without Supervision** <2025-12-26>  
  *Hongliang Lu, Yuhang Wen, Pengyu Cheng, Ruijin Ding, Jiaqi Guo, Haotian Xu, Chutian Wang, Haonan Chen, Xiaoxi Jiang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2510.18821v2)
- **StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion** <2025-12-26>  
  *Yutong Wu, Di Huang, Ruosi Wan, Yue Peng, Shijie Shang, Chenrui Cao, Lei Qi, Rui Zhang, Zidong Du, Jie Yan, Xing Hu*. [[Paper]](https://arxiv.org/abs/2508.04440v3)
- **AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning in LLMs** <2025-12-25>  
  *Xiang Feng, Wentao Jiang, Zengmao Wang, Yong Luo, Pingbo Xu, Baosheng Yu, Hua Jin, Bo Du, Jing Zhang*. [[Paper]](https://arxiv.org/abs/2504.02404v3)
- **Rethinking Sample Polarity in Reinforcement Learning with Verifiable Rewards** <2025-12-25>  
  *Xinyu Tang, Yuliang Zhan, Zhixun Li, Wayne Xin Zhao, Zhenduo Zhang, Zujie Wen, Zhiqiang Zhang, Jun Zhou*. [[Paper]](https://arxiv.org/abs/2512.21625v1)
- **Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning** <2025-12-25>  
  *Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang*. [[Paper]](https://arxiv.org/abs/2512.19920v2)
- **dUltra: Ultra-Fast Diffusion Language Models via Reinforcement Learning** <2025-12-24>  
  *Shirui Chen, Jiantao Jiao, Lillian J. Ratliff, Banghua Zhu*. [[Paper]](https://arxiv.org/abs/2512.21446v1)
- **SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning** <2025-12-24>  
  *Xiaojun Guo, Runyu Zhou, Yifei Wang, Qi Zhang, Chenheng Zhang, Stefanie Jegelka, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Yisen Wang*. [[Paper]](https://arxiv.org/abs/2510.16416v3)
- **Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers** <2025-12-24>  
  *Xin-Qiang Cai, Wei Wang, Feng Liu, Tongliang Liu, Gang Niu, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2510.00915v3)
- **Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners** <2025-12-24>  
  *Xin Xu, Cliveb AI, Kai Yang, Tianhao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2509.26226v2)
- **The Silent Scholar Problem: A Probabilistic Framework for Breaking Epistemic Asymmetry in LLM Agents** <2025-12-24>  
  *Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng*. [[Paper]](https://arxiv.org/abs/2512.20884v1)
- **Generalization of RLVR Using Causal Reasoning as a Testbed** <2025-12-23>  
  *Brian Lu, Hongyu Zhao, Shuo Sun, Hao Peng, Rui Ding, Hongyuan Mei*. [[Paper]](https://arxiv.org/abs/2512.20760v1)
- **Reinforcement Learning for Large Model: A Survey** <2025-12-23>  
  *Weijia Wu, Chen Gao, Joya Chen, Kevin Qinghong Lin, Qingwei Meng, Yiming Zhang, Yuke Qiu, Hong Zhou, Mike Zheng Shou*. [[Paper]](https://arxiv.org/abs/2508.08189v3)
- **Scaling Reinforcement Learning for Content Moderation with Large Language Models** <2025-12-23>  
  *Hamed Firooz, Rui Liu, Yuchen Lu, Zhenyu Hou, Fangzhou Xiong, Xiaoyang Zhang, Changshu Jian, Zhicheng Zhu, Jiayuan Ma, Jacob Tao, Chaitali Gupta, Xiaochang Peng, Shike Mei, Hang Cui, Yang Qin, Shuo Tang, Jason Gaedtke, Arpit Mittal*. [[Paper]](https://arxiv.org/abs/2512.20061v1)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal** <2025-12-22>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v1)
- **SPELL: Self-Play Reinforcement Learning for evolving Long-Context Language Models** <2025-12-22>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v2)
- **Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling** <2025-12-22>  
  *Yitian Chen, Jingfan Xia, Siyu Shao, Dongdong Ge, Yinyu Ye*. [[Paper]](https://arxiv.org/abs/2505.11792v3)
- **Sharpness-Controlled Group Relative Policy Optimization with Token-Level Probability Shaping** <2025-12-22>  
  *Tue Le, Nghi D. Q. Bui, Linh Ngo Van, Trung Le*. [[Paper]](https://arxiv.org/abs/2511.00066v2)
- **CORE: Concept-Oriented Reinforcement for Bridging the Definition-Application Gap in Mathematical Reasoning** <2025-12-21>  
  *Zijun Gao, Zhikun Xu, Xiao Ye, Ben Zhou*. [[Paper]](https://arxiv.org/abs/2512.18857v1)
- **Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward** <2025-12-21>  
  *Peter Chen, Xiaopeng Li, Ziniu Li, Wotao Yin, Xi Chen, Tianyi Lin*. [[Paper]](https://arxiv.org/abs/2512.16912v2)
- **A Theoretical Lens for RL-Tuned Language Models via Energy-Based Models** <2025-12-21>  
  *Zhiquan Tan, Yinrong Hong*. [[Paper]](https://arxiv.org/abs/2512.18730v1)
- **PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design** <2025-12-21>  
  *Andy Xu, Rohan Desai, Larry Wang, Gabriel Hope, Ethan Ritz*. [[Paper]](https://arxiv.org/abs/2509.07150v3)
- **Stable and Efficient Single-Rollout RL for Multimodal Reasoning** <2025-12-20>  
  *Rui Liu, Dian Yu, Lei Ke, Haolin Liu, Yujun Zhou, Zhenwen Liang, Haitao Mi, Pratap Tokekar, Dong Yu*. [[Paper]](https://arxiv.org/abs/2512.18215v1)
- **AdaTooler-V: Adaptive Tool-Use for Images and Videos** <2025-12-19>  
  *Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue*. [[Paper]](https://arxiv.org/abs/2512.16918v2)
- **MEML-GRPO: Heterogeneous Multi-Expert Mutual Learning for RLVR Advancement** <2025-12-18>  
  *Weitao Jia, Jinghui Lu, Haiyang Yu, Siqi Wang, Guozhi Tang, An-Lan Wang, Weijie Yin, Dingkang Yang, Yuxiang Nie, Bin Shan, Hao Feng, Irene Li, Kun Yang, Han Wang, Jingqun Tang, Teng Fu, Changhong Jin, Chao Feng, Xiaohui Lv, Can Huang*. [[Paper]](https://arxiv.org/abs/2508.09670v2)
- **Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning** <2025-12-18>  
  *Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang*. [[Paper]](https://arxiv.org/abs/2512.15146v2)
- **Many Minds from One Model: Bayesian Transformers for Population Intelligence** <2025-12-31>  
  *Diji Yang, Yi Zhang*. [[Paper]](https://arxiv.org/abs/2512.25063v1)
- **Evaluating Parameter Efficient Methods for RLVR** <2025-12-30>  
  *Qingyu Yin, Yulun Wu, Zhennan Shen, Sunbowen Li, Zhilin Wang, Yanshu Li, Chak Tou Leong, Jiale Kang, Jinjin Gu*. [[Paper]](https://arxiv.org/abs/2512.23165v2)
- **OpenSIR: Open-Ended Self-Improving Reasoner** <2025-12-30>  
  *Wai-Chung Kwan, Joshua Ong Jun Leang, Pavlos Vougiouklis, Jeff Z. Pan, Marco Valentino, Pasquale Minervini*. [[Paper]](https://arxiv.org/abs/2511.00602v2)
- **Audited Skill-Graph Self-Improvement for Agentic LLMs via Verifiable Rewards, Experience Synthesis, and Continual Memory** <2025-12-28>  
  *Ken Huang, Jerry Huang*. [[Paper]](https://arxiv.org/abs/2512.23760v1)
- **No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping** <2025-12-27>  
  *Thanh-Long V. Le, Myeongho Jeon, Kim Vu, Viet Lai, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2509.21880v2)
- **Search Self-play: Pushing the Frontier of Agent Capability without Supervision** <2025-12-26>  
  *Hongliang Lu, Yuhang Wen, Pengyu Cheng, Ruijin Ding, Jiaqi Guo, Haotian Xu, Chutian Wang, Haonan Chen, Xiaoxi Jiang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2510.18821v2)
- **StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion** <2025-12-26>  
  *Yutong Wu, Di Huang, Ruosi Wan, Yue Peng, Shijie Shang, Chenrui Cao, Lei Qi, Rui Zhang, Zidong Du, Jie Yan, Xing Hu*. [[Paper]](https://arxiv.org/abs/2508.04440v3)
- **AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning in LLMs** <2025-12-25>  
  *Xiang Feng, Wentao Jiang, Zengmao Wang, Yong Luo, Pingbo Xu, Baosheng Yu, Hua Jin, Bo Du, Jing Zhang*. [[Paper]](https://arxiv.org/abs/2504.02404v3)
- **Rethinking Sample Polarity in Reinforcement Learning with Verifiable Rewards** <2025-12-25>  
  *Xinyu Tang, Yuliang Zhan, Zhixun Li, Wayne Xin Zhao, Zhenduo Zhang, Zujie Wen, Zhiqiang Zhang, Jun Zhou*. [[Paper]](https://arxiv.org/abs/2512.21625v1)
- **Mitigating LLM Hallucination via Behaviorally Calibrated Reinforcement Learning** <2025-12-25>  
  *Jiayun Wu, Jiashuo Liu, Zhiyuan Zeng, Tianyang Zhan, Tianle Cai, Wenhao Huang*. [[Paper]](https://arxiv.org/abs/2512.19920v2)
- **dUltra: Ultra-Fast Diffusion Language Models via Reinforcement Learning** <2025-12-24>  
  *Shirui Chen, Jiantao Jiao, Lillian J. Ratliff, Banghua Zhu*. [[Paper]](https://arxiv.org/abs/2512.21446v1)
- **SSL4RL: Revisiting Self-supervised Learning as Intrinsic Reward for Visual-Language Reasoning** <2025-12-24>  
  *Xiaojun Guo, Runyu Zhou, Yifei Wang, Qi Zhang, Chenheng Zhang, Stefanie Jegelka, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Yisen Wang*. [[Paper]](https://arxiv.org/abs/2510.16416v3)
- **Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers** <2025-12-24>  
  *Xin-Qiang Cai, Wei Wang, Feng Liu, Tongliang Liu, Gang Niu, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2510.00915v3)
- **Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners** <2025-12-24>  
  *Xin Xu, Cliveb AI, Kai Yang, Tianhao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2509.26226v2)
- **The Silent Scholar Problem: A Probabilistic Framework for Breaking Epistemic Asymmetry in LLM Agents** <2025-12-24>  
  *Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng*. [[Paper]](https://arxiv.org/abs/2512.20884v1)
- **Generalization of RLVR Using Causal Reasoning as a Testbed** <2025-12-23>  
  *Brian Lu, Hongyu Zhao, Shuo Sun, Hao Peng, Rui Ding, Hongyuan Mei*. [[Paper]](https://arxiv.org/abs/2512.20760v1)
- **Reinforcement Learning for Large Model: A Survey** <2025-12-23>  
  *Weijia Wu, Chen Gao, Joya Chen, Kevin Qinghong Lin, Qingwei Meng, Yiming Zhang, Yuke Qiu, Hong Zhou, Mike Zheng Shou*. [[Paper]](https://arxiv.org/abs/2508.08189v3)
- **Scaling Reinforcement Learning for Content Moderation with Large Language Models** <2025-12-23>  
  *Hamed Firooz, Rui Liu, Yuchen Lu, Zhenyu Hou, Fangzhou Xiong, Xiaoyang Zhang, Changshu Jian, Zhicheng Zhu, Jiayuan Ma, Jacob Tao, Chaitali Gupta, Xiaochang Peng, Shike Mei, Hang Cui, Yang Qin, Shuo Tang, Jason Gaedtke, Arpit Mittal*. [[Paper]](https://arxiv.org/abs/2512.20061v1)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal** <2025-12-22>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v1)
- **SPELL: Self-Play Reinforcement Learning for evolving Long-Context Language Models** <2025-12-22>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v2)
- **Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling** <2025-12-22>  
  *Yitian Chen, Jingfan Xia, Siyu Shao, Dongdong Ge, Yinyu Ye*. [[Paper]](https://arxiv.org/abs/2505.11792v3)
- **Sharpness-Controlled Group Relative Policy Optimization with Token-Level Probability Shaping** <2025-12-22>  
  *Tue Le, Nghi D. Q. Bui, Linh Ngo Van, Trung Le*. [[Paper]](https://arxiv.org/abs/2511.00066v2)
- **CORE: Concept-Oriented Reinforcement for Bridging the Definition-Application Gap in Mathematical Reasoning** <2025-12-21>  
  *Zijun Gao, Zhikun Xu, Xiao Ye, Ben Zhou*. [[Paper]](https://arxiv.org/abs/2512.18857v1)
- **Exploration vs Exploitation: Rethinking RLVR through Clipping, Entropy, and Spurious Reward** <2025-12-21>  
  *Peter Chen, Xiaopeng Li, Ziniu Li, Wotao Yin, Xi Chen, Tianyi Lin*. [[Paper]](https://arxiv.org/abs/2512.16912v2)
- **A Theoretical Lens for RL-Tuned Language Models via Energy-Based Models** <2025-12-21>  
  *Zhiquan Tan, Yinrong Hong*. [[Paper]](https://arxiv.org/abs/2512.18730v1)
- **PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design** <2025-12-21>  
  *Andy Xu, Rohan Desai, Larry Wang, Gabriel Hope, Ethan Ritz*. [[Paper]](https://arxiv.org/abs/2509.07150v3)
- **Stable and Efficient Single-Rollout RL for Multimodal Reasoning** <2025-12-20>  
  *Rui Liu, Dian Yu, Lei Ke, Haolin Liu, Yujun Zhou, Zhenwen Liang, Haitao Mi, Pratap Tokekar, Dong Yu*. [[Paper]](https://arxiv.org/abs/2512.18215v1)
- **AdaTooler-V: Adaptive Tool-Use for Images and Videos** <2025-12-19>  
  *Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue*. [[Paper]](https://arxiv.org/abs/2512.16918v2)
- **MEML-GRPO: Heterogeneous Multi-Expert Mutual Learning for RLVR Advancement** <2025-12-18>  
  *Weitao Jia, Jinghui Lu, Haiyang Yu, Siqi Wang, Guozhi Tang, An-Lan Wang, Weijie Yin, Dingkang Yang, Yuxiang Nie, Bin Shan, Hao Feng, Irene Li, Kun Yang, Han Wang, Jingqun Tang, Teng Fu, Changhong Jin, Chao Feng, Xiaohui Lv, Can Huang*. [[Paper]](https://arxiv.org/abs/2508.09670v2)
- **Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning** <2025-12-18>  
  *Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang*. [[Paper]](https://arxiv.org/abs/2512.15146v2)
- **Well Begun, Half Done: Reinforcement Learning with Prefix Optimization for LLM Reasoning** <2025-12-17>  
  *Yiliu Sun, Zicheng Zhao, Yang Wei, Yanfang Zhang, Chen Gong*. [[Paper]](https://arxiv.org/abs/2512.15274v1)
- **Puzzle Curriculum GRPO for Vision-Centric Reasoning** <2025-12-16>  
  *Ahmadreza Jeddi, Hakki Can Karaimer, Hue Nguyen, Zhongling Wang, Ke Zhao, Javad Rajabi, Ran Zhang, Raghav Goyal, Babak Taati, Radek Grzeszczuk*. [[Paper]](https://arxiv.org/abs/2512.14944v1)
- **TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs** <2025-12-16>  
  *Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang*. [[Paper]](https://arxiv.org/abs/2512.14698v1)
- **Efficient Reinforcement Learning with Semantic and Token Entropy for LLM Reasoning** <2025-12-16>  
  *Hongye Cao, Zhixin Bai, Ziyue Peng, Boyan Wang, Tianpei Yang, Jing Huo, Yuyao Zhang, Yang Gao*. [[Paper]](https://arxiv.org/abs/2512.04359v2)
- **A Scientific Reasoning Model for Organic Synthesis Procedure Generation** <2025-12-15>  
  *Guoqing Liu, Junren Li, Zihan Zhao, Eray Inanc, Krzysztof Maziarz, Jose Garrido Torres, Victor Garcia Satorras, Shoko Ueda, Christopher M. Bishop, Marwin Segler*. [[Paper]](https://arxiv.org/abs/2512.13668v1)
- **Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models** <2025-12-15>  
  *Boxin Wang, Chankyu Lee, Nayeon Lee, Sheng-Chieh Lin, Wenliang Dai, Yang Chen, Yangyi Chen, Zhuolin Yang, Zihan Liu, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping*. [[Paper]](https://arxiv.org/abs/2512.13607v1)
- **TraPO: A Semi-Supervised Reinforcement Learning Framework for Boosting LLM Reasoning** <2025-12-15>  
  *Shenzhi Yang, Guangcheng Zhu, Xing Zheng, Yingfan MA, Zhongqi Chen, Bowen Song, Weiqiang Wang, Junbo Zhao, Gang Chen, Haobo Wang*. [[Paper]](https://arxiv.org/abs/2512.13106v1)
- **Coupled Variational Reinforcement Learning for Language Model General Reasoning** <2025-12-14>  
  *Xueru Wen, Jie Lou, Yanjiang Liu, Hongyu Lin, Ben He, Xianpei Han, Le Sun, Yaojie Lu, Debing Zhang*. [[Paper]](https://arxiv.org/abs/2512.12576v1)
- **More Than the Final Answer: Improving Visual Extraction and Logical Consistency in Vision-Language Models** <2025-12-13>  
  *Hoang Anh Just, Yifei Fan, Handong Zhao, Jiuxiang Gu, Ruiyi Zhang, Simon Jenni, Kushal Kafle, Ruoxi Jia, Jing Shi*. [[Paper]](https://arxiv.org/abs/2512.12487v1)
- **Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR** <2025-12-13>  
  *Xiao Liang, Zhongzhi Li, Yeyun Gong, Yelong Shen, Ying Nian Wu, Zhijiang Guo, Weizhu Chen*. [[Paper]](https://arxiv.org/abs/2508.14029v4)
- **Long-horizon Reasoning Agent for Olympiad-Level Mathematical Problem Solving** <2025-12-12>  
  *Songyang Gao, Yuzhe Gu, Zijian Wu, Lingkai Kong, Wenwei Zhang, Zhongrui Cai, Fan Zheng, Tianyou Ma, Junhao Shen, Haiteng Zhao, Duanyang Zhang, Huilun Zhang, Kuikun Liu, Chengqi Lyu, Yanhui Duan, Chiyu Chen, Ningsheng Ma, Jianfei Gao, Han Lyu, Dahua Lin, Kai Chen*. [[Paper]](https://arxiv.org/abs/2512.10739v2)
- **ICPO: Intrinsic Confidence-Driven Group Relative Preference Optimization for Efficient Reinforcement Learning** <2025-12-12>  
  *Jinpeng Wang, Chao Li, Ting Ye, Mengyuan Zhang, Wei Liu, Jian Luan*. [[Paper]](https://arxiv.org/abs/2511.21005v4)
- **Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning** <2025-12-11>  
  *Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, Yanbo Wen, Fan Song, Jiahao Zhan, Yuyang Lu, Chaoran Tao, Zhiyuan Guo, Jizhou Yu, Tianhao Cheng, Zhiheng Xi, Changhao Jiang, Zhangyue Yin, Yining Zheng, Weifeng Ge, Guanhua Chen, Tao Gui, Xipeng Qiu, Qi Zhang, Xuanjing Huang*. [[Paper]](https://arxiv.org/abs/2505.13886v8)
- **OPV: Outcome-based Process Verifier for Efficient Long Chain-of-Thought Verification** <2025-12-11>  
  *Zijian Wu, Lingkai Kong, Wenwei Zhang, Songyang Gao, Yuzhe Gu, Zhongrui Cai, Tianyou Ma, Yuhong Liu, Zhi Wang, Runyuan Ma, Guangyu Wang, Wei Li, Conghui He, Dahua Lin, Kai Chen*. [[Paper]](https://arxiv.org/abs/2512.10756v1)
- **Training Task Reasoning LLM Agents for Multi-turn Task Planning via Single-turn Reinforcement Learning** <2025-12-08>  
  *Hanjiang Hu, Changliu Liu, Na Li, Yebin Wang*. [[Paper]](https://arxiv.org/abs/2509.20616v2)
- **ReLaX: Reasoning with Latent Exploration for Large Reasoning Models** <2025-12-08>  
  *Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, Jibin Wu*. [[Paper]](https://arxiv.org/abs/2512.07558v1)
- **InfiGUI-G1: Advancing GUI Grounding with Adaptive Exploration Policy Optimization** <2025-12-08>  
  *Yuhang Liu, Zeyu Liu, Shuanghe Zhu, Pengxiang Li, Congkai Xie, Jiasheng Wang, Xavier Hu, Xiaotian Han, Jianbo Yuan, Xinyao Wang, Shengyu Zhang, Hongxia Yang, Fei Wu*. [[Paper]](https://arxiv.org/abs/2508.05731v2)



<h2 id="core-papers">🧠 Core Papers</h2>

<h3 id="rlvr-foundations">RLVR Foundations</h3>

<h4>2025</h4>

1. **Optimizing Anytime Reasoning via Budget Relative Policy Optimization.**   <2025.06>   
    *Penghui Qi, Zichen Liu, Tianyu Pang, Chao Du, Wee Sun Lee, Min Lin.*    **arXiv**   
    [[Paper]](https://arxiv.org/abs/2505.13438)
2. **Response-Level Rewards Are All You Need for Online Reinforcement Learning in LLMs: A Mathematical Perspective.**  <2025.06>    
    *Shenghua He, Tian Xia, Xuan Zhou, Hui Wei.*  **arXiv**   
    [[Paper]](https://www.arxiv.org/abs/2506.02553)
3. **Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts.** <2025.06>   
   *Haizhong Zheng, Yang Zhou, Brian R. Bartoldson, Bhavya Kailkhura, Fan Lai, Jiawei Zhao, Beidi Chen.* **arXiv**  
   [[Paper]](https://www.arxiv.org/abs/2506.02177) [[Code]](https://github.com/Infini-AI-Lab/GRESO/)
4. **KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning.** <2025.06>  
    *Hongling Xu, Qi Zhu, Heyuan Deng, Jinpeng Li, Lu Hou.*, **arXiv**  
   [[Paper]](https://arxiv.org/pdf/2506.02208v1)
5. **Rewarding the Unlikely: Lifting GRPO Beyond Distribution Sharpening.** <2025.06>  
    *Andre He, Daniel Fried, Sean Welleck.* **arXiv**  
   [[Paper]](https://www.arxiv.org/abs/2506.02355)
6. **Critique-GRPO: Advancing LLM Reasoning with Natural Language and Numerical Feedback** <2025.06>  
    *Xiaoying Zhang, Hao Sun, Yipeng Zhang, Kaituo Feng, Chaochao Lu, Chao Yang, Helen Meng* **arXiv**    
   [[Paper]](https://www.arxiv.org/abs/2506.03106) [[Code]](https://github.com/zhangxy-2019/critique-GRPO)
7. **Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning.** <2025.05>  
   *Shenao Zhang, Yaqing Wang, Yinxiao Liu, Tianqi Liu, Peter Grabowski, Eugene Ie, Zhaoran Wang, Yunxuan Li.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.20561)
8. **S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models.** <2025.05>  
    *Muzhi Dai, Chenxu Yang, Qingyi Si.* **arXiv**  
   [[Paper]](https://arxiv.org/abs/2505.07686)
9. **Temporal Sampling for Forgotten Reasoning in LLMs** <2025.05>   
   *Yuetai Li, Zhangchen Xu, Fengqing Jiang, Bhaskar Ramasubramanian, Luyao Niu, Bill Yuchen Lin, Xiang Yue, Radha Poovendran.* **arXiv**    
   [[Paper]](https://arxiv.org/abs/2505.20196) [[Code]](https://github.com/uw-nsl/Temporal_Forgetting)
10. **DAPO: An Open-Source LLM Reinforcement Learning System at Scale.**  <2025.05>   
   *Yu et al.* **arXiv**    
   [[Paper]](https://arxiv.org/abs/2503.14476) [[Code]](https://github.com/BytedTsinghua-SIA/DAPO)
11. **RM-R1: Reward Modeling as Reasoning**  <2025.05>  
    *Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, Hanghang Tong, Heng Ji.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.02387) [[Code]](https://github.com/RM-R1-UIUC/RM-R1)
12. **GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models.**  <2025.04>   
    *Jixiao Zhang, Chunsheng Zuo.* **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.09696)
13. **VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks.** <2025.04>
    *Yu Yue, Yufeng Yuan, Qiying Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, Xiangpeng Wei, Xiangyu Yu, Gaohong Liu, Juncai Liu, Lingjun Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Ru Zhang, Xin Liu, Mingxuan Wang, Yonghui Wu, Lin Yan.* **arXiv**
    [Paper]()
14. **Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning.**  <2025.04>   
    *Sanghwan Bae, Jiwoo Hong, Min Young Lee, Hanbyul Kim, JeongYeon Nam, Donghyun Kwak.*  **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.03380)
15. **SRPO: A Cross-Domain Implementation of Large-Scale Reinforcement Learning on LLM.** <2025.04>   
    *Xiaojiang Zhang, Jinghui Wang, Zifei Cheng, Wenhao Zhuang, Zheng Lin, Minglei Zhang, Shaojie Wang, Yinghan Cui, Chao Wang, Junyi Peng, Shimiao Jiang, Shiqi Kuang, Shouyu Yin, Chaohang Wen, Haotian Zhang, Bin Chen, Bing Yu.*  **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.14286)
16. **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.**  <2025.01>  
    *DeepSeek-AI.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2501.12948)
17. **ProRL: Prolonged Reinforcement Learning Expands Reasoning Boundaries in Large Language Models.**  <2025.05>  
    *Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, Yi Dong.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.24864)
18. **GHPO: Adaptive Guidance for Stable and Efficient LLM Reinforcement Learning.**  <2025.07>  
    *Ziru Liu, Cheng Gong, Xinyu Fu, Yaofang Liu, Ran Chen, Shoubo Hu, Suiyun Zhang, Rui Liu, Qingfu Zhang, Dandan        Tu.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2507.10628)
19. **GPG: A Simple and Strong Reinforcement Learning Baseline for Model Reasoning.**  <2025.04>  
    *Xiangxiang Chu, Hailang Huang, Xiao Zhang, Fei Wei, Yong Wang.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2504.02546)
20. **SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data.**  <2025.05>  
    *Wenkai Fang, Shunyu Liu, Yang Zhou, Kongcheng Zhang, Tongya Zheng, Kaixuan Chen, Mingli Song, Dacheng Tao.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.20347)
21. **SPEED-RL: Faster Training of Reasoning Models via Online Curriculum Learning.**  <2025.06>  
    *Ruiqi Zhang, Daman Arora, Song Mei, Andrea Zanette.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.09016)
22. **Bingo: Boosting Efficient Reasoning of LLMs via Dynamic and Significance-based Reinforcement Learning.**  <2025.06>  
    *Hanbing Liu, Lang Cao, Yuanyi Ren, Mengyu Zhou, Haoyu Dong, Xiaojun Ma, Shi Han, Dongmei Zhang.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.08125)
23. **Reinforcement Pre-Training.**  <2025.06>  
    *Qingxiu Dong, Li Dong, Yao Tang, Tianzhu Ye, Yutao Sun, Zhifang Sui, Furu Wei.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.08007)
24. **Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification.**  <2025.03>  
    *Youssef Mroueh.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2503.06639)

<h4>2024</h4>

1. **DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models** <2024.02>  
   *Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo.* **arXiv**   
    [[Paper]](https://arxiv.org/abs/2402.03300) [[Code]](https://github.com/deepseek-ai/DeepSeek-Math)
2. **ReFT: Reasoning with Reinforced Fine-Tuning** <2024.01>  
   *Trung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, Hang Li.* **arXiv / ACL 2024**  
   [[Paper]](https://arxiv.org/abs/2401.08967) [[Code]](https://github.com/lqtrung1998/mwp_ReFT)


---

<h3 id="rlvr-foundations">Unsupervised RLVR</h3>

<h4>2025</h4>

1. **Can Large Reasoning Models Self-Train?** <2025.05> 
    *Sheikh Shafayat, Fahim Tajwar, Ruslan Salakhutdinov, Jeff Schneider, Andrea Zanette.* **arXiv**   
    [[Paper]](https://arxiv.org/abs/2505.21444) 
2. **Right Question is Already Half the Answer: Fully Unsupervised LLM Reasoning Incentivization. **    <2025.05>   
    *Qingyang Zhang, Haitao Wu, Changqing Zhang, Peilin Zhao, Yatao Bian.*     **arXiv**
    [[Paper]](https://arxiv.org/abs/2504.05812)  
4.  **Maximizing Confidence Alone Improves Reasoning**  <2025.05>     
    *Mihir Prabhudesai, Lili Chen, Alex Ippoliti, Katerina Fragkiadaki, Hao Liu, Deepak Pathak.*   **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.22660)
5.  **Learning to Reason without External Rewards.**   **arXiv**
    *Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song.*      **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.19590)
6. **NOVER: Incentive Training for Language Models via Verifier-Free Reinforcement Learning.**  <2025.05>  
    *Wei Liu, Siya Qi, Xinyu Wang, Chen Qian, Yali Du, Yulan He.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.16022)
7. **Absolute Zero: Reinforced Self-Play Reasoning with Zero Data.**  <2025.05>  
    *Andrew Zhao et al.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.03335)
---

<h3 id="rlvr-foundations">Entropy in RLVR</h3>

<h4>2025</h4>

1. **Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning** <2025.06>  
    *Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xionghui Chen, Jianxin Yang, Zhenru Zhang, Yuqiong Liu, An Yang, Andrew Zhao, Yang Yue, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin.* **arXiv**    
    [[Paper]](https://arxiv.org/abs/2506.01939)
2. **The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models.** <2025.05>   
    *Ganqu Cui, Yuchen Zhang, Jiacheng Chen, Lifan Yuan, Zhi Wang, Yuxin Zuo, Haozhan Li, Yuchen Fan, Huayu Chen, Weize Chen, Zhiyuan Liu, Hao Peng, Lei Bai, Wanli Ouyang, Yu Cheng, Bowen Zhou, Ning Ding.* **arXiv**    
    [[Paper]](https://arxiv.org/abs/2505.22617) [[Code]](https://github.com/PRIME-RL/Entropy-Mechanism-of-RL)
3. **One-shot Entropy Minimization.** <2025.05>  
    *Zitian Gao, Lynx Chen, Joey Zhou, Bryan Dai.* **arXiv**  
   [[Paper]](https://www.arxiv.org/pdf/2505.20282) [[Code]](https://github.com/zitian-gao/one-shot-em)
4. **The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning.** <2025.05>  
   *Shivam Agarwal, Zimin Zhang, Lifan Yuan, Jiawei Han, Hao Peng.* **arXiv**  
   [[Paper]](https://arxiv.org/abs/2505.15134)
5. **FR3E: First Return, Entropy-Eliciting Explore.**  <2025.07>  
   *Tianyu Zheng, Tianshun Xing, Qingshui Gu, Taoran Liang, Xingwei Qu, Xin Zhou, Yizhi Li, Zhoufutu Wen, Chenghua Lin, Wenhao Huang, Qian Liu, Ge Zhang, Zejun Ma*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2507.07017)
6. **Pass@k Training for Adaptively Balancing Exploration and Exploitation of Large Reasoning Models.**  <2025.08>  
   *Zhipeng Chen, Xiaobo Qin, Youbin Wu, Yue Ling, Qinghao Ye, Wayne Xin Zhao, Guang Shi.*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2508.10751)
---

<h3 id="rlvr-analysis">RLVR Analysis</h3>

<h4>2025</h4>

1. **Spurious Rewards: Rethinking Training Signals in RLVR.**  <2025.05>  
    *Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Yiping Wang, Sewoong Oh, Simon Shaolei Du, Nathan Lambert, Sewon Min, Ranjay Krishna, Yulia Tsvetkov, Hannaneh Hajishirzi, Pang Wei Koh, Luke Zettlemoyer.*  **Preprint**  
    [[Paper]](https://github.com/ruixin31/Rethink_RLVR/blob/main/paper/rethink-rlvr.pdf) [[Code]](https://github.com/ruixin31/Rethink_RLVR)
2. **Reinforcement Learning Finetunes Small Subnetworks in Large Language Models.**  <2025.05>  
    *Sagnik Mukherjee, Lifan Yuan, Dilek Hakkani-Tur, Hao Peng.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.11711)
3. **Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**  <2025.04>  
    *Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2504.13837) [[Code]](https://github.com/LeapLabTHU/limit-of-RLVR)
4. **The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning.**  <2025.06>  
    *Xinyu Zhu, Mengzhou Xia, Zhepei Wei, Wei-Lin Chen, Danqi Chen, Yu Meng.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.01347) [[Code]](https://github.com/TianHongZXY/RLVR-Decomposed)
5. **Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination.**  <2025.07>  
    *Mingqi Wu, Zhihao Zhang, Qiaole Dong, Zhiheng Xi, Jun Zhao, Senjie Jin, Xiaoran Fan, Yuhao Zhou, Huijie Lv, Ming Zhang, Yanwei Fu, Qin Liu, Songyang Zhang, Qi Zhang.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2507.10532)
6. **One Token to Fool LLM-as-a-Judge.**  <2025.07>  
    *Yulai Zhao, Haolin Liu, Dian Yu, S. Y. Kung, Haitao Mi, Dong Yu.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2507.08794)

---
<h3 id="mllm">Multimodal LLM</h3>

<h4>2025</h4>

1. *SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning.***  <2025.06> 
    *Zhongwei Wan, Zhihao Dou, Che Liu, Yu Zhang, Dongfei Cui, Qinjian Zhao, Hui Shen, Jing Xiong, Yi Xin, Yifan Jiang, Yangfan He, Mi Zhang, Shen Yan.*   **arXiv**   
    [[Paper]](https://arxiv.org/abs/2506.01713) [[Code]](https://srpo.pages.dev/)
2. **R1-Omni: Explainable Omni-Multimodal Emotion Recognition with Reinforcement Learning** <2025.05>   
    *Jiaxing Zhao, Xihan Wei, Liefeng Bo*  **arXiv**   
    [[Paper]](https://arxiv.org/abs/2503.05379) [[Code]](https://github.com/HumanMLLM/R1-Omni)
3. **R1-VL: Learning to Reason with Multimodal Large Language Models via Step-Wise GRPO.**  <2025.03>  
   *Jingyi Zhang, Jiaxing Huang, Huanjin Yao, Shunyu Liu, Xikun Zhang, Shijian Lu, Dacheng Tao.*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2503.12937)
4. **VL-Rethinker: Incentivizing Self-Reflection of Vision-Language Models with Reinforcement Learning.**  <2025.04>  
   *Haozhe Wang, Chao Qu, Zuming Huang, Wei Chu, Fangzhen Lin, Wenhu Chen.*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2504.08837)
5. **GTR: Guided Thought Reinforcement Prevents Thought Collapse in RL-based VLM Agent Training.**  <2025.03>  
   *Tong Wei, Yijun Yang, Junliang Xing, Yuanchun Shi, Zongqing Lu, Deheng Ye.*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2503.08525)

---
<h3 id="evaluation">Evaluation Issue </h3>

<h4>2025</h4>

1. **A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility.**  <2025.04>  
    *Andreas Hochlehnert, Hardik Bhatnagar, Vishaal Udandarao, Samuel Albanie, Ameya Prabhu, Matthias Bethge.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2504.07086)
2. **Incorrect Baseline Evaluations Call into Question Recent LLM-RL Claims.**  <2025.05>  
    *Nikhil Chandak, Shashwat Goel, Ameya Prabhu.*  **Blog**  
    [[Paper]](https://safe-lip-9a8.notion.site/Incorrect-Baseline-Evaluations-Call-into-Question-Recent-LLM-RL-Claims-2012f1fbf0ee8094ab8ded1953c15a37)
3. **Evaluation is All You Need: Strategic Overclaiming of LLM Reasoning Capabilities Through Evaluation Design.**  <2025.06>  
    *Lin Sun, Weihong Lin, Jinzhu Wu, Yongfu Zhu, Xiaoqi Jian, Guangxiang Zhao, Linglin Zhang, Sai-er Hu, Yuhan Wu, Xiangzheng Zhang.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.04734)
4. **AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions.**  <2025.06>  
    *Polina Kirichenko, Shauli Ravfogel, Roee Aharoni, Yonatan Belinkov.*  **arXiv**  
    [[Paper]](https://arxiv.org/abs/2506.09038)
5. **IFBench: Generalizing Verifiable Instruction Following.**  <2025.07>  
   *Valentina Pyatkin, Saumya Malik, Victoria Graf, Hamish Ivison, Shengyi Huang, Pradeep Dasigi, Nathan Lambert, Hannaneh Hajishirzi.*  **arXiv**  
   [[Paper]](https://arxiv.org/abs/2507.02833) [[Code]](https://github.com/allenai/if-bench)
 
--- 

<h2 id="blogs">📚 Awesome Blogs about RLVR</h2>

[SemiAnalysis](https://semianalysis.com/2025/06/08/scaling-reinforcement-learning-environments-reward-hacking-agents-scaling-data/): 
Scaling Reinforcement Learning: Environments, Reward Hacking, Agents, Scaling Data.    


---

[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;<h2 id="surveys-and-theory">📚 Surveys and Theory</h2>&#41;)
[//]: # ()
[//]: # ()
[//]: # (<h2 id="datasets-and-benchmarks">🏗️ Datasets and Benchmarks</h2>)

[//]: # ()
[//]: # (---)

<h2 id="toolkits-and-libraries">🛠️ Toolkits and Libraries</h2>

- 【[open-r1](https://github.com/huggingface/open-r1)】-- Fully open reproduction of DeepSeek-R1. ![GitHub Stars](https://img.shields.io/github/stars/huggingface/open-r1?style=social)
- 【[PRIME](https://github.com/PRIME-RL/PRIME)】 -- Scalable RL solution for advanced reasoning of language models.  ![GitHub Stars](https://img.shields.io/github/stars/PRIME-RL/PRIME?style=social)
- 【[simpleRL-reason](https://github.com/hkust-nlp/simpleRL-reason)】 -- Simple RL training for reasoning.  ![GitHub Stars](https://img.shields.io/github/stars/hkust-nlp/simpleRL-reason?style=social)
- 【[TinyZero](https://github.com/Jiayi-Pan/TinyZero)】 -- Minimal reproduction of DeepSeek R1-Zero. ![GitHub Stars](https://img.shields.io/github/stars/Jiayi-Pan/TinyZero?style=social)
- 【[OpenR](https://github.com/openreasoner/openr)】 -- OpenR: An Open Source Framework for Advanced Reasoning with LLMs![GitHub Stars](https://img.shields.io/github/stars/openreasoner/openr?style=social)
- 【[verl](https://github.com/volcengine/verl)】 -- verl: Volcano Engine Reinforcement Learning for LLMs. ![GitHub Stars](https://img.shields.io/github/stars/volcengine/verl?style=social)
- 【[rl](https://github.com/pytorch/rl)】 -- A modular, primitive-first, python-first PyTorch library for Reinforcement Learning. ![GitHub Stars](https://img.shields.io/github/stars/pytorch/rl?style=social)
- 【[all-rl-algorithms](https://github.com/FareedKhan-dev/all-rl-algorithms)】 -- Implementation of all RL algorithms in a simpler way. ![GitHub Stars](https://img.shields.io/github/stars/FareedKhan-dev/all-rl-algorithms?style=social)
- 【[AReaL](https://github.com/inclusionAI/AReaL)】 -- Distributed RL System for LLM Reasoning. ![GitHub Stars](https://img.shields.io/github/stars/inclusionAI/AReaL?style=social)
- 【[rllm](https://github.com/agentica-project/rllm)】 -- Democratizing Reinforcement Learning for LLMs. ![GitHub Stars](https://img.shields.io/github/stars/agentica-project/rllm?style=social)
- 【[MARTI](https://github.com/TsinghuaC3I/MARTI)】 -- A Framework for LLM-based Multi-Agent Reinforced Training and Inference.  ![GitHub Stars](https://img.shields.io/github/stars/TsinghuaC3I/MARTI?style=social)
- 【[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) 】-- An Easy-to-use, Scalable and High-performance RLHF Framework based on Ray. ![GitHub Stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=social)
- 【[ROLL](https://github.com/alibaba/ROLL)】-- An Efficient and User-Friendly Scaling Library for Reinforcement Learning with Large Language Models. ![GitHub Stars](https://img.shields.io/github/stars/alibaba/ROLL?style=social)

<h2>💡 Other Awesome Lists</h2>

- **[Awesome-RL-based-LLM-Reasoning](https://github.com/bruno686/Awesome-RL-based-LLM-Reasoning)** Materials that enhance LLM reasoning with reinforcement learning. 
- **[Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning)**  Curated collection of papers and resources on how to unlock the reasoning ability of LLMs and MLLMs.
- **[Awesome-Controllable-Generation](https://github.com/atfortes/Awesome-Controllable-Generation)**  Collection of papers and resources on Controllable Generation using Diffusion Models.
- **[Chain-of-ThoughtsPapers](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers)**  A trend starting from "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models".
- **[LM-reasoning](https://github.com/jeffhj/LM-reasoning)**  Collection of papers and resources on Reasoning in Large Language Models.
- **[Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers)**  Repository for the paper "Reasoning with Language Model Prompting: A Survey".
- **[ReasoningNLP](https://github.com/FreedomIntelligence/ReasoningNLP)**  Paper list on reasoning in NLP.
- **[Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)**  Curated list of Large Language Model.
- **[Awesome LLM Self-Consistency](https://github.com/SuperBruceJia/Awesome-LLM-Self-Consistency)**  Curated list of Self-consistency in Large Language Models.
- **[Deep-Reasoning-Papers](https://github.com/floodsung/Deep-Reasoning-Papers)**  Recent Papers including Neural-Symbolic Reasoning, Logical Reasoning, and Visual Reasoning.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>

---

<h2 id="contributing">🤝 Contributing</h2>

Have a new paper, tool, or idea? Please open a [Pull Request](https://github.com/yourname/awesome-llm-rlvr/pulls) or submit an [Issue](https://github.com/yourname/awesome-llm-rlvr/issues).  
Let’s make LLMs reason better, faster, and more verifiably.

### Contributors

<a href="https://github.com/smiles724/Awesome-LLM-RLVR/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=smiles724/Awesome-LLM-RLVR" />
</a>


---

<h2 id="star"> ⭐ Star History</h2>

[![Star History Chart](https://api.star-history.com/svg?repos=smiles724/Awesome-LLM-RLVR&type=Date)](https://www.star-history.com/#smiles724/Awesome-LLM-RLVR&Date)
---

<h2 id="license">🧾 License</h2>

MIT License © 2025 <a href="mailto:fangwu97@stanford.edu">Fang Wu</a> and Contributors

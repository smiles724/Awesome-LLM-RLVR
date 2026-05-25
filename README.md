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
- **VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction** <2026-05-22>  
  *Xin-Qiang Cai, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2602.12579v2)
- **Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers** <2026-05-22>  
  *Xin-Qiang Cai, Wei Wang, Feng Liu, Tongliang Liu, Gang Niu, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2510.00915v4)
- **CoSPlay: Cooperative Self-Play at Test-Time with Self-Generated Code and Unit Test** <2026-05-22>  
  *Zhangyi Hu, Chenhui Liu, Tian Huang, Jindong Li, Yang Yang, Jiemin Wu, Zining Zhong, Menglin Yang, Yutao Yue*. [[Paper]](https://arxiv.org/abs/2605.23491v1)
- **Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals** <2026-05-22>  
  *Sirui Chen, Lei Xu, Yuying Zhao, Yutian Chen, Yu Wang, Beier Zhu, Hanwang Zhang, Shengjie Zhao, Chaochao Lu*. [[Paper]](https://arxiv.org/abs/2605.23384v1)
- **Visually-Guided Policy Optimization for Multimodal Reasoning** <2026-05-22>  
  *Zengbin Wang, Feng Xiong, Liang Lin, Xuecai Hu, Yong Wang, Yanlin Wang, Man Zhang, Xiangxiang Chu*. [[Paper]](https://arxiv.org/abs/2604.09349v2)
- **VISD: Enhancing Video Reasoning via Structured Self-Distillation** <2026-05-22>  
  *Hao Lin, Kunyang Lv, Xu Jiang, Jingqi Tian, Zhongjing Du, Jiayu Ding, Qiaoman Zhang, Hongbo Jin*. [[Paper]](https://arxiv.org/abs/2605.06094v4)
- **OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning** <2026-05-22>  
  *Yu Li, Rui Miao, Tian Lan, Zhengling Qi*. [[Paper]](https://arxiv.org/abs/2605.21851v2)
- **Clipping Bottleneck: Stabilizing RLVR via Stochastic Recovery of Near-Boundary Signals** <2026-05-21>  
  *Shuo Yang, Jinda Lu, Chiyu Ma, Kexin Huang, Haoming Meng, Qihui Zhang, Yuyang Liu, Bolin Ding, Guoyin Wang, Li Yuan, Jingren Zhou*. [[Paper]](https://arxiv.org/abs/2605.22703v1)
- **Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework** <2026-05-21>  
  *Shourov Joarder, Diganta Sikdar, Ahsan Habib Akash, Binod Bhattarai, Prashnna Gyawali*. [[Paper]](https://arxiv.org/abs/2605.22620v1)
- **Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning** <2026-05-21>  
  *Hongbin Zhang, Chaozheng Wang, Kehai Chen, Youcheng Pan, Yang Xiang, Jinpeng Wang, Min Zhang*. [[Paper]](https://arxiv.org/abs/2605.22263v1)
- **Linear Dynamics in the RLVR Training of Large Language Models** <2026-05-21>  
  *Tianle Wang, Jiayu Liu, Zhongyuan Wu, Shenghao Jin, Wei Chen, Hao Xu, Ning Miao*. [[Paper]](https://arxiv.org/abs/2601.04537v3)
- **One-Way Policy Optimization for Self-Evolving LLMs** <2026-05-21>  
  *Shuo Yang, Jinda Lu, Kexin Huang, Chiyu Ma, Shaohang Wei, Yuyang Liu, Guoyin Wang, Jingren Zhou, Li Yuan*. [[Paper]](https://arxiv.org/abs/2605.22156v1)
- **From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning** <2026-05-21>  
  *Xitai Jiang, Zihan Tang, Wenze Lin, Yang Yue, Shenzhi Wang, Gao Huang*. [[Paper]](https://arxiv.org/abs/2605.22074v1)
- **Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention** <2026-05-21>  
  *Changyuan Tian, Zhicong Lu, Huaxing Liu, Xiang Wang, Shuai Li, Yu Chen, Wenqian Lv, Zichuan Lin, Juncheng Diao, Deheng Ye*. [[Paper]](https://arxiv.org/abs/2605.22072v1)
- **Heterogeneous Agent Collaborative Reinforcement Learning** <2026-05-21>  
  *Zhixia Zhang, Zixuan Huang, Gongxun Li, Huaiyang Wang, Chengyi Yuan, Xin Xia, Deqing Wang, Fuzhen Zhuang, Shuai Ma, Ning Ding, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2603.02604v2)
- **General Preference Reinforcement Learning** <2026-05-21>  
  *Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, Arslan Chaudhry, Andreas Haupt, Sanmi Koyejo, Emily Fox, John M. Cioffi*. [[Paper]](https://arxiv.org/abs/2605.18721v3)
- **Reinforced Preference Optimization for Reasoning-Augmented Recommendations** <2026-05-21>  
  *Jingtong Gao, Zeyu Song, Chi Lu, Xiaopeng Li, Derong Xu, Maolin Wang, Peng Jiang, Kun Gai, Qingpeng Cai, Xiangyu Zhao*. [[Paper]](https://arxiv.org/abs/2605.21967v1)
- **Calibrating LLMs with Semantic-level Reward** <2026-05-20>  
  *Fengfei Yu, Ruijia Niu, Dongxia Wu, Yian Ma, Rose Yu*. [[Paper]](https://arxiv.org/abs/2605.15588v2)
- **You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories** <2026-05-20>  
  *Zhepei Wei, Xinyu Zhu, Wei-Lin Chen, Chengsong Huang, Jiaxin Huang, Yu Meng*. [[Paper]](https://arxiv.org/abs/2605.21468v1)
- **DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards** <2026-05-20>  
  *Kaiyi Zhang, Wei Wu, Yankai Lin*. [[Paper]](https://arxiv.org/abs/2605.21467v1)
- **TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health** <2026-05-20>  
  *Yuang Fan, Lilin Xu, Millie Wu, Jingping Nie, Qingyu Chen, Yuzhe Yang, Zhuo Zhang, Xin Liu, Subigya Nepal, Xiaofan Jiang, Xuhai "Orson" Xu*. [[Paper]](https://arxiv.org/abs/2605.21295v1)
- **How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR** <2026-05-20>  
  *Richa Verma, Balaraman Ravindran*. [[Paper]](https://arxiv.org/abs/2605.21266v1)
- **LamPO: A Lambda Style Policy Optimization for Reasoning Language Models** <2026-05-20>  
  *Zhe Yuan, Yipeng Zhou, Jinghan Li, Xinyuan Chen, Bowen Deng, Zhiqian Chen, Liang Zhao*. [[Paper]](https://arxiv.org/abs/2605.21235v1)
- **Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation** <2026-05-20>  
  *Xixiang He, Qiyao Sun, Ao Cheng, Xingming Li, Xuanyu Ji, Hailun Lu, Runke Huang, Qingyong Hu*. [[Paper]](https://arxiv.org/abs/2605.21125v1)
- **Listwise Policy Optimization: Group-based RLVR as Target-Projection on the LLM Response Simplex** <2026-05-20>  
  *Yun Qu, Qi Wang, Yixiu Mao, Heming Zou, Yuhang Jiang, Yingyue Li, Wutong Xu, Lizhou Cai, Weijie Liu, Clive Bai, Kai Yang, Yangkun Chen, Saiyong Yang, Xiangyang Ji*. [[Paper]](https://arxiv.org/abs/2605.06139v2)
- **Multi-Step Likelihood-Ratio Correction for Reinforcement Learning with Verifiable Rewards** <2026-05-20>  
  *Deokgyu Yoon, Hyungkyu Kang, Joongkyu Lee, Byeongchan Kim, Gyungin Shin, Sungrae Park, Min-hwan Oh*. [[Paper]](https://arxiv.org/abs/2605.20865v1)
- **PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR** <2026-05-20>  
  *Yiqi Zhang, Fangzheng Jiao, Tian Tang, Boyu Tian, Hangyu Wang, Qiaoling Chen, Guoteng Wang, Zhen Jiang, Peng Sun, Ping Zhang, Xiaohe Hu, Ziming Liu, Menghao Zhang, Yanmin Jia, Yang You, Siyuan Feng*. [[Paper]](https://arxiv.org/abs/2605.20863v1)
- **Bayesian Preference Learning for Test-Time Steerable Reward Models** <2026-05-20>  
  *Jiwoo Hong, Shao Tang, Zhipeng Wang*. [[Paper]](https://arxiv.org/abs/2602.08819v2)
- **Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs** <2026-05-19>  
  *Xingwei Gan, Ying Zhu*. [[Paper]](https://arxiv.org/abs/2605.20555v1)
- **Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR** <2026-05-19>  
  *Utkarsh Tyagi, Xingang Guo, MohammadHossein Rezaei, Daniel George, Anas Mahmoud, Jackson Lee, Bing Liu, Yunzhong He*. [[Paper]](https://arxiv.org/abs/2605.20164v1)
- **Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents** <2026-05-19>  
  *Wenjie Tang, Minne Li, Sijie Huang, Liquan Xiao, Yuan Zhou*. [[Paper]](https://arxiv.org/abs/2605.20061v1)
- **GeoX: Mastering Geospatial Reasoning Through Self-Play and Verifiable Rewards** <2026-05-19>  
  *Kyeongjin Ahn, Seungeon Lee, Krishna P. Gummadi, Meeyoung Cha*. [[Paper]](https://arxiv.org/abs/2605.20006v1)
- **Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients** <2026-05-19>  
  *Omar El Mansouri, Fathinah Asma Izzati, Mohamed El Amine Seddik, Salem Lahlou*. [[Paper]](https://arxiv.org/abs/2510.18924v3)
- **GoLongRL: Capability-Oriented Long Context Reinforcement Learning with Multitask Alignment** <2026-05-19>  
  *Minxuan Lv, Tiehua Mei, Tanlong Du, Junmin Chen, Zhenpeng Su, Ziyang Chen, Ziqi Wang, Zhennan Wu, Ruotong Pan, jian Liang, Ruiming Tang, Han Li*. [[Paper]](https://arxiv.org/abs/2605.19577v1)
- **Search Self-play: Pushing the Frontier of Agent Capability without Supervision** <2026-05-19>  
  *Hongliang Lu, Yuhang Wen, Pengyu Cheng, Ruijin Ding, Jiaqi Guo, Haotian Xu, Chutian Wang, Haonan Chen, Xiaoxi Jiang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2510.18821v3)
- **CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization** <2026-05-19>  
  *Ahmed Heakl, Abdelrahman M. Shaker, Youssef Mohamed, Rania Elbadry, Omar Fetouh, Fahad Shahbaz Khan, Salman Khan*. [[Paper]](https://arxiv.org/abs/2605.19436v1)
- **When to Stop Reusing: Dynamic Gradient Gating for Sample-Efficient RLVR** <2026-05-19>  
  *Yuchun Miao, Sen Zhang, Yuqi Zhang, Yaorui Shi, Qi Gu, Xunliang Cai, Lefei Zhang*. [[Paper]](https://arxiv.org/abs/2605.19425v1)
- **Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR** <2026-05-19>  
  *Chongyu Fan, Gaowen Liu, Mingyi Hong, Ramana Rao Kompella, Sijia Liu*. [[Paper]](https://arxiv.org/abs/2605.19282v1)
- **Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models** <2026-05-19>  
  *Khiem Le, Phuc Nguyen, Youssef Mroueh, Chi-Heng Lin, Shangqian Gao, Ting Hua, Nitesh V. Chawla*. [[Paper]](https://arxiv.org/abs/2601.22478v5)
- **Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs** <2026-05-18>  
  *Hamed Khosravi, Xiaoming Huo*. [[Paper]](https://arxiv.org/abs/2605.20270v1)
- **WARC-Bench: Web Archive Based Benchmark for GUI Subtask Executions** <2026-05-18>  
  *Sanjari Srivastava, Gang Li, Cheng Chang, Rishu Garg, Manpreet Kaur, Charlene Y. Lee, Yuezhang Li, Yining Mao, Ignacio Cases, Yanan Xie, Peng Qi*. [[Paper]](https://arxiv.org/abs/2510.09872v2)
- **Learning from Language Feedback via Variational Policy Distillation** <2026-05-18>  
  *Yang Li, Erik Nijkamp, Semih Yavuz, Shafiq Joty*. [[Paper]](https://arxiv.org/abs/2605.15113v2)
- **AMR-SD: Asymmetric Meta-Reflective Self-Distillation for Token-Level Credit Assignment** <2026-05-18>  
  *Zhenlin Wei, Pu Jian, Yingzhuo Deng, Xiaohan Wang, Jiajun Chai, Zhexin Hu, Wei Lin, Shanbin Zhang, Guojun Yin*. [[Paper]](https://arxiv.org/abs/2605.18529v1)
- **Knowledge-to-Verification: Exploring RLVR for LLMs in Knowledge-Intensive Domains** <2026-05-18>  
  *Zhonghang Yuan, Zhefan Wang, Fang Hu, Zihong Chen, Jinzhe Li, Gang Li, Jie Ying, Huanjun Kong, Songyang Zhang, Nanqing Dong*. [[Paper]](https://arxiv.org/abs/2605.18261v1)
- **Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation** <2026-05-18>  
  *Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang*. [[Paper]](https://arxiv.org/abs/2605.18191v1)
- **Breaking $\textit{Winner-Takes-All}$: Cooperative Policy Optimization Improves Diverse LLM Reasoning** <2026-05-18>  
  *Haoxuan Chen, Tianming Liang, Wei-Shi Zheng, Jian-Fang Hu*. [[Paper]](https://arxiv.org/abs/2605.11461v2)
- **Revisiting Reinforcement Learning with Verifiable Rewards from a Contrastive Perspective** <2026-05-18>  
  *Feng Zhang, Xinhong Ma, Ziqiang Dong, Xi Leng, Jianfei Zhao, Xin Sun, Yang Yang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2605.12969v2)
- **HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL** <2026-05-18>  
  *Zhi Li, Songkun Yan, Jie Cao, Mofan Zhang, Anjiang Wei, Jinwoong Yoo, Yang Hong*. [[Paper]](https://arxiv.org/abs/2605.17792v1)
- **Learning from Self-Debate: Preparing Reasoning Models for Multi-Agent Debate** <2026-05-17>  
  *Chenxi Liu, Yanshuo Chen, Ruibo Chen, Tianyi Xiong, Tong Zheng, Heng Huang*. [[Paper]](https://arxiv.org/abs/2601.22297v2)
- **SAPO: Step-Aligned Policy Optimization for Reasoning-Based Generative Recommendation** <2026-05-17>  
  *Zaiyi Zheng, Guanghui Min, Yaochen Zhu, Liang Wu, Liangjie Hong, Chen Chen, Jundong Li*. [[Paper]](https://arxiv.org/abs/2605.17648v1)
- **From Synthetic to Real: Toward Identity-Consistent Makeup Transfer with Synthetic and Real Data** <2026-05-08>  
  *Yue Yu, Jiayu Wang, Jiajia Shi, Jingjing Chen, Yu-Gang Jiang*. [[Paper]](https://arxiv.org/abs/2605.07861v1)
- **Gradient Starvation in Binary-Reward GRPO: Why Group-Mean Centering Fails and Why the Simplest Fix Works** <2026-05-08>  
  *Wenhua Nie, Jianan Wu, Junlin Liu, Ziwei Li, Zheng Lin, Zhang Zijian, Yilong Fan, Haoran Zheng, Jyh-Shing Roger Jang*. [[Paper]](https://arxiv.org/abs/2605.07689v1)
- **VISD: Enhancing Video Reasoning via Structured Self-Distillation** <2026-05-08>  
  *Hao Lin, Kunyang Lv, Xu Jiang, Jingqi Tian, Zhongjing Du, Jiayu Ding, Qiaoman Zhang, Hongbo Jin*. [[Paper]](https://arxiv.org/abs/2605.06094v2)
- **ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning** <2026-05-08>  
  *Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Li Wang, Xiaodong Lu, Wei Lin, Ran He, Guojun Yin*. [[Paper]](https://arxiv.org/abs/2605.00380v2)
- **Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States** <2026-05-08>  
  *Yunho Choi, Jongwon Lim, Woojin Ahn, Minjae Oh, Jeonghoon Shim, Yohan Jo*. [[Paper]](https://arxiv.org/abs/2605.07579v1)
- **Multi-Modal Multi-Agent Reinforcement Learning for Radiology Report Generation** <2026-05-08>  
  *Kaito Baba, Risa Kishikawa, Satoshi Kodera*. [[Paper]](https://arxiv.org/abs/2603.16876v2)
- **Flexible Entropy Control in RLVR with a Gradient-Preserving Perspective** <2026-05-08>  
  *Kun Chen, Peng Shi, Fanfan Liu, Haibo Qiu, Zhixiong Zeng, Siqi Yang, Wenji Mao*. [[Paper]](https://arxiv.org/abs/2602.09782v2)
- **Rethinking Importance Sampling in LLM Policy Optimization: A Cumulative Token Perspective** <2026-05-08>  
  *Yuheng Zhang, Chenlu Ye, Shuowei Jin, Changlong Yu, Wei Xiong, Saurabh Sahu, Nan Jiang*. [[Paper]](https://arxiv.org/abs/2605.07331v1)
- **Implicit Compression Regularization: Concise Reasoning via Internal Shorter Distributions in RL Post-Training** <2026-05-08>  
  *Chen Wang, Hexuan Deng, Yining Zhang, Yuchen Zhang, Jionghao Bai, Zhaochun Li, Ge Lan, Yue Wang*. [[Paper]](https://arxiv.org/abs/2605.07316v1)
- **Structured Role-Aware Policy Optimization for Multimodal Reasoning** <2026-05-08>  
  *Bingqing Jiang, Difan Zou*. [[Paper]](https://arxiv.org/abs/2605.07274v1)
- **OASES: Outcome-Aligned Search-Evaluation Co-Training for Agentic Search** <2026-05-08>  
  *Erhan Zhang, Yiqun Chen, Zechun Niu, Wei Yang, Xiaochi Wei, Yan Gao, Yi Wu, Yao Hu, Jiaxin Mao*. [[Paper]](https://arxiv.org/abs/2604.03675v2)
- **Adaptive Negative Reinforcement for LLM Reasoning:Dynamically Balancing Correction and Diversity in RLVR** <2026-05-08>  
  *Yash Ingle, Jaival Chauhan, Ankit Yadav, Sudhakar Mishra*. [[Paper]](https://arxiv.org/abs/2605.07137v1)
- **Where to Spend Rollouts: Hit-Utility Optimal Rollout Allocation for Group-Based RLVR** <2026-05-08>  
  *Tao Wang, Shuo Li, Yan Sun, Dongsheng Ding, Edgar Dobriban*. [[Paper]](https://arxiv.org/abs/2605.07114v1)
- **Dr. Post-Training: A Data Regularization Perspective on LLM Post-Training** <2026-05-08>  
  *Pingbang Hu, Xueshen Liu, Z. Morley Mao, Jiaqi W. Ma*. [[Paper]](https://arxiv.org/abs/2605.07063v1)
- **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs** <2026-05-07>  
  *Md Tanvirul Alam, Aritran Piplai, Ionut Cardei, Nidhi Rastogi, Peter J Worth*. [[Paper]](https://arxiv.org/abs/2602.00513v3)
- **Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients** <2026-05-07>  
  *Mingwei Xu, Hao Fang*. [[Paper]](https://arxiv.org/abs/2605.06650v1)
- **On the optimization dynamics of RLVR: Gradient gap and step size thresholds** <2026-05-07>  
  *Joe Suk, Yaqi Duan*. [[Paper]](https://arxiv.org/abs/2510.08539v4)
- **How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum** <2026-05-07>  
  *Chu-Cheng Lin, Eugene Ie*. [[Paper]](https://arxiv.org/abs/2604.25907v2)
- **On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR** <2026-05-07>  
  *Hao Ye, Jisheng Dang, Junfeng Fang, Bimei Wang, Yizhou Zhang, Ning Lv, Wencan Zhang, Hong Peng, Bin Hu, Tat-Seng Chua*. [[Paper]](https://arxiv.org/abs/2605.06523v1)
- **P^2O: Joint Policy and Prompt Optimization** <2026-05-07>  
  *Xinyu Lu, Kaiqi Zhang, Jinglin Yang, Boxi Cao, Yaojie Lu, Hongyu Lin, Min He, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2603.21877v3)
- **Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning** <2026-05-07>  
  *Qianjia Cheng, Yuchen Zhang, Zhilin Wang, Yuxin Zuo, Shunkai Zhang, Yuchen Fan, Yu Qiao, Bowen Zhou, Ning Ding, Yu Cheng, Yun Luo, Ganqu Cui*. [[Paper]](https://arxiv.org/abs/2605.06326v1)
- **OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models** <2026-05-07>  
  *Jaehoon Kim, Dongha Lee*. [[Paper]](https://arxiv.org/abs/2605.06188v1)
- **Listwise Policy Optimization: Group-based RLVR as Target-Projection on the LLM Response Simplex** <2026-05-07>  
  *Yun Qu, Qi Wang, Yixiu Mao, Heming Zou, Yuhang Jiang, Yingyue Li, Wutong Xu, Lizhou Cai, Weijie Liu, Clive Bai, Kai Yang, Yangkun Chen, Saiyong Yang, Xiangyang Ji*. [[Paper]](https://arxiv.org/abs/2605.06139v1)
- **Schedule-and-Calibrate: Utility-Guided Multi-Task Reinforcement Learning for Code LLMs** <2026-05-07>  
  *Yujia Chen, Yang Ye, Xiao Chu, Yuchi Ma, Cuiyun Gao*. [[Paper]](https://arxiv.org/abs/2605.06111v1)
- **CORE: Concept-Oriented Reinforcement for Bridging the Definition-Application Gap in Mathematical Reasoning** <2026-05-07>  
  *Zijun Gao, Zhikun Xu, Xiao Ye, Ben Zhou*. [[Paper]](https://arxiv.org/abs/2512.18857v3)
- **Beyond Uniform Credit Assignment: Selective Eligibility Traces for RLVR** <2026-05-07>  
  *Chaoli Mou, Zhan Zhuang, Xinning Chen, Yu Zhang*. [[Paper]](https://arxiv.org/abs/2605.05965v1)
- **Reinforced Informativeness Optimization for Long-Form Retrieval-Augmented Generation** <2026-05-07>  
  *Yuhao Wang, Ruiyang Ren, Yucheng Wang, Wayne Xin Zhao, Jing Liu, Hua Wu, Haifeng Wang*. [[Paper]](https://arxiv.org/abs/2505.20825v2)
- **Alternating Reinforcement Learning with Contextual Rubric Rewards: Beyond the Scalarization Strategy** <2026-05-07>  
  *Guangchen Lan, Lian Xiong, Xin Zhou, Hejie Cui, Yuwei Zhang, Mao Li, Zhenyu Shi, Besnik Fetahu, Lihong Li, Xian Li*. [[Paper]](https://arxiv.org/abs/2603.15646v2)
- **Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards** <2026-05-07>  
  *Tianyang Han, Hengyu Shi, Junjie Hu, Xu Yang, Zhiling Wang, Junhao Su*. [[Paper]](https://arxiv.org/abs/2605.03862v3)
- **AGPO: Asymmetric Group Policy Optimization for Verifiable Reasoning and Search Ads Relevance at JD** <2026-05-07>  
  *Yang Xu, Kun Yao, Yiming Deng, Zheng Fang, Kai Ming Ting, Ming Pang*. [[Paper]](https://arxiv.org/abs/2605.05826v1)
- **Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning** <2026-05-07>  
  *Yiming Huang, Zhenbo Shi, Shuzheng Gao, Cuiyun Gao, Peiyi Han, Chuanyi Liu*. [[Paper]](https://arxiv.org/abs/2605.04066v2)
- **Boosting Reasoning in Large Multimodal Models via Activation Replay** <2026-05-07>  
  *Yun Xing, Xiaobin Hu, Qingdong He, Jiangning Zhang, Shuicheng Yan, Shijian Lu, Yu-Gang Jiang*. [[Paper]](https://arxiv.org/abs/2511.19972v3)
- **Emergent Slow Thinking in LLMs as Inverse Tree Freezing** <2026-05-07>  
  *Sihan Hu, Xiansheng Cai, Yuan Huang, Zhiyuan Yao, Linfeng Zhang, Pan Zhang, Youjin Deng, Kun Chen*. [[Paper]](https://arxiv.org/abs/2509.23629v3)
- **Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration** <2026-05-07>  
  *Langlin Huang, Chengsong Huang, Jinyuan Li, Donghong Cai, Yuyi Yang, Jiaxin Huang*. [[Paper]](https://arxiv.org/abs/2605.05566v1)
- **SPARK: Self-Play with Asymmetric Reward from Knowledge Graphs** <2026-05-07>  
  *Hyobin Park, Taeseop Kim, Dong-Geol Choi*. [[Paper]](https://arxiv.org/abs/2605.05546v1)
- **EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance** <2026-05-06>  
  *Song Yu, Li Li, Wenwen Zhao, Zhisheng Yang*. [[Paper]](https://arxiv.org/abs/2605.04960v1)
- **Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning** <2026-05-06>  
  *Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang*. [[Paper]](https://arxiv.org/abs/2512.15146v4)
- **Beyond Variance: Prompt-Efficient RLVR via Rare-Event Amplification and Bidirectional Pairing** <2026-05-06>  
  *Yujuan Pang, Jiaxin Li, Xin Sheng, Ran Peng, Yong Ma*. [[Paper]](https://arxiv.org/abs/2602.03452v2)
- **The Implicit Curriculum: Learning Dynamics in RL with Verifiable Rewards** <2026-05-06>  
  *Yu Huang, Zixin Wen, Yuejie Chi, Yuting Wei, Aarti Singh, Yingbin Liang, Yuxin Chen*. [[Paper]](https://arxiv.org/abs/2602.14872v2)
- **Efficiently Aligning Language Models with Online Natural Language Feedback** <2026-05-05>  
  *Christine Ye, Joe Benton*. [[Paper]](https://arxiv.org/abs/2605.04356v1)
- **Reference-Sampled Boltzmann Projection for KL-Regularized RLVR: Target-Matched Weighted SFT, Finite One-Shot Gaps, and Policy Mirror Descent** <2026-05-04>  
  *Yao Shu, Chenxing Wei, Hongbin Lin, Shuang Qiu, Hui Xiong*. [[Paper]](https://arxiv.org/abs/2605.02469v1)
- **Think2SQL: Reinforce LLM Reasoning Capabilities for Text2SQL** <2026-05-04>  
  *Simone Papicchio, Simone Rossi, Luca Cagliero, Paolo Papotti*. [[Paper]](https://arxiv.org/abs/2504.15077v5)
- **Enhancing Multimodal In-Context Learning via Inductive-Deductive Reasoning** <2026-05-04>  
  *Haoyu Wang, Haonan Wang, Yuyan Chen, Jun Chen, Gang Liu, Qian Wang, Jiahong Yan, Yanghua Xiao*. [[Paper]](https://arxiv.org/abs/2605.02378v1)
- **Binary Rewards and Reinforcement Learning: Fundamental Challenges** <2026-05-04>  
  *Marc Dymetman*. [[Paper]](https://arxiv.org/abs/2605.02375v1)
- **CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting** <2026-05-04>  
  *Bokai Pan, Mingyue Cheng, Zhiding Liu, Shuo Yu, Xiaoyu Tao, Yuchong Wu, Qi Liu, Defu Lian, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2604.27840v2)
- **Selector-Guided Autonomous Curriculum for One-Shot Reinforcement Learning from Verifiable Rewards** <2026-05-03>  
  *Rudray Dave, Vedang Dubey, Smit Deoghare, Sudhakar Mishra*. [[Paper]](https://arxiv.org/abs/2605.01823v1)
- **MIRL: Mutual Information-Guided Reinforcement Learning for Vision-Language Models** <2026-05-02>  
  *Yin Zhang, Jiaxuan Zhao, Zonghan Wu, Zengxiang Li, Junfeng Fang, Kun Wang, Qingsong Wen, Yilei Shao*. [[Paper]](https://arxiv.org/abs/2605.01520v1)
- **Resource-Efficient Reinforcement for Reasoning Large Language Models via Dynamic One-Shot Policy Refinement** <2026-05-02>  
  *Yunjian Zhang, Sudong Wang, Yang Li, Peiran Xu, Conghao Zhou, Xiaoyue Ma, Jianing Li, Yao Zhu*. [[Paper]](https://arxiv.org/abs/2602.00815v2)
- **Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL** <2026-05-01>  
  *Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin, Keming Wu, Chaojun Xiao, Chen Chen, Wenxuan Wang, Beier Zhu, Yunjian Zhang, Chengwei Qin*. [[Paper]](https://arxiv.org/abs/2604.28123v2)
- **Decouple before Integration: Test-time Synthesis of SFT and RLVR Task Vectors** <2026-05-01>  
  *Chaohao Yuan, Chenghao Xiao, Yu Rong, Hong Cheng, Long-Kai Huang*. [[Paper]](https://arxiv.org/abs/2605.00610v1)
- **Decouple before Integration: Test-time Synthesis of SFT and RLVR Task Vectors** <2026-05-01>  
  *Chaohao Yuan, Chenghao Xiao, Yu Rong, Hong Cheng, Long-Kai Huang*. [[Paper]](https://arxiv.org/abs/2605.00610v1)
- **Reward Modeling from Natural Language Human Feedback** <2026-05-01>  
  *Zongqi Wang, Rui Wang, Yuchuan Wu, Yiyao Yu, Pinyi Zhang, Shaoning Sun, Yujiu Yang, Yongbin Li*. [[Paper]](https://arxiv.org/abs/2601.07349v3)
- **ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning** <2026-05-01>  
  *Zihan Lin, Xiaohan Wang, Jie Cao, Jiajun Chai, Li Wang, Xiaodong Lu, Wei Lin, Ran He, Guojun Yin*. [[Paper]](https://arxiv.org/abs/2605.00380v1)
- **Uniform-Correct Policy Optimization: Breaking RLVR's Indifference to Diversity** <2026-05-01>  
  *Anamika Lochab, Bolian Li, Ruqi Zhang*. [[Paper]](https://arxiv.org/abs/2605.00365v1)
- **Unlocking Zero-Shot Geospatial Reasoning via Indirect Rewards** <2026-04-30>  
  *Chenhui Xu, Fuxun Yu, Michael J. Bianco, Jacob Kovarskiy, Raphael Tang, Qi Zhang, Zirui Xu, Will LeVine, Brandon Dubbs, Heming Liao, Cassandra Burgess, Suvam Bag, Jay Patravali, Rupanjali Kukal, Mikael Figueroa, Rishi Madhok, Nikolaos Karianakis, Jinjun Xiong*. [[Paper]](https://arxiv.org/abs/2510.00072v2)
- **Reinforcement Learning for LLM Post-Training: A Survey** <2026-04-30>  
  *Zhichao Wang, Kiran Ramnath, Bin Bi, Shiva Kumar Pentyala, Sougata Chaudhuri, Shubham Mehrotra, Zixu, Zhu, Xiang-Bo Mao, Sitaram Asur, Na, Cheng*. [[Paper]](https://arxiv.org/abs/2407.16216v3)
- **PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning** <2026-04-30>  
  *Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin, Keming Wu, Chaojun Xiao, Chen Chen, Wenxuan Wang, Beier Zhu, Yunjian Zhang, Chengwei Qin*. [[Paper]](https://arxiv.org/abs/2604.28123v1)
- **CastFlow: Learning Role-Specialized Agentic Workflows for Time Series Forecasting** <2026-04-30>  
  *Bokai Pan, Mingyue Cheng, Zhiding Liu, Shuo Yu, Xiaoyu Tao, Yuchong Wu, Qi Liu, Defu Lian, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2604.27840v1)
- **Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards** <2026-04-30>  
  *Zhengzhao Ma, Xueru Wen, Boxi Cao, Yaojie Lu, Hongyu Lin, Jinglin Yang, Min He, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2603.09117v2)
- **ScaleBox: Enabling High-Fidelity and Scalable Code Verification for Large Language Models** <2026-04-30>  
  *Jiasheng Zheng, Xin Zheng, Boxi Cao, Pengbo Wang, Zhengzhao Ma, Qiming Zhu, Jiazhen Jiang, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2604.27467v1)
- **Mitigating Lost in Multi-turn Conversation via Curriculum RL with Verifiable Accuracy and Abstention Rewards** <2026-04-29>  
  *Ming Li, Pei Chen, Zhenhao Zhang, Tao Yang, Xinyang Zhang, Han Li, Tianyu Cao, Ming Zeng, Zhuofeng Wu, Meng Jiang, Huasheng Li, Lihong Li, Bing Yin*. [[Paper]](https://arxiv.org/abs/2510.18731v3)
- **Co-Evolving Policy Distillation** <2026-04-29>  
  *Naibin Gu, Chenxu Yang, Qingyi Si, Chuanyu Qin, Dingyu Yao, Peng Fu, Zheng Lin, Weiping Wang, Nan Duan, Jiaqi Wang*. [[Paper]](https://arxiv.org/abs/2604.27083v1)
- **PAINT: Partial-Solution Adaptive Interpolated Training for Self-Distilled Reasoners** <2026-04-29>  
  *Zhiquan Tan, Yinrong Hong*. [[Paper]](https://arxiv.org/abs/2604.26573v1)
- **Rethinking Entropy Interventions in RLVR: An Entropy Change Perspective** <2026-04-29>  
  *Zhezheng Hao, Hong Wang, Haoyang Liu, Jian Luo, Jiarui Yu, Hande Dong, Qiang Lin, Can Wang, Jiawei Chen*. [[Paper]](https://arxiv.org/abs/2510.10150v4)
- **How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum** <2026-04-28>  
  *Chu-Cheng Lin, Eugene Ie*. [[Paper]](https://arxiv.org/abs/2604.25907v1)
- **When Errors Can Be Beneficial: A Categorization of Imperfect Rewards for Policy Gradient** <2026-04-28>  
  *Shuning Shang, Hubert Strauss, Stanley Wei, Sanjeev Arora, Noam Razin*. [[Paper]](https://arxiv.org/abs/2604.25872v1)
- **Step-Audio-R1.5 Technical Report** <2026-04-28>  
  *Yuxin Zhang, Xiangyu Tony Zhang, Daijiao Liu, Fei Tian, Yayue Deng, Jun Chen, Qingjian Lin, Haoyang Zhang, Yuxin Li, Jinglan Gong, Yechang Huang, Liang Zhao, Chengyuan Yao, Hexin Liu, Eng Siong Chng, Xuerui Yang, Gang Yu, Xiangyu Zhang, Daxin Jiang*. [[Paper]](https://arxiv.org/abs/2604.25719v1)
- **Policy Improvement Reinforcement Learning** <2026-04-28>  
  *Huaiyang Wang, Xiaojie Li, Deqing Wang, Haoyi Zhou, Zixuan Huang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2604.00860v2)
- **AdaTooler-V: Adaptive Tool-Use for Images and Videos** <2026-04-28>  
  *Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng, Xu Zhou, Manyuan Zhang, Yuzhang Shang, Xiangyu Yue*. [[Paper]](https://arxiv.org/abs/2512.16918v3)
- **JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR** <2026-04-28>  
  *Xinjie Chen, Biao Fu, Jing Wu, Guoxin Chen, Xinggao Liu, Dayiheng Liu, Minpeng Liao*. [[Paper]](https://arxiv.org/abs/2604.25419v1)
- **Scheduling Your LLM Reinforcement Learning with Reasoning Trees** <2026-04-27>  
  *Hong Wang, Zhezheng Hao, Jian Luo, Chenxing Wei, Yao Shu, Lei Liu, Qiang Lin, Hande Dong, Jiawei Chen*. [[Paper]](https://arxiv.org/abs/2510.24832v2)
- **Improving Vision-language Models with Perception-centric Process Reward Models** <2026-04-27>  
  *Yingqian Min, Kun Zhou, Yifan Li, Yuhuan Wu, Han Peng, Yifan Du, Wayne Xin Zhao, Min Yang, Ji-Rong Wen*. [[Paper]](https://arxiv.org/abs/2604.24583v1)
- **V-GRPO: Online Reinforcement Learning for Denoising Generative Models Is Easier than You Think** <2026-04-25>  
  *Bingda Tang, Yuhui Zhang, Xiaohan Wang, Jiayuan Mao, Ludwig Schmidt, Serena Yeung-Levy*. [[Paper]](https://arxiv.org/abs/2604.23380v1)
- **Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance** <2026-04-25>  
  *Xinzhu Chen, Wei He, Huichuan Fan, Wenzhe Niu, Zhongxiang Sun, Xuanru Wang, Jiuchong Gao, Jinghua Hao, Renqing He, Weijie Yu*. [[Paper]](https://arxiv.org/abs/2604.23318v1)
- **LearnAlign: Data Selection for LLM Reinforcement Learning with Improved Gradient Alignment** <2026-04-25>  
  *Shipeng Li, Zhiqin Yang, Shikun Li, Xiaobo Xia, Hengyu Liu, Xinghua Zhang, Gaode Chen, Dong Fang, Ying Tai, Zhe Peng*. [[Paper]](https://arxiv.org/abs/2506.11480v4)
- **DeepImagine: Learning Biomedical Reasoning via Successive Counterfactual Imagining** <2026-04-24>  
  *Youze Zheng, Jianyou Wang, Yuhan Chen, Matthew Feng, Longtian Bao, Hanyuan Zhang, Maxim Khan, Aditya K. Sehgal, Christopher D. Rosin, Umber Dube, Ramamohan Paturi*. [[Paper]](https://arxiv.org/abs/2604.23054v1)
- **UR$^2$: Unify RAG and Reasoning through Reinforcement Learning** <2026-04-24>  
  *Weitao Li, Boran Xiang, Xiaolong Wang, Zhinan Gou, Weizhi Ma, Yang Liu*. [[Paper]](https://arxiv.org/abs/2508.06165v4)
- **TexOCR: Advancing Document OCR Models for Compilable Page-to-LaTeX Reconstruction** <2026-04-24>  
  *Chengye Wang, Lin Fu, Zexi Kuang, Yilun Zhao*. [[Paper]](https://arxiv.org/abs/2604.22880v1)
- **Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning** <2026-04-23>  
  *Qinan Yu, Alexa Tartaglini, Peter Hase, Carlos Guestrin, Christopher Potts*. [[Paper]](https://arxiv.org/abs/2604.22074v1)
- **How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization** <2026-04-23>  
  *Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin Shi, Chaowen Hu, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.19208v2)
- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** <2026-04-23>  
  *Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He*. [[Paper]](https://arxiv.org/abs/2601.09361v3)
- **Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems** <2026-04-22>  
  *Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan, Gaowen Liu, Shiyu Chang*. [[Paper]](https://arxiv.org/abs/2604.21138v1)
- **V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization** <2026-04-22>  
  *Yubo Jiang, Yitong An, Xin Yang, Abudukelimu Wuerkaixi, Xuxin Cheng, Fengying Xie, Zhiguo Jiang, Cao Liu, Ke Zeng, Haopeng Zhang*. [[Paper]](https://arxiv.org/abs/2604.20755v1)
- **Near-Future Policy Optimization** <2026-04-22>  
  *Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao, Zheng Lin, Peng Fu, Nan Duan, Jiaqi Wang*. [[Paper]](https://arxiv.org/abs/2604.20733v1)
- **SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models** <2026-04-22>  
  *Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr, Federico Tombari, Bernt Schiele*. [[Paper]](https://arxiv.org/abs/2604.20705v1)
- **GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning** <2026-04-22>  
  *Jingyi Wang, Lei Zhu, Tengjin Weng, Song-Li Wu, Haochen Tan, Jierun Chen, Chaofan Tao, Haoli Bai, Lu Hou, Lifeng Shang, Xiao-Ping Zhang*. [[Paper]](https://arxiv.org/abs/2604.20659v1)
- **CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment** <2026-04-22>  
  *Xue Jiang, Yihong Dong, Mengyang Liu, Hongyi Deng, Tian Wang, Yongding Tao, Rongyu Cao, Binhua Li, Zhi Jin, Wenpin Jiao, Fei Huang, Yongbin Li, Ge Li*. [[Paper]](https://arxiv.org/abs/2510.18471v2)
- **Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models** <2026-04-22>  
  *Xin Xu, Clive Bai, Kai Yang, Tianhao Chen, Yangkun Chen, Weijie Liu, Hao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2602.12036v2)
- **Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning** <2026-04-22>  
  *Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang*. [[Paper]](https://arxiv.org/abs/2512.15146v3)
- **Not All Rollouts are Useful: Down-Sampling Rollouts in LLM Reinforcement Learning** <2026-04-22>  
  *Yixuan Even Xu, Yash Savani, Fei Fang, J. Zico Kolter*. [[Paper]](https://arxiv.org/abs/2504.13818v5)
- **Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization** <2026-04-21>  
  *Carter Adams, Rafael Oliveira, Gabriel Almeida, Sofia Torres*. [[Paper]](https://arxiv.org/abs/2604.19857v1)
- **AeSlides: Incentivizing Aesthetic Layout in LLM-Based Slide Generation via Verifiable Rewards** <2026-04-21>  
  *Yiming Pan, Chengwei Hu, Xuancheng Huang, Can Huang, Mingming Zhao, Yuean Bi, Xiaohan Zhang, Aohan Zeng, Linmei Hu*. [[Paper]](https://arxiv.org/abs/2604.22840v1)
- **Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness** <2026-04-20>  
  *Mengzhao Jia, Zhihan Zhang, Meng Jiang*. [[Paper]](https://arxiv.org/abs/2604.18892v1)
- **When and What to Ask: AskBench and Rubric-Guided RLVR for LLM Clarification** <2026-04-20>  
  *Jiale Zhao, Ke Fang, Lu Cheng*. [[Paper]](https://arxiv.org/abs/2602.11199v2)
- **When Can LLMs Learn to Reason with Weak Supervision?** <2026-04-20>  
  *Salman Rahman, Jingyan Shen, Anna Mordvina, Hamid Palangi, Saadia Gabriel, Pavel Izmailov*. [[Paper]](https://arxiv.org/abs/2604.18574v1)
- **OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning** <2026-04-20>  
  *Xinyu Ma, Mingzhou Xu, Xuebo Liu, Chang Jin, Qiang Wang, Derek F. Wong, Min Zhang*. [[Paper]](https://arxiv.org/abs/2604.18530v1)
- **SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents** <2026-04-20>  
  *Xinshun Feng, Xinhao Song, Lijun Li, Gongshen Liu, Jing Shao*. [[Paper]](https://arxiv.org/abs/2604.07791v3)
- **Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks** <2026-04-20>  
  *Md Rysul Kabir, Zoran Tiganj*. [[Paper]](https://arxiv.org/abs/2604.18510v1)
- **StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning** <2026-04-20>  
  *Daoyu Wang, Qingchuan Li, Mingyue Cheng, Jie Ouyang, Shuo Yu, Qi Liu, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2604.18401v1)
- **Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes** <2026-04-20>  
  *Justin Bauer, Thomas Walshe, Derek Pham, Harit Vishwakarma, Armin Parchami, Frederic Sala, Paroma Varma*. [[Paper]](https://arxiv.org/abs/2604.18381v1)
- **UR$^2$: Unify RAG and Reasoning through Reinforcement Learning** <2026-04-24>  
  *Weitao Li, Boran Xiang, Xiaolong Wang, Zhinan Gou, Weizhi Ma, Yang Liu*. [[Paper]](https://arxiv.org/abs/2508.06165v4)
- **Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning** <2026-04-23>  
  *Qinan Yu, Alexa Tartaglini, Peter Hase, Carlos Guestrin, Christopher Potts*. [[Paper]](https://arxiv.org/abs/2604.22074v1)
- **How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization** <2026-04-23>  
  *Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin Shi, Chaowen Hu, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.19208v2)
- **Mitigating Lost in Multi-turn Conversation via Curriculum RL with Verifiable Accuracy and Abstention Rewards** <2026-04-23>  
  *Ming Li*. [[Paper]](https://arxiv.org/abs/2510.18731v2)
- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** <2026-04-23>  
  *Jiaying Zhang, Lei Shi, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He*. [[Paper]](https://arxiv.org/abs/2601.09361v3)
- **Navigating the Clutter: Waypoint-Based Bi-Level Planning for Multi-Robot Systems** <2026-04-22>  
  *Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan, Gaowen Liu, Shiyu Chang*. [[Paper]](https://arxiv.org/abs/2604.21138v1)
- **V-tableR1: Process-Supervised Multimodal Table Reasoning with Critic-Guided Policy Optimization** <2026-04-22>  
  *Yubo Jiang, Yitong An, Xin Yang, Abudukelimu Wuerkaixi, Xuxin Cheng, Fengying Xie, Zhiguo Jiang, Cao Liu, Ke Zeng, Haopeng Zhang*. [[Paper]](https://arxiv.org/abs/2604.20755v1)
- **Near-Future Policy Optimization** <2026-04-22>  
  *Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao, Zheng Lin, Peng Fu, Nan Duan, Jiaqi Wang*. [[Paper]](https://arxiv.org/abs/2604.20733v1)
- **SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models** <2026-04-22>  
  *Jiahao Xie, Alessio Tonioni, Nathalie Rauschmayr, Federico Tombari, Bernt Schiele*. [[Paper]](https://arxiv.org/abs/2604.20705v1)
- **GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning** <2026-04-22>  
  *Jingyi Wang, Lei Zhu, Tengjin Weng, Song-Li Wu, Haochen Tan, Jierun Chen, Chaofan Tao, Haoli Bai, Lu Hou, Lifeng Shang, Xiao-Ping Zhang*. [[Paper]](https://arxiv.org/abs/2604.20659v1)
- **CodeRL+: Improving Code Generation via Reinforcement with Execution Semantics Alignment** <2026-04-22>  
  *Xue Jiang, Yihong Dong, Mengyang Liu, Hongyi Deng, Tian Wang, Yongding Tao, Rongyu Cao, Binhua Li, Zhi Jin, Wenpin Jiao, Fei Huang, Yongbin Li, Ge Li*. [[Paper]](https://arxiv.org/abs/2510.18471v2)
- **Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models** <2026-04-22>  
  *Xin Xu, Clive Bai, Kai Yang, Tianhao Chen, Yangkun Chen, Weijie Liu, Hao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2602.12036v2)
- **Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning** <2026-04-22>  
  *Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang*. [[Paper]](https://arxiv.org/abs/2512.15146v3)
- **Not All Rollouts are Useful: Down-Sampling Rollouts in LLM Reinforcement Learning** <2026-04-22>  
  *Yixuan Even Xu, Yash Savani, Fei Fang, J. Zico Kolter*. [[Paper]](https://arxiv.org/abs/2504.13818v5)
- **Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization** <2026-04-21>  
  *Carter Adams, Rafael Oliveira, Gabriel Almeida, Sofia Torres*. [[Paper]](https://arxiv.org/abs/2604.19857v1)
- **Prioritizing the Best: Incentivizing Reliable Multimodal Reasoning by Rewarding Beyond Answer Correctness** <2026-04-20>  
  *Mengzhao Jia, Zhihan Zhang, Meng Jiang*. [[Paper]](https://arxiv.org/abs/2604.18892v1)
- **When and What to Ask: AskBench and Rubric-Guided RLVR for LLM Clarification** <2026-04-20>  
  *Jiale Zhao, Ke Fang, Lu Cheng*. [[Paper]](https://arxiv.org/abs/2602.11199v2)
- **When Can LLMs Learn to Reason with Weak Supervision?** <2026-04-20>  
  *Salman Rahman, Jingyan Shen, Anna Mordvina, Hamid Palangi, Saadia Gabriel, Pavel Izmailov*. [[Paper]](https://arxiv.org/abs/2604.18574v1)
- **OGER: A Robust Offline-Guided Exploration Reward for Hybrid Reinforcement Learning** <2026-04-20>  
  *Xinyu Ma, Mingzhou Xu, Xuebo Liu, Chang Jin, Qiang Wang, Derek F. Wong, Min Zhang*. [[Paper]](https://arxiv.org/abs/2604.18530v1)
- **SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents** <2026-04-20>  
  *Xinshun Feng, Xinhao Song, Lijun Li, Gongshen Liu, Jing Shao*. [[Paper]](https://arxiv.org/abs/2604.07791v3)
- **Different Paths to Harmful Compliance: Behavioral Side Effects and Mechanistic Divergence Across LLM Jailbreaks** <2026-04-20>  
  *Md Rysul Kabir, Zoran Tiganj*. [[Paper]](https://arxiv.org/abs/2604.18510v1)
- **StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement Learning** <2026-04-20>  
  *Daoyu Wang, Qingchuan Li, Mingyue Cheng, Jie Ouyang, Shuo Yu, Qi Liu, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2604.18401v1)
- **Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes** <2026-04-20>  
  *Justin Bauer, Thomas Walshe, Derek Pham, Harit Vishwakarma, Armin Parchami, Frederic Sala, Paroma Varma*. [[Paper]](https://arxiv.org/abs/2604.18381v1)
- **GeometryZero: Advancing Geometry Solving via Group Contrastive Policy Optimization** <2026-04-20>  
  *Yikun Wang, Yibin Wang, Dianyi Wang, Zimian Peng, Qipeng Guo, Dacheng Tao, Jiaqi Wang*. [[Paper]](https://arxiv.org/abs/2506.07160v3)
- **QuantumQA: Enhancing Scientific Reasoning via Physics-Consistent Dataset and Verification-Aware Reinforcement Learning** <2026-04-20>  
  *Songxin Qu, Tai-Ping Sun, Yun-Jie Wang, Huan-Yu Liu, Cheng Xue, Xiao-Fan Xu, Han Fang, Yang Yang, Yu-Chun Wu, Guo-Ping Guo, Zhao-Yun Chen*. [[Paper]](https://arxiv.org/abs/2604.18176v1)
- **Reinforced Efficient Reasoning via Semantically Diverse Exploration** <2026-04-20>  
  *Ziqi Zhao, Zhaochun Ren, Jiahong Zou, Liu Yang, Zhiwei Xu, Xuri Ge, Zhumin Chen, Xinyu Ma, Daiting Shi, Shuaiqiang Wang, Dawei Yin, Xin Xin*. [[Paper]](https://arxiv.org/abs/2601.05053v2)
- **Semantic-Space Exploration and Exploitation in RLVR for LLM Reasoning** <2026-04-20>  
  *Fanding Huang, Guanbo Huang, Xiao Fan, Yi He, Xiao Liang, Xiao Chen, Qinting Jiang, Faisal Nadeem Khan, Jingyan Jiang, Zhi Wang*. [[Paper]](https://arxiv.org/abs/2509.23808v5)
- **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** <2026-04-20>  
  *Xinping Zhao, Shouzheng Huang, Yan Zhong, Xinshuo Hu, Meishan Zhang, Baotian Hu, Min Zhang*. [[Paper]](https://arxiv.org/abs/2507.15586v7)
- **EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning** <2026-04-20>  
  *Huanyu Liu, Jia Li, Yihong Dong, Chang Yu, Taozhi Chen, Lecheng Wang, Yongding Tao, Bin Gu, Ge Li*. [[Paper]](https://arxiv.org/abs/2508.07809v5)
- **HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment** <2026-04-20>  
  *Zhanyu Liu, Qingguo Hu, Ante Wang, Chenqing Liu, Zhishang Xiang, Hui Li, Delai Qiu, Jinsong Su*. [[Paper]](https://arxiv.org/abs/2604.17928v1)
- **Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification** <2026-04-20>  
  *Yiju Guo, Tianyi Hu, Zexu Sun, Yankai Lin*. [[Paper]](https://arxiv.org/abs/2601.21244v3)
- **Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR** <2026-04-19>  
  *Muhammad Khalifa, Zohaib Khan, Omer Tafveez, Hao Peng, Lu Wang*. [[Paper]](https://arxiv.org/abs/2603.07084v2)
- **Revisiting Entropy in Reinforcement Learning for Large Reasoning Models** <2026-04-19>  
  *Renren Jin, Pengzhi Gao, Yuqi Ren, Zhuowen Han, Tongxuan Zhang, Wuwei Huang, Wei Liu, Jian Luan, Deyi Xiong*. [[Paper]](https://arxiv.org/abs/2511.05993v3)
- **From $\log π$ to $π$: Taming Divergence in Soft Clipping via Bilateral Decoupled Decay of Probability Gradient Weight** <2026-04-19>  
  *Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Chaowen Hu, Cong Qin, Zekai Shao, Binbin Zheng, Lu Pan, Ke Zeng*. [[Paper]](https://arxiv.org/abs/2603.14389v2)
- **Writing-RL: Advancing Long-form Writing via Adaptive Curriculum Reinforcement Learning** <2026-04-19>  
  *Xuanyu Lei, Chenliang Li, Yuning Wu, Kaiming Liu, Weizhou Shen, Peng Li, Ming Yan, Fei Huang, Ya-Qin Zhang, Yang Liu*. [[Paper]](https://arxiv.org/abs/2506.05760v2)
- **GanitLLM: Difficulty-Aware Bengali Mathematical Reasoning through Curriculum-GRPO** <2026-04-19>  
  *Shubhashis Roy Dipta, Khairul Mahbub, Nadia Najjar*. [[Paper]](https://arxiv.org/abs/2601.06767v3)
- **AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning** <2026-04-18>  
  *Mengzhao Jia, Zhihan Zhang, Ignacio Cases, Zheyuan Liu, Meng Jiang, Peng Qi*. [[Paper]](https://arxiv.org/abs/2510.14738v2)
- **MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning** <2026-04-18>  
  *Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.17550v3)
- **Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL** <2026-04-18>  
  *Skylar Zhai, Jingcheng Liang, Dongyeop Kang*. [[Paper]](https://arxiv.org/abs/2604.17073v1)
- **MCPO: Mastery-Consolidated Policy Optimization for Large Reasoning Models** <2026-04-18>  
  *Zhaokang Liao, Yingguo Gao, Yi Yang, Yongheng Hu, Jingting Ding*. [[Paper]](https://arxiv.org/abs/2604.16972v1)
- **EasyVideoR1: Easier RL for Video Understanding** <2026-04-18>  
  *Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao, Zheng Lin, Peng Fu, Nan Duan, Jiaqi Wang*. [[Paper]](https://arxiv.org/abs/2604.16893v1)
- **Incentivizing Parametric Knowledge via Reinforcement Learning with Verifiable Rewards for Cross-Cultural Entity Translation** <2026-04-18>  
  *Jiang Zhou, Xiaohu Zhao, Xinwei Wu, Tianyu Dong, Hao Wang, Yangyang Liu, Heng Liu, Linlong Xu, Longyue Wang, Weihua Luo, Deyi Xiong*. [[Paper]](https://arxiv.org/abs/2604.16881v1)
- **Detecting and Suppressing Reward Hacking with Gradient Fingerprints** <2026-04-17>  
  *Songtao Wang, Quang Hieu Pham, Fangcong Yin, Xinpeng Wang, Jocelyn Qiaochu Chen, Greg Durrett, Xi Ye*. [[Paper]](https://arxiv.org/abs/2604.16242v1)
- **ATTNPO: Attention-Guided Process Supervision for Efficient Reasoning** <2026-04-17>  
  *Shuaiyi Nie, Siyu Ding, Wenyuan Zhang, Linhao Yu, Tianmeng Yang, Yao Chen, Weichong Yin, Yu Sun, Hua Wu, Tingwen Liu*. [[Paper]](https://arxiv.org/abs/2602.09953v2)
- **Revisiting Entropy Regularization: Adaptive Coefficient Unlocks Its Potential for LLM Reinforcement Learning** <2026-04-17>  
  *Xiaoyun Zhang, Xiaojian Yuan, Di Huang, Wang You, Chen Hu, Jingqing Ruan, Ai Jian, Kejiang Chen, Xing Hu*. [[Paper]](https://arxiv.org/abs/2510.10959v3)
- **Self-Aligned Reward: Towards Effective and Efficient Reasoners** <2026-04-16>  
  *Peixuan Han, Adit Krishnan, Gerald Friedland, Jiaxuan You, Chris Kong*. [[Paper]](https://arxiv.org/abs/2509.05489v2)
- **LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking** <2026-04-16>  
  *Lukas Helff, Quentin Delfosse, David Steinmann, Ruben Härle, Hikaru Shindo, Patrick Schramowski, Wolfgang Stammer, Kristian Kersting, Felix Friedrich*. [[Paper]](https://arxiv.org/abs/2604.15149v1)
- **Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning** <2026-04-16>  
  *Can Xie, Ruotong Pan, Xiangyu Wu, Yunfei Zhang, Jiayi Fu, Tingting Gao, Guorui Zhou*. [[Paper]](https://arxiv.org/abs/2510.10649v2)
- **Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language** <2026-04-16>  
  *Peijie Wang, Ming-Liang Zhang, Jun Cao, Chao Deng, Dekang Ran, Hongda Sun, Pi Bu, Xuan Zhang, Yingyao Wang, Jun Song, Bo Zheng, Fei Yin, Cheng-Lin Liu*. [[Paper]](https://arxiv.org/abs/2604.11600v2)
- **Do Not Step Into the Same River Twice: Learning to Reason from Trial and Error** <2026-04-16>  
  *Chenming Tang, Hsiu-Yuan Huang, Weijie Liu, Clive Bai, Saiyong Yang, Yunfang Wu*. [[Paper]](https://arxiv.org/abs/2510.26109v4)
- **SSPO: Subsentence-level Policy Optimization** <2026-04-10>  
  *Kun Yang, Zikang chen, Yanmeng Wang, Zhigen Li, Ning Cheng, Shaojun Wang, Jing Xiao*. [[Paper]](https://arxiv.org/abs/2511.04256v2)
- **Visually-Guided Policy Optimization for Multimodal Reasoning** <2026-04-10>  
  *Zengbin Wang, Feng Xiong, Liang Lin, Xuecai Hu, Yong Wang, Yanlin Wang, Man Zhang, Xiangxiang Chu*. [[Paper]](https://arxiv.org/abs/2604.09349v1)
- **ActFER: Agentic Facial Expression Recognition via Active Tool-Augmented Visual Reasoning** <2026-04-10>  
  *Shifeng Liu, Zhengye Zhang, Sirui Zhao, Xinglong Mao, Zhehan Kan, Zhixiang Wei, Shiwei Wu, Chaoyou Fu, Tong Xu, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2604.08990v1)
- **PerMix-RLVR: Preserving Persona Expressivity under Verifiable-Reward Alignment** <2026-04-10>  
  *Jihwan Oh, Soowon Oh, Murad Aghazada, Minchan Jeong, Sungnyun Kim, Se-Young Yun*. [[Paper]](https://arxiv.org/abs/2604.08986v1)
- **Skip-Connected Policy Optimization for Implicit Advantage** <2026-04-09>  
  *Fengwei Teng, Jinyi Bai, Xinhao Yao, Demi Ruohan Wang, Jiahao Zhao, Zhijiang Guo*. [[Paper]](https://arxiv.org/abs/2604.08690v1)
- **SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions** <2026-04-09>  
  *Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh, Hritik Bansal, Saadia Gabriel*. [[Paper]](https://arxiv.org/abs/2604.08477v1)
- **Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization** <2026-04-09>  
  *Sai Srinivas Kancheti, Aditya Kanade, Rohit Sinha, Vineeth N Balasubramanian, Tanuja Ganu*. [[Paper]](https://arxiv.org/abs/2604.08476v1)
- **TTVS: Boosting Self-Exploring Reinforcement Learning via Test-time Variational Synthesis** <2026-04-09>  
  *Sikai Bai, Haoxi Li, Jie Zhang, Yongjiang Liu, Song Guo*. [[Paper]](https://arxiv.org/abs/2604.08468v1)
- **Fundus-R1: Training a Fundus-Reading MLLM with Knowledge-Aware Reasoning on Public Data** <2026-04-09>  
  *Yuchuan Deng, Qijie Wei, Kaiheng Qian, Jiazhen Liu, Zijie Xin, Bangxiang Lan, Jingyu Liu, Jianfeng Dong, Xirong Li*. [[Paper]](https://arxiv.org/abs/2604.08322v1)
- **Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning** <2026-04-09>  
  *Ziqi Miao, Haonan Jia, Lijun Li, Chen Qian, Yuan Xiong, Wenting Yan, Jing Shao*. [[Paper]](https://arxiv.org/abs/2603.28618v2)
- **ZeroCoder: Can LLMs Improve Code Generation Without Ground-Truth Supervision?** <2026-04-09>  
  *Lishui Fan, Mouxiang Chen, Tingwei Zhu, Kui Liu, Xin Xia, Shanping Li, Zhongxin Liu*. [[Paper]](https://arxiv.org/abs/2604.07864v1)
- **SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents** <2026-04-09>  
  *Xinshun Feng, Xinhao Song, Lijun Li, Gongshen Liu, Jing Shao*. [[Paper]](https://arxiv.org/abs/2604.07791v1)
- **Mitigating Distribution Sharpening in Math RLVR via Distribution-Aligned Hint Synthesis and Backward Hint Annealing** <2026-04-09>  
  *Pei-Xi Xie, Che-Yu Lin, Cheng-Lin Yang*. [[Paper]](https://arxiv.org/abs/2604.07747v1)
- **An Imperfect Verifier is Good Enough: Learning with Noisy Rewards** <2026-04-09>  
  *Andreas Plesner, Francisco Guzmán, Anish Athalye*. [[Paper]](https://arxiv.org/abs/2604.07666v1)
- **Gym-V: A Unified Vision Environment System for Agentic Vision Research** <2026-04-08>  
  *Fanqing Meng, Lingxiao Du, Jiawei Gu, Jiaqi Liao, Linjie Li, Zijian Wu, Xiangyan Liu, Ziqi Zhao, Mengkang Hu, Zichen Liu, Jiaheng Zhang, Michael Qizhe Shieh*. [[Paper]](https://arxiv.org/abs/2603.15432v3)
- **Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models** <2026-04-08>  
  *Zekai Ye, Qiming Li, Xiaocheng Feng, Ruihan Chen, Ziming Li, Haoyu Ren, Kun Chen, Dandan Tu, Bing Qin*. [[Paper]](https://arxiv.org/abs/2604.01840v2)
- **Self-Distilled RLVR** <2026-04-08>  
  *Chenxu Yang, Chuanyu Qin, Qingyi Si, Minghui Chen, Naibin Gu, Dingyu Yao, Zheng Lin, Weiping Wang, Jiaqi Wang, Nan Duan*. [[Paper]](https://arxiv.org/abs/2604.03128v2)
- **GIFT: Group-Relative Implicit Fine-Tuning Integrates GRPO with DPO and UNA** <2026-04-08>  
  *Zhichao Wang*. [[Paper]](https://arxiv.org/abs/2510.23868v4)
- **Reinforcement Learning for LLM Post-Training: A Survey** <2026-04-08>  
  *Zhichao Wang, Kiran Ramnath, Bin Bi, Shiva Kumar Pentyala, Sougata Chaudhuri, Shubham Mehrotra, Zixu, Zhu, Xiang-Bo Mao, Sitaram Asur, Na, Cheng*. [[Paper]](https://arxiv.org/abs/2407.16216v2)
- **Rectifying LLM Thought from Lens of Optimization** <2026-04-07>  
  *Junnan Liu, Hongwei Liu, Songyang Zhang, Kai Chen*. [[Paper]](https://arxiv.org/abs/2512.01925v2)
- **Target Policy Optimization** <2026-04-07>  
  *Jean Kaddour*. [[Paper]](https://arxiv.org/abs/2604.06159v1)
- **DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search** <2026-04-06>  
  *Fang Wu, Weihao Xuan, Heli Qi, Ximing Lu, Aaron Tu, Li Erran Li, Yejin Choi*. [[Paper]](https://arxiv.org/abs/2509.25454v4)
- **ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement** <2026-04-06>  
  *Difan Jiao, Qianfeng Wen, Blair Yang, Zhenwei Tang, Ashton Anderson*. [[Paper]](https://arxiv.org/abs/2604.01591v2)
- **Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation** <2026-04-06>  
  *Hengrui Gu, Xiaotian Han, Yujing Bian, Kaixiong Zhou*. [[Paper]](https://arxiv.org/abs/2604.04894v1)
- **A Model Can Help Itself: Reward-Free Self-Training for LLM Reasoning** <2026-04-06>  
  *Mengqi Li, Lei Zhao, Anthony Man-Cho So, Ruoyu Sun, Xiao Li*. [[Paper]](https://arxiv.org/abs/2510.18814v2)
- **Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems** <2026-04-06>  
  *Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal*. [[Paper]](https://arxiv.org/abs/2604.04767v1)
- **Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration** <2026-04-06>  
  *Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Dongchun Xie, Hanhui Li, Yiwei Wang, Xiaodan Liang, Jing Tang*. [[Paper]](https://arxiv.org/abs/2508.13755v7)
- **SPHINX: A Synthetic Environment for Visual Perception and Reasoning** <2026-04-05>  
  *Md Tanvirul Alam, Saksham Aggarwal, Justin Yang Chae, Nidhi Rastogi*. [[Paper]](https://arxiv.org/abs/2511.20814v2)
- **Scaling the Scaling Logic: Agentic Meta-Synthesis of Logic Reasoning** <2026-04-05>  
  *Bowen Liu, Zhi Wu, Runquan Xie, Zhanhui Kang, Jia Li*. [[Paper]](https://arxiv.org/abs/2602.13218v2)
- **Can LLMs Learn to Reason Robustly under Noisy Supervision?** <2026-04-05>  
  *Shenzhi Yang, Guangcheng Zhu, Bowen Song, Sharon Li, Haobo Wang, Xing Zheng, Yingfan Ma, Zhongqi Chen, Weiqiang Wang, Gang Chen*. [[Paper]](https://arxiv.org/abs/2604.03993v1)
- **Hindsight-Anchored Policy Optimization: Turning Failure into Feedback in Sparse Reward Settings** <2026-04-04>  
  *Yuning Wu, Ke Wang, Devin Chen, Kai Wei*. [[Paper]](https://arxiv.org/abs/2603.11321v2)
- **Apriel-1.5-OpenReasoner: RL Post-Training for General-Purpose and Efficient Reasoning** <2026-04-03>  
  *Rafael Pardinas, Ehsan Kamalloo, David Vazquez, Alexandre Drouin*. [[Paper]](https://arxiv.org/abs/2604.02007v2)
- **ERPO: Token-Level Entropy-Regulated Policy Optimization for Large Reasoning Models** <2026-04-03>  
  *Song Yu, Li Li, Wenwen Zhao, Zhisheng Yang*. [[Paper]](https://arxiv.org/abs/2603.28204v2)
- **Reinforcement Learning-based Knowledge Distillation with LLM-as-a-Judge** <2026-04-03>  
  *Yiyang Shen, Lifu Tu, Weiran Wang*. [[Paper]](https://arxiv.org/abs/2604.02621v1)
- **Future Policy Approximation for Offline Reinforcement Learning Improves Mathematical Reasoning** <2026-04-03>  
  *Minjae Oh, Yunho Choi, Dongmin Choi, Yohan Jo*. [[Paper]](https://arxiv.org/abs/2509.19893v2)
- **Reinforcement Learning from Human Feedback: A Statistical Perspective** <2026-04-02>  
  *Pangpang Liu, Chengchun Shi, Will Wei Sun*. [[Paper]](https://arxiv.org/abs/2604.02507v1)
- **Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing** <2026-04-02>  
  *Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng, Haiyun Guo, Dan Zhang, Jinqiao Wang, Tat-Seng Chua*. [[Paper]](https://arxiv.org/abs/2604.02288v1)
- **Policy Improvement Reinforcement Learning** <2026-04-01>  
  *Huaiyang Wang, Xiaojie Li, Deqing Wang, Haoyi Zhou, Zixuan Huang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2604.00860v1)
- **RefineRL: Advancing Competitive Programming with Self-Refinement Reinforcement Learning** <2026-04-01>  
  *Shaopeng Fu, Xingxing Zhang, Li Dong, Di Wang, Furu Wei*. [[Paper]](https://arxiv.org/abs/2604.00790v1)
- **Learning to Hint for Reinforcement Learning** <2026-04-01>  
  *Yu Xia, Canwen Xu, Zhewei Yao, Julian McAuley, Yuxiong He*. [[Paper]](https://arxiv.org/abs/2604.00698v1)
- **Execution-Verified Reinforcement Learning for Optimization Modeling** <2026-04-01>  
  *Runda Guan, Xiangqing Shen, Jiajun Zhang, Yifan Zhang, Jian Cheng, Rui Xia*. [[Paper]](https://arxiv.org/abs/2604.00442v1)
- **Replacing Multi-Step Assembly of Data Preparation Pipelines with One-Step LLM Pipeline Generation for Table QA** <2026-04-01>  
  *Fengyu Li, Junhao Zhu, Kaishi Song, Lu Chen, Zhongming Yao, Tianyi Li, Christian S. Jensen*. [[Paper]](https://arxiv.org/abs/2602.22721v2)
- **Reinforced Reasoning for End-to-End Retrosynthetic Planning** <2026-03-31>  
  *Chenyang Zuo, Siqi Fan, Yizhen Luo, Zaiqing Nie*. [[Paper]](https://arxiv.org/abs/2603.29723v1)
- **Towards Policy-Adaptive Image Guardrail: Benchmark and Method** <2026-03-31>  
  *Caiyong Piao, Zhiyuan Yan, Haoming Xu, Yunzhen Zhao, Kaiqing Lin, Feiyang Xu, Shuigeng Zhou*. [[Paper]](https://arxiv.org/abs/2603.01228v2)
- **When Rubrics Fail: Error Enumeration as Reward in Reference-Free RL Post-Training for Virtual Try-On** <2026-03-31>  
  *Wisdom Ikezogwo, Mehmet Saygin Seyfioglu, Ranjay Krishna, Karim Bouyarmane*. [[Paper]](https://arxiv.org/abs/2603.05659v2)
- **ReViSQL: Achieving Human-Level Text-to-SQL** <2026-03-30>  
  *Yuxuan Zhu, Tengjun Jin, Yoojin Choi, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.20004v2)
- **SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning** <2026-03-30>  
  *Philip Schroeder, Thomas Weng, Karl Schmeckpeper, Eric Rosen, Stephen Hart, Ondrej Biza*. [[Paper]](https://arxiv.org/abs/2603.28730v1)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** <2026-03-30>  
  *Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu*. [[Paper]](https://arxiv.org/abs/2602.05548v3)
- **SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology** <2026-03-30>  
  *Yifan Wang, Bolian Li, David Cho, Ruqi Zhang, Fanping Sui, Ananth Grama*. [[Paper]](https://arxiv.org/abs/2603.27977v1)
- **Wan-R1: Verifiable-Reinforcement Learning for Video Reasoning** <2026-03-29>  
  *Ming Liu, Yunbei Zhang, Shilong Liu, Liwen Wang, Wensheng Zhang*. [[Paper]](https://arxiv.org/abs/2603.27866v1)
- **Self-Distilled RLVR** <2026-04-03>  
  *Chenxu Yang, Chuanyu Qin, Qingyi Si, Minghui Chen, Naibin Gu, Dingyu Yao, Zheng Lin, Weiping Wang, Jiaqi Wang, Nan Duan*. [[Paper]](https://arxiv.org/abs/2604.03128v1)
- **ERPO: Token-Level Entropy-Regulated Policy Optimization for Large Reasoning Models** <2026-04-03>  
  *Song Yu, Li Li, Wenwen Zhao, Zhisheng Yang*. [[Paper]](https://arxiv.org/abs/2603.28204v2)
- **Reinforcement Learning-based Knowledge Distillation with LLM-as-a-Judge** <2026-04-03>  
  *Yiyang Shen, Lifu Tu, Weiran Wang*. [[Paper]](https://arxiv.org/abs/2604.02621v1)
- **Future Policy Approximation for Offline Reinforcement Learning Improves Mathematical Reasoning** <2026-04-03>  
  *Minjae Oh, Yunho Choi, Dongmin Choi, Yohan Jo*. [[Paper]](https://arxiv.org/abs/2509.19893v2)
- **Reinforcement Learning from Human Feedback: A Statistical Perspective** <2026-04-02>  
  *Pangpang Liu, Chengchun Shi, Will Wei Sun*. [[Paper]](https://arxiv.org/abs/2604.02507v1)
- **Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing** <2026-04-02>  
  *Gengsheng Li, Tianyu Yang, Junfeng Fang, Mingyang Song, Mao Zheng, Haiyun Guo, Dan Zhang, Jinqiao Wang, Tat-Seng Chua*. [[Paper]](https://arxiv.org/abs/2604.02288v1)
- **Apriel-Reasoner: RL Post-Training for General-Purpose and Efficient Reasoning** <2026-04-02>  
  *Rafael Pardinas, Ehsan Kamalloo, David Vazquez, Alexandre Drouin*. [[Paper]](https://arxiv.org/abs/2604.02007v1)
- **Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models** <2026-04-02>  
  *Zekai Ye, Qiming Li, Xiaocheng Feng, Ruihan Chen, Ziming Li, Haoyu Ren, Kun Chen, Dandan Tu, Bing Qin*. [[Paper]](https://arxiv.org/abs/2604.01840v1)
- **ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement** <2026-04-02>  
  *Difan Jiao, Qianfeng Wen, Blair Yang, Zhenwei Tang, Ashton Anderson*. [[Paper]](https://arxiv.org/abs/2604.01591v1)
- **Policy Improvement Reinforcement Learning** <2026-04-01>  
  *Huaiyang Wang, Xiaojie Li, Deqing Wang, Haoyi Zhou, Zixuan Huang, Yaodong Yang, Jianxin Li, Yikun Ban*. [[Paper]](https://arxiv.org/abs/2604.00860v1)
- **RefineRL: Advancing Competitive Programming with Self-Refinement Reinforcement Learning** <2026-04-01>  
  *Shaopeng Fu, Xingxing Zhang, Li Dong, Di Wang, Furu Wei*. [[Paper]](https://arxiv.org/abs/2604.00790v1)
- **Learning to Hint for Reinforcement Learning** <2026-04-01>  
  *Yu Xia, Canwen Xu, Zhewei Yao, Julian McAuley, Yuxiong He*. [[Paper]](https://arxiv.org/abs/2604.00698v1)
- **Execution-Verified Reinforcement Learning for Optimization Modeling** <2026-04-01>  
  *Runda Guan, Xiangqing Shen, Jiajun Zhang, Yifan Zhang, Jian Cheng, Rui Xia*. [[Paper]](https://arxiv.org/abs/2604.00442v1)
- **Replacing Multi-Step Assembly of Data Preparation Pipelines with One-Step LLM Pipeline Generation for Table QA** <2026-04-01>  
  *Fengyu Li, Junhao Zhu, Kaishi Song, Lu Chen, Zhongming Yao, Tianyi Li, Christian S. Jensen*. [[Paper]](https://arxiv.org/abs/2602.22721v2)
- **Reinforced Reasoning for End-to-End Retrosynthetic Planning** <2026-03-31>  
  *Chenyang Zuo, Siqi Fan, Yizhen Luo, Zaiqing Nie*. [[Paper]](https://arxiv.org/abs/2603.29723v1)
- **Towards Policy-Adaptive Image Guardrail: Benchmark and Method** <2026-03-31>  
  *Caiyong Piao, Zhiyuan Yan, Haoming Xu, Yunzhen Zhao, Kaiqing Lin, Feiyang Xu, Shuigeng Zhou*. [[Paper]](https://arxiv.org/abs/2603.01228v2)
- **When Rubrics Fail: Error Enumeration as Reward in Reference-Free RL Post-Training for Virtual Try-On** <2026-03-31>  
  *Wisdom Ikezogwo, Mehmet Saygin Seyfioglu, Ranjay Krishna, Karim Bouyarmane*. [[Paper]](https://arxiv.org/abs/2603.05659v2)
- **ReViSQL: Achieving Human-Level Text-to-SQL** <2026-03-30>  
  *Yuxuan Zhu, Tengjun Jin, Yoojin Choi, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.20004v2)
- **SOLE-R1: Video-Language Reasoning as the Sole Reward for On-Robot Reinforcement Learning** <2026-03-30>  
  *Philip Schroeder, Thomas Weng, Karl Schmeckpeper, Eric Rosen, Stephen Hart, Ondrej Biza*. [[Paper]](https://arxiv.org/abs/2603.28730v1)
- **Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning** <2026-03-30>  
  *Ziqi Miao, Haonan Jia, Lijun Li, Chen Qian, Yuan Xiong, Wenting Yan, Jing Shao*. [[Paper]](https://arxiv.org/abs/2603.28618v1)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** <2026-03-30>  
  *Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu*. [[Paper]](https://arxiv.org/abs/2602.05548v3)
- **SARL: Label-Free Reinforcement Learning by Rewarding Reasoning Topology** <2026-03-30>  
  *Yifan Wang, Bolian Li, David Cho, Ruqi Zhang, Fanping Sui, Ananth Grama*. [[Paper]](https://arxiv.org/abs/2603.27977v1)
- **Wan-R1: Verifiable-Reinforcement Learning for Video Reasoning** <2026-03-29>  
  *Ming Liu, Yunbei Zhang, Shilong Liu, Liwen Wang, Wensheng Zhang*. [[Paper]](https://arxiv.org/abs/2603.27866v1)
- **Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models** <2026-03-28>  
  *Yuhang Han, Yuyang Wu, Zhengbo Jiao, Yiyu Wang, Xuyang Liu, Shaobo Wang, Hanlin Xu, Xuming Hu, Linfeng Zhang*. [[Paper]](https://arxiv.org/abs/2603.27375v1)
- **Incentivizing Temporal-Awareness in Egocentric Video Understanding Models** <2026-03-28>  
  *Zhiyang Xu, Tian Qin, Bowen Jin, Zhengfeng Lai, Meng Cao, Lifu Huang, Peng Zhang*. [[Paper]](https://arxiv.org/abs/2603.27184v1)
- **From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training** <2026-03-28>  
  *Donglai Xu, Hongzheng Yang, Yuzhi Zhao, Pingping Zhang, Jinpeng Chen, Wenao Ma, Zhijian Hou, Mengyang Wu, Xiaolei Li, Senkang Hu, Ziyi Guan, Jason Chun Lok Li, Lai Man Po*. [[Paper]](https://arxiv.org/abs/2511.07738v2)
- **Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR** <2026-03-27>  
  *Jinda Lu, Junkang Wu, Jinghan Li, Kexin Huang, Shuo Yang, Mingzhu Chen, Jiancan Wu, Kuien Liu, Xiang Wang*. [[Paper]](https://arxiv.org/abs/2603.26126v1)
- **Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models** <2026-03-27>  
  *Boxin Wang, Chankyu Lee, Nayeon Lee, Sheng-Chieh Lin, Wenliang Dai, Yang Chen, Yangyi Chen, Zhuolin Yang, Zihan Liu, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping*. [[Paper]](https://arxiv.org/abs/2512.13607v2)
- **Do Language Models Follow Occam's Razor? An Evaluation of Parsimony in Inductive and Abductive Reasoning** <2026-03-26>  
  *Yunxin Sun, Abulhair Saparov*. [[Paper]](https://arxiv.org/abs/2509.03345v2)
- **P^2O: Joint Policy and Prompt Optimization** <2026-03-26>  
  *Xinyu Lu, Kaiqi Zhang, Jinglin Yang, Boxi Cao, Yaojie Lu, Hongyu Lin, Min He, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2603.21877v2)
- **TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs** <2026-03-26>  
  *Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang*. [[Paper]](https://arxiv.org/abs/2512.14698v2)
- **MSRL: Scaling Generative Multimodal Reward Modeling via Multi-Stage Reinforcement Learning** <2026-03-26>  
  *Chenglong Wang, Yifu Huo, Yang Gan, Qiaozhi He, Qi Meng, Bei Li, Yan Wang, Junfu Liu, Tianhua Zhou, Jingbo Zhu, Tong Xiao*. [[Paper]](https://arxiv.org/abs/2603.25108v1)
- **Bridging Perception and Reasoning: Token Reweighting for RLVR in Multimodal LLMs** <2026-03-26>  
  *Jinda Lu, Junkang Wu, Jinghan Li, Kexin Huang, Shuo Yang, Guoyin Wang, Jiancan Wu, Xiang Wang, Xiangnan He*. [[Paper]](https://arxiv.org/abs/2603.25077v1)
- **Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR** <2026-03-25>  
  *Haobo Xu, Sirui Chen, Ruizhong Qiu, Yuchen Yan, Chen Luo, Monica Cheng, Jingrui He, Hanghang Tong*. [[Paper]](https://arxiv.org/abs/2603.24840v1)
- **Towards Effective Experiential Learning: Dual Guidance for Utilization and Internalization** <2026-03-25>  
  *Fei Bai, Zhipeng Chen, Chuan Hao, Ming Yang, Ran Tao, Bryan Dai, Wayne Xin Zhao, Jian Yang, Hongteng Xu*. [[Paper]](https://arxiv.org/abs/2603.24093v1)
- **Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought** <2026-03-24>  
  *Yunheng Li, Hangyi Kuang, Hengrui Zhang, Jiangxia Cao, Zhaojie Liu, Qibin Hou, Ming-Ming Cheng*. [[Paper]](https://arxiv.org/abs/2603.22847v1)
- **Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs** <2026-03-23>  
  *Haoming Meng, Kexin Huang, Shaohang Wei, Chiyu Ma, Shuo Yang, Xue Wang, Guoyin Wang, Bolin Ding, Jingren Zhou*. [[Paper]](https://arxiv.org/abs/2603.22446v1)
- **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation** <2026-03-23>  
  *Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan*. [[Paper]](https://arxiv.org/abs/2603.22435v1)
- **SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation** <2026-03-23>  
  *Sashuai Zhou, Qiang Zhou, Junpeng Ma, Yue Cao, Ruofan Hu, Ziang Zhang, Xiaoda Yang, Zhibin Wang, Jun Song, Cheng Yu, Bo Zheng, Zhou Zhao*. [[Paper]](https://arxiv.org/abs/2603.22228v1)
- **Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment** <2026-03-23>  
  *Aleksander Boruch-Gruszecki, Yangtian Zi, Zixuan Wu, Tejas Oberoi, Carolyn Jane Anderson, Joydeep Biswas, Arjun Guha*. [[Paper]](https://arxiv.org/abs/2508.04865v3)
- **On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation** <2026-03-23>  
  *Kexin Huang, Haoming Meng, Junkang Wu, Jinda Lu, Chiyu Ma, Ziqian Chen, Xue Wang, Bolin Ding, Jiancan Wu, Xiang Wang, Xiangnan He, Guoyin Wang, Jingren Zhou*. [[Paper]](https://arxiv.org/abs/2603.22117v1)
- **Native Reasoning Models: Training Language Models to Reason on Unverifiable Data** <2026-03-23>  
  *Yuanfu Wang, Zhixuan Liu, Xiangtian Li, Chaochao Lu, Chao Yang*. [[Paper]](https://arxiv.org/abs/2602.11549v2)
- **Learning to Reason without External Rewards** <2026-03-23>  
  *Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song*. [[Paper]](https://arxiv.org/abs/2505.19590v4)
- **Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts** <2026-03-22>  
  *Andrei Baroian, Rutger Berger*. [[Paper]](https://arxiv.org/abs/2603.21177v1)
- **WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement** <2026-03-22>  
  *Fangyuan Li, Pengfei Li, Shijie Wang, Junqi Gao, Jianxing Liu, Biqing Qi, Yuqiang Li*. [[Paper]](https://arxiv.org/abs/2603.22352v1)
- **Advantage Shaping as Surrogate Reward Maximization: Unifying Pass@K Policy Gradients** <2026-03-21>  
  *Christos Thrampoulidis, Sadegh Mahdavi, Wenlong Deng*. [[Paper]](https://arxiv.org/abs/2510.23049v3)
- **RLVR Training of LLMs Does Not Improve Thinking Ability for General QA: Evaluation Method and a Simple Solution** <2026-03-21>  
  *Kaiyuan Li, Jing-Cheng Pang, Yang Yu*. [[Paper]](https://arxiv.org/abs/2603.20799v1)
- **Grounded Chess Reasoning in Language Models via Master Distillation** <2026-03-20>  
  *Zhenwei Tang, Qianfeng Wen, Seth Grief-Albert, Yahya Elgabra, Blair Yang, Honghua Dong, Ashton Anderson*. [[Paper]](https://arxiv.org/abs/2603.20510v1)
- **Think and Answer ME: Benchmarking and Exploring Multi-Entity Reasoning Grounding in Remote Sensing** <2026-03-20>  
  *Shuchang Lyu, Haiquan Wen, Guangliang Cheng, Meng Li, Zheng Zhou, You Zhou, Dingding Yao, Zhenwei Shi*. [[Paper]](https://arxiv.org/abs/2603.12788v2)
- **ReLaX: Reasoning with Latent Exploration for Large Reasoning Models** <2026-03-20>  
  *Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, Jibin Wu*. [[Paper]](https://arxiv.org/abs/2512.07558v2)
- **Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR** <2026-03-27>  
  *Jinda Lu, Junkang Wu, Jinghan Li, Kexin Huang, Shuo Yang, Mingzhu Chen, Jiancan Wu, Kuien Liu, Xiang Wang*. [[Paper]](https://arxiv.org/abs/2603.26126v1)
- **Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models** <2026-03-27>  
  *Boxin Wang, Chankyu Lee, Nayeon Lee, Sheng-Chieh Lin, Wenliang Dai, Yang Chen, Yangyi Chen, Zhuolin Yang, Zihan Liu, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping*. [[Paper]](https://arxiv.org/abs/2512.13607v2)
- **Do Language Models Follow Occam's Razor? An Evaluation of Parsimony in Inductive and Abductive Reasoning** <2026-03-26>  
  *Yunxin Sun, Abulhair Saparov*. [[Paper]](https://arxiv.org/abs/2509.03345v2)
- **P^2O: Joint Policy and Prompt Optimization** <2026-03-26>  
  *Xinyu Lu, Kaiqi Zhang, Jinglin Yang, Boxi Cao, Yaojie Lu, Hongyu Lin, Min He, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2603.21877v2)
- **TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs** <2026-03-26>  
  *Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang*. [[Paper]](https://arxiv.org/abs/2512.14698v2)
- **MSRL: Scaling Generative Multimodal Reward Modeling via Multi-Stage Reinforcement Learning** <2026-03-26>  
  *Chenglong Wang, Yifu Huo, Yang Gan, Qiaozhi He, Qi Meng, Bei Li, Yan Wang, Junfu Liu, Tianhua Zhou, Jingbo Zhu, Tong Xiao*. [[Paper]](https://arxiv.org/abs/2603.25108v1)
- **Bridging Perception and Reasoning: Token Reweighting for RLVR in Multimodal LLMs** <2026-03-26>  
  *Jinda Lu, Junkang Wu, Jinghan Li, Kexin Huang, Shuo Yang, Guoyin Wang, Jiancan Wu, Xiang Wang, Xiangnan He*. [[Paper]](https://arxiv.org/abs/2603.25077v1)
- **Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR** <2026-03-25>  
  *Haobo Xu, Sirui Chen, Ruizhong Qiu, Yuchen Yan, Chen Luo, Monica Cheng, Jingrui He, Hanghang Tong*. [[Paper]](https://arxiv.org/abs/2603.24840v1)
- **Towards Effective Experiential Learning: Dual Guidance for Utilization and Internalization** <2026-03-25>  
  *Fei Bai, Zhipeng Chen, Chuan Hao, Ming Yang, Ran Tao, Bryan Dai, Wayne Xin Zhao, Jian Yang, Hongteng Xu*. [[Paper]](https://arxiv.org/abs/2603.24093v1)
- **Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought** <2026-03-24>  
  *Yunheng Li, Hangyi Kuang, Hengrui Zhang, Jiangxia Cao, Zhaojie Liu, Qibin Hou, Ming-Ming Cheng*. [[Paper]](https://arxiv.org/abs/2603.22847v1)
- **Sparse but Critical: A Token-Level Analysis of Distributional Shifts in RLVR Fine-Tuning of LLMs** <2026-03-23>  
  *Haoming Meng, Kexin Huang, Shaohang Wei, Chiyu Ma, Shuo Yang, Xue Wang, Guoyin Wang, Bolin Ding, Jingren Zhou*. [[Paper]](https://arxiv.org/abs/2603.22446v1)
- **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation** <2026-03-23>  
  *Max Fu, Justin Yu, Karim El-Refai, Ethan Kou, Haoru Xue, Huang Huang, Wenli Xiao, Guanzhi Wang, Fei-Fei Li, Guanya Shi, Jiajun Wu, Shankar Sastry, Yuke Zhu, Ken Goldberg, Linxi "Jim" Fan*. [[Paper]](https://arxiv.org/abs/2603.22435v1)
- **SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation** <2026-03-23>  
  *Sashuai Zhou, Qiang Zhou, Junpeng Ma, Yue Cao, Ruofan Hu, Ziang Zhang, Xiaoda Yang, Zhibin Wang, Jun Song, Cheng Yu, Bo Zheng, Zhou Zhao*. [[Paper]](https://arxiv.org/abs/2603.22228v1)
- **Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment** <2026-03-23>  
  *Aleksander Boruch-Gruszecki, Yangtian Zi, Zixuan Wu, Tejas Oberoi, Carolyn Jane Anderson, Joydeep Biswas, Arjun Guha*. [[Paper]](https://arxiv.org/abs/2508.04865v3)
- **On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitation** <2026-03-23>  
  *Kexin Huang, Haoming Meng, Junkang Wu, Jinda Lu, Chiyu Ma, Ziqian Chen, Xue Wang, Bolin Ding, Jiancan Wu, Xiang Wang, Xiangnan He, Guoyin Wang, Jingren Zhou*. [[Paper]](https://arxiv.org/abs/2603.22117v1)
- **Native Reasoning Models: Training Language Models to Reason on Unverifiable Data** <2026-03-23>  
  *Yuanfu Wang, Zhixuan Liu, Xiangtian Li, Chaochao Lu, Chao Yang*. [[Paper]](https://arxiv.org/abs/2602.11549v2)
- **Learning to Reason without External Rewards** <2026-03-23>  
  *Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song*. [[Paper]](https://arxiv.org/abs/2505.19590v4)
- **Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts** <2026-03-22>  
  *Andrei Baroian, Rutger Berger*. [[Paper]](https://arxiv.org/abs/2603.21177v1)
- **WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement** <2026-03-22>  
  *Fangyuan Li, Pengfei Li, Shijie Wang, Junqi Gao, Jianxing Liu, Biqing Qi, Yuqiang Li*. [[Paper]](https://arxiv.org/abs/2603.22352v1)
- **Advantage Shaping as Surrogate Reward Maximization: Unifying Pass@K Policy Gradients** <2026-03-21>  
  *Christos Thrampoulidis, Sadegh Mahdavi, Wenlong Deng*. [[Paper]](https://arxiv.org/abs/2510.23049v3)
- **RLVR Training of LLMs Does Not Improve Thinking Ability for General QA: Evaluation Method and a Simple Solution** <2026-03-21>  
  *Kaiyuan Li, Jing-Cheng Pang, Yang Yu*. [[Paper]](https://arxiv.org/abs/2603.20799v1)
- **Grounded Chess Reasoning in Language Models via Master Distillation** <2026-03-20>  
  *Zhenwei Tang, Qianfeng Wen, Seth Grief-Albert, Yahya Elgabra, Blair Yang, Honghua Dong, Ashton Anderson*. [[Paper]](https://arxiv.org/abs/2603.20510v1)
- **ReViSQL: Achieving Human-Level Text-to-SQL** <2026-03-20>  
  *Yuxuan Zhu, Tengjun Jin, Yoojin Choi, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.20004v1)
- **Think and Answer ME: Benchmarking and Exploring Multi-Entity Reasoning Grounding in Remote Sensing** <2026-03-20>  
  *Shuchang Lyu, Haiquan Wen, Guangliang Cheng, Meng Li, Zheng Zhou, You Zhou, Dingding Yao, Zhenwei Shi*. [[Paper]](https://arxiv.org/abs/2603.12788v2)
- **ReLaX: Reasoning with Latent Exploration for Large Reasoning Models** <2026-03-20>  
  *Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, Jibin Wu*. [[Paper]](https://arxiv.org/abs/2512.07558v2)
- **VEPO: Variable Entropy Policy Optimization for Low-Resource Language Foundation Models** <2026-03-19>  
  *Chonghan Liu, Yimin Du, Qi An, Xin He, Cunqi Zhai, Fei Tan, Weijia Lin, Xiaochun Gong, Yongchao Deng, Shousheng Jia, Xiangzheng Zhang*. [[Paper]](https://arxiv.org/abs/2603.19152v1)
- **How Uncertainty Estimation Scales with Sampling in Reasoning Models** <2026-03-19>  
  *Maksym Del, Markus Kängsepp, Marharyta Domnich, Ardi Tampuu, Lisa Yankovskaya, Meelis Kull, Mark Fishel*. [[Paper]](https://arxiv.org/abs/2603.19118v1)
- **Context Bootstrapped Reinforcement Learning** <2026-03-19>  
  *Saaket Agashe, Jayanth Srinivasa, Gaowen Liu, Ramana Kompella, Xin Eric Wang*. [[Paper]](https://arxiv.org/abs/2603.18953v1)
- **HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning** <2026-03-19>  
  *Shenzhi Wang, Shixuan Liu, Jing Zhou, Chang Gao, Xiong-Hui Chen, Binghai Wang, An Yang, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin*. [[Paper]](https://arxiv.org/abs/2603.17024v2)
- **Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards** <2026-03-19>  
  *Haechan Kim, Soohyun Ryu, Gyouk Chu, Doohyuk Jang, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2603.18444v1)
- **ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning** <2026-03-18>  
  *Yu Li, Rui Miao, Zhengling Qi, Tian Lan*. [[Paper]](https://arxiv.org/abs/2603.16060v2)
- **Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards** <2026-03-18>  
  *Philipp Normann, Andreas Happe, Jürgen Cito, Daniel Arp*. [[Paper]](https://arxiv.org/abs/2603.17673v1)
- **Gym-V: A Unified Vision Environment System for Agentic Vision Research** <2026-03-17>  
  *Fanqing Meng, Lingxiao Du, Jiawei Gu, Jiaqi Liao, Linjie Li, Zijian Wu, Xiangyan Liu, Ziqi Zhao, Mengkang Hu, Yue Zhang, Zichen Liu, Jiaheng Zhang, Michael Qizhe Shieh*. [[Paper]](https://arxiv.org/abs/2603.15432v2)
- **Aletheia: What Makes RLVR For Code Verifiers Tick?** <2026-03-17>  
  *Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych*. [[Paper]](https://arxiv.org/abs/2601.12186v2)
- **Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning** <2026-03-17>  
  *Yuxuan Gu, Weimin Bai, Yifei Wang, Weijian Luo, He Sun*. [[Paper]](https://arxiv.org/abs/2511.15190v3)
- **Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism** <2026-03-17>  
  *Kaixuan Du, Meng Cao, Hang Zhang, Yukun Wang, Xiangzhou Huang, Ni Li*. [[Paper]](https://arxiv.org/abs/2603.16223v1)
- **Offline Exploration-Aware Fine-Tuning for Long-Chain Mathematical Reasoning** <2026-03-17>  
  *Yongyu Mu, Jiali Zeng, Fandong Meng, JingBo Zhu, Tong Xiao*. [[Paper]](https://arxiv.org/abs/2603.16206v1)
- **SAGE: Multi-Agent Self-Evolution for LLM Reasoning** <2026-03-17>  
  *Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Ying Tiffany He, F. Richard Yu*. [[Paper]](https://arxiv.org/abs/2603.15255v2)
- **Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing** <2026-03-17>  
  *Jiahe Song, Chuang Wang, Yinfan Wang, Hao Zheng, Rui Nie, Bowen Jiang, Xingjian Wei, Junyuan Gao, Yubin Wang, Bin Wang, Lijun Wu, Jiang Wu, Qian Yu, Conghui He*. [[Paper]](https://arxiv.org/abs/2603.15011v2)
- **Execution-Grounded Credit Assignment for GRPO in Code Generation** <2026-03-17>  
  *Abhijit Kumar, Natalya Kumar, Shikhar Gupta*. [[Paper]](https://arxiv.org/abs/2603.16158v1)
- **DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay** <2026-03-17>  
  *Long Li, Zhijian Zhou, Tianyi Wang, Weidi Xu, Zuming Huang, Wei Chu, Zhe Wang, Shirui Pan, Chao Qu, Yuan Qi*. [[Paper]](https://arxiv.org/abs/2603.16157v1)
- **Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards** <2026-03-17>  
  *Yuxuan Zhu, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.16140v1)
- **Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning** <2026-03-16>  
  *Aozhe Wang, Yuchen Yan, Nan Zhou, Zhengxi Lu, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen*. [[Paper]](https://arxiv.org/abs/2603.15611v1)
- **Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models** <2026-03-16>  
  *Samy Jelassi, Mujin Kwun, Rosie Zhao, Yuanzhi Li, Nicolo Fusi, Yilun Du, Sham M. Kakade, Carles Domingo-Enrich*. [[Paper]](https://arxiv.org/abs/2603.12248v2)
- **Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning** <2026-03-16>  
  *Xu Wan, Yansheng Wang, Wenqi Huang, Mingyang Sun*. [[Paper]](https://arxiv.org/abs/2602.20722v2)
- **Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling** <2026-03-16>  
  *Shuyang Jiang, Yusheng Liao, Ya Zhang, Yanfeng Wang, Yu Wang*. [[Paper]](https://arxiv.org/abs/2509.25827v2)
- **VisionCoach: Reinforcing Grounded Video Reasoning via Visual-Perception Prompting** <2026-03-15>  
  *Daeun Lee, Shoubin Yu, Yue Zhang, Mohit Bansal*. [[Paper]](https://arxiv.org/abs/2603.14659v1)
- **Nemotron-CrossThink: Scaling Self-Learning beyond Math Reasoning** <2026-03-15>  
  *Syeda Nahida Akter, Shrimai Prabhumoye, Matvei Novikov, Seungju Han, Ying Lin, Evelina Bakhturina, Eric Nyberg, Yejin Choi, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro*. [[Paper]](https://arxiv.org/abs/2504.13941v3)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning** <2026-03-15>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v4)
- **An Industrial-Scale Insurance LLM Achieving Verifiable Domain Mastery and Hallucination Control without Competence Trade-offs** <2026-03-15>  
  *Qian Zhu, Xinnan Guo, Jingjing Huo, Jun Li, Pan Liu, Wenyan Yang, Wanqing Xu, Xuan Lin*. [[Paper]](https://arxiv.org/abs/2603.14463v1)
- **ReViSQL: Achieving Human-Level Text-to-SQL** <2026-03-20>  
  *Yuxuan Zhu, Tengjun Jin, Yoojin Choi, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.20004v1)
- **Think and Answer ME: Benchmarking and Exploring Multi-Entity Reasoning Grounding in Remote Sensing** <2026-03-20>  
  *Shuchang Lyu, Haiquan Wen, Guangliang Cheng, Meng Li, Zheng Zhou, You Zhou, Dingding Yao, Zhenwei Shi*. [[Paper]](https://arxiv.org/abs/2603.12788v2)
- **ReLaX: Reasoning with Latent Exploration for Large Reasoning Models** <2026-03-20>  
  *Shimin Zhang, Xianwei Chen, Yufan Shen, Ziyuan Ye, Jibin Wu*. [[Paper]](https://arxiv.org/abs/2512.07558v2)
- **VEPO: Variable Entropy Policy Optimization for Low-Resource Language Foundation Models** <2026-03-19>  
  *Chonghan Liu, Yimin Du, Qi An, Xin He, Cunqi Zhai, Fei Tan, Weijia Lin, Xiaochun Gong, Yongchao Deng, Shousheng Jia, Xiangzheng Zhang*. [[Paper]](https://arxiv.org/abs/2603.19152v1)
- **How Uncertainty Estimation Scales with Sampling in Reasoning Models** <2026-03-19>  
  *Maksym Del, Markus Kängsepp, Marharyta Domnich, Ardi Tampuu, Lisa Yankovskaya, Meelis Kull, Mark Fishel*. [[Paper]](https://arxiv.org/abs/2603.19118v1)
- **Context Bootstrapped Reinforcement Learning** <2026-03-19>  
  *Saaket Agashe, Jayanth Srinivasa, Gaowen Liu, Ramana Kompella, Xin Eric Wang*. [[Paper]](https://arxiv.org/abs/2603.18953v1)
- **HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning** <2026-03-19>  
  *Shenzhi Wang, Shixuan Liu, Jing Zhou, Chang Gao, Xiong-Hui Chen, Binghai Wang, An Yang, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin*. [[Paper]](https://arxiv.org/abs/2603.17024v2)
- **Discounted Beta--Bernoulli Reward Estimation for Sample-Efficient Reinforcement Learning with Verifiable Rewards** <2026-03-19>  
  *Haechan Kim, Soohyun Ryu, Gyouk Chu, Doohyuk Jang, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2603.18444v1)
- **ARISE: Agent Reasoning with Intrinsic Skill Evolution in Hierarchical Reinforcement Learning** <2026-03-18>  
  *Yu Li, Rui Miao, Zhengling Qi, Tian Lan*. [[Paper]](https://arxiv.org/abs/2603.16060v2)
- **Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards** <2026-03-18>  
  *Philipp Normann, Andreas Happe, Jürgen Cito, Daniel Arp*. [[Paper]](https://arxiv.org/abs/2603.17673v1)
- **Gym-V: A Unified Vision Environment System for Agentic Vision Research** <2026-03-17>  
  *Fanqing Meng, Lingxiao Du, Jiawei Gu, Jiaqi Liao, Linjie Li, Zijian Wu, Xiangyan Liu, Ziqi Zhao, Mengkang Hu, Yue Zhang, Zichen Liu, Jiaheng Zhang, Michael Qizhe Shieh*. [[Paper]](https://arxiv.org/abs/2603.15432v2)
- **Aletheia: What Makes RLVR For Code Verifiers Tick?** <2026-03-17>  
  *Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych*. [[Paper]](https://arxiv.org/abs/2601.12186v2)
- **Masked Auto-Regressive Variational Acceleration: Fast Inference Makes Practical Reinforcement Learning** <2026-03-17>  
  *Yuxuan Gu, Weimin Bai, Yifei Wang, Weijian Luo, He Sun*. [[Paper]](https://arxiv.org/abs/2511.15190v3)
- **Dual Consensus: Escaping from Spurious Majority in Unsupervised RLVR via Two-Stage Vote Mechanism** <2026-03-17>  
  *Kaixuan Du, Meng Cao, Hang Zhang, Yukun Wang, Xiangzhou Huang, Ni Li*. [[Paper]](https://arxiv.org/abs/2603.16223v1)
- **Offline Exploration-Aware Fine-Tuning for Long-Chain Mathematical Reasoning** <2026-03-17>  
  *Yongyu Mu, Jiali Zeng, Fandong Meng, JingBo Zhu, Tong Xiao*. [[Paper]](https://arxiv.org/abs/2603.16206v1)
- **SAGE: Multi-Agent Self-Evolution for LLM Reasoning** <2026-03-17>  
  *Yulin Peng, Xinxin Zhu, Chenxing Wei, Nianbo Zeng, Leilei Wang, Ying Tiffany He, F. Richard Yu*. [[Paper]](https://arxiv.org/abs/2603.15255v2)
- **Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing** <2026-03-17>  
  *Jiahe Song, Chuang Wang, Yinfan Wang, Hao Zheng, Rui Nie, Bowen Jiang, Xingjian Wei, Junyuan Gao, Yubin Wang, Bin Wang, Lijun Wu, Jiang Wu, Qian Yu, Conghui He*. [[Paper]](https://arxiv.org/abs/2603.15011v2)
- **Execution-Grounded Credit Assignment for GRPO in Code Generation** <2026-03-17>  
  *Abhijit Kumar, Natalya Kumar, Shikhar Gupta*. [[Paper]](https://arxiv.org/abs/2603.16158v1)
- **DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay** <2026-03-17>  
  *Long Li, Zhijian Zhou, Tianyi Wang, Weidi Xu, Zuming Huang, Wei Chu, Zhe Wang, Shirui Pan, Chao Qu, Yuan Qi*. [[Paper]](https://arxiv.org/abs/2603.16157v1)
- **Noisy Data is Destructive to Reinforcement Learning with Verifiable Rewards** <2026-03-17>  
  *Yuxuan Zhu, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2603.16140v1)
- **Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning** <2026-03-16>  
  *Aozhe Wang, Yuchen Yan, Nan Zhou, Zhengxi Lu, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen*. [[Paper]](https://arxiv.org/abs/2603.15611v1)
- **Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models** <2026-03-16>  
  *Samy Jelassi, Mujin Kwun, Rosie Zhao, Yuanzhi Li, Nicolo Fusi, Yilun Du, Sham M. Kakade, Carles Domingo-Enrich*. [[Paper]](https://arxiv.org/abs/2603.12248v2)
- **Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning** <2026-03-16>  
  *Xu Wan, Yansheng Wang, Wenqi Huang, Mingyang Sun*. [[Paper]](https://arxiv.org/abs/2602.20722v2)
- **Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling** <2026-03-16>  
  *Shuyang Jiang, Yusheng Liao, Ya Zhang, Yanfeng Wang, Yu Wang*. [[Paper]](https://arxiv.org/abs/2509.25827v2)
- **VisionCoach: Reinforcing Grounded Video Reasoning via Visual-Perception Prompting** <2026-03-15>  
  *Daeun Lee, Shoubin Yu, Yue Zhang, Mohit Bansal*. [[Paper]](https://arxiv.org/abs/2603.14659v1)
- **Nemotron-CrossThink: Scaling Self-Learning beyond Math Reasoning** <2026-03-15>  
  *Syeda Nahida Akter, Shrimai Prabhumoye, Matvei Novikov, Seungju Han, Ying Lin, Evelina Bakhturina, Eric Nyberg, Yejin Choi, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro*. [[Paper]](https://arxiv.org/abs/2504.13941v3)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning** <2026-03-15>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v4)
- **An Industrial-Scale Insurance LLM Achieving Verifiable Domain Mastery and Hallucination Control without Competence Trade-offs** <2026-03-15>  
  *Qian Zhu, Xinnan Guo, Jingjing Huo, Jun Li, Pan Liu, Wenyan Yang, Wanqing Xu, Xuan Lin*. [[Paper]](https://arxiv.org/abs/2603.14463v1)
- **Co-rewarding: Stable Self-supervised RL for Eliciting Reasoning in Large Language Models** <2026-03-15>  
  *Zizhuo Zhang, Jianing Zhu, Xinmu Ge, Zihua Zhao, Zhanke Zhou, Xuan Li, Xiao Feng, Jiangchao Yao, Bo Han*. [[Paper]](https://arxiv.org/abs/2508.00410v3)
- **From $\boldsymbol{\logπ}$ to $\boldsymbolπ$: Taming Divergence in Soft Clipping via Bilateral Decoupled Decay of Probability Gradient Weight** <2026-03-15>  
  *Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Chaowen Hu, Cong Qin, Zekai Shao, Binbin Zheng, Lu Pan, Ke Zeng*. [[Paper]](https://arxiv.org/abs/2603.14389v1)
- **Eliciting Chain-of-Thought Reasoning for Time Series Analysis using Reinforcement Learning** <2026-03-14>  
  *Felix Parker, Nimeesha Chan, Chi Zhang, Kimia Ghobadi*. [[Paper]](https://arxiv.org/abs/2510.01116v2)
- **PuzzleCraft: Exploration-Aware Curriculum Learning for Puzzle-Based RLVR in VLMs** <2026-03-13>  
  *Ahmadreza Jeddi, Hakki Can Karaimer, Hue Nguyen, Zhongling Wang, Ke Zhao, Javad Rajabi, Ran Zhang, Raghav Goyal, Konstantinos G. Derpanis, Babak Taati, Radek Grzeszczuk*. [[Paper]](https://arxiv.org/abs/2512.14944v2)
- **Thinking in Streaming Video** <2026-03-13>  
  *Zikang Liu, Longteng Guo, Handong Li, Ru Zhen, Xingjian He, Ruyi Ji, Xiaoming Ren, Yanhao Zhang, Haonan Lu, Jing Liu*. [[Paper]](https://arxiv.org/abs/2603.12938v1)
- **SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models** <2026-03-13>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v4)
- **Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks** <2026-03-13>  
  *Kun Wang, Reinhard Heckel*. [[Paper]](https://arxiv.org/abs/2603.12875v1)
- **Rethinking Multiple-Choice Questions for RLVR: Unlocking Potential via Distractor Design** <2026-03-13>  
  *Xu Guo, Qiming Ge, Jian Tong, Kedi Chen, Jin Zhang, Xiaogui Yang, Xuan Gao, Haijun Lv, Zhihui Lu, Yicheng Zou, Qipeng Guo*. [[Paper]](https://arxiv.org/abs/2603.12826v1)
- **mAceReason-Math: A Dataset of High-Quality Multilingual Math Problems Ready For RLVR** <2026-03-13>  
  *Konstantin Dobler, Simon Lehnerer, Federico Scozzafava, Jonathan Janke, Mohamed Ali*. [[Paper]](https://arxiv.org/abs/2603.10767v2)
- **EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning** <2026-03-13>  
  *Chi Ruan, Dongfu Jiang, Huaye Zeng, Ping Nie, Wenhu Chen*. [[Paper]](https://arxiv.org/abs/2603.12698v1)
- **MedEyes: Learning Dynamic Visual Focus for Medical Progressive Diagnosis** <2026-03-12>  
  *Chunzheng Zhu, Yangfang Lin, Shen Chen, Yijun Wang, Jianxin Lin*. [[Paper]](https://arxiv.org/abs/2511.22018v2)
- **Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning** <2026-03-12>  
  *Zhuoxu Huang, Mengxi Jia, Hao Sun, Xuelong Li, Jungong Han*. [[Paper]](https://arxiv.org/abs/2602.20197v2)
- **Hindsight-Anchored Policy Optimization: Turning Failure into Feedback in Sparse Reward Settings** <2026-03-11>  
  *Yuning Wu, Ke Wang, Devin Chen, Kai Wei*. [[Paper]](https://arxiv.org/abs/2603.11321v1)
- **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images** <2026-03-11>  
  *Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak*. [[Paper]](https://arxiv.org/abs/2602.06965v2)
- **DeReason: A Difficulty-Aware Curriculum Improves Decoupled SFT-then-RL Training for General Reasoning** <2026-03-11>  
  *Hanxu Hu, Yuxuan Wang, Maggie Huan, Jannis Vamvas, Yinya Huang, Zhijiang Guo, Rico Sennrich*. [[Paper]](https://arxiv.org/abs/2603.11193v1)
- **$V_{0.5}$: Generalist Value Model as a Prior for Sparse RL Rollouts** <2026-03-11>  
  *Yi-Kai Zhang, Yueqing Sun, Hongyan Hao, Qi Gu, Xunliang Cai, De-Chuan Zhan, Han-Jia Ye*. [[Paper]](https://arxiv.org/abs/2603.10848v1)
- **Multilingual Reasoning Gym: Multilingual Scaling of Procedural Reasoning Environments** <2026-03-11>  
  *Konstantin Dobler, Simon Lehnerer, Federico Scozzafava, Jonathan Janke, Mohamed Ali*. [[Paper]](https://arxiv.org/abs/2603.10793v1)
- **To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models** <2026-03-11>  
  *Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang*. [[Paper]](https://arxiv.org/abs/2602.12566v3)
- **CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework** <2026-03-11>  
  *Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu*. [[Paper]](https://arxiv.org/abs/2603.01607v2)
- **Reinforcement Learning with Conditional Expectation Reward** <2026-03-11>  
  *Changyi Xiao, Caijun Xu, Yixin Cao*. [[Paper]](https://arxiv.org/abs/2603.10624v1)
- **Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning** <2026-03-11>  
  *Zhaowei Zhang, Xiaohan Liu, Xuekai Zhu, Junchao Huang, Ceyao Zhang, Zhiyuan Feng, Yaodong Yang, Xiaoyuan Yi, Xing Xie*. [[Paper]](https://arxiv.org/abs/2603.10588v1)
- **Tackling Length Inflation Without Trade-offs: Group Relative Reward Rescaling for Reinforcement Learning** <2026-03-11>  
  *Zichao Li, Jie Lou, Fangchen Dong, Zhiyuan Fan, Mengjie Ren, Hongyu Lin, Xianpei Han, Debing Zhang, Le Sun, Yaojie Lu, Xing Yu*. [[Paper]](https://arxiv.org/abs/2603.10535v1)
- **Thinking in Streaming Video** <2026-03-13>  
  *Zikang Liu, Longteng Guo, Handong Li, Ru Zhen, Xingjian He, Ruyi Ji, Xiaoming Ren, Yanhao Zhang, Haonan Lu, Jing Liu*. [[Paper]](https://arxiv.org/abs/2603.12938v1)
- **SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models** <2026-03-13>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v4)
- **Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks** <2026-03-13>  
  *Kun Wang, Reinhard Heckel*. [[Paper]](https://arxiv.org/abs/2603.12875v1)
- **Rethinking Multiple-Choice Questions for RLVR: Unlocking Potential via Distractor Design** <2026-03-13>  
  *Xu Guo, Qiming Ge, Jian Tong, Kedi Chen, Jin Zhang, Xiaogui Yang, Xuan Gao, Haijun Lv, Zhihui Lu, Yicheng Zou, Qipeng Guo*. [[Paper]](https://arxiv.org/abs/2603.12826v1)
- **mAceReason-Math: A Dataset of High-Quality Multilingual Math Problems Ready For RLVR** <2026-03-13>  
  *Konstantin Dobler, Simon Lehnerer, Federico Scozzafava, Jonathan Janke, Mohamed Ali*. [[Paper]](https://arxiv.org/abs/2603.10767v2)
- **Think and Answer ME: Benchmarking and Exploring Multi-Entity Reasoning Grounding in Remote Sensing** <2026-03-13>  
  *Shuchang Lyu, Haiquan Wen, Guangliang Cheng, Meng Li, Zheng Zhou, You Zhou, Dingding Yao, Zhenwei Shi*. [[Paper]](https://arxiv.org/abs/2603.12788v1)
- **EvolveCoder: Evolving Test Cases via Adversarial Verification for Code Reinforcement Learning** <2026-03-13>  
  *Chi Ruan, Dongfu Jiang, Huaye Zeng, Ping Nie, Wenhu Chen*. [[Paper]](https://arxiv.org/abs/2603.12698v1)
- **Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models** <2026-03-12>  
  *Samy Jelassi, Mujin Kwun, Rosie Zhao, Yuanzhi Li, Nicolo Fusi, Yilun Du, Sham M. Kakade, Carles Domingo-Enrich*. [[Paper]](https://arxiv.org/abs/2603.12248v1)
- **MedEyes: Learning Dynamic Visual Focus for Medical Progressive Diagnosis** <2026-03-12>  
  *Chunzheng Zhu, Yangfang Lin, Shen Chen, Yijun Wang, Jianxin Lin*. [[Paper]](https://arxiv.org/abs/2511.22018v2)
- **Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning** <2026-03-12>  
  *Zhuoxu Huang, Mengxi Jia, Hao Sun, Xuelong Li, Jungong Han*. [[Paper]](https://arxiv.org/abs/2602.20197v2)
- **Hindsight-Anchored Policy Optimization: Turning Failure into Feedback in Sparse Reward Settings** <2026-03-11>  
  *Yuning Wu, Ke Wang, Devin Chen, Kai Wei*. [[Paper]](https://arxiv.org/abs/2603.11321v1)
- **MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images** <2026-03-11>  
  *Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak*. [[Paper]](https://arxiv.org/abs/2602.06965v2)
- **DeReason: A Difficulty-Aware Curriculum Improves Decoupled SFT-then-RL Training for General Reasoning** <2026-03-11>  
  *Hanxu Hu, Yuxuan Wang, Maggie Huan, Jannis Vamvas, Yinya Huang, Zhijiang Guo, Rico Sennrich*. [[Paper]](https://arxiv.org/abs/2603.11193v1)
- **$V_{0.5}$: Generalist Value Model as a Prior for Sparse RL Rollouts** <2026-03-11>  
  *Yi-Kai Zhang, Yueqing Sun, Hongyan Hao, Qi Gu, Xunliang Cai, De-Chuan Zhan, Han-Jia Ye*. [[Paper]](https://arxiv.org/abs/2603.10848v1)
- **Multilingual Reasoning Gym: Multilingual Scaling of Procedural Reasoning Environments** <2026-03-11>  
  *Konstantin Dobler, Simon Lehnerer, Federico Scozzafava, Jonathan Janke, Mohamed Ali*. [[Paper]](https://arxiv.org/abs/2603.10793v1)
- **To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models** <2026-03-11>  
  *Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang*. [[Paper]](https://arxiv.org/abs/2602.12566v3)
- **CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework** <2026-03-11>  
  *Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu*. [[Paper]](https://arxiv.org/abs/2603.01607v2)
- **Reinforcement Learning with Conditional Expectation Reward** <2026-03-11>  
  *Changyi Xiao, Caijun Xu, Yixin Cao*. [[Paper]](https://arxiv.org/abs/2603.10624v1)
- **Does LLM Alignment Really Need Diversity? An Empirical Study of Adapting RLVR Methods for Moral Reasoning** <2026-03-11>  
  *Zhaowei Zhang, Xiaohan Liu, Xuekai Zhu, Junchao Huang, Ceyao Zhang, Zhiyuan Feng, Yaodong Yang, Xiaoyuan Yi, Xing Xie*. [[Paper]](https://arxiv.org/abs/2603.10588v1)
- **Tackling Length Inflation Without Trade-offs: Group Relative Reward Rescaling for Reinforcement Learning** <2026-03-11>  
  *Zichao Li, Jie Lou, Fangchen Dong, Zhiyuan Fan, Mengjie Ren, Hongyu Lin, Xianpei Han, Debing Zhang, Le Sun, Yaojie Lu, Xing Yu*. [[Paper]](https://arxiv.org/abs/2603.10535v1)
- **Graph-GRPO: Training Graph Flow Models with Reinforcement Learning** <2026-03-11>  
  *Baoheng Zhu, Deyu Bo, Delvin Ce Zhang, Xiao Wang*. [[Paper]](https://arxiv.org/abs/2603.10395v1)
- **CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR** <2026-03-10>  
  *Sijia Cui, Pengyu Cheng, Jiajun Song, Yongbo Gai, Guojun Zhang, Zhechao Yu, Jianhe Lin, Xiaoxi Jiang, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2603.10101v1)
- **Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning** <2026-03-10>  
  *Tiehua Mei, Minxuan Lv, Leiyu Pan, Zhenpeng Su, Hongru Hou, Hengrui Chen, Ao Xu, Deqing Yang*. [[Paper]](https://arxiv.org/abs/2603.09803v1)
- **Rewards as Labels: Revisiting RLVR from a Classification Perspective** <2026-03-10>  
  *Zepeng Zhai, Meilin Chen, Jiaxuan Zhao, Junlang Qian, Lei Shen, Yuan Lu*. [[Paper]](https://arxiv.org/abs/2602.05630v4)
- **Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards** <2026-03-10>  
  *Zhengzhao Ma, Xueru Wen, Boxi Cao, Yaojie Lu, Hongyu Lin, Jinglin Yang, Min He, Xianpei Han, Le Sun*. [[Paper]](https://arxiv.org/abs/2603.09117v1)
- **Bradley-Terry Policy Optimization for Generative Preference Modeling** <2026-03-09>  
  *Shengyu Feng, Yun He, Shuang Ma, Beibin Li, Yuanhao Xiong, Songlin Li, Karishma Mandyam, Julian Katz-Samuels, Shengjie Bi, Licheng Yu, Hejia Zhang, Karthik Abinav Sankararaman, Han Fang, Yiming Yang, Manaal Faruqui*. [[Paper]](https://arxiv.org/abs/2510.15242v3)
- **How Far Can Unsupervised RLVR Scale LLM Training?** <2026-03-09>  
  *Bingxiang He, Yuxin Zuo, Zeyuan Liu, Shangziqi Zhao, Zixuan Fu, Junlin Yang, Cheng Qian, Kaiyan Zhang, Yuchen Fan, Ganqu Cui, Xiusi Chen, Youbang Sun, Xingtai Lv, Xuekai Zhu, Li Sheng, Ran Li, Huan-ang Gao, Yuchen Zhang, Bowen Zhou, Zhiyuan Liu, Ning Ding*. [[Paper]](https://arxiv.org/abs/2603.08660v1)
- **Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills** <2026-03-09>  
  *Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi, Zifeng Wang, Luxi He, Yichen Wu, Ming Zhong, Peiyang Song, Qizheng Zhang, Heng Wang, Xueqiang Xu, Hanwen Xu, Pengrui Han, Dylan Zhang, Jiashuo Sun, Chaoqi Yang, Kun Qian, Tian Wang, Changran Hu, Manling Li, Quanzheng Li, Hao Peng, Sheng Wang, Jingbo Shang, Chao Zhang, Jiaxuan You, Liyuan Liu, Pan Lu, Yu Zhang, Heng Ji, Yejin Choi, Dawn Song, Jimeng Sun, Jiawei Han*. [[Paper]](https://arxiv.org/abs/2512.16301v3)
- **Thickening-to-Thinning: Reward Shaping via Human-Inspired Learning Dynamics for LLM Reasoning** <2026-03-09>  
  *Wenze Lin, Zhen Yang, Xitai Jiang, Pony Ma, Gao Huang*. [[Paper]](https://arxiv.org/abs/2602.04265v2)
- **A Simple "Motivation" Can Enhance Reinforcement Finetuning of Large Reasoning Models** <2026-03-09>  
  *Junjie Zhang, Guozheng Ma, Shunyu Liu, Haoyu Wang, Jiaxing Huang, Ting-En Lin, Fei Huang, Yongbin Li, Dacheng Tao*. [[Paper]](https://arxiv.org/abs/2506.18485v3)
- **SWE-Fuse: Empowering Software Agents via Issue-free Trajectory Learning and Entropy-aware RLVR Training** <2026-03-09>  
  *Xin-Cheng Wen, Binbin Chen, Haoxuan Lan, Hang Yu, Peng Di, Cuiyun Gao*. [[Paper]](https://arxiv.org/abs/2603.07927v1)
- **SynPlanResearch-R1: Encouraging Tool Exploration for Deep Research with Synthetic Plans** <2026-03-09>  
  *Hansi Zeng, Zoey Li, Yifan Gao, Chenwei Zhang, Xiaoman Pan, Tao Yang, Fengran Mo, Jiacheng Lin, Xian Li, Jingbo Shang*. [[Paper]](https://arxiv.org/abs/2603.07853v1)
- **$\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving** <2026-03-07>  
  *Pinzheng Wang, Shuli Xu, Juntao Li, Yu Luo, Dong Li, Jianye Hao, Min Zhang*. [[Paper]](https://arxiv.org/abs/2603.07197v1)
- **Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR** <2026-03-07>  
  *Muhammad Khalifa, Zohaib Khan, Omer Tafveez, Hao Peng, Lu Wang*. [[Paper]](https://arxiv.org/abs/2603.07084v1)
- **Chart-RL: Generalized Chart Comprehension via Reinforcement Learning with Verifiable Rewards** <2026-03-07>  
  *Xin Zhang, Xingyu Li, Rongguang Wang, Ruizhong Miao, Zheng Wang, Dan Roth, Chenyang Li*. [[Paper]](https://arxiv.org/abs/2603.06958v1)
- **From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty** <2026-03-06>  
  *Azza Jenane, Nassim Walha, Lukas Kuhn, Florian Buettner*. [[Paper]](https://arxiv.org/abs/2603.06317v1)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal** <2026-03-06>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v3)
- **IntelliAsk: Learning to Ask High-Quality Research Questions via RLVR** <2026-03-06>  
  *Karun Sharma, Vidushee Vats, Shengzhi Li, Yuxiang Wang, Zhongtian Sun, Prayag Tiwari*. [[Paper]](https://arxiv.org/abs/2602.15849v2)
- **RM-R1: Reward Modeling as Reasoning** <2026-03-06>  
  *Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, Hanghang Tong, Heng Ji*. [[Paper]](https://arxiv.org/abs/2505.02387v4)
- **Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning** <2026-03-06>  
  *Xuan Li, Zhanke Zhou, Zongze Li, Jiangchao Yao, Yu Rong, Lu Zhang, Bo Han*. [[Paper]](https://arxiv.org/abs/2603.05900v1)
- **When Rubrics Fail: Error Enumeration as Reward in Reference-Free RL Post-Training for Virtual Try-On** <2026-03-05>  
  *Wisdom Ikezogwo, Mehmet Saygin Seyfioglu, Ranjay Krishna, Karim Bouyarmane*. [[Paper]](https://arxiv.org/abs/2603.05659v1)
- **3D-RFT: Reinforcement Fine-Tuning for Video-based 3D Scene Understanding** <2026-03-05>  
  *Xiongkun Linghu, Jiangyong Huang, Baoxiong Jia, Siyuan Huang*. [[Paper]](https://arxiv.org/abs/2603.04976v1)
- **Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards** <2026-03-05>  
  *Hieu Trung Nguyen, Bao Nguyen, Wenao Ma, Yuzhi Zhao, Ruifeng She, Viet Anh Nguyen*. [[Paper]](https://arxiv.org/abs/2602.01601v3)
- **CoRPO: Adding a Correctness Bias to GRPO Improves Generalization** <2026-03-04>  
  *Anisha Garg, Claire Zhang, Nishit Neema, David Bick, Ganesh Venkatesh, Joel Hestness*. [[Paper]](https://arxiv.org/abs/2511.04439v3)
- **SPEED-RL: Faster Training of Reasoning Models via Online Curriculum Learning** <2026-03-04>  
  *Ruiqi Zhang, Daman Arora, Song Mei, Andrea Zanette*. [[Paper]](https://arxiv.org/abs/2506.09016v3)
- **Generalization of RLVR Using Causal Reasoning as a Testbed** <2026-03-04>  
  *Brian Lu, Hongyu Zhao, Shuo Sun, Hao Peng, Rui Ding, Hongyuan Mei*. [[Paper]](https://arxiv.org/abs/2512.20760v2)
- **BeamPERL: Parameter-Efficient RL with Verifiable Rewards Specializes Compact LLMs for Structured Beam Mechanics Reasoning** <2026-03-04>  
  *Tarjei Paule Hage, Markus J. Buehler*. [[Paper]](https://arxiv.org/abs/2603.04124v1)
- **SHE: Stepwise Hybrid Examination Reinforcement Learning Framework for E-commerce Search Relevance** <2026-03-04>  
  *Pengkun Jiao, Yiming Jin, Jianhui Yang, Chenhe Dong, Zerui Huang, Shaowei Yao, Xiaojiang Zhou, Dan Ou, Haihong Tang*. [[Paper]](https://arxiv.org/abs/2510.07972v2)
- **Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play** <2026-03-04>  
  *Qinsi Wang, Bo Liu, Tianyi Zhou, Jing Shi, Yueqian Lin, Yiran Chen, Hai Helen Li, Kun Wan, Wentian Zhao*. [[Paper]](https://arxiv.org/abs/2509.25541v2)
- **Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning** <2026-03-03>  
  *Anas Zafar, Leema Krishna Murali, Ashish Vashist*. [[Paper]](https://arxiv.org/abs/2603.03437v1)
- **From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty** <2026-03-06>  
  *Azza Jenane, Nassim Walha, Lukas Kuhn, Florian Buettner*. [[Paper]](https://arxiv.org/abs/2603.06317v1)
- **CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal** <2026-03-06>  
  *Yongxin Wang, Zhicheng Yang, Meng Cao, Mingfei Han, Haokun Lin, Yingying Zhu, Xiaojun Chang, Xiaodan Liang*. [[Paper]](https://arxiv.org/abs/2512.19554v3)
- **IntelliAsk: Learning to Ask High-Quality Research Questions via RLVR** <2026-03-06>  
  *Karun Sharma, Vidushee Vats, Shengzhi Li, Yuxiang Wang, Zhongtian Sun, Prayag Tiwari*. [[Paper]](https://arxiv.org/abs/2602.15849v2)
- **RM-R1: Reward Modeling as Reasoning** <2026-03-06>  
  *Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, Hanghang Tong, Heng Ji*. [[Paper]](https://arxiv.org/abs/2505.02387v4)
- **Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning** <2026-03-06>  
  *Xuan Li, Zhanke Zhou, Zongze Li, Jiangchao Yao, Yu Rong, Lu Zhang, Bo Han*. [[Paper]](https://arxiv.org/abs/2603.05900v1)
- **When Rubrics Fail: Error Enumeration as Reward in Reference-Free RL Post-Training for Virtual Try-On** <2026-03-05>  
  *Wisdom Ikezogwo, Mehmet Saygin Seyfioglu, Ranjay Krishna, Karim Bouyarmane*. [[Paper]](https://arxiv.org/abs/2603.05659v1)
- **3D-RFT: Reinforcement Fine-Tuning for Video-based 3D Scene Understanding** <2026-03-05>  
  *Xiongkun Linghu, Jiangyong Huang, Baoxiong Jia, Siyuan Huang*. [[Paper]](https://arxiv.org/abs/2603.04976v1)
- **Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards** <2026-03-05>  
  *Hieu Trung Nguyen, Bao Nguyen, Wenao Ma, Yuzhi Zhao, Ruifeng She, Viet Anh Nguyen*. [[Paper]](https://arxiv.org/abs/2602.01601v3)
- **CoRPO: Adding a Correctness Bias to GRPO Improves Generalization** <2026-03-04>  
  *Anisha Garg, Claire Zhang, Nishit Neema, David Bick, Ganesh Venkatesh, Joel Hestness*. [[Paper]](https://arxiv.org/abs/2511.04439v3)
- **SPEED-RL: Faster Training of Reasoning Models via Online Curriculum Learning** <2026-03-04>  
  *Ruiqi Zhang, Daman Arora, Song Mei, Andrea Zanette*. [[Paper]](https://arxiv.org/abs/2506.09016v3)
- **Generalization of RLVR Using Causal Reasoning as a Testbed** <2026-03-04>  
  *Brian Lu, Hongyu Zhao, Shuo Sun, Hao Peng, Rui Ding, Hongyuan Mei*. [[Paper]](https://arxiv.org/abs/2512.20760v2)
- **BeamPERL: Parameter-Efficient RL with Verifiable Rewards Specializes Compact LLMs for Structured Beam Mechanics Reasoning** <2026-03-04>  
  *Tarjei Paule Hage, Markus J. Buehler*. [[Paper]](https://arxiv.org/abs/2603.04124v1)
- **SHE: Stepwise Hybrid Examination Reinforcement Learning Framework for E-commerce Search Relevance** <2026-03-04>  
  *Pengkun Jiao, Yiming Jin, Jianhui Yang, Chenhe Dong, Zerui Huang, Shaowei Yao, Xiaojiang Zhou, Dan Ou, Haihong Tang*. [[Paper]](https://arxiv.org/abs/2510.07972v2)
- **Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play** <2026-03-04>  
  *Qinsi Wang, Bo Liu, Tianyi Zhou, Jing Shi, Yueqian Lin, Yiran Chen, Hai Helen Li, Kun Wan, Wentian Zhao*. [[Paper]](https://arxiv.org/abs/2509.25541v2)
- **Rewards as Labels: Revisiting RLVR from a Classification Perspective** <2026-03-04>  
  *Zepeng Zhai, Meilin Chen, Jiaxuan Zhao, Junlang Qian, Lei Shen, Yuan Lu*. [[Paper]](https://arxiv.org/abs/2602.05630v2)
- **Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning** <2026-03-03>  
  *Anas Zafar, Leema Krishna Murali, Ashish Vashist*. [[Paper]](https://arxiv.org/abs/2603.03437v1)
- **RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning** <2026-03-03>  
  *Yukun Chen, Jiaming Li, Longze Chen, Ze Gong, Jingpeng Li, Zhen Qin, Hengyu Chang, Ancheng Xu, Zhihao Yang, Hamid Alinejad-Rokny, Qiang Qu, Bo Zheng, Min Yang*. [[Paper]](https://arxiv.org/abs/2602.21628v2)
- **The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward** <2026-03-03>  
  *Long Li, Zhijian Zhou, Jiaran Hao, Jason Klein Liu, Yanting Miao, Wei Pang, Xiaoyu Tan, Wei Chu, Zhe Wang, Shirui Pan, Chao Qu, Yuan Qi*. [[Paper]](https://arxiv.org/abs/2509.07430v4)
- **Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward** <2026-03-03>  
  *Tong Xiao, Xin Xu, Zhenya Huang, Hongyu Gao, Quan Liu, Qi Liu, Enhong Chen*. [[Paper]](https://arxiv.org/abs/2506.07218v3)
- **CORE: Concept-Oriented Reinforcement for Bridging the Definition-Application Gap in Mathematical Reasoning** <2026-03-02>  
  *Zijun Gao, Zhikun Xu, Xiao Ye, Ben Zhou*. [[Paper]](https://arxiv.org/abs/2512.18857v2)
- **Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training** <2026-03-02>  
  *Valentin Lacombe, Valentin Quesnel, Damien Sileo*. [[Paper]](https://arxiv.org/abs/2603.02208v1)
- **LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards** <2026-03-02>  
  *Guanzheng Chen, Michael Qizhe Shieh, Lidong Bing*. [[Paper]](https://arxiv.org/abs/2603.02146v1)
- **Efficient RLVR Training via Weighted Mutual Information Data Selection** <2026-03-02>  
  *Xinyu Zhou, Boyu Zhu, Haotian Zhang, Huiming Wang, Zhijiang Guo*. [[Paper]](https://arxiv.org/abs/2603.01907v1)
- **SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning** <2026-03-02>  
  *Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques*. [[Paper]](https://arxiv.org/abs/2506.24119v3)
- **Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm** <2026-03-02>  
  *Tianxiang Xu, Jiayi Liu, Yixuan Tong, Jialu Xu, Yunqing Wei, Kaiwen Feng, PanPan Hou, Kangping Yin, Jiyuan Hu, Hao Zhou, Zhenxin Ma, Jian Xu, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2602.11661v2)
- **Spotlight on Token Perception for Multimodal Reinforcement Learning** <2026-03-02>  
  *Siyuan Huang, Xiaoye Qu, Yafu Li, Yun Luo, Zefeng He, Daizong Liu, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2510.09285v2)
- **CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework** <2026-03-02>  
  *Yuexi Du, Jinglu Wang, Shujie Liu, Nicha C. Dvornek, Yan Lu*. [[Paper]](https://arxiv.org/abs/2603.01607v1)
- **Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models** <2026-03-02>  
  *Qiyuan Zhang, Yufei Wang, Tianhe Wu, Can Xu, Qingfeng Sun, Kai Zheng, Xue Liu, Chen Ma*. [[Paper]](https://arxiv.org/abs/2603.01571v1)
- **LFPO: Likelihood-Free Policy Optimization for Masked Diffusion Models** <2026-03-02>  
  *Chenxing Wei, Jiazhen Kang, Hong Wang, Jianqing Zhang, Hao Jiang, Xiaolong Xu, Ningyuan Sun, Ying He, F. Richard Yu, Yao Shu, Bo Jiang*. [[Paper]](https://arxiv.org/abs/2603.01563v1)
- **Document Reconstruction Unlocks Scalable Long-Context RLVR** <2026-03-02>  
  *Yao Xiao, Lei Wang, Yue Deng, Guanzheng Chen, Ziqi Jin, Jung-jae Kim, Xiaoli Li, Roy Ka-wei Lee, Lidong Bing*. [[Paper]](https://arxiv.org/abs/2602.08237v4)
- **Breaking Barriers: Do Reinforcement Post Training Gains Transfer To Unseen Domains?** <2026-03-02>  
  *Chuxuan Hu, Yuxuan Zhu, Antony Kellermann, Caleb Biddulph, Suppakit Waiwitlikhit, Jason Benn, Daniel Kang*. [[Paper]](https://arxiv.org/abs/2506.19733v3)
- **AnesSuite: A Comprehensive Benchmark and Dataset Suite for Anesthesiology Reasoning in LLMs** <2026-03-02>  
  *Xiang Feng, Wentao Jiang, Zengmao Wang, Yong Luo, Pingbo Xu, Baosheng Yu, Hua Jin, Jing Zhang*. [[Paper]](https://arxiv.org/abs/2504.02404v4)
- **Learning to Reason without External Rewards** <2026-03-02>  
  *Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song*. [[Paper]](https://arxiv.org/abs/2505.19590v3)
- **Diversity-Enhanced Reasoning for Subjective Questions** <2026-03-01>  
  *Yumeng Wang, Zhiyuan Fan, Jiayu Liu, Jen-tse Huang, Yi R. Fung*. [[Paper]](https://arxiv.org/abs/2507.20187v4)
- **Towards Policy-Adaptive Image Guardrail: Benchmark and Method** <2026-03-01>  
  *Caiyong Piao, Zhiyuan Yan, Haoming Xu, Yunzhen Zhao, Kaiqing Lin, Feiyang Xu, Shuigeng Zhou*. [[Paper]](https://arxiv.org/abs/2603.01228v1)
- **ExGRPO: Learning to Reason from Experience** <2026-02-28>  
  *Runzhe Zhan, Yafu Li, Zhi Wang, Xiaoye Qu, Dongrui Liu, Jing Shao, Derek F. Wong, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2510.02245v2)
- **Learning to Explore with Parameter-Space Noise: A Deep Dive into Parameter-Space Noise for Reinforcement Learning with Verifiable Rewards** <2026-02-28>  
  *Bizhe Bai, Xinyue Wang, Peng Ye, Tao Chen*. [[Paper]](https://arxiv.org/abs/2602.02555v3)
- **Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning** <2026-02-28>  
  *Xichen Zhang, Sitong Wu, Yinghao Zhu, Haoru Tan, Shaozuo Yu, Ziyi He, Jiaya Jia*. [[Paper]](https://arxiv.org/abs/2510.19807v2)
- **Quantile Advantage Estimation: Stabilizing RLVR for LLM Reasoning** <2026-02-28>  
  *Junkang Wu, Kexin Huang, Jiancan Wu, An Zhang, Xiang Wang, Xiangnan He*. [[Paper]](https://arxiv.org/abs/2509.22611v2)
- **Lookahead Tree-Based Rollouts for Enhanced Trajectory-Level Exploration in Reinforcement Learning with Verifiable Rewards** <2026-02-28>  
  *Shangyu Xing, Siyuan Wang, Chenyuan Yang, Xinyu Dai, Xiang Ren*. [[Paper]](https://arxiv.org/abs/2510.24302v3)
- **Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment** <2026-02-28>  
  *Aleksander Boruch-Gruszecki, Yangtian Zi, Zixuan Wu, Tejas Oberoi, Carolyn Jane Anderson, Joydeep Biswas, Arjun Guha*. [[Paper]](https://arxiv.org/abs/2508.04865v2)
- **Recycling Failures: Salvaging Exploration in RLVR via Fine-Grained Off-Policy Guidance** <2026-02-27>  
  *Yanwei Ren, Haotian Zhang, Likang Xiao, Xikai Zhang, Jiaxing Huang, Jiayan Qiu, Baosheng Yu, Quan Chen, Liu Liu*. [[Paper]](https://arxiv.org/abs/2602.24110v1)
- **Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning** <2026-02-27>  
  *Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren*. [[Paper]](https://arxiv.org/abs/2509.26578v2)
- **Empowering Small VLMs to Think with Dynamic Memorization and Exploration** <2026-02-27>  
  *Jiazhen Liu, Yuchuan Deng, Long Chen*. [[Paper]](https://arxiv.org/abs/2506.23061v2)
- **FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning** <2026-02-27>  
  *Yuyang Ding, Chi Zhang, Juntao Li, Haibin Lin, Min Zhang*. [[Paper]](https://arxiv.org/abs/2510.22543v2)
- **Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning** <2026-02-27>  
  *Yihe Deng, I-Hung Hsu, Jun Yan, Zifeng Wang, Rujun Han, Gufeng Zhang, Yanfei Chen, Wei Wang, Tomas Pfister, Chen-Yu Lee*. [[Paper]](https://arxiv.org/abs/2510.25992v3)
- **Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning** <2026-02-26>  
  *Qiannian Zhao, Chen Yang, Jinhao Jing, Yunke Zhang, Xuhui Ren, Lu Yu, Shijie Zhang, Hongzhi Yin*. [[Paper]](https://arxiv.org/abs/2602.22751v1)
- **Replacing Multi-Step Assembly of Data Preparation Pipelines with One-Step LLM Pipeline Generation for Table QA** <2026-02-26>  
  *Fengyu Li, Junhao Zhu, Kaishi Song, Lu Chen, Zhongming Yao, Tianyi Li, Christian S. Jensen*. [[Paper]](https://arxiv.org/abs/2602.22721v1)
- **Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization** <2026-02-26>  
  *Jinghan Li, Junfeng Fang, Jinda Lu, Yuan Wang, Xiaoyan Guo, Tianyu Zhang, Xiang Wang, Xiangnan He*. [[Paper]](https://arxiv.org/abs/2602.21743v2)
- **ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL** <2026-02-26>  
  *Xingyu Lu, Jinpeng Wang, YiFan Zhang, Shijie Ma, Xiao Hu, Tianke Zhang, Haonan fan, Kaiyu Jiang, Changyi Liu, Kaiyu Tang, Bin Wen, Fan Yang, Tingting Gao, Han Li, Chun Yuan*. [[Paper]](https://arxiv.org/abs/2602.22623v1)
- **Recycling Failures: Salvaging Exploration in RLVR via Fine-Grained Off-Policy Guidance** <2026-02-27>  
  *Yanwei Ren, Haotian Zhang, Likang Xiao, Xikai Zhang, Jiaxing Huang, Jiayan Qiu, Baosheng Yu, Quan Chen, Liu Liu*. [[Paper]](https://arxiv.org/abs/2602.24110v1)
- **Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning** <2026-02-27>  
  *Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, Kan Ren*. [[Paper]](https://arxiv.org/abs/2509.26578v2)
- **Empowering Small VLMs to Think with Dynamic Memorization and Exploration** <2026-02-27>  
  *Jiazhen Liu, Yuchuan Deng, Long Chen*. [[Paper]](https://arxiv.org/abs/2506.23061v2)
- **FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning** <2026-02-27>  
  *Yuyang Ding, Chi Zhang, Juntao Li, Haibin Lin, Min Zhang*. [[Paper]](https://arxiv.org/abs/2510.22543v2)
- **Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning** <2026-02-27>  
  *Yihe Deng, I-Hung Hsu, Jun Yan, Zifeng Wang, Rujun Han, Gufeng Zhang, Yanfei Chen, Wei Wang, Tomas Pfister, Chen-Yu Lee*. [[Paper]](https://arxiv.org/abs/2510.25992v3)
- **Document Reconstruction Unlocks Scalable Long-Context RLVR** <2026-02-26>  
  *Yao Xiao, Lei Wang, Yue Deng, Guanzheng Chen, Ziqi Jin, Jung-jae Kim, Xiaoli Li, Roy Ka-wei Lee, Lidong Bing*. [[Paper]](https://arxiv.org/abs/2602.08237v3)
- **Know What You Know: Metacognitive Entropy Calibration for Verifiable RL Reasoning** <2026-02-26>  
  *Qiannian Zhao, Chen Yang, Jinhao Jing, Yunke Zhang, Xuhui Ren, Lu Yu, Shijie Zhang, Hongzhi Yin*. [[Paper]](https://arxiv.org/abs/2602.22751v1)
- **Replacing Multi-Step Assembly of Data Preparation Pipelines with One-Step LLM Pipeline Generation for Table QA** <2026-02-26>  
  *Fengyu Li, Junhao Zhu, Kaishi Song, Lu Chen, Zhongming Yao, Tianyi Li, Christian S. Jensen*. [[Paper]](https://arxiv.org/abs/2602.22721v1)
- **Enhancing Multi-Modal LLMs Reasoning via Difficulty-Aware Group Normalization** <2026-02-26>  
  *Jinghan Li, Junfeng Fang, Jinda Lu, Yuan Wang, Xiaoyan Guo, Tianyu Zhang, Xiang Wang, Xiangnan He*. [[Paper]](https://arxiv.org/abs/2602.21743v2)
- **ContextRL: Enhancing MLLM's Knowledge Discovery Efficiency with Context-Augmented RL** <2026-02-26>  
  *Xingyu Lu, Jinpeng Wang, YiFan Zhang, Shijie Ma, Xiao Hu, Tianke Zhang, Haonan fan, Kaiyu Jiang, Changyi Liu, Kaiyu Tang, Bin Wen, Fan Yang, Tingting Gao, Han Li, Chun Yuan*. [[Paper]](https://arxiv.org/abs/2602.22623v1)
- **Improving Parametric Knowledge Access in Reasoning Language Models** <2026-02-25>  
  *Melody Ma, John Hewitt*. [[Paper]](https://arxiv.org/abs/2602.22193v1)
- **GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL** <2026-02-25>  
  *Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang, Hao Cheng, Huaxiu Yao, Baoling Peng, Huan Zhang, Jianfeng Gao, Tong Zhang*. [[Paper]](https://arxiv.org/abs/2602.22190v1)
- **UpSkill: Mutual Information Skill Learning for Structured Response Diversity in LLMs** <2026-02-25>  
  *Devan Shah, Owen Yang, Daniel Yang, Chongyi Zheng, Benjamin Eysenbach*. [[Paper]](https://arxiv.org/abs/2602.22296v1)
- **Depth-Breadth Synergy in RLVR: Unlocking LLM Reasoning Gains with Adaptive Exploration** <2026-02-25>  
  *Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Dongchun Xie, Hanhui Li, Yiwei Wang, Xiaodan Liang, Jing Tang*. [[Paper]](https://arxiv.org/abs/2508.13755v6)
- **SERL: Self-Examining Reinforcement Learning on Open-Domain** <2026-02-25>  
  *Weixuan Ou, Yanzhao Zheng, Shuoshuo Sun, Wei Zhang, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu, Pengwei Yan, Yifan Qiao*. [[Paper]](https://arxiv.org/abs/2511.07922v3)
- **RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning** <2026-02-25>  
  *Yukun Chen, Jiaming Li, Longze Chen, Ze Gong, Jingpeng Li, Zhen Qin, Hengyu Chang, Ancheng Xu, Zhihao Yang, Hamid Alinejad-Rokny, Qiang Qu, Bo Zheng, Min Yang*. [[Paper]](https://arxiv.org/abs/2602.21628v1)
- **Spurious Rewards: Rethinking Training Signals in RLVR** <2026-02-25>  
  *Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Yiping Wang, Sewoong Oh, Simon Shaolei Du, Nathan Lambert, Sewon Min, Ranjay Krishna, Yulia Tsvetkov, Hannaneh Hajishirzi, Pang Wei Koh, Luke Zettlemoyer*. [[Paper]](https://arxiv.org/abs/2506.10947v2)
- **Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning** <2026-02-24>  
  *Yuanda Xu, Hejian Sang, Zhengze Zhou, Ran He, Zhipeng Wang*. [[Paper]](https://arxiv.org/abs/2602.21420v1)
- **EARL: Entropy-Aware RL Alignment of LLMs for Reliable RTL Code Generation** <2026-02-24>  
  *Jiahe Shi, Zhengqi Gao, Ching-Yun Ko, Duane Boning*. [[Paper]](https://arxiv.org/abs/2511.12033v2)
- **Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs** <2026-02-24>  
  *Sagnik Mukherjee, Lifan Yuan, Pavan Jayasinha, Dilek Hakkani-Tür, Hao Peng*. [[Paper]](https://arxiv.org/abs/2602.07729v2)
- **Buffer Matters: Unleashing the Power of Off-Policy Reinforcement Learning in Large Language Model Reasoning** <2026-02-24>  
  *Xu Wan, Yansheng Wang, Wenqi Huang, Mingyang Sun*. [[Paper]](https://arxiv.org/abs/2602.20722v1)
- **MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning** <2026-02-24>  
  *Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.17550v2)
- **ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models** <2026-02-23>  
  *Andre He, Nathaniel Weir, Kaj Bostrom, Allen Nie, Darion Cassel, Sam Bayless, Huzefa Rangwala*. [[Paper]](https://arxiv.org/abs/2602.20117v1)
- **EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization** <2026-02-23>  
  *Kevin Han, Yuhang Zhou, Mingze Gao, Gedi Zhou, Serena Li, Abhishek Kumar, Xiangjun Fan, Weiwei Li, Lizhu Zhang*. [[Paper]](https://arxiv.org/abs/2602.05165v3)
- **Think2SQL: Reinforce LLM Reasoning Capabilities for Text2SQL** <2026-02-23>  
  *Simone Papicchio, Simone Rossi, Luca Cagliero, Paolo Papotti*. [[Paper]](https://arxiv.org/abs/2504.15077v4)
- **DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning** <2026-02-23>  
  *Zhongwei Wan, Yun Shen, Zhihao Dou, Donghao Zhou, Yu Zhang, Xin Wang, Hui Shen, Jing Xiong, Chaofan Tao, Zixuan Zhong, Peizhou Huang, Mi Zhang*. [[Paper]](https://arxiv.org/abs/2602.19895v1)
- **QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation** <2026-02-23>  
  *Yaoyu Zhu, Di Huang, Hanqi Lyu, Xiaoyun Zhang, Chongxiao Li, Wenxuan Shi, Yutong Wu, Jianan Mu, Jinghua Wang, Yang Zhao, Pengwei Jin, Shuyao Cheng, Shengwen Liang, Xishan Zhang, Rui Zhang, Zidong Du, Qi Guo, Xing Hu, Yunji Chen*. [[Paper]](https://arxiv.org/abs/2505.24183v5)
- **Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models** <2026-02-23>  
  *Cheonbok Park, Jeonghoon Kim, Joosung Lee, Sanghwan Bae, Jaegul Choo, Kang Min Yoo*. [[Paper]](https://arxiv.org/abs/2506.05850v3)
- **SenTSR-Bench: Thinking with Injected Knowledge for Time-Series Reasoning** <2026-02-23>  
  *Zelin He, Boran Han, Xiyuan Zhang, Shuai Zhang, Haotian Lin, Qi Zhu, Haoyang Fang, Danielle C. Maddix, Abdul Fatir Ansari, Akash Chandrayan, Abhinav Pradhan, Bernie Wang, Matthew Reimherr*. [[Paper]](https://arxiv.org/abs/2602.19455v1)
- **How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization** <2026-02-22>  
  *Yangyi Fang, Jiaye Lin, Xiaoliang Fu, Cong Qin, Haolin Shi, Chaowen Hu, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.19208v1)
- **Adaptive Problem Generation via Symbolic Representations** <2026-02-22>  
  *Teresa Yeo, Myeongho Jeon, Dulaj Weerakoon, Rui Qiao, Alok Prakash, Armando Solar-Lezama, Archan Misra*. [[Paper]](https://arxiv.org/abs/2602.19187v1)
- **Generative Reasoning Re-ranker** <2026-02-22>  
  *Mingfu Liang, Yufei Li, Jay Xu, Kavosh Asadi, Xi Liu, Shuo Gu, Kaushik Rangadurai, Frank Shyu, Shuaiwen Wang, Song Yang, Zhijing Li, Jiang Liu, Mengying Sun, Fei Tian, Xiaohan Wei, Chonglin Sun, Jacob Tao, Shike Mei, Wenlin Chen, Santanu Kolay, Sandeep Pandey, Hamed Firooz, Luke Simon*. [[Paper]](https://arxiv.org/abs/2602.07774v4)
- **Controllable Exploration in Hybrid-Policy RLVR for Multi-Modal Reasoning** <2026-02-22>  
  *Zhuoxu Huang, Mengxi Jia, Hao Sun, Xuelong Li, Jungong Han*. [[Paper]](https://arxiv.org/abs/2602.20197v1)
- **Diversity-Incentivized Exploration for Versatile Reasoning** <2026-02-21>  
  *Zican Hu, Shilin Zhang, Yafu Li, Jianhao Yan, Xuyang Hu, Leyang Cui, Xiaoye Qu, Chunlin Chen, Yu Cheng, Zhi Wang*. [[Paper]](https://arxiv.org/abs/2509.26209v2)
- **CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use** <2026-02-20>  
  *Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang*. [[Paper]](https://arxiv.org/abs/2602.12268v2)
- **Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards** <2026-02-20>  
  *Johannes Ackermann, Michael Noukhovitch, Takashi Ishida, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2602.18037v1)
- **RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward** <2026-02-19>  
  *Qiucheng Wu, Jing Shi, Simon Jenni, Kushal Kafle, Tianyu Wang, Shiyu Chang, Handong Zhao*. [[Paper]](https://arxiv.org/abs/2602.17558v1)
- **Efficient Reinforcement Learning for Large Language Models with Intrinsic Exploration** <2026-02-19>  
  *Yan Sun, Jia Guo, Stanley Kok, Zihao Wang, Zujie Wen, Zhiqiang Zhang*. [[Paper]](https://arxiv.org/abs/2511.00794v3)
- **Proof-RM: A Scalable and Generalizable Reward Model for Math Proof** <2026-02-19>  
  *Haotong Yang, Zitong Wang, Shijia Kang, Siqi Yang, Wenkai Yu, Xu Niu, Yike Sun, Yi Hu, Zhouchen Lin, Muhan Zhang*. [[Paper]](https://arxiv.org/abs/2602.02377v2)
- **CaveAgent: Transforming LLMs into Stateful Runtime Operators** <2026-02-19>  
  *Maohao Ran, Zhenglin Wan, Cooper Lin, Yanting Zhang, Hongyu Xin, Hongwei Fan, Yibo Xu, Beier Luo, Yaxin Zhou, Wangbo Zhao, Lijie Yang, Lang Feng, Fuchao Yang, Jingxuan Wu, Yiqiao Huang, Chendong Ma, Dailing Jiang, Jianbo Deng, Sirui Han, Yang You, Bo An, Yike Guo, Jun Song*. [[Paper]](https://arxiv.org/abs/2601.01569v3)
- **References Improve LLM Alignment in Non-Verifiable Domains** <2026-02-18>  
  *Kejian Shi, Yixin Liu, Peifeng Wang, Alexander R. Fabbri, Shafiq Joty, Arman Cohan*. [[Paper]](https://arxiv.org/abs/2602.16802v1)
- **Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards** <2026-02-18>  
  *Guanning Zeng, Zhaoyi Zhou, Daman Arora, Andrea Zanette*. [[Paper]](https://arxiv.org/abs/2511.03710v2)
- **SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models** <2026-02-18>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v3)
- **DeepVision-103K: A Visually Diverse, Broad-Coverage, and Verifiable Mathematical Dataset for Multimodal Reasoning** <2026-02-18>  
  *Haoxiang Sun, Lizhen Xu, Bing Zhao, Wotao Yin, Wei Wang, Boyu Yang, Rui Wang, Hu Wei*. [[Paper]](https://arxiv.org/abs/2602.16742v1)
- **Synthesizing High-Quality Visual Question Answering from Medical Documents with Generator-Verifier LMMs** <2026-02-18>  
  *Xiaoke Huang, Ningsen Wang, Hui Liu, Xianfeng Tang, Yuyin Zhou*. [[Paper]](https://arxiv.org/abs/2510.25867v2)
- **MedVLThinker: Simple Baselines for Multimodal Medical Reasoning** <2026-02-18>  
  *Xiaoke Huang, Juncheng Wu, Hui Liu, Xianfeng Tang, Yuyin Zhou*. [[Paper]](https://arxiv.org/abs/2508.02669v3)
- **Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation** <2026-02-18>  
  *Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu*. [[Paper]](https://arxiv.org/abs/2509.15194v3)
- **The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes** <2026-02-17>  
  *Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy*. [[Paper]](https://arxiv.org/abs/2602.15515v1)
- **Generalized Parallel Scaling with Interdependent Generations** <2026-02-16>  
  *Harry Dong, David Brandfonbrener, Eryk Helenowski, Yun He, Mrinal Kumar, Han Fang, Yuejie Chi, Karthik Abinav Sankararaman*. [[Paper]](https://arxiv.org/abs/2510.01143v3)
- **Reward Modeling from Natural Language Human Feedback** <2026-02-16>  
  *Zongqi Wang, Rui Wang, Yuchuan Wu, Yiyao Yu, Pinyi Zhang, Shaoning Sun, Yujiu Yang, Yongbin Li*. [[Paper]](https://arxiv.org/abs/2601.07349v2)
- **Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards** <2026-02-20>  
  *Johannes Ackermann, Michael Noukhovitch, Takashi Ishida, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2602.18037v1)
- **RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward** <2026-02-19>  
  *Qiucheng Wu, Jing Shi, Simon Jenni, Kushal Kafle, Tianyu Wang, Shiyu Chang, Handong Zhao*. [[Paper]](https://arxiv.org/abs/2602.17558v1)
- **MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning** <2026-02-19>  
  *Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Binbin Zheng, Chaowen Hu, Zekai Shao, Cong Qin, Lu Pan, Ke Zeng, Xunliang Cai*. [[Paper]](https://arxiv.org/abs/2602.17550v1)
- **Efficient Reinforcement Learning for Large Language Models with Intrinsic Exploration** <2026-02-19>  
  *Yan Sun, Jia Guo, Stanley Kok, Zihao Wang, Zujie Wen, Zhiqiang Zhang*. [[Paper]](https://arxiv.org/abs/2511.00794v3)
- **Proof-RM: A Scalable and Generalizable Reward Model for Math Proof** <2026-02-19>  
  *Haotong Yang, Zitong Wang, Shijia Kang, Siqi Yang, Wenkai Yu, Xu Niu, Yike Sun, Yi Hu, Zhouchen Lin, Muhan Zhang*. [[Paper]](https://arxiv.org/abs/2602.02377v2)
- **CaveAgent: Transforming LLMs into Stateful Runtime Operators** <2026-02-19>  
  *Maohao Ran, Zhenglin Wan, Cooper Lin, Yanting Zhang, Hongyu Xin, Hongwei Fan, Yibo Xu, Beier Luo, Yaxin Zhou, Wangbo Zhao, Lijie Yang, Lang Feng, Fuchao Yang, Jingxuan Wu, Yiqiao Huang, Chendong Ma, Dailing Jiang, Jianbo Deng, Sirui Han, Yang You, Bo An, Yike Guo, Jun Song*. [[Paper]](https://arxiv.org/abs/2601.01569v3)
- **References Improve LLM Alignment in Non-Verifiable Domains** <2026-02-18>  
  *Kejian Shi, Yixin Liu, Peifeng Wang, Alexander R. Fabbri, Shafiq Joty, Arman Cohan*. [[Paper]](https://arxiv.org/abs/2602.16802v1)
- **Shrinking the Variance: Shrinkage Baselines for Reinforcement Learning with Verifiable Rewards** <2026-02-18>  
  *Guanning Zeng, Zhaoyi Zhou, Daman Arora, Andrea Zanette*. [[Paper]](https://arxiv.org/abs/2511.03710v2)
- **SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models** <2026-02-18>  
  *Ziyi Yang, Weizhou Shen, Chenliang Li, Ruijun Chen, Fanqi Wan, Ming Yan, Xiaojun Quan, Fei Huang*. [[Paper]](https://arxiv.org/abs/2509.23863v3)
- **DeepVision-103K: A Visually Diverse, Broad-Coverage, and Verifiable Mathematical Dataset for Multimodal Reasoning** <2026-02-18>  
  *Haoxiang Sun, Lizhen Xu, Bing Zhao, Wotao Yin, Wei Wang, Boyu Yang, Rui Wang, Hu Wei*. [[Paper]](https://arxiv.org/abs/2602.16742v1)
- **Synthesizing High-Quality Visual Question Answering from Medical Documents with Generator-Verifier LMMs** <2026-02-18>  
  *Xiaoke Huang, Ningsen Wang, Hui Liu, Xianfeng Tang, Yuyin Zhou*. [[Paper]](https://arxiv.org/abs/2510.25867v2)
- **MedVLThinker: Simple Baselines for Multimodal Medical Reasoning** <2026-02-18>  
  *Xiaoke Huang, Juncheng Wu, Hui Liu, Xianfeng Tang, Yuyin Zhou*. [[Paper]](https://arxiv.org/abs/2508.02669v3)
- **Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation** <2026-02-18>  
  *Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu*. [[Paper]](https://arxiv.org/abs/2509.15194v3)
- **The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes** <2026-02-17>  
  *Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy*. [[Paper]](https://arxiv.org/abs/2602.15515v1)
- **Generalized Parallel Scaling with Interdependent Generations** <2026-02-16>  
  *Harry Dong, David Brandfonbrener, Eryk Helenowski, Yun He, Mrinal Kumar, Han Fang, Yuejie Chi, Karthik Abinav Sankararaman*. [[Paper]](https://arxiv.org/abs/2510.01143v3)
- **Reward Modeling from Natural Language Human Feedback** <2026-02-16>  
  *Zongqi Wang, Rui Wang, Yuchuan Wu, Yiyao Yu, Pinyi Zhang, Shaoning Sun, Yujiu Yang, Yongbin Li*. [[Paper]](https://arxiv.org/abs/2601.07349v2)
- **On the Learning Dynamics of RLVR at the Edge of Competence** <2026-02-16>  
  *Yu Huang, Zixin Wen, Yuejie Chi, Yuting Wei, Aarti Singh, Yingbin Liang, Yuxin Chen*. [[Paper]](https://arxiv.org/abs/2602.14872v1)
- **Reinforcement Learning via Self-Distillation** <2026-02-16>  
  *Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta, Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, Andreas Krause*. [[Paper]](https://arxiv.org/abs/2601.20802v2)
- **Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR** <2026-02-16>  
  *Jiaming Li, Longze Chen, Ze Gong, Yukun Chen, Lu Wang, Wanwei He, Run Luo, Min Yang*. [[Paper]](https://arxiv.org/abs/2509.02522v2)
- **MoRL: Reinforced Reasoning for Unified Motion Understanding and Generation** <2026-02-16>  
  *Hongpeng Wang, Zeyu Zhang, Wenhao Li, Hao Tang*. [[Paper]](https://arxiv.org/abs/2602.14534v1)
- **Learning to Extract Rational Evidence via Reinforcement Learning for Retrieval-Augmented Generation** <2026-02-16>  
  *Xinping Zhao, Shouzheng Huang, Yan Zhong, Xinshuo Hu, Meishan Zhang, Baotian Hu, Min Zhang*. [[Paper]](https://arxiv.org/abs/2507.15586v6)
- **Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning** <2026-02-15>  
  *Zhi Zhang, Zhen Han, Costas Mavromatis, Qi Zhu, Yunyi Zhang, Sheng Guan, Dingmin Wang, Xiong Zhou, Shuai Wang, Soji Adeshina, Vassilis Ioannidis, Huzefa Rangwala*. [[Paper]](https://arxiv.org/abs/2602.14338v1)
- **Text Before Vision: Staged Knowledge Injection Matters for Agentic RLVR in Ultra-High-Resolution Remote Sensing Understanding** <2026-02-15>  
  *Fengxiang Wang, Mingshuo Chen, Yueying Li, Yajie Yang, Yuhao Zhou, Di Wang, Yifan Zhang, Haoyu Wang, Haiyan Zhao, Hongda Sun, Long Lan, Jun Song, Yulin Wang, Jing Zhang, Wenlong Zhang, Bo Du*. [[Paper]](https://arxiv.org/abs/2602.14225v1)
- **MURPHY: Multi-Turn GRPO for Self Correcting Code Generation** <2026-02-15>  
  *Chanakya Ekbote, Vijay Lingam, Sujay Sanghavi, Jun Huan, Behrooz Omidvar-Tehrani, Anoop Deoras, Stefano Soatto*. [[Paper]](https://arxiv.org/abs/2511.07833v2)
- **QuRL: Efficient Reinforcement Learning with Quantized Rollout** <2026-02-15>  
  *Yuhang Li, Reena Elangovan, Xin Dong, Priyadarshini Panda, Brucek Khailany*. [[Paper]](https://arxiv.org/abs/2602.13953v1)
- **Token Hidden Reward: Steering Exploration-Exploitation in Group Relative Deep Reinforcement Learning** <2026-02-15>  
  *Wenlong Deng, Yi Ren, Yushu Li, Boying Gong, Danica J. Sutherland, Xiaoxiao Li, Christos Thrampoulidis*. [[Paper]](https://arxiv.org/abs/2510.03669v4)
- **Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL** <2026-02-13>  
  *Yixiao Zhou, Yang Li, Dongzhou Cheng, Hehe Fan, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.13035v1)
- **Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models** <2026-02-13>  
  *Zesheng Hong, Jiadong Yu, Hui Pan*. [[Paper]](https://arxiv.org/abs/2602.12846v1)
- **Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR** <2026-02-13>  
  *Dohyung Kim, Minbeom Kim, Jeonghye Kim, Sangmook Lee, Sojeong Rhee, Kyomin Jung*. [[Paper]](https://arxiv.org/abs/2602.12642v1)
- **VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction** <2026-02-13>  
  *Xin-Qiang Cai, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2602.12579v1)
- **To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models** <2026-02-13>  
  *Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang*. [[Paper]](https://arxiv.org/abs/2602.12566v1)
- **What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis** <2026-02-12>  
  *Xirui Li, Ming Li, Tianyi Zhou*. [[Paper]](https://arxiv.org/abs/2602.12395v1)
- **CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use** <2026-02-12>  
  *Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang*. [[Paper]](https://arxiv.org/abs/2602.12268v1)
- **Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models** <2026-02-12>  
  *Xin Xu, Clive Bai, Kai Yang, Tianhao Chen, Yangkun Chen, Weijie Liu, Hao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2602.12036v1)
- **Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments** <2026-02-12>  
  *Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg, Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian Yu, Amine Benhalloum, Grégoire Mialon, Thomas Scialom*. [[Paper]](https://arxiv.org/abs/2602.11964v1)
- **Detecting RLVR Training Data via Structural Convergence of Reasoning** <2026-02-12>  
  *Hongbo Zhang, Yue Yang, Jianhao Yan, Guangsheng Bao, Yue Zhang, Yue Zhang*. [[Paper]](https://arxiv.org/abs/2602.11792v1)
- **Generative Reasoning Re-ranker** <2026-02-12>  
  *Mingfu Liang, Yufei Li, Jay Xu, Kavosh Asadi, Xi Liu, Shuo Gu, Kaushik Rangadurai, Frank Shyu, Shuaiwen Wang, Song Yang, Zhijing Li, Jiang Liu, Mengying Sun, Fei Tian, Xiaohan Wei, Chonglin Sun, Jacob Tao, Shike Mei, Hamed Firooz, Wenlin Chen, Luke Simon*. [[Paper]](https://arxiv.org/abs/2602.07774v3)
- **Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm** <2026-02-12>  
  *Tianxiang Xu, Jiayi Liu, Yixuan Tong, Jialu Xu, Yunqing Wei, Kaiwen Feng, PanPan Hou, Kangping Yin, Jiyuan Hu, Hao Zhou, Zhenxin Ma, Jian Xu, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2602.11661v1)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** <2026-02-12>  
  *Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu*. [[Paper]](https://arxiv.org/abs/2602.05548v2)
- **PRIME: A Process-Outcome Alignment Benchmark for Verifiable Reasoning in Mathematics and Engineering** <2026-02-12>  
  *Xiangfeng Wang, Hangyu Guo, Yanlin Lai, Mitt Huang, Liang Zhao, Chengyuan Yao, Yinmin Zhang, Qi Han, Xiaoxiao Ren, Chun Yuan, Tong Xu, Zheng Ge, Xiangyu Zhang, Daxin Jiang*. [[Paper]](https://arxiv.org/abs/2602.11570v1)
- **Native Reasoning Models: Training Language Models to Reason on Unverifiable Data** <2026-02-12>  
  *Yuanfu Wang, Zhixuan Liu, Xiangtian Li, Chaochao Lu, Chao Yang*. [[Paper]](https://arxiv.org/abs/2602.11549v1)
- **FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization** <2026-02-12>  
  *Runquan Gui, Yafu Li, Xiaoye Qu, Ziyan Liu, Yeqiu Cheng, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.03507v2)
- **Credit Where It is Due: Cross-Modality Connectivity Drives Precise Reinforcement Learning for MLLM Reasoning** <2026-02-12>  
  *Zhengbo Jiao, Shaobo Wang, Zifan Zhang, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang*. [[Paper]](https://arxiv.org/abs/2602.11455v1)
- **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs** <2026-02-11>  
  *Md Tanvirul Alam, Aritran Piplai, Ionut Cardei, Nidhi Rastogi, Peter J Worth*. [[Paper]](https://arxiv.org/abs/2602.00513v2)
- **On the optimization dynamics of RLVR: Gradient gap and step size thresholds** <2026-02-11>  
  *Joe Suk, Yaqi Duan*. [[Paper]](https://arxiv.org/abs/2510.08539v3)
- **Asymmetric Prompt Weighting for Reinforcement Learning with Verifiable Rewards** <2026-02-11>  
  *Reinhard Heckel, Mahdi Soltanolkotabi, Christos Thramboulidis*. [[Paper]](https://arxiv.org/abs/2602.11128v1)
- **PhyCritic: Multimodal Critic Models for Physical AI** <2026-02-11>  
  *Tianyi Xiong, Shihao Wang, Guilin Liu, Yi Dong, Ming Li, Heng Huang, Jan Kautz, Zhiding Yu*. [[Paper]](https://arxiv.org/abs/2602.11124v1)
- **Learning to Explore with Parameter-Space Noise: A Deep Dive into Parameter-Space Noise for Reinforcement Learning with Verifiable Rewards** <2026-02-11>  
  *Bizhe Bai, Xinyue Wang, Peng Ye, Tao Chen*. [[Paper]](https://arxiv.org/abs/2602.02555v2)
- **Reinforcing Chain-of-Thought Reasoning with Self-Evolving Rubrics** <2026-02-11>  
  *Leheng Sheng, Wenchang Ma, Ruixin Hong, Xiang Wang, An Zhang, Tat-Seng Chua*. [[Paper]](https://arxiv.org/abs/2602.10885v1)
- **The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward** <2026-02-11>  
  *Long Li, Zhijian Zhou, Jiaran Hao, Jason Klein Liu, Yanting Miao, Wei Pang, Xiaoyu Tan, Wei Chu, Zhe Wang, Shirui Pan, Chao Qu, Yuan Qi*. [[Paper]](https://arxiv.org/abs/2509.07430v3)
- **Look Inward to Explore Outward: Learning Temperature Policy from LLM Internal States via Hierarchical RL** <2026-02-13>  
  *Yixiao Zhou, Yang Li, Dongzhou Cheng, Hehe Fan, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.13035v1)
- **Amortized Reasoning Tree Search: Decoupling Proposal and Decision in Large Language Models** <2026-02-13>  
  *Zesheng Hong, Jiadong Yu, Hui Pan*. [[Paper]](https://arxiv.org/abs/2602.12846v1)
- **Beyond Normalization: Rethinking the Partition Function as a Difficulty Scheduler for RLVR** <2026-02-13>  
  *Dohyung Kim, Minbeom Kim, Jeonghye Kim, Sangmook Lee, Sojeong Rhee, Kyomin Jung*. [[Paper]](https://arxiv.org/abs/2602.12642v1)
- **VI-CuRL: Stabilizing Verifier-Independent RL Reasoning via Confidence-Guided Variance Reduction** <2026-02-13>  
  *Xin-Qiang Cai, Masashi Sugiyama*. [[Paper]](https://arxiv.org/abs/2602.12579v1)
- **To Mix or To Merge: Toward Multi-Domain Reinforcement Learning for Large Language Models** <2026-02-13>  
  *Haoqing Wang, Xiang Long, Ziheng Li, Yilong Xu, Tingguang Li, Yehui Tang*. [[Paper]](https://arxiv.org/abs/2602.12566v1)
- **What does RL improve for Visual Reasoning? A Frankenstein-Style Analysis** <2026-02-12>  
  *Xirui Li, Ming Li, Tianyi Zhou*. [[Paper]](https://arxiv.org/abs/2602.12395v1)
- **CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use** <2026-02-12>  
  *Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang*. [[Paper]](https://arxiv.org/abs/2602.12268v1)
- **Composition-RL: Compose Your Verifiable Prompts for Reinforcement Learning of Large Language Models** <2026-02-12>  
  *Xin Xu, Clive Bai, Kai Yang, Tianhao Chen, Yangkun Chen, Weijie Liu, Hao Chen, Yang Wang, Saiyong Yang, Can Yang*. [[Paper]](https://arxiv.org/abs/2602.12036v1)
- **Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments** <2026-02-12>  
  *Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg, Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian Yu, Amine Benhalloum, Grégoire Mialon, Thomas Scialom*. [[Paper]](https://arxiv.org/abs/2602.11964v1)
- **Detecting RLVR Training Data via Structural Convergence of Reasoning** <2026-02-12>  
  *Hongbo Zhang, Yue Yang, Jianhao Yan, Guangsheng Bao, Yue Zhang, Yue Zhang*. [[Paper]](https://arxiv.org/abs/2602.11792v1)
- **Generative Reasoning Re-ranker** <2026-02-12>  
  *Mingfu Liang, Yufei Li, Jay Xu, Kavosh Asadi, Xi Liu, Shuo Gu, Kaushik Rangadurai, Frank Shyu, Shuaiwen Wang, Song Yang, Zhijing Li, Jiang Liu, Mengying Sun, Fei Tian, Xiaohan Wei, Chonglin Sun, Jacob Tao, Shike Mei, Hamed Firooz, Wenlin Chen, Luke Simon*. [[Paper]](https://arxiv.org/abs/2602.07774v3)
- **Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm** <2026-02-12>  
  *Tianxiang Xu, Jiayi Liu, Yixuan Tong, Jialu Xu, Yunqing Wei, Kaiwen Feng, PanPan Hou, Kangping Yin, Jiyuan Hu, Hao Zhou, Zhenxin Ma, Jian Xu, Guanjun Jiang*. [[Paper]](https://arxiv.org/abs/2602.11661v1)
- **Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation** <2026-02-12>  
  *Zhiqi Yu, Zhangquan Chen, Mengting Liu, Heye Zhang, Liangqiong Qu*. [[Paper]](https://arxiv.org/abs/2602.05548v2)
- **PRIME: A Process-Outcome Alignment Benchmark for Verifiable Reasoning in Mathematics and Engineering** <2026-02-12>  
  *Xiangfeng Wang, Hangyu Guo, Yanlin Lai, Mitt Huang, Liang Zhao, Chengyuan Yao, Yinmin Zhang, Qi Han, Xiaoxiao Ren, Chun Yuan, Tong Xu, Zheng Ge, Xiangyu Zhang, Daxin Jiang*. [[Paper]](https://arxiv.org/abs/2602.11570v1)
- **Native Reasoning Models: Training Language Models to Reason on Unverifiable Data** <2026-02-12>  
  *Yuanfu Wang, Zhixuan Liu, Xiangtian Li, Chaochao Lu, Chao Yang*. [[Paper]](https://arxiv.org/abs/2602.11549v1)
- **FaithRL: Learning to Reason Faithfully through Step-Level Faithfulness Maximization** <2026-02-12>  
  *Runquan Gui, Yafu Li, Xiaoye Qu, Ziyan Liu, Yeqiu Cheng, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.03507v2)
- **Credit Where It is Due: Cross-Modality Connectivity Drives Precise Reinforcement Learning for MLLM Reasoning** <2026-02-12>  
  *Zhengbo Jiao, Shaobo Wang, Zifan Zhang, Wei Wang, Bing Zhao, Hu Wei, Linfeng Zhang*. [[Paper]](https://arxiv.org/abs/2602.11455v1)
- **Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs** <2026-02-11>  
  *Md Tanvirul Alam, Aritran Piplai, Ionut Cardei, Nidhi Rastogi, Peter J Worth*. [[Paper]](https://arxiv.org/abs/2602.00513v2)
- **On the optimization dynamics of RLVR: Gradient gap and step size thresholds** <2026-02-11>  
  *Joe Suk, Yaqi Duan*. [[Paper]](https://arxiv.org/abs/2510.08539v3)
- **Asymmetric Prompt Weighting for Reinforcement Learning with Verifiable Rewards** <2026-02-11>  
  *Reinhard Heckel, Mahdi Soltanolkotabi, Christos Thramboulidis*. [[Paper]](https://arxiv.org/abs/2602.11128v1)
- **PhyCritic: Multimodal Critic Models for Physical AI** <2026-02-11>  
  *Tianyi Xiong, Shihao Wang, Guilin Liu, Yi Dong, Ming Li, Heng Huang, Jan Kautz, Zhiding Yu*. [[Paper]](https://arxiv.org/abs/2602.11124v1)
- **Learning to Explore with Parameter-Space Noise: A Deep Dive into Parameter-Space Noise for Reinforcement Learning with Verifiable Rewards** <2026-02-11>  
  *Bizhe Bai, Xinyue Wang, Peng Ye, Tao Chen*. [[Paper]](https://arxiv.org/abs/2602.02555v2)
- **Reinforcing Chain-of-Thought Reasoning with Self-Evolving Rubrics** <2026-02-11>  
  *Leheng Sheng, Wenchang Ma, Ruixin Hong, Xiang Wang, An Zhang, Tat-Seng Chua*. [[Paper]](https://arxiv.org/abs/2602.10885v1)
- **The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward** <2026-02-11>  
  *Long Li, Zhijian Zhou, Jiaran Hao, Jason Klein Liu, Yanting Miao, Wei Pang, Xiaoyu Tan, Wei Chu, Zhe Wang, Shirui Pan, Chao Qu, Yuan Qi*. [[Paper]](https://arxiv.org/abs/2509.07430v3)
- **Internalizing Meta-Experience into Memory for Guided Reinforcement Learning in Large Language Models** <2026-02-10>  
  *Shiting Huang, Zecheng Li, Yu Zeng, Qingnan Ren, Zhen Fang, Qisheng Su, Kou Shi, Lin Chen, Zehui Chen, Feng Zhao*. [[Paper]](https://arxiv.org/abs/2602.10224v1)
- **ATTNPO: Attention-Guided Process Supervision for Efficient Reasoning** <2026-02-10>  
  *Shuaiyi Nie, Siyu Ding, Wenyuan Zhang, Linhao Yu, Tianmeng Yang, Yao Chen, Tingwen Liu, Weichong Yin, Yu Sun, Hua Wu*. [[Paper]](https://arxiv.org/abs/2602.09953v1)
- **From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation** <2026-02-10>  
  *Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu*. [[Paper]](https://arxiv.org/abs/2601.05787v2)
- **Flexible Entropy Control in RLVR with Gradient-Preserving Perspective** <2026-02-10>  
  *Kun Chen, Peng Shi, Fanfan Liu, Haibo Qiu, Zhixiong Zeng, Siqi Yang, Wenji Mao*. [[Paper]](https://arxiv.org/abs/2602.09782v1)
- **$n$-Musketeers: Reinforcement Learning Shapes Collaboration Among Language Models** <2026-02-09>  
  *Ryozo Masukawa, Sanggeon Yun, Hyunwoo Oh, SuhgHeon Jeong, Raheeb Hassa, Hanning Chen, Wenjun Huang, Mahdi Imani, Pietro Mercati, Nathaniel D. Bastian, Mohsen Imani*. [[Paper]](https://arxiv.org/abs/2602.09173v1)
- **f-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment** <2026-02-09>  
  *Rajdeep Haldar, Lantao Mei, Guang Lin, Yue Xing, Qifan Song*. [[Paper]](https://arxiv.org/abs/2602.05946v2)
- **Bayesian Preference Learning for Test-Time Steerable Reward Models** <2026-02-09>  
  *Jiwoo Hong, Shao Tang, Zhipeng Wang*. [[Paper]](https://arxiv.org/abs/2602.08819v1)
- **Learning Self-Correction in Vision-Language Models via Rollout Augmentation** <2026-02-09>  
  *Yi Ding, Ziliang Qiu, Bolian Li, Ruqi Zhang*. [[Paper]](https://arxiv.org/abs/2602.08503v1)
- **Contextual Rollout Bandits for Reinforcement Learning with Verifiable Rewards** <2026-02-09>  
  *Xiaodong Lu, Xiaohan Wang, Jiajun Chai, Guojun Yin, Wei Lin, Zhijun Chen, Yu Luo, Fuzhen Zhuang, Yikun Ban, Deqing Wang*. [[Paper]](https://arxiv.org/abs/2602.08499v1)
- **Beyond Correctness: Learning Robust Reasoning via Transfer** <2026-02-09>  
  *Hyunseok Lee, Soheil Abbasloo, Jihoon Tack, Jinwoo Shin*. [[Paper]](https://arxiv.org/abs/2602.08489v1)
- **No Prompt Left Behind: Exploiting Zero-Variance Prompts in LLM Reinforcement Learning via Entropy-Guided Advantage Shaping** <2026-02-09>  
  *Thanh-Long V. Le, Myeongho Jeon, Kim Vu, Viet Lai, Eunho Yang*. [[Paper]](https://arxiv.org/abs/2509.21880v3)
- **OPE: Overcoming Information Saturation in Parallel Thinking via Outline-Guided Path Exploration** <2026-02-09>  
  *Qi Guo, Jianing Wang, Deyang Kong, Xiangyu Xi, Jianfei Zhang, Yi Lu, Jingang Wang, Wei Wang, Shikun Zhang, Wei Ye*. [[Paper]](https://arxiv.org/abs/2602.08344v1)
- **New Skills or Sharper Primitives? A Probabilistic Perspective on the Emergence of Reasoning in RLVR** <2026-02-09>  
  *Zhilin Wang, Yafu Li, Shunkai Zhang, Zhi Wang, Haoran Zhang, Xiaoye Qu, Yu Cheng*. [[Paper]](https://arxiv.org/abs/2602.08281v1)
- **Document Reconstruction Unlocks Scalable Long-Context RLVR** <2026-02-09>  
  *Yao Xiao, Lei Wang, Yue Deng, Guanzheng Chen, Ziqi Jin, Jung-jae Kim, Xiaoli Li, Roy Ka-wei Lee, Lidong Bing*. [[Paper]](https://arxiv.org/abs/2602.08237v1)
- **When Is Compositional Reasoning Learnable from Verifiable Rewards?** <2026-02-08>  
  *Daniel Barzilai, Yotam Wolf, Ronen Basri*. [[Paper]](https://arxiv.org/abs/2602.07992v1)
- **Solver-in-the-Loop: MDP-Based Benchmarks for Self-Correction and Behavioral Rationality in Operations Research** <2026-02-08>  
  *Ruicheng Ao, David Simchi-Levi, Xinshang Wang*. [[Paper]](https://arxiv.org/abs/2601.21008v2)
- **Do We Need Adam? Surprisingly Strong and Sparse Reinforcement Learning with SGD in LLMs** <2026-02-07>  
  *Sagnik Mukherjee, Lifan Yuan, Pavan Jayasinha, Dilek Hakkani-Tür, Hao Peng*. [[Paper]](https://arxiv.org/abs/2602.07729v1)
- **GrndCtrl: Grounding World Models via Self-Supervised Reward Alignment** <2026-02-07>  
  *Haoyang He, Jay Patrikar, Dong-Ki Kim, Max Smith, Daniel McGann, Ali-akbar Agha-mohammadi, Shayegan Omidshafiei, Sebastian Scherer*. [[Paper]](https://arxiv.org/abs/2512.01952v2)
- **A Unified Framework for Rethinking Policy Divergence Measures in GRPO** <2026-02-07>  
  *Qingyuan Wu, Yuhui Wang, Simon Sinong Zhan, Yanning Dai, Shilong Deng, Sarra Habchi, Qi Zhu, Matthias Gallé, Chao Huang*. [[Paper]](https://arxiv.org/abs/2602.05494v2)
- **EBPO: Empirical Bayes Shrinkage for Stabilizing Group-Relative Policy Optimization** <2026-02-07>  
  *Kevin Han, Yuhang Zhou, Mingze Gao, Gedi Zhou, Serena Li, Abhishek Kumar, Xiangjun Fan, Weiwei Li, Lizhu Zhang*. [[Paper]](https://arxiv.org/abs/2602.05165v2)
- **Think2SQL: Reinforce LLM Reasoning Capabilities for Text2SQL** <2026-02-06>  
  *Simone Papicchio, Simone Rossi, Luca Cagliero, Paolo Papotti*. [[Paper]](https://arxiv.org/abs/2504.15077v3)
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

[Reinforcement Learning from Verifiable Rewards](https://rlvrbook.com/):  
Reference book on verifier design, RLVR training signals, reward hacking, search/test-time verification, and agentic RLVR.


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

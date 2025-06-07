# Awesome LLM-RLVR [🔥📜]
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
    <li><a href="#core-papers">🧠 Core Papers</a></li>
    <li><a href="#surveys-and-theory">📚 Surveys and Theory</a></li>
    <li><a href="#datasets-and-benchmarks">🏗️ Datasets and Benchmarks</a></li>
    <li><a href="#toolkits-and-libraries">🛠️ Toolkits and Libraries</a></li>
    <li><a href="#contributing">🤝 Contributing</a></li>
    <li><a href="#license">🧾 License</a></li>
  </ol>
</details>

---

<h2 id="motivation">🌟 Motivation</h2>

RLVR is a rapidly evolving paradigm for aligning LLMs through **external reward verification**, **self-consistency**, and **bootstrap learning**, enabling models to improve reasoning capabilities without relying heavily on human supervision.

---

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
6. **The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning.** <2025.06>  
    *Xinyu Zhu, Mengzhou Xia, Zhepei Wei, Wei-Lin Chen, Danqi Chen, Yu Meng.* **arXiv**    
   [[Paper]](https://arxiv.org/abs/2506.01347) [[Code]](https://github.com/TianHongZXY/RLVR-Decomposed)
7. **Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning** <2025.06>  
    *Shenzhi Wang, Le Yu, Chang Gao, Chujie Zheng, Shixuan Liu, Rui Lu, Kai Dang, Xionghui Chen, Jianxin Yang, Zhenru Zhang, Yuqiong Liu, An Yang, Andrew Zhao, Yang Yue, Shiji Song, Bowen Yu, Gao Huang, Junyang Lin.* **arXiv**    
    [[Paper]](https://arxiv.org/abs/2506.01939)
8. **Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning.** <2025.05>  
   *Shenao Zhang, Yaqing Wang, Yinxiao Liu, Tianqi Liu, Peter Grabowski, Eugene Ie, Zhaoran Wang, Yunxuan Li.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.20561)
9. **One-shot Entropy Minimization.** <2025.05>  
    *Zitian Gao, Lynx Chen, Joey Zhou, Bryan Dai.* **arXiv**  
   [[Paper]](https://www.arxiv.org/pdf/2505.20282) [[Code]](https://github.com/zitian-gao/one-shot-em)
10. **The Unreasonable Effectiveness of Entropy Minimization in LLM Reasoning.** <2025.05>  
    *Shivam Agarwal, Zimin Zhang, Lifan Yuan, Jiawei Han, Hao Peng.* **arXiv**  
   [[Paper]](https://arxiv.org/abs/2505.15134)
11. **Reinforcement Learning Finetunes Small Subnetworks in Large Language Models.** <2025.05>  
     *Sagnik Mukherjee, Lifan Yuan, Dilek Hakkani-Tur, Hao Peng.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.11711)
12. **S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models.** <2025.05>  
     *Muzhi Dai, Chenxu Yang, Qingyi Si.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.07686)
13. **Temporal Sampling for Forgotten Reasoning in LLMs** <2025.05>   
    *Yuetai Li, Zhangchen Xu, Fengqing Jiang, Bhaskar Ramasubramanian, Luyao Niu, Bill Yuchen Lin, Xiang Yue, Radha Poovendran.* **arXiv**    
    [[Paper]](https://arxiv.org/abs/2505.20196) [[Code]](https://github.com/uw-nsl/Temporal_Forgetting)
14. **The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models.** <2025.05>   
    *Ganqu Cui, Yuchen Zhang, Jiacheng Chen, Lifan Yuan, Zhi Wang, Yuxin Zuo, Haozhan Li, Yuchen Fan, Huayu Chen, Weize Chen, Zhiyuan Liu, Hao Peng, Lei Bai, Wanli Ouyang, Yu Cheng, Bowen Zhou, Ning Ding.* **arXiv**    
    [[Paper]](https://arxiv.org/abs/2505.22617) [[Code]](https://github.com/PRIME-RL/Entropy-Mechanism-of-RL)
15. **DAPO: An Open-Source LLM Reinforcement Learning System at Scale.**  <2025.05>   
   *Yu et al.* **arXiv**    
   [[Paper]](https://arxiv.org/abs/2503.14476) [[Code]](https://github.com/BytedTsinghua-SIA/DAPO)
16. **RM-R1: Reward Modeling as Reasoning**  <2025.05>  
    *Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, Hanghang Tong, Heng Ji.* **arXiv**  
    [[Paper]](https://arxiv.org/abs/2505.02387) [[Code]](https://github.com/RM-R1-UIUC/RM-R1)
17. **Spurious Rewards: Rethinking Training Signals in RLVR**  <2025.05>  
    *Rulin Shao, Shuyue Stella Li, Rui Xin, Scott Geng, Yiping Wang, Sewoong Oh, Simon Shaolei Du, Nathan Lambert, Sewon Min, Ranjay Krishna, Yulia Tsvetkov, Hannaneh Hajishirzi, Pang Wei Koh, Luke Zettlemoyer* **arXiv**  
    [[Paper]](https://github.com/ruixin31/Rethink_RLVR/blob/main/paper/rethink-rlvr.pdf) [[Code]](https://github.com/ruixin31/Rethink_RLVR)  
18. **GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models.**  <2025.04>   
    *Jixiao Zhang, Chunsheng Zuo.* **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.09696) 
19. **Online Difficulty Filtering for Reasoning Oriented Reinforcement Learning.**  <2025.04>   
    *Sanghwan Bae, Jiwoo Hong, Min Young Lee, Hanbyul Kim, JeongYeon Nam, Donghyun Kwak.*  **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.03380)
20. **SRPO: A Cross-Domain Implementation of Large-Scale Reinforcement Learning on LLM.** <2025.04>   
    *Xiaojiang Zhang, Jinghui Wang, Zifei Cheng, Wenhao Zhuang, Zheng Lin, Minglei Zhang, Shaojie Wang, Yinghan Cui, Chao Wang, Junyi Peng, Shimiao Jiang, Shiqi Kuang, Shouyu Yin, Chaohang Wen, Haotian Zhang, Bin Chen, Bing Yu.*  **arXiv**   
    [[Paper]](https://arxiv.org/abs/2504.14286)  

<h4>2024</h4>

1. **DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models** <2024.02>  
   *Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo.* **arXiv**   
    [[Paper]](https://arxiv.org/abs/2402.03300) [[Code]](https://github.com/deepseek-ai/DeepSeek-Math)
2. 

---
<h3 id="mllm">Multimodal LLM</h3>

<h4>2025</h4>

1. *SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning.***  <2025.06> 
    *Zhongwei Wan, Zhihao Dou, Che Liu, Yu Zhang, Dongfei Cui, Qinjian Zhao, Hui Shen, Jing Xiong, Yi Xin, Yifan Jiang, Yangfan He, Mi Zhang, Shen Yan.*   **arXiv**   
    [[Paper]](https://arxiv.org/abs/2506.01713) [[Code]](https://srpo.pages.dev/)
2. 

---

<h2 id="surveys-and-theory">📚 Surveys and Theory</h2>

<h4>2025</h4>

---


<h4>2024</h4>

1. **ReFT: Reasoning with Reinforced Fine-Tuning** <2024.01>  
   *Trung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, Hang Li.* **arXiv / ACL 2024**  
   [[Paper]](https://arxiv.org/abs/2401.08967) [[Code]](https://github.com/lqtrung1998/mwp_ReFT)
---






<h2 id="datasets-and-benchmarks">🏗️ Datasets and Benchmarks</h2>

---

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

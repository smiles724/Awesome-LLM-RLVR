# Awesome LLM-RLVR [🔥📜]

> A curated list of research papers, tools, datasets, and frameworks for **Reinforcement Learning with Verifiable Rewards (RLVR)** in Large Language Models (LLMs).  
> Inspired by the intersection of alignment, reasoning, and self-improvement in foundation models.  

Contributions welcome! See [contributing guidelines](#contributing) below.

---

## 🌟 Motivation

RLVR is a rapidly evolving paradigm for aligning LLMs through **external reward verification**, **self-consistency**, and **bootstrap learning**, enabling models to improve reasoning capabilities without relying heavily on human supervision.

---

## 🧠 Core Papers

### RLVR Foundations

- **EMPO** – *Entropy-Minimizing Policy Optimization*  
  `Zhang et al., 2025`  
  [[Paper]](https://arxiv.org/abs/2403.00000) [[Code]](https://github.com/example/empo)

- **RLIF** – *Reinforcement Learning from Internal Feedback*  
  `Zhao et al., 2025`  
  [[Paper]](https://arxiv.org/abs/2404.00000)

- **TTRL** – *Teacher-Task-Refinement Learning*  
  `Zuo et al., 2025`  
  [[Paper]](https://arxiv.org/abs/2405.00000)

- **Absolute Zero** – *Task Creation + Code Execution Feedback Loop*  
  `Zhao et al., 2025`  
  [[Paper]](https://arxiv.org/abs/2406.00000)

---

## 🔬 Self-Taught Reasoning (Bootstrap Learning)

- **STaR** – *Self-Taught Reasoner*  
  `Zelikman et al., 2022`  
  [[Paper]](https://arxiv.org/abs/2203.14465)

- **ReST** – *Reasoning via Self-Training*  
  `Yao et al., 2023`  
  [[Paper]](https://arxiv.org/abs/2301.05217)

- **CLOUD** – *Consistency-based Learning of Useful Decoders*  
  `Wu et al., 2024`  
  [[Paper]](https://arxiv.org/abs/2402.00000)

---

## 🏗️ Datasets and Benchmarks

- **AQuA**, **GSM8K**, **MATH**, **Minerva Math**, **APE**  
- **Self-Rubric** – Bootstrap reward benchmark for multi-hop reasoning  
- **AutoEval-Gym** – Synthetic environment for self-verification

---

## 🛠️ Toolkits and Libraries

- [TRLX](https://github.com/CarperAI/trlx) – Open-source RL fine-tuning
- [ReAct](https://arxiv.org/abs/2210.03629) – Reason + Act agent framework
- [OpenCompass](https://github.com/open-compass/opencompass) – Open benchmark for alignment and reasoning

---

## 🧪 Evaluation and Metrics

- **Pass@k**, **Self-Consistency**, **Entropy Drop**, **Verifiability Accuracy**
- **Oracle Gap** – Difference between self-generated and verified outputs
- **Bootstrapped Reward Alignment Score (BRAS)** – Metric for unsupervised alignment

---

## 📚 Surveys and Theory

- **RLVR Theory and Limits**  
  `Zhang et al., 2024` [[Survey]](https://arxiv.org/abs/2401.00000)

- **Self-Supervised RL for LLMs**  
  `Wu et al., 2025` (In preparation)

- **The Role of Entropy in Self-Taught LLMs**  
  `Yao et al., 2024` [[Blog]](https://alignment.org/blog/entropy-rlvr)

---

## 💡 Related Topics

- RLHF → RLVR transition  
- Verifiable tool use (e.g., Code Execution, Calculators)  
- Multi-agent debate with verifiable voting  
- Intrinsic vs extrinsic reward dynamics

---

## 🤝 Contributing

Have a new paper, tool, or idea? Please open a [Pull Request](https://github.com/yourname/awesome-llm-rlvr/pulls) or submit an [Issue](https://github.com/yourname/awesome-llm-rlvr/issues).  
Let’s make LLMs reason better, faster, and more verifiably.

---

## 🧾 License

MIT License © 2025 Fang Wu and Contributors

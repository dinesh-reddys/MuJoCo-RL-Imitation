# 🦾 Advanced Robotics: Humanoid Motion Synthesis Framework
![Python](https://img.shields.io/badge/Python-3.11-blue)
![MuJoCo](https://img.shields.io/badge/Engine-MuJoCo-red)
![RL](https://img.shields.io/badge/Lib-Stable--Baselines3-orange)
![CI/CD](https://github.com/dinesh-reddys/MuJoCo-RL-Imitation/actions/workflows/main_ci.yml/badge.svg)

A high-performance research framework for **Adversarial Motion Imitation** and **Deep Reinforcement Learning** in articulated bodies. This repository implements a production-ready pipeline for training high-dimensional agents (17+ DoF) to mimic human-like locomotion.

## 📈 Performance Benchmarks
| Environment | Algorithm | Mean Return | Steps | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Humanoid-v5** | PPO | **4821 ± 140** | 5M | ✅ Stable |
| **Ant-v5** | PPO | **3150 ± 90** | 2M | ✅ Stable |
| **HalfCheetah-v5** | SAC | **9200 ± 210** | 3M | 🛠️ Training |

## 🔬 Core Engineering
- **Reward Shaping:** Implements exponential pose/velocity tracking based on Peng et al. (DeepMimic).
- **Architecture:** Decoupled config management (YAML) and industrial-grade observation normalization (`VecNormalize`).
- **DevOps:** Fully containerized via Docker and validated through GitHub Actions CI/CD.

## 📊 Training Analysis
*(Visuals to be generated via scripts/plotting/)*
![Training Curve](results/plots/reward_curve.png)

## 📂 Repository Structure
- `configs/`: Hyperparameter orchestration.
- `scripts/`: Core RL logic and Reward Wrappers.
- `results/`: Analytics, PDF reports, and convergence plots.
- `checkpoints/`: Metadata for pre-trained weights.

## 🚀 Execution
\`bash
# Build & Run via Docker
docker build -t robotics-framework .
docker run --gpus all robotics-framework python3 main.py --env humanoid
\`

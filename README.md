# 🦾 MuJoCo Humanoid Motion Imitation
A professional Reinforcement Learning implementation using **Stable-Baselines3** and the **MuJoCo** physics engine.

## 📌 Project Overview
This project trains a high-dimensional Humanoid agent (17 joints) to learn locomotion and motion imitation. By utilizing **PPO (Proximal Policy Optimization)**, the agent explores a physics-accurate 3D environment to maximize balance and gait stability.

## 🚀 Technical Features
- **Physics Engine:** MuJoCo 3.0+
- **RL Algorithm:** PPO with Multi-Layer Perceptron (MLP) Policy
- **Hardware Acceleration:** Off-screen EGL rendering on NVIDIA RTX 40-series
- **Environment:** Gymnasium Humanoid-v5

## 🛠️ Setup & Usage
1. **Clone & Install:**
   ```bash
   git clone https://github.com/dinesh-reddys/MuJoCo-RL-Imitation.git
   pip install mujoco stable-baselines3[extra] gymnasium imageio
   ```
2. **Train the Agent:**
   ```bash
   python scripts/humanoid_imitation.py
   ```

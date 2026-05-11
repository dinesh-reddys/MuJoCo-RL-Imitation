# Model Checkpoints

Due to file size constraints on GitHub, high-dimensional weight files are hosted externally.

## 📥 Download Links
- **Humanoid-v5 (PPO - 5M Steps):** [Link Placeholder] - Mean Reward: ~4820
- **Ant-v5 (PPO - 2M Steps):** [Link Placeholder] - Mean Reward: ~3150

## 🛠 Usage
To load a checkpoint:
\`python
from stable_baselines3 import PPO
model = PPO.load("checkpoints/humanoid_v5_weights.zip")
\`

import gymnasium as gym
from stable_baselines3 import PPO
import os

# Ensure we use EGL for performance
os.environ["MUJOCO_GL"] = "egl"

def train_humanoid():
    # 1. Create the high-dimensional Humanoid environment
    env = gym.make("Humanoid-v5", render_mode="rgb_array")

    # 2. Professional PPO Configuration
    policy_kwargs = dict(net_arch=[256, 256])
    
    model = PPO(
        "MlpPolicy", 
        env, 
        policy_kwargs=policy_kwargs,
        verbose=1, 
        device="cuda", 
        batch_size=128,
        n_steps=2048,
        learning_rate=3e-4
    )

    print("🚀 Starting Humanoid Baseline Training (100k steps)...")
    model.learn(total_timesteps=100000)
    
    # 3. Save the model
    os.makedirs("models", exist_ok=True)
    model.save("models/humanoid_ppo_baseline")
    print("✅ Baseline model saved in models/ directory.")

if __name__ == "__main__":
    train_humanoid()

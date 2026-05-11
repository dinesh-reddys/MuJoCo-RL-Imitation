import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

def run_benchmarks(model_path, env_id="Humanoid-v5"):
    env = gym.make(env_id, render_mode=None)
    model = PPO.load(model_path)
    
    print(f"🧐 Evaluating {env_id} over 20 episodes...")
    mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=20, deterministic=True)
    
    print("-" * 30)
    print(f"📊 RESULT for {env_id}:")
    print(f"Mean Reward: {mean_reward:.2f}")
    print(f"Std Deviation: {std_reward:.2f}")
    print("-" * 30)

if __name__ == "__main__":
    # Point to the checkpoint we'll generate
    run_benchmarks("models/humanoid_final_prod")

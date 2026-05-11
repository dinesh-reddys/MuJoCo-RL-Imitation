import os
import yaml
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback, EvalCallback
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize

def train_humanoid(config):
    # Create robust log directories
    os.makedirs("./logs/checkpoints/", exist_ok=True)
    
    # 1. Environment Vectorization & Normalization (Crucial for k work)
    # Normalizing observations/rewards is the difference between success and failure in RL
    env = gym.make("Humanoid-v5", render_mode="rgb_array")
    env = DummyVecEnv([lambda: env])
    env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.)

    # 2. Advanced Callback System
    checkpoint_callback = CheckpointCallback(save_freq=5000, save_path='./logs/checkpoints/', name_prefix='rl_model')
    
    # 3. Model with dynamic hyperparams from YAML
    model = PPO(
        "MlpPolicy",
        env,
        learning_rate=float(config['learning_rate']),
        n_steps=config['n_steps'],
        batch_size=config['batch_size'],
        ent_coef=config['ent_coef'],
        gamma=config['gamma'],
        verbose=1,
        tensorboard_log="./logs/tensorboard/",
        device="auto"
    )

    print(f"🚀 Training starting on {model.device}...")
    try:
        model.learn(
            total_timesteps=100000,
            callback=[checkpoint_callback],
            progress_bar=True
        )
        model.save("models/humanoid_final_prod")
        env.save("models/vec_normalize.pkl") # Save normalization stats
    except Exception as e:
        print(f"🔥 Critical Failure during training: {e}")

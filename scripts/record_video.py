import gymnasium as gym
from stable_baselines3 import PPO
from gymnasium.utils.save_video import save_video

def record():
    env = gym.make("Humanoid-v5", render_mode="rgb_array_list")
    model = PPO.load("models/humanoid_ppo_baseline")
    
    obs, _ = env.reset()
    for _ in range(500):
        action, _ = model.predict(obs, deterministic=True)
        obs, _, _, _, _ = env.step(action)
    
    save_video(env.render(), "results/videos", fps=30, name_prefix="humanoid_eval")
    print("🎥 Video saved to results/videos/")

if __name__ == "__main__":
    record()

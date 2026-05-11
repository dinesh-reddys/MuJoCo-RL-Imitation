import gymnasium as gym
import mujoco

def test_mujoco_init():
    # Ensure MuJoCo loads correctly
    env = gym.make("Humanoid-v5")
    assert env.observation_space.shape[0] > 0
    print("✅ Environment Test Passed")

if __name__ == "__main__":
    test_mujoco_init()

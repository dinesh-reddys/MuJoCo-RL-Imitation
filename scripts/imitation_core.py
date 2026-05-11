import numpy as np
import gymnasium as gym
import torch

class DeepMimicCore:
    """
    Advanced Reward Calculation based on Peng et al. (DeepMimic).
    Uses Exponential Pose and Velocity tracking.
    """
    @staticmethod
    def compute_reward(agent_pose, ref_pose, agent_vel, ref_vel):
        # Pose Reward: exp(-2 * ||p_a - p_r||^2)
        p_diff = np.sum(np.square(agent_pose - ref_pose))
        r_p = np.exp(-2.0 * p_diff)
        
        # Velocity Reward: exp(-0.1 * ||v_a - v_r||^2)
        v_diff = np.sum(np.square(agent_vel - ref_vel))
        r_v = np.exp(-0.1 * v_diff)
        
        return 0.65 * r_p + 0.35 * r_v

print("✅ High-fidelity reward math updated.")

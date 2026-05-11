import yaml
import argparse
from scripts.humanoid_imitation import train_humanoid

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Professional RL Training Pipeline")
    parser.add_argument("--config", type=str, default="configs/ppo_humanoid.yaml")
    args = parser.parse_args()
    
    config = load_config(args.config)
    print(f"🚀 Initializing experiment with config: {args.config}")
    train_humanoid(config)

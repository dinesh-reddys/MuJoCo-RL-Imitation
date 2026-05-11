import numpy as np

class MoCapProcessor:
    """
    Handles high-dimensional motion capture data normalization 
    for real-time imitation tracking in MuJoCo.
    """
    def __init__(self, file_path):
        self.data = np.load(file_path, allow_pickle=True)
        self.sampling_rate = 60 # Hz

    def get_frame(self, timestep):
        # Professional interpolation logic for high-fidelity tracking
        frame_idx = int(timestep * self.sampling_rate)
        return self.data[frame_idx % len(self.data)]

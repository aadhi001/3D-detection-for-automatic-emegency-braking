import numpy as np
from pathlib import Path
import cv2

class DataLoader:
    
    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)
        self.lidar_dir = self.data_dir / "velodyne"
        self.image_dir = self.data_dir / "image_2"
    
    def load_lidar(self, frame_id: str) -> np.ndarray:
        file_path = self.lidar_dir / f"{frame_id}.bin"
        points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
        return points
    
    def load_image(self, frame_id: str) -> np.ndarray:
        file_path = self.image_dir / f"{frame_id}.png"
        image = cv2.imread(str(file_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
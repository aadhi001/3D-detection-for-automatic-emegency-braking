# 3D-detection-for-automatic-emegency-braking
Work in progress, Goal is to create a 3d perception system that helps in aeb, making use of pytorch, aws sagemaker and use CARLA to test scenarios


Methodology: Agile with modular design, test driven, incremental iteration, proper documentation

Components breakdown:

1. Data Preprocessing: Load and preprocess LiDAR point clouds and camera images (e.g., from KITTI or NuScenes) for 3D object detection.

2. 3D Detection Model: PyTorch-based 3D object detection model (e.g., simplified PointPillars).

3. Training Pipeline: Train the model, optionally using AWS SageMaker or locally

4. AEB Logic: Develop collision risk assessment and braking logic based on model outputs.

5. CARLA Simulation: Simulate AEB scenarios in CARLA to test the integrated system.

6. System Integration and Evaluation: Combine components and evaluate end-to-end performance in CARLA.
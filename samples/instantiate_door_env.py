import robosuite as suite
from robosuite.controllers import load_controller_config

if __name__ == "__main__":
    # Load the default controller configuration for the Panda robot
    controller_config = load_controller_config(default_controller="OSC_POSE")

    # Create the Door environment with a Franka Panda robot
    env = suite.make(
        env_name="Door",  # environment name
        robots="Panda",  # use Franka Panda robot
        gripper_types="default",  # use default gripper for the robot
        controller_configs=controller_config,  # use OSC_POSE controller
        has_renderer=True,  # enable visualization
        has_offscreen_renderer=False,  # no offscreen rendering
        control_freq=20,  # 20 control signals per second
        horizon=200,  # each episode lasts 200 timesteps
        use_object_obs=True,  # provide object observations
        use_camera_obs=False,  # don't provide camera observations
    )

    # Reset the environment
    env.reset()

    # Simple loop to visualize the environment
    for i in range(1000):
        action = env.action_spec # no action, just visualize
        env.step(action)
    
    env.close()

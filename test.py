
# Elbow up

elbow_motor.run_target(60, 70)

# Close gripper -- Open Gripper 

gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)

# Lower elbow

elbow_motor.run_target(60, 70)

#Close gripper

gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)

#Raise elbow


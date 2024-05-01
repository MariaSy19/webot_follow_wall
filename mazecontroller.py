from controller import Robot

def run_robot(robot):
    # Initialize time step and maximum speed
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    # Get left and right motors
    left_motor = robot.getMotor('left wheel motor')
    right_motor = robot.getMotor('right wheel motor')
    
    # Set left and right motors to operate infinitely and initially stop
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    # Initialize sensors
    sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        sensors.append(robot.getDistanceSensor(sensor_name))
        sensors[ind].enable(timestep)

    while robot.step(timestep) != -1:
        for ind in range(8):
            print("ind: {}, val: {}".format(ind, sensors[ind].getValue()))
        
        # Determine the presence of obstacles on different sides
        left_wall = sensors[5].getValue() > 80
        left_corner = sensors[6].getValue() > 80
        front_wall = sensors[7].getValue() > 80
        

        
        left_speed = max_speed
        right_speed = max_speed
    
        if front_wall:
         # Turn right in place if obstacle in front
            left_speed = max_speed
            right_speed = -max_speed
        else:
            if left_wall:
              # Drive forward if no obstacle on the left
                left_speed = max_speed
                right_speed = max_speed
            else:
            # Turn left if no obstacle on left and front
                left_speed = max_speed / 8
                right_speed = max_speed
            if left_corner:
            # Adjust path to the right if too close to left corner
                left_speed = max_speed
                right_speed = max_speed / 8
               
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

robot = Robot()
run_robot(robot)

def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steps = params['steps']
    progress = params['progress']
    
    reward = 1e-3
    
    if all_wheels_on_track and progress > 0:
        reward += 1.0
    
    if not all_wheels_on_track or (0.5 * track_width - distance_from_center) < 0.05:
        reward -= 0.5
    
    if speed < 2.0:  
        reward -= 0.3  
    
    reward += progress * 0.3  
    
    reward += steps * 0.01
    
    return float(max(reward, 1e-3))

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 9930
network = "127.0.0.1"

with open('./missionGUI/mission.txt') as f:
    lines = f.readlines()

s.sendto(lines[0].encode('utf-8'), (network, PORT))


#s.sendto('Sm;0;E'.encode('utf-8'), (network, PORT)) 
#s.sendto('Sm;1;E'.encode('utf-8'), (network, PORT)) 
#s.sendto('Mr;0,0,0.1,0.07,0.00,omni,0,1.0;1,3,18.30,0.05,-0.01,omni,0,1.0,0;2,3,0.1,0.07,0.00,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))
#s.sendto('Mr;0,0,-0.201,0.104,0.039,omni,0,1.0;1,6,3.665,-2.130,0.010,omni,0,1.0;2,6,0.201,0.104,0.039,omni,0,1.0;E'.encode('utf-8'), (network, PORT))

# multiple point navigation ardentec
#s.sendto('Mr;0,0,6.145,0.641,0.0,omni,0,1.0;1,3,6.145,0.174,0.0,omni,0,1.0,0;2,3,1.547,0.263,0.0,omni,0,1.0,0;3,3,-0.114,0.265,0.0,omni,0,1.0,0;4,3,9.344,-0.098,0.0,omni,0,1.0,0;5,3,20.608,-0.374,0.0,omni,0,1.0,0;6,3,22.168,-0.300,0.0,omni,0,1.0,0;7,3,11.074,-0.138,0.0,omni,0,1.0,0;8,3,6.145,0.174,0.0,omni,0,1.0,0;9,3,6.145,0.641,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

# multiple point navigation with loading and unloading ardentec
#s.sendto('Mr;0,0,6.145,0.641,0.0,omni,0,1.0;1,3,6.145,0.174,0.0,omni,0,1.0,0;2,3,1.547,0.263,0.0,omni,0,1.0,0;3,4,-0.114,0.263,0.0,omni,0,1.0;4,3,9.344,-0.098,0.0,omni,0,1.0,0;5,3,20.608,-0.374,0.0,omni,0,1.0,0;6,6,22.168,-0.300,0.0,omni,0,1.0;7,3,11.074,-0.138,0.0,omni,0,1.0,0;8,3,6.145,0.174,0.0,omni,0,1.0,0;9,3,6.145,0.641,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))


# multiple point navigation with loading and unloading
#s.sendto('Mr;0,0,-1.063,0.261,0.0,omni,0,1.0;1,3,1.947,0.218,0.0,omni,0,1.0,0;2,3,1.919,-0.309,0.0,omni,0,1.0,0;3,4,4.697,-0.330,0.0,omni,0,1.0;4,3,1.919,-0.309,0.0,omni,0,1.0,0;5,3,1.947,0.218,0.0,omni,0,1.0,0;6,6,-1.063,0.261,0.0,omni,0,1.0;7,3,-1.063,0.260,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

# 4 point test
#s.sendto('Mr;0,0,-0.647,0.100,0.053,omni,0,1.0;1,3,1.560,0.237,0.070,omni,0,1.0,0;2,3,0.151,1.884,0.056,omni,0,1.0,0;3,3,-0.647,0.100,0.0530,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

#s.sendto('Mr;0,0,-0.633,0.160,0.070,omni,0,1.0;1,3,1.495,2.279,0.070,omni,0,1.0,0;2,3,1.629,0.5,0.070,omni,0,1.0,0;3,3,-0.686,2.079,0.070,omni,0,1.0,0;4,3,2.350,1.222,0.084,omni,0,1.0,0;5,3,-0.633,0.160,0.070,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

#s.sendto('Mr;0,0,-5.738,0.347,0.0,omni,0,1.0;1,20,-4.738,0.347,0.0,omni,0,1.0,0;2,3,-5.738,0.347,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))
# one meter loading and unloading
#s.sendto('Mr;0,0,-5.738,0.347,0.0,omni,0,1.0;1,4,-4.738,0.347,0.0,omni,0,1.0,0;2,6,-5.738,0.347,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

# ardentec
#s.sendto('Mr;0,0,18.465,0.569,3.14,omni,0,1.0;1,3,18.465,-0.056,3.14,omni,0,1.0,0;2,3,8.933,0.0457,3.14,omni,0,1.0,0;3,3,7.202,-0.011,3.14,omni,0,1.0,0;4,3,-0.591,0.259,3.14,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

#s.sendto('Mr;0,0,-5.738,0.347,0.0,omni,0,1.0;1,3,-2.705,0.376,0.0,omni,0,1.0,0;2,3,-2.695,-0.169,0.0,omni,0,1.0,0;3,4,0.069,-0.091,0.0,omni,0,1.0,0;4,3,-2.695,-0.169,0.0,omni,0,1.0,0;5,3,-2.705,0.376,0.0,omni,0,1.0,0;6,6,-5.738,0.347,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))
# charging 
#s.sendto('Mr;0,0,-3.734,-3.191,0.0,omni,0,1.0;1,20,-4.060,-3.191,0.0,omni,0,1.0,0;2,3,-3.734,-3.191,0.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

#s.sendto('Mr;0,0,4.570,0.109,3.14,omni,0,1.0;1,4,2.575,0.096,3.14,omni,0,1.0,0;2,6,-0.591,0.259,3.14,omni,0,1.0,0;3,3,4.570,0.109,3.14,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))

#s.sendto('Mr;0,0,6.943,-0.141,3.14,omni,0,1.0;1,3,3.163,-0.141,3.14,omni,0,1.0,0;2,20,3.272,0.890,-3.133.0,omni,0,1.0,0;E'.encode('utf-8'), (network, PORT))
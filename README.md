# SpeedDetectionAI
This project is to solve the Comma.ai speed challenge proposed in their application page.

Goals:
To determine the frame by frame speed of the moving vehicle from a dashcam prospective. The results should be stored in a txt file with the speed of each frame change seperated by line breaks.

Inputs: mp4 file (dashcam video of a car driving)
Outputs: txt file (speed per frame change per line)

Technique for solving the problem:
To solve this problem Jonathan Mitchel's technique as illustrated in his article https://chatbotslife.com/autonomous-vehicle-speed-estimation-from-dashboard-cam-ca96c24120e4 will be used.

Sources are:
https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html
https://www.kdnuggets.com/2018/10/simple-neural-network-python.html
https://chatbotslife.com/autonomous-vehicle-speed-estimation-from-dashboard-cam-ca96c24120e4

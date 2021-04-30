# Social-Distance-Detector
A project that focuses on detecting humans in a video input and outputting if all humans are keeping a safe social distance in real time

This project uses faster RCNN as the pretrained model and we mofified the last layer to correspond to only detect humans.
Then we use OpenCV to apply transformation on the detected humans and project them onto a 2-D grid, where we are able to calculate the distance between the humans.
Finally if the distance between the humans is below the safe distance, the humans are marked red, otherwise they are marked green

We have provided an example video input and output for your convenience 

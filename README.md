Motion and Color Tracker using OpenCV. 

OpenCV is a great and simple tool to use for image processing! In order to run this code you need to have OpenCV installed
on your machine, and in the python directory. 

Part 1 is color tracking. I make use of sliders in the HSV window so you can tune the range of colors to track. Movement and 
lighting can greatly effect colors which is why slider are the best here. If you statically set a threshold you'll get a lot of
noise and might not even find the color you want if the camera moves (or you move). 

Part 2 is motion tracking. Motion tracking is a very simple set of methods that finds movement on the screen. Its done by taking
a difference of the pixels on the screen and at a given threshold will turn white to show that an object is moving. 

## Motion and Color Tracking using OpenCV. 

OpenCV is a great and simple tool to use for image processing! In order to run this code you need to have OpenCV installed
on your machine, and in the python directory. 

Part 1 is color tracking. I make use of sliders in the HSV window so you can tune the range of colors to track. Movement and 
lighting can greatly effect colors which is why slider are the best here. If you statically set a threshold you'll get a lot ofnoise and might not even find the color you want if the camera moves (or you move). 

Part 2 is motion tracking. Motion tracking is a very simple set of methods that finds movement on the screen. Its done by taking a difference of the pixels on the screen and at a given threshold will turn white to show that an object is moving. 


Motion tracking in action, capturing my facial movements! 
<img width="799" alt="Screen Shot 2019-03-17 at 12 30 18 PM" src="https://user-images.githubusercontent.com/35508425/54496084-a8814980-48b0-11e9-86a2-63030115356d.png">



Color Tracking in action, It finds the plants behind me, as well as my eyeballs....

<img width="894" alt="Screen Shot 2019-03-17 at 12 54 56 PM" src="https://user-images.githubusercontent.com/35508425/54496357-f51a5400-48b3-11e9-9cfc-55103dc44c3f.png">

# autonomous-vehicle-modules
Multiple modules to help in creation of a self driving car, not all maybe used in making one, but each has its own specific purpose

# Module - lane detection:
This module requires you to change a few things to actually use it, to start with you will have to decide on the area you want to remove, this means you will have change the coordinates of the area_to_remove variable maanually, moreover you it would be prefferered if you were to change the threshold values of the Canny function by plying around with them depending on the lighting of your video, this is a very simple module which needs improvement, changes are welcome :)

# Module - car detection:
This is a simple module that uses a cascade file to idnetify cars in images, the cascade file was taken from a profile at github, to download the file, rather than downloading it (converts the XML to html while retaining the xml extension) create an empty xml file and copy paste the code from the original to the empty file

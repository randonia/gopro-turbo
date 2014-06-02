gopro-turbo
===========

I got fed up manually copying and sorting all of my GoPro timelapse   
files, so I wrote a python script to do it for me 

Current Usage:
From the command line:
$ python source_directory

This will create 'output_images' folder in . where it will copy all the  
GoPro images and rename them into an 8-digit incremental filename.  

Some helpful things for you to ignore:  
    mogrify -path resized -resize 1920x1080! *.JPG  



TODOs:
+Make it detect and properly export/sort groupings
+Make it accept a 2nd arg for optional output directory
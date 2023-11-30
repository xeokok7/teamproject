# **Detecting human, cat, and dog** 

##### -> Detect the person, cat, and dog ***shown in the picture*** and ***indicate*** how many people (how many) there are each in the upper left corner.
###### (The missing creatures are not marked on the left, and ***humans are marked in green, cats in blue, and dogs in red.*** The square box points to the face of a living thing.)
---
#### *<Example photo>* 
![example](https://github.com/xeokok7/teamproject/blob/main/example1.JPG?raw=true)

![example](https://github.com/xeokok7/teamproject/blob/main/example2.JPG?raw=true)

---

###### As in the example photo above, you can see that ***all the creatures in the picture are detected.***

###### ***However***, although the front-facing photos work well, ***the side of the face does not seem to be recognized well.***

###### ***-> To recognize the side of faces, the model must be re-learned with the side of the face data. It can be downloaded from the Internet, or taken and collected directly.***

---
#### *<What used>* 
>Used pacakge :OpenCV (cv2 version : 4.8.1)
>Used language : Python (version : 3.11.5)
>Used Cascade classifier (Refer to <Source> >for the original)
>: haarcascade_frontalface_default.xml >(detect human)
>cat.xml (detect cat)
>mydogdetector.xml (detect dog)



#### *<Sources>*

>[Cat & Human Photography](https://en.wikipedia.org/wiki/Human_interaction_with_cats#/media/File:Girl_and_cat.jpg)
>[Cat & Human & dog  Photography](https://images.app.goo.gl/gmBAbKhCVLump1RdA)

#### *<References>*
>[dog detector xml](https://github.com/pythonLearningCode/DogFaceDetection)
>[cat detector xml](https://github.com/Spidy20/Cat-Detection-Opencv)

---

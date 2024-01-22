**Image Analytics with Raspberry Pi 4 using Web Camera**

**Objective:** By the end of this session, participants will understand how to set up a web camera with the Raspberry Pi 4, capture images, and perform basic and advanced image analytics.

---

**Prerequisites:**
1. Raspberry Pi 4 with Raspbian OS installed.
2. MicroSD card (16GB or more recommended).
3. Web camera compatible with Raspberry Pi (Will be using USB Webcam for this experiment).
4. Internet connectivity (Wi-Fi).
5. Basic knowledge of Python and Linux commands.

---

**1. Introduction (10 minutes)**
Computer vision has been a very popular field since the advent of digital systems. However computer vision on the edge devices such as Raspberry Pi is challenging due to resource contraints. Edge Computer Vision (ECV) has emerged as a transformative technology, with [Gartner](https://www.linkedin.com/pulse/what-edge-computer-vision-how-get-started-deep-block-net) recognizing it as one of the top emerging technologies of 2023. ECV offers several benefits such as 1) they can operate in real-time or near-real-time, providing instant insights and enabling immediate actions, 2) they offer enhanced privacy and security and 3) It reduces dependency on network connectivity or relaxes the bandwidth requirements as some processing will be done within. 
In this lab, few basic and advanced image processing tasks on edge devices is introduced. An overview of the experiments/setup is as follows:
![image](https://github.com/drfuzzi/INF2009_ImageAnalytics/assets/52023898/fc8cc7f0-ff75-4548-8dbe-889b2abface4)


**2. Setting up the Raspberry Pi (15 minutes)**
- Booting up the Raspberry Pi.
- Setting up Wi-Fi/Ethernet.
- System updates:
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
- Set up a [virtual environment](https://github.com/drfuzzi/INF2009_Setup) for this experiment (to avoid conflicts in libraries) using the details mentioned in Section 4.a
- Activate the virtual environment and complete the next steps within the environment

**3. Connecting and Testing the Web Camera (15 minutes)**
- Physically connecting the web camera to the Raspberry Pi.
- Installing necessary packages:
  ```bash
  sudo apt install fswebcam
  ```
- Capturing a test image:
  ```bash
  fswebcam image.jpg
  ```
- Observe the image (through VNC) in the current directory to ensure the image is correctly captured.

**4. Introduction to Real-time Image Processing with Python (25 minutes)**
- Installing OpenCV:
  ```bash
  pip install opencv-python  
  ```
- The [sample code](Codes/image_capture_display.py) shows the code to read frames from a webcam and then based on the intensity range for each colour channel (RGB), how to segment the image into red green and blue images.
- Expand the code to segment another colour (say yellow)

**5. Real-time Image Analysis (25 minutes)**
- Installing scikit-image:
  ```bash
  pip install scikit-image  
  ```
- Computer vision employs feature extraction from images. Some important image features include edges and textures. In this section we will employ a feature named histogram of gradients (HoG) which is widely employed for face recognition and other tasks. HoG involves gradient operation (basically extracting edges) on various image patches (by dividing the image into blocks). A [sample code](Codes/image_hog_feature.py) involving scikit-image is employed for the same. The code displays the dominant HoG image for each image patch overlaid on the actual image. It has to be noted that OpenCV can also be employed for the same task, but the visualization using scikit-image is better compared to that from OpenCV. A sample image and the colour segmentation is as shown below:
  ![image](https://github.com/drfuzzi/INF2009_ImageAnalytics/assets/52023898/fd7c115d-0301-40d2-b2c1-7966d4ce3fec)

- Note the usage of colour (RGB) to gray scale converion employed before HoG feature extraction.
- Run the code with and without resizing the image and observe the resultant frame rate. It is important to note that for edge computing, downsizing the image will speed up the compute and many such informed decisions are critical.
- Change the patch size in line 25 (feature.hog) and observe the changes in the results.

**6. Storing and Visualizing Results (20 minutes)**
- Saving processed images and videos.
- Displaying images with detected features using OpenCV's visualization tools.
- Introduction to more advanced analytics techniques, e.g., feature extraction, image classification.

---

**Homework/Extended Activities:**
1. Build a basic motion detection system using the web camera.
2. Explore more advanced OpenCV functionalities like SIFT, SURF, and ORB for feature detection.
3. Build a simple image classification system using pre-trained models.

---

**Resources:**
1. Raspberry Pi official documentation.
2. OpenCV documentation and tutorials.
3. Relevant Python libraries documentation for image processing.

---


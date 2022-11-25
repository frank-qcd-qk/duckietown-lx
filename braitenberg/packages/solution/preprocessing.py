import cv2
import numpy as np

# Change random with your own values! 

l_h = 171 # np.random.randint(0,255)
l_s = 140 # np.random.randint(0,255)
l_v = 100 # np.random.randint(0,255)

u_h = 179 # np.random.randint(0,255)
u_s = 200 # np.random.randint(0,255)
u_v = 255 # np.random.randint(0,255) 

l_array = [l_h, l_s, l_v]
u_array =[u_h, u_s, u_v]

lower_hsv = np.array(l_array)
upper_hsv = np.array(u_array)


def preprocess(image_rgb: np.ndarray) -> np.ndarray:
    """ Returns a 2D array """
    hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    #     masked = cv2.bitwise_and(image, image, mask=mask)
    return mask

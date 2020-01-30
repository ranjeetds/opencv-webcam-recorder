'''
    Script by :- Ranjeet Dhumal

    Hit ESC key to close the window and stop recording
'''
# Importing libraries
import cv2
import argparse, os

# Function to record and store frames in specified folder
def storeFrames(_path):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            break
        k = cv2.waitKey(1)

        # SPACE pressed
        img_name = _path + '/' + "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        # on hitting ESC key close frame
        if k%256 == 27:
            print("Escape entered, closing...")
            break

    cam.release()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help= 'add path to store images')
    args = parser.parse_args()
    _path = args.path
    if not os.path.exists(_path):
        os.makedirs(_path)
    storeFrames(_path)
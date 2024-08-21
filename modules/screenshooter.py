import pyautogui
import os
import cv2

def screenshoter(fileName):
    input('When Ready, Press Enter to take screenshot: ')
    screenshot = pyautogui.screenshot()
    
    screenshot.save(fr'../resources/{fileName}.png')
    
    print(f'Screenshot saved to {os.getcwd()}\\resources\\{fileName}.png')
    screenshot.show()

def webcam_capture():
    print('Capturing Start, Please Remove Webcam Physical shield...')
    #Open Connection tp webcam (0 is the default ID for the primary camera)
    capture = cv2.VideoCapture(0)
    
    #Check webcam open correctly
    if not capture.isOpened():
        print('Could not open camera')
        exit()
        
    #Read a frame from the webcam
    ret, frame = capture.read()
    
    #Check frame captured successfully
    if ret:
        #Write captured image to png file
        cv2.imwrite(r'../resources/webcam_capture.png', frame)
        print('Webcam Capture savedd to ../resources/webcam_capture.png')
    else:
        print('Failed to capture frame')
    
    #Release webcam
    capture.release()
    
    #display Captured image as frame
    cv2.imshow('Webcam Capture', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    try:
        while True:
            chooser = input(' Enter 1 to take screenshot,\n Enter 2 to capture webcam: \n Enter 99 to Exit \n')
            if chooser == '1':
                screenshoter('screenshot')
            elif chooser == '2':
                webcam_capture()
            elif chooser == '99':
                exit()
            else:
                print('Invalid Input')
            print(os.listdir(r'../resources'))
            
    except KeyboardInterrupt:
        print('Exiting... Goodbye & Goodluck Ninja 🥷👋👋')
        exit()
    except Exception as e:
        print(f'Error: {e}')
        exit()
if __name__ == '__main__':
    main()
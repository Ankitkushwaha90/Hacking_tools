import cv2

def main():
    # Open the first webcam connected to the computer
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Loop to continuously capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Check if the user pressed the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def task1(video_path, roi_params):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Crop the frame to focus on the ROI
        roi = frame[roi_params[1]:roi_params[1] + roi_params[3], roi_params[0]:roi_params[0] + roi_params[2]]

        # Perform any pre-processing if needed

        # Display the result
        cv2.namedWindow('Data Display Area', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Data Display Area', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Data Display Area', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Return the ROI for Task 2
    return roi

def task2(roi):
    # Function to extract numeric values using OCR
    def extract_numeric_values(image):
        # Perform any additional pre-processing if needed
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use pytesseract to perform OCR
        values = pytesseract.image_to_string(gray, config='--psm 8')

        return values

    # Apply OCR to extract numeric values
    numeric_values = extract_numeric_values(roi)

    # Print the result
    print('Extracted Numeric Values:', numeric_values)

# Define the region of interest (ROI) based on the monitor layout
# Adjust these values based on your monitor's design
roi_params = [100, 100, 500, 300]

# Call Task 1 and obtain ROI
video_path = 'C:\\Users\\Chinmay Mulgund\\Videos\\test.mp4'
roi_from_task1 = task1(video_path, roi_params)

# Call Task 2 with the obtained ROI
task2(roi_from_task1)

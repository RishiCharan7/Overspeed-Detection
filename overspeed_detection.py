import cv2
import time

def calculate_speed(distance, time):
    return distance / time

previous_frame_time = 0
previous_frame_location = None
speed_threshold = 25 
screenshot_count = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    if previous_frame_location is not None:
        current_frame_time = time.time()
        flow = cv2.calcOpticalFlowFarneback(previous_frame_location, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        speed = calculate_speed(cv2.mean(flow)[0], current_frame_time - previous_frame_time)

        if speed > speed_threshold:
            cv2.putText(frame, "Overspeeding", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            screenshot_count += 1
            screenshot_filename = f"screenshot_{screenshot_count}.png"
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved: {screenshot_filename}")

        previous_frame_time = current_frame_time
        previous_frame_location = gray.copy()
    else:
        previous_frame_time = time.time()
        previous_frame_location = gray.copy()

    cv2.imshow('Speed Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

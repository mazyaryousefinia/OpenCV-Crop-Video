import cv2
import numpy as np

pos = []
global pts1
def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))
        pos.append([x, y])
        print(pos)


def draw ():
    pts1 = np.float32([pos[0], pos[1], pos[2], pos[3]])
    pts2 = np.float32([[0, 0], [576, 0], [0, 704], [576, 704]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (576, 704))
    cv2.imshow("pres", result)


cap = cv2.VideoCapture('video.mp4')

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)
circles = []
#camera_matrix = np.eye(3, 3, 0, float, 'F')
#dist_coeffi = np.zeros((1,5), float, 'F')
camera_matrix = np.array([[594.42385933,  0, 278.82680292],
                           [ 0, 409.03779744, 364.68900831],
                            [ 0, 0, 1]], dtype='float64')
dist_coeffi = np.array([-0.21770742, 0.01302767, 0.00908937, 0.00659773, 0.04729608], dtype='float64')


while True:
    _, frame = cap.read()
    h, w = frame.shape[:2]
    frame = cv2.undistort(frame, camera_matrix, dist_coeffi, None, None)
    for center_position in circles:
        cv2.circle(frame, center_position, 5, (0, 0, 255), -1)

    cv2.imshow("Frame", frame)


    if len(pos) == 4:
        draw()

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circles = []

cap.release()
cv2.destroyAllWindows()
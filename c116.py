import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (100,210),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Venus",
            (200,210),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Earth",
            (300,210),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mars",
            (400,210),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Jupiter",
            (610,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Saturn",
            (730,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Uranus",
            (1000,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Neptunr",
            (1100,280),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.imshow("output",img)
key = cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
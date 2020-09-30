import numpy
import cv2

# create a black image
img = numpy.zeros((512, 512, 3), numpy.uint8)

# draw a green rectangle with thickness 2
img = cv2.rectangle(img, (20, 10), (490, 150), (0, 255, 0), 2)

# draw a skyblue filled circle on the left side of the rectangle
img = cv2.circle(img, (137, 80), 60, (255, 255, 0), -1)

# draw a skyblue filled circle on the right side of the rectangle
img = cv2.circle(img, (373, 80), 60, (255, 255, 0), -1)

# draw a blue horizontal line with thickness 2
img = cv2.line(img, (5, 180), (505, 180), (255, 0, 0), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Yara Elzahy', (140, 250), font, 1.3, (255, 255, 255), 2, cv2.LINE_AA)

# draw a blue horizontal line with thickness 2
img = cv2.line(img, (5, 300), (505, 300), (255, 0, 0), 2)

# draw a pink ellipse at the bottom of the page
img = cv2.ellipse(img, (255, 400), (150, 50), 0, 0, 360, (255, 0, 255), -1)


cv2.imshow('blank1', img)    # show image in window
cv2.imwrite('output_image.jpg', img)  # save image
cv2.waitKey(0)               # wait indefinitely for a key stroke
cv2.destroyAllWindows()      # destroy all windows we created

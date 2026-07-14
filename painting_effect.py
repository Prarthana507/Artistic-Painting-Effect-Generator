import cv2
import numpy as np
# Read image
img = cv2.imread("flower.jpg")
if img is None:
    print("Error: Image not found!")
    exit()
# Resize image
img = cv2.resize(img, (600, 600))
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Histogram Equalization
equalized = cv2.equalizeHist(gray)
# Apply Bilateral Filter
smooth = cv2.bilateralFilter(img, 9, 75, 75)
# Detect edges
edges = cv2.Canny(equalized, 80, 150)
# Dilate edges
kernel = np.ones((2, 2), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
# Invert edges
edges = cv2.bitwise_not(edges)
# Convert edges to 3-channel image
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
# Create painting effect
painting = cv2.bitwise_and(smooth, edges)
# Save output
cv2.imwrite("output/painting.jpg", painting)
# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Painting Effect", painting)
cv2.waitKey(0)
cv2.destroyAllWindows()

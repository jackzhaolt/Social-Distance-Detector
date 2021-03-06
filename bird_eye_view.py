import numpy as np
import cv2
import matplotlib.pyplot as plt


# This will return the 4 corner points of the region that will be transformed into bird eye view
def get_corner_points():
    corner_pts = np.zeros((4, 2), dtype='float32')
    corner_pts[0] = [91, 163]  # top-left corner
    corner_pts[1] = [241, 163]  # top-right corner
    corner_pts[2] = [322, 265]  # bottom-right corner
    corner_pts[3] = [98, 266]  # bottom-left corner

    return corner_pts


def four_point_transform(image):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = get_corner_points()
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordinates or the top-right and top-left x-coordinates
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(width_a), int(width_b))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(height_a), int(height_b))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    maxl = max(max_width, max_height)

    dst = np.array([
        [0, 0],
        [290 - 1, 0],
        [290 - 1, 1085 - 1],
        [0, 1085 - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    H = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, H, (290, 1085))
    # return the warped image and the transformation matrix

    image2 = cv2.polylines(image, [np.int32(rect)], True, 255, 3, cv2.LINE_AA)
    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(image2)
    axarr[1].imshow(warped)
    axarr[0].axis('off')
    axarr[1].axis('off')
    plt.show()

    return warped, H


if __name__ == '__main__':
    img = cv2.imread('../input/ThreePastShop1cor/ThreePastShaoplcor0027.jpg')
    # img = cv2.imread('./hello.jpg')
    warped, H = four_point_transform(img)


    # plt.imshow(img)

    f, axarr = plt.subplots(1, 2)
    axarr[0].imshow(img)
    axarr[1].imshow(warped)

    plt.show()

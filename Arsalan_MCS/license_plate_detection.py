import cv2
import imutils
import pytesseract
import numpy as np
import PIL
from PIL import Image , ImageDraw , ImageFont


def main_function(image_name : str,detection_method):

    image = cv2.imread(image_name)


    image,pre_processed_image = pre_processing(image=image,image_name=image_name)

    license_plate_image = image
    try:

        if detection_method == "HAAR Cascade":

            bounding_box_image, license_plate_coordinates, \
            license_plate_image = Haar_casscade_licensePlate_detection(original_image=image,
                                                                       pre_processed_image=pre_processed_image)

            pass

        if detection_method == "Contour boundaries based segmentation":

            bounding_box_image, license_plate_coordinates, \
            license_plate_image = contour_based_licensePlate_detection(original_image=image,
                                                                       pre_processed_image=pre_processed_image)

            pass


        x, y, w, h = license_plate_coordinates
        pass

    except:

        h = 0

        pass





    text = "None"



    if h > 0:

        license_plate_points = x, y, w, h
        text = license_plate_recognition(source_image=bounding_box_image,license_plate_image=license_plate_image,license_plate_points=license_plate_points)
        pass


    return text, license_plate_image

    pass


###################################################



def pre_processing(image,image_name):

    # Image resizing

    """
        scale_percent = 70 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        #thresh , image = cv2.threshold(image,150,250,cv2.THRESH_BINARY_INV,None)

        image = cv2.resize(image,dim)

        """

    """if image.shape[1] < 500:

            pass"""

    if "car4.jpg" in image_name:

        pass

    else:

        image = imutils.resize(image, width=500)

        pass

    # converting image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # applying smooth filter

    gray = cv2.bilateralFilter(gray, 11, 17, 17)


    return image,gray

    pass


###################################################

#                                   METHOD 1

def Haar_casscade_licensePlate_detection(original_image,pre_processed_image):

    path = "haarcascade_russian_plate_number.xml"
    Haar_cascade_classifier = cv2.CascadeClassifier(path)

    license_plate = Haar_cascade_classifier.detectMultiScale(pre_processed_image,1.1,4)

    license_plate = sorted(license_plate,key= lambda a:a[2])

    bounding_box_image = original_image.copy()




    for (x, y, w, h) in license_plate:


        wT, hT, cT = original_image.shape
        a, b = (int(0.02 * wT), int(0.02 * hT))
        plate = original_image[y + a:y + h - a, x + b:x + w - b, :]

        #Image pre processing


        cv2.rectangle(bounding_box_image, (x + b, y + a), (x + w - b, y + h - a), (51, 51, 255), 2)
        #cv2.rectangle(bounding_box_image, (x - 1, y - 40), (x + w + 1, y), (51, 51, 255), -1)
        pass

    license_plate_coordinates = [x, y, w, h]

    license_plate_image = plate

    return bounding_box_image,license_plate_coordinates,license_plate_image
    pass



###################################################


#                                  METHOD 2

def contour_based_licensePlate_detection(original_image,pre_processed_image):


    image = original_image


    # Computing edges

    edged = cv2.Canny(pre_processed_image, 30, 200)


    # Using Edges computing contours


    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    image1 = image.copy()


    # Drawing contours to the orignal image

    cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)


    # Selecting only 30 contours after sorting

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

    LicensePlateCount = None

    image2 = image.copy()


    # Drawing 30 contours on orignal image

    cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)

    count = 0
    name = 1

    h = 0

    # Detecting close polygon with square shape (BOX)

    for i in cnts:

        perimeter = cv2.arcLength(i, True)

        approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)

        if (len(approx) == 4):
            LicensePlateCount = approx

            x, y, w, h = cv2.boundingRect(i)

            crop_image = image[y:y + h, x:x + w]

            new_crop_image = crop_image.copy()

            name = name + 1

            break
            pass

        pass

    image4 = image.copy()

    try:

        cv2.drawContours(image4, [LicensePlateCount], -1, (0, 255, 0), 3)

    except:

        pass

    bounding_box_image = image4

    license_plate_coordinates = [x,y,w,h]

    license_plate_image = new_crop_image

    return bounding_box_image,license_plate_coordinates,license_plate_image
    pass


###################################################



###################################################



def license_plate_recognition(source_image, license_plate_image, license_plate_points):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    x,y,w,h = license_plate_points


    image4 = source_image

    license_plate_image = cv2.resize(license_plate_image,(140,40))


    license_plate_image = np.invert(license_plate_image)

    license_plate_image = cv2.GaussianBlur(license_plate_image,(1,1),5)



    car_image = image4

    copy_image = car_image.copy()


    pil_image = Image.fromarray(cv2.cvtColor(copy_image, cv2.COLOR_BGR2RGB))

    title_font = ImageFont.truetype('arial.ttf', 20)

    editable_image = ImageDraw.Draw(pil_image)

    text = pytesseract.image_to_string(license_plate_image, lang='eng')

    try:

        """editable_image.text(((x + w) / 2, (y + h) / 2), text=text, fill=(255, 0, 0), stroke_fill=(255, 255, 255),
                            stroke_width=1, font=title_font)"""

        editable_image.text((x + ((x+w)/5), y + h), text=text, fill=(255, 0, 0), stroke_fill=(255, 255, 255),
                            stroke_width=1, font=title_font)

    except:

        pass


    final_image = np.array(pil_image)


    return text
    pass




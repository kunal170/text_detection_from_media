#importing all libraries of use
import cv2
import pytesseract



pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\tesseract.exe'

print("The choices for grabbing text are:")
print("1) Detecting character from an image")
print("2) Detecting word from an image")
print("3 Detecting a digit from an image")
print("4) Detecting a text from video")
print("5) Detecting a text from webcam")

choice=int(input("Enter the choice: "))

if choice==1:
    img = cv2.imread('test1.jpeg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


 # Detecting Characters

    img_hgt, img_wdt, _ = img.shape
    boxes = pytesseract.image_to_boxes(img)

    print(pytesseract.image_to_string(img))

    for line in boxes.splitlines():
      line = line.split()
      x, y, w, h = int(line[1]), int(line[2]), int(line[3]), int(line[4])
      cv2.rectangle(img, (x, img_hgt - y), (w, img_hgt - h), (50, 50, 255), 2)
      cv2.putText(img, line[0], (x, img_hgt - y + 25), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)


    cv2.imshow('img', img)
    cv2.waitKey(0)


#  detecting words
elif choice==2:
    img1 = cv2.imread('test2.jpeg')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img_hgt, img_wdt, _ = img1.shape
    boxes = pytesseract.image_to_data(img1)
    print(boxes)
    for count, line in enumerate(boxes.splitlines()):
      if count != 0:
          line = line.split()
          #print(line)
          if len(line) == 12:
              x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
              cv2.rectangle(img1, (x, y), (x + w, y + h), (50, 50, 255), 1)
              cv2.putText(img1, line[11], (x, y), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
              print(line[11],end =" ")

    cv2.imshow('img', img1)
    cv2.waitKey(0)


#  detecting digits
if choice==3:
    img2 = cv2.imread('test.jpeg')
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img_hgt, img_wdt, _ = img2.shape
    conf = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_boxes(img2, config=conf)
    for line in boxes.splitlines():
      line = line.split(' ')
      x, y, w, h = int(line[1]), int(line[2]), int(line[3]), int(line[4])
      cv2.rectangle(img2, (x, img_hgt - y), (w, img_hgt-h), (50, 50, 255), 1)
      cv2.putText(img2, line[0], (x, img_hgt-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 1)

    cv2.imshow('only_digits', img2)
    cv2.waitKey(0)


#  for the video section
elif choice==4:
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture('check.mp4')
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    while True:
      scs, img = cap.read()   #img = video frame capture
      #DETECTING CHARACTERES
      img_hgt, img_wdt, _ = img.shape
      boxes = pytesseract.image_to_boxes(img)
      for line in boxes.splitlines():
          line = line.split(' ')
          x, y, w, h = int(line[1]), int(line[2]), int(line[3]), int(line[4])
          cv2.rectangle(img, (x, img_hgt-y), (w, img_hgt- h), (255, 0, 0), 2)
          cv2.putText(img, line[0], (x, img_hgt-y+25), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
      cv2.imshow("Result", img)
      if cv2.waitKey(20) & 0xFF==ord('x'):
          break
      cv2.waitKey(10)


#  for the webcam section
elif choice==5:
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
     scs, img = cap.read()   #img = video frame capture
     #DETECTING CHARACTERES
     img_hgt, img_wdt, _ = img.shape
     boxes = pytesseract.image_to_boxes(img)
     for line in boxes.splitlines():
         line = line.split(' ')
         x, y, w, h = int(line[1]), int(line[2]), int(line[3]), int(line[4])
         cv2.rectangle(img, (x, img_hgt-y), (w, img_hgt- h), (255, 0, 0), 2)
         cv2.putText(img, line[0], (x, img_hgt-y+25), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
     cv2.imshow("Result", img)
     cv2.waitKey(1)
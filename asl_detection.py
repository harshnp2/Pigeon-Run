# libraries
from roboflow import Roboflow
import cv2 as cv
import random


rf = Roboflow(api_key="kQE5W7nH700WcHLhL9TN")
project = rf.workspace().project("american-sign-language-letters")
model = project.version(6).model

cam = cv.VideoCapture(0)


def detect_letter(letters_assigned, gone_through, pos_state, moving, playerY, time):
    font = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (50, 400)
    fontScale = 0.5
    fontColor = (255, 255, 255)
    thickness = 2
    lineType = 2

    time_left_coordinates = (10, 10)
    for i in range(0, time):
        isTrue, frame = cam.read()

        cv.imwrite("frame.jpg", frame)
        cv.imread('frame.jpg')

        # check how much time is left
        time_left = (time-1) - i
        time_left_text = str(f'{time_left} seconds left')

        # infer on a local image
        prediction = model.predict("frame.jpg", confidence=40, overlap=30).json()

        model.predict("frame.jpg", confidence=40, overlap=30).save("prediction.jpg")

        image = cv.imread("prediction.jpg")
        value = prediction.get('predictions')

        if playerY <= 33:
            moving = 'down'
            text = f'Sign {letters_assigned[0]} to move {moving}'
            pos_state = 1

        elif playerY >= 450:
            moving = 'up'
            text = f'Sign {letters_assigned[0]} to move {moving}'
            pos_state = 1

        elif 33 < playerY < 450:
            text = f'Sign {letters_assigned[0]} to move down OR sign {letters_assigned[1]} to move up'
            pos_state = 2

        cv.putText(image, text,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)

        cv.putText(image, time_left_text,
                   time_left_coordinates,
                   font,
                   fontScale,
                   fontColor,
                   thickness,
                   lineType)

        cv.imshow('hand sign', image)
        cv.resizeWindow('hand sign', 450, 450)



        if not value:
            letter = ""
            gone_through = True
        else:
            list_zero = value[0]
            letter = list_zero.get('class')
            if pos_state == 1:
                if letter == letters_assigned[0]:
                    once = True
                    gone_through = False
                    return letter, letters_assigned, gone_through, moving
                    break

            elif pos_state == 2:
                if letter == letters_assigned[0]:
                    moving = 'down'
                    once = True
                    gone_through = False
                    return letter, letters_assigned, gone_through, moving
                    break

                if letter == letters_assigned[1]:
                    moving = 'up'
                    once = True
                    gone_through = False
                    return letter, letters_assigned, gone_through, moving
                    break

        print(i)
        cv.waitKey(1)

    return letter, letters_assigned, gone_through, moving



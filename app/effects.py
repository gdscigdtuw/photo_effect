import cv2

class effects_lib (object):

    ds_factor = 0.8

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()


    def oil_painting(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def watercolor(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def cooling_effect(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def warming_effect(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def edge_detection(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def cartoonize(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def coloured_sketch(self):
        frame_status, frame = self.video.read()
        #modify frame here


        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def black_and_white_sketch(self):
        frame_status, frame = self.video.read()
        #modify frame here
        
        frame = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

import cv2
num_down = 2       # number of downsampling steps
num_bilateral = 7  # number of bilateral filtering steps

class effects_lib (object):

    ds_factor = 0.8
    
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
   
    def get_frame(self):
        frame_status , frame = self.video.read()
        ret , jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes() 

    def oil_painting(self):
        frame_status, frame = self.video.read()
        #modify frame here
        frame = cv2.xphoto.oilPainting(frame, 7, 1)
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
        blur=cv2.gaussianBlur(frame,(5,5),0)
        edges=cv2.Canny(blur,100,200)
        cv2.imshow("canny detection",edges)

            
 
        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()

    def cartoonize(self):
        frame_status, frame = self.video.read()
        #modify frame here
        img_color =  frame
        # downsample image using Gaussian pyramid
        for _ in range(num_down):
            img_color = cv2.pyrDown(img_color)
        # repeatedly apply small bilateral filter instead of
        # applying one large filter
        for _ in range(num_bilateral):
            img_color = cv2.bilateralFilter(img_color, d=9,sigmaColor=9,sigmaSpace=7)
        # upsample image to original size
        for _ in range(num_down):
            img_color = cv2.pyrUp(img_color)

        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)

        # detect and enhance edges
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY,
                                        blockSize=9,
                                        C=2)
                            
        # convert back to color, bit-AND with color image
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
        frame = cv2.bitwise_and(img_color, img_edge)
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
        
        frame, color_sketch = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

        frame = cv2.resize(frame,None, fx = self.ds_factor, fy = self.ds_factor, interpolation = cv2.INTER_AREA)
        ret, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
    

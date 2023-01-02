import cv2 as cv2

class ImageProcessing:

    def __init__(self, image_path, setup_dto):
        self._image = cv2.imread(image_path)
        self.__max_threshold = setup_dto.max_threshold
        self.__min_threshold = setup_dto.min_threshold 
        self.__max_canny = setup_dto.max_canny
        self.__min_canny = setup_dto.min_canny
        self._contour, self._image_copy = self._image_preparation()

    def _fixColor(self, image):
        return(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    def _treshold_image(self):
        ret, th = cv2.threshold(self._image, self.__min_threshold, self.__max_threshold , cv2.THRESH_BINARY)
        return th

    def _canny_image(self, th):
        blurred = cv2.GaussianBlur(th, (5, 5), 0)
        canny = cv2.Canny(blurred, self.__min_canny, self.__max_canny)
        return canny

    def set_new_setup(self, setup_dto):
        self.__max_threshold = setup_dto.max_threshold
        self.__min_threshold = setup_dto.min_threshold
        self.__max_canny = setup_dto.max_canny
        self.__min_canny = setup_dto.min_canny
        self._image, self._cnt, self._coins = self._image_preparation()

    def _image_preparation(self):  
        th = self._treshold_image()
        canny = self._canny_image(th)
        (cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        coins = self._image.copy()
        cnt = cnts[-1]
        for data in cnts:
            if data.sum() > cnt.sum():
                cnt = data
        return cnt, coins

    def get_processed_image(self):
        return self._image, self._contour, self._image_copy
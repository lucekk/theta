import math

class ThetaCalulcator:

    @staticmethod
    def calculate_angle(right_point, central_point, left_point):
        return math.degrees(math.atan2(right_point[1]-central_point[1], right_point[0]-central_point[0]) - math.atan2(left_point[1]-central_point[1], left_point[0]-central_point[0]))

    @staticmethod
    def rotate(origin, point, angle):
        angle = math.radians(angle)
        ox, oy = origin
        px, py = point
        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return int(qx), int(qy)
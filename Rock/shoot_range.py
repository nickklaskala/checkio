#!/usr/bin/env checkio --domain=py run shoot-range

# On a shooting range, shooters use a wall to practice, trying to hit it from various positions.    Shooters do not have problems with with vertical deviation,    so we can use a simplified model for this mission.    We placed a camera above the shooting range and    useCartesian coordinatesto describe states.    We know coordinates of wall (target) ends and shooting point.    And we know the point where is a bullet after a small time.    You should determine the result of the shot.
# 
# You are given coordinates for the end-points of the target wall on a grid.    In addition, you have two points describing the shot: A starting point where the bullet was fired,    and a second point indicating the location of the bullet after a specified length of time.    You should calculate the result of the shot, specifically if a bullet hit the wall in the center,    then it's 100 points. Awarded points reduce in relation to the distance from the center.    An impact on the end of the wall is 0 points and a missed shot deducts a point (-1).    The result should berounded to the nearest integer.
# 
# 
# 
# Input:Four arguments. Two wall ends, a firing point and a later point as tuples of two numbers.
# 
# Output:The results as an integer from -1 to 100.
# 
# Preconditions:
# all(all(0 < i < 100 for i in coor) for coor in args)
# wall1, wall2 and shot_point are not collinear.
# 
# 
# END_DESC

import collections
import math


class Point(collections.namedtuple('Point', ['x', 'y'])):

    def __neg__(self):
        return Point(-self.x, -self.y)


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


    def __mul__(self, scale):
        return Point(self.x * scale, self.y * scale)


    def __truediv__(self, scale):
        return Point(self.x / scale, self.y / scale)


    def distTo(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


    @staticmethod
    def crossProduct(p1, p2, p3):
        del1 = p2 - p1
        del2 = p3 - p2
        return del1.x * del2.y - del1.y * del2.x


class LineSegment:
    ''' implements line segment intersection algorithm as described at
    https://www.topcoder.com/community/data-science/data-science-tutorials/geometry-concepts-line-intersection-and-its-applications/
    '''

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.a = p2.y - p1.y
        self.b = p1.x - p2.x
        self.c = self.a * p1.x + self.b * p1.y


    def pointWithinBoundingBox(self, point):
        xs = [self.p1.x, self.p2.x]
        ys = [self.p1.y, self.p2.y]
        return (min(xs) <= point.x <= max(xs) and min(ys) <= point.y <= max(ys))


    def containsPoint(self, point):
        return (Point.crossProduct(self.p1, self.p2, point) == 0
            and self.pointWithinBoundingBox(point))


    def getIntersection(self, other):
        determinant = self.a * other.b - other.a * self.b

        if determinant == 0:
            return None
        else:
            lineIntersection = Point(
                (other.b * self.c - self.b * other.c) / determinant,
                (self.a * other.c - other.a * self.c) / determinant)

            intersectionIsOnBothSegments = (
                self.pointWithinBoundingBox(lineIntersection)
                and other.pointWithinBoundingBox(lineIntersection))

            if intersectionIsOnBothSegments:
                return lineIntersection

            return None


def shot(wall1, wall2, shotStart, shotLater):
    wall1 = Point(*wall1)
    wall2 = Point(*wall2)
    shotStart = Point(*shotStart)
    shotLater = Point(*shotLater)

    # make safe end of shot segment such that it is more than enough
    # to hit the wall
    laterDist = shotStart.distTo(shotLater)
    maxWallDist = max(shotStart.distTo(wall1), shotStart.distTo(wall2))
    safetyScaler = 2 * maxWallDist / laterDist
    shotEnd = shotStart + (shotLater - shotStart) * safetyScaler

    wallSegment = LineSegment(Point(*wall1), Point(*wall2))
    shotSegment = LineSegment(shotStart, shotEnd)

    intersection = wallSegment.getIntersection(shotSegment)

    if not intersection:
        return -1

    wallCenter = (wall1 + wall2) / 2
    wallHalfLen = wallCenter.distTo(wall2)

    score = 100 * (1 - intersection.distTo(wallCenter) / wallHalfLen)

    roundedScore = round(score)
    return roundedScore








if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
	assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
	assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
	assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
	assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
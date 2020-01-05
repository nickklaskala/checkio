#!/usr/bin/env checkio --domain=py run four-to-the-floor

# body .page__container #main__container {    background-color: black;    color: white;}body .page__container #main__container a{    color: white}body .page__container #main__container .main-container__missions__title .missions-title__name {    color: black;    background-color: white;}body .page__container #main__container .solve_it_panel .btn {    background-color: #5ae4aa;}body .page__container #main__container .solve_it_panel .btn.disabled {    background-color: #808080;}body .page__container #main__container .mission-content__metainfo a {    color: #009c70;}body .content-controls-tags ul li .main-tag {    background-color: #474747;}body .page__container #main__container .content-controls label {    color: white;}body .page__container #main__container .main-container__missions__content .missions-content__description__status div {    display: none;}The mission was created with the support ofAjax company
# 
# In 2011, Ajax Systems was just an ambitious idea. Today, our security systems are being sold in 90 countries and protect more than 350 thousand people. Over the past 3 years, the company has become 30 times larger and has already sold more than two million devices. Each of them is designed, manufactured and tested in Kiev.
# 
# Ajax, as a system, is not just a set of sensors, but also beautiful and user-friendly applications that help users configure the system and manage their security. We are looking for a Python Developer to join the team that is currently working on Ajax PRO Desktop. Out tech stack consists of: Python 3, pyside2, QML, asyncio.Want to know more?
# 
# Why don't we talk about thePIR sensors(passive infrared sensors) systems?
# Let's talk about them and then solve a thematic mission.
# 
# If there's a need for motion detection, we have various options at our disposal, all based on the general principle of tracking environmental change.    Narrowing the concept of "motion detection" down to the concept of "human detection", it becomes obvious that one of the most convenient way to detect    a human presence (entrance) is to keep tracking constantly a certain distinctive environmental characteristic that is attributable for a human as well as for any other possible object.    And this kind of a characteristic really exists. Everything in the world emitsthermal radiation. The    radiation density depends on the temperature of the object and its surface area. And here I must add that infrared light is nothing but thermal radiation.    Although this radiation is not visible to the human eye, it is quite intense.    You can feel it if place your palm near (not onto!) a hot object, a cup of coffee for example.
# 
# 
# 
# 
# Knowing mentioned above, it's quite easy to realize how PIR sensor systems operate, right?    Imagine a locked room and a sensor "looking" down from the ceiling (or look at the schema below). Remember that everything emits thermal radiation, so    our sensor will register a conventionally constant level of the background thermal emission, so called thermal imprint.    In order a PIR sensor system won't be triggered by a pet, the maintainers of such a system increase its sensitivity threshold.    That threshold isn't that high though, especially taking into account the human body that emits ~1kW of thermal radiation.    So when a man enters a sensor's field of view, the sensor detects significantly increased level of thermal radiation    and triggers either a security system which notifies the owner or a lighting system which turns on the lights.
# 
# 
# 
# 
# 
# And now, finally, the mission's objective. Given a room's size and a list of PIR sensors mounted on the room's ceiling and looking down on the floor,    your task is to determine whether the floor area is completely into the sensors coverage area (return True) or not (return False). The bottom left corner of the rectangle matches the origin pointO,    the top right corner is defined byWandH. Each sensor is defined by its mounting point (coordinatesxiandyi) and its range (Ri).
# 
# Input:Two arguments:the first is a list containing a room's top right corner coordinates,all are integers [W, H]the second is a list containing sensors info, all are integers            [[xi, yi, Ri],            [xi+1, yi+1, Ri+1],            .....,            [xn, yn, Rn]]
# 
# Output:True or False.
# 
# 
# 
# Precondition:
# All given values are integers.if (int - 10e-6<f<int + 10e-6) then (f == int)H ∈ (0; 1000]W ∈ [H; 4*H]xi∈ [0; W]yi∈ [0; H]Ri∈ (0; 1600]n ∈ [1; 10]
# 
# 
# END_DESC

def is_covered(room, sensors):
    # your code here
    return True


if __name__ == '__main__':
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
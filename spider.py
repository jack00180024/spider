#coding:utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By



search_keyword = "dota2"

def printEx(str):
    print(str.encode("utf-8"))

def collectWeatherInfo(webDriver):
    webDriver.get("http://www.weather.com.cn/weather1d/101200101.shtml")
    WebDriverWait(webDriver, 10).until(EC.visibility_of_element_located((By.ID, "today")))
    
    curTemp = webDriver.find_element_by_xpath("//div[@id='today']/div[@class='t']/div[@class='sk']/div[@class='tem']/span").text
    
    dayTemp = webDriver.find_element_by_xpath("//div[@id='today']/div[@class='t']/ul[@class='clearfix']/li[1]/p[@class='tem']/span").text
    nightTemp = webDriver.find_element_by_xpath("//div[@id='today']/div[@class='t']/ul[@class='clearfix']/li[2]/p[@class='tem']/span").text
    
    sunUp = webDriver.find_element_by_xpath("//div[@id='today']/div[@class='t']/ul[@class='clearfix']/li[1]/p[@class='sun sunUp']/span").text
    
    sunDown = webDriver.find_element_by_xpath("//div[@id='today']/div[@class='t']/ul[@class='clearfix']/li[2]/p[@class='sun sunDown']/span").text
    
    return [curTemp, dayTemp, nightTemp, sunUp, sunDown]
    # printEx("current temp is %s; high temp is %s; low temp is %s; sun rise at %s; sun down at %s"%(curTemp, dayTemp, nightTemp, sunUp, sunDown))

def collectClockInfo():
    return datetime.cu
    
def collectBusInfo(webDriver):
    pass
 
import os
import time
print('cls')
os.system('cls')
time.sleep(3)


def refresh():
    weather = collectWeatherInfo(driver)
    os.system('cls')
    printEx("current temp is %s; high temp is %s; low temp is %s; sun rise at %s; sun down at %s"%(weather[0], weather[1], weather[2], weather[3], weather[4]))
    return 0
if 1: 
    # Create a new instance of the Firefox driver
    driver = webdriver.PhantomJS()

    # go to the google home page
    driver.get("https://www.baidu.com/")

    # the page is ajaxy so the title is originally this:
    # print(type(driver.title))
    # import chardet
    # print chardet.detect(driver.title)
    # print driver.title.encode("utf-8")
    driver.get_screenshot_as_file("%s.png"%driver.title)



    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_id("kw")

    # type in the search
    inputElement.send_keys(search_keyword.decode("utf-8"))
    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "nums_text")))
    # import time
    # time.sleep(3)

    # confirmButton = driver.find_element_by_id("su")
    # confirmButton.click()


    driver.get_screenshot_as_file("keyword.png")

    try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            WebDriverWait(driver, 10).until(EC.title_contains(search_keyword.decode("utf-8")))

            # You should see "cheese! - Google Search"
            # print driver.title.encode("utf-8")
            
            
            driver.get_screenshot_as_file("search result.png")
            while True:
                refresh()
                time.sleep(15)
            
    finally:
            driver.quit()
        
        
        

import turtle
from datetime import *
 
 
# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()
 
 
def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    turtle.reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    turtle.end_poly()
    # 返回最后记录的多边形。
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)
 
 
def Init():
    global secHand, minHand, hurHand, printer
    # 重置Turtle指向北
    turtle.mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
 
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
 
        # 建立输出文字Turtle
    printer = turtle.Turtle()
 
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()
 
 
def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    turtle.pencolor("#ff5500")
    turtle.fillcolor("green")
 
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)
 
            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)
 
 
def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s-%d-%d" % (y, m, d)
 
 
def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
 
    turtle.tracer(False)
 
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)
 
    # 100ms后继续调用tick
    turtle.ontimer(Tick, 100)
 
 
def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()
 
if 0: 
    if __name__ == "__main__":
        main()
        
        
def mygoto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down();


def drawwjx(x):
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(x)
        turtle.right(144)
    turtle.end_fill()

    
if 0:

    turtle.setup(600, 400, 0, 0)
    turtle.color("yellow")
    turtle.bgcolor("red")
    turtle.fillcolor("yellow")


    mygoto(-250, 75)
    drawwjx(100)

    mygoto(-120,130)
    drawwjx(30)

    mygoto(-100,100)
    drawwjx(30)

    mygoto(-100,70)
    drawwjx(30)

    mygoto(-120,40)
    drawwjx(30)

    mygoto(0, 0)
    


import os
import webbrowser
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def webop(prompt, copied):
    if prompt == "cite this":
        print("Last reference copied to clipboard")
        driver = webdriver.Chrome()
        driver.get("https://www.citethisforme.com/cite/website")
        elem = driver.find_element_by_name("autociteUrl")
        elem.clear()
        elem.send_keys(copied)


def made(filefound):
    if filefound:
        ref = input("reference:")
        while (ref != "Done"):
            file = open("Masters reference.txt")
            sNum = file.readlines()[-1]
            result = sNum.index(']')
            sNum = sNum[1:(result)]
            iNum = int(sNum)
            iNum = iNum + 1
            file = open("Masters reference.txt", "a+")
            sNum = str(iNum)
            if ref != 'cite this':
                file.write(ref + "\n[" + str(iNum) + "]")
                copied = ref
                file.close()
                ref = input("reference [" + sNum + "]:")
            else:
                sNum = str(iNum - 1)
                ref = input("reference [" + sNum + "]:")
            webop(ref, copied)
    else:
        print("Error with file")


def startup():
    if os.path.isfile("Masters reference.txt"):
        made(1)
    else:
        file = open("Masters reference.txt", "w+")
        file.write("References:\n[1]")
        file.close()
        made(os.path.isfile("Masters reference.txt"))


if __name__ == '__main__':
    startup()

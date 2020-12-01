from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def addTradinglogComments():
    # 스티커 박스 클릭
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()')
    time.sleep(1)
    # 스티커 선택
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(6) > button").click()')
    time.sleep(1)
    # 등록 클릭
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
    time.sleep(2)


def addNewsComments():
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()')
    time.sleep(1)
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(5) > button").click()')
    time.sleep(1)
    driver.execute_script(
        'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
    time.sleep(2)

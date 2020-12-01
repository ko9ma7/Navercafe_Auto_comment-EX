from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def addTradinglogComments(i):
    # 페이지 상단글부터 클릭
    driver.execute_script(
        f'document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_article > div.board-list > div > a").click()')
    time.sleep(2)
    # 좋아요 값 확인
    like = driver.execute_script(
        "return document.querySelector('#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a').getAttribute('aria-pressed')")
    # 좋아요가 눌러져있으면 종료.
    if like == 'true':
        driver.quit()
    else:
        # 좋아요 클릭
        driver.execute_script(
            'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a > span").click()')
        time.sleep(1)
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
        # 새로고침해서 밖으로 빠져나가기
        driver.refresh()
        time.sleep(3)


def addNewsComments(i):
    driver.execute_script(
        f'document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_article > div.board-list > div > a").click()')
    time.sleep(2)
    like = driver.execute_script(
        "return document.querySelector('#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a').getAttribute('aria-pressed')")
    if like == 'true':
        driver.quit()
    else:
        driver.execute_script(
            'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a > span").click()')
        time.sleep(1)
        driver.execute_script(
            'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()')
        time.sleep(1)
        driver.execute_script(
            'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(5) > button").click()')
        time.sleep(1)
        driver.execute_script(
            'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
        time.sleep(2)
        driver.refresh()
        time.sleep(3)


def addJoinus(i):
    # 본인 닉네임
    getYournickname = driver.execute_script(
        'return document.querySelector("#gnb_name1").innerText')
    driver.switch_to_frame("cafe_main")
    # 작성자 등급확인
    getRating = driver.execute_script(
        f'return document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_name > div > table > tbody > tr > td > span > img").src')
    # 등급 1 확인
    if getRating == "https://cafe.pstatic.net/levelicon/1/1_110.gif":
        driver.execute_script(
            f'document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_article > div.board-list > div > a").click()')
        time.sleep(2)
        # 댓글 작성자 리스트
        setAuthorList = driver.find_elements_by_css_selector(
            ".comment_nickname")

        for x in setAuthorList:
            if x == getYournickname:
                driver.execute_script(
                    'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()')
                time.sleep(1)
                driver.execute_script(
                    'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(12) > button").click()')
                time.sleep(1)
                driver.execute_script(
                    'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
                time.sleep(2)
                driver.refresh()
                time.sleep(3)
            else:
                continue
    else:
        driver.refresh()
        time.sleep(1)

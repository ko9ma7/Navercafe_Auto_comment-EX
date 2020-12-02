from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from tkinter import ttk
from passlist import *
import time
import pyperclip

# 로그인 창
win = Tk()
win.geometry('200x150')
win.title('Login')

# ID 입력창
idLabel = Label(win, text="ID")
idLabel.pack()
idEntry = Entry(win)
idEntry.pack()

# password 입력
pwLabel = Label(win, text="Password")
pwLabel.pack()
pwEntry = Entry(win, show='*')
pwEntry.pack()

# 게시판 선택
comboExample = ttk.Combobox(win,
                            values=[
                                "매매일지",
                                "뉴스",
                                "모바일수익",
                                "가입인사"])
comboExample.current(1)
comboExample.pack()


def login():
    # 네이버 로그인 열기
    driver = webdriver.Chrome()
    driver.get('https://nid.naver.com/nidlogin.login')

    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    pyperclip.copy(idEntry.get())
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    pyperclip.copy(pwEntry.get())
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

    # 슬립을 꼭 넣어줘야 한다.
    # 그렇지 않으면 로그인 끝나기도 전에 다음 명령어가 실행되어 제대로 작동하지 않는다.
    time.sleep(3)

    # 게시판 (189 매매일지, 940 모바일수익, 195 뉴스, 74 가입인사)
    if comboExample.get() == "매매일지":
        board = 189
    elif comboExample.get() == "뉴스":
        board = 195
    elif comboExample.get() == "모바일수익":
        board = 940
    elif comboExample.get() == "가입인사":
        board = 74

    # 게시글 페이지 1번부터 확인(1페이지에 15개씩 default는 총 195개까지)
    for j in range(1, 14):
        driver.get(
            f'https://cafe.naver.com/stockschart?iframe_url=/ArticleList.nhn%3Fsearch.clubid=11974608%26search.menuid={board}%26search.boardtype=L%26search.totalCount=151%26search.page={j}')
        time.sleep(2)

        # 첫글부터 클릭. 좋아요 눌러져있으면 아래는 이미 다 달았던 글이므로 프로그램 종료
        for i in range(1, 16):
            # 본문은 iframe으로 이뤄져있다. 들어가기.
            driver.switch_to_frame("cafe_main")
            # 작성자 확인
            nickname = driver.execute_script(
                f'return document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_name > div > table > tbody > tr > td > a").innerText')
            # passlist와 비교
            if nickname not in passlist:
                # 좋아요 없는 게시판
                if board == 74:
                    # 작성자 등급확인
                    getRating = driver.execute_script(
                        f'return document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_name > div > table > tbody > tr > td > span > img").src')
                    # 등급 1 확인
                    if getRating == "https://cafe.pstatic.net/levelicon/1/1_110.gif":
                        driver.switch_to_default_content()
                        # 본인 닉네임
                        getYournickname = driver.execute_script(
                            'return document.querySelector("#gnb_name1").innerText')
                        driver.switch_to_frame("cafe_main")
                        # 글 들어가기
                        driver.execute_script(
                            f'document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_article > div.board-list > div > a").click()')
                        time.sleep(2)
                        # 댓글 작성자 node 리스트
                        setAuthorList = driver.find_elements_by_css_selector(
                            ".comment_nickname")
                        # 댓글을 일일이 확인하며 작성자 닉네임만 리스트로
                        alterAuthorList = []
                        for x in range(len(setAuthorList)):
                            alterAuthorList.append(
                                setAuthorList[x].get_attribute('innerText'))
                        # 본인 닉네임과 비교해서 중복 없을 시 댓글 달기
                        if getYournickname not in alterAuthorList:
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
                        # 중복 있으면 종료
                        else:
                            driver.quit()
                    else:
                        driver.refresh()
                        time.sleep(1)
                else:
                    # 매매일지 or 모바일 수익
                    if board == 189 or board == 940:
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
                    # 뉴스
                    elif board == 195:
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
            else:
                driver.refresh()
                time.sleep(1)


# login 버튼
loginButton = Button(win, text="Login", command=login)
loginButton.pack()

win.mainloop()
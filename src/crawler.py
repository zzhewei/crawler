"""
Python臉書社團爬蟲
爬取Costco社團中的所有貼文與留言
程式啟動後會不斷爬文, 直到被終止, 或所有文章被爬完
將爬取內容存在檔案, 而非僅顯示在console
編程規範要符合附件中的"Python" section
作法, 框架, 使用套件, 均沒有限制
完成後請將程式碼上傳至Github (或類似平台)並提供Readme
"""
import os
import pandas as pd
import facebook_scraper as fs

GROUP_ID = "1260448967306807"
"""# Costco 台灣粉絲團 ID"""

OUTPUT_FILE = "costco_posts.csv"
"""輸出檔名"""

PARENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""檔案上層絕對路徑"""

OUTPUT_PATH = os.path.join(PARENT_PATH, "outputs")
"""輸出檔案路徑"""


def get_comments(post_id):
    """
    根據文章的post_id再丟到對應的function以取得留言

    Args:
        post_id (str): 用來查詢對應文章ID的留言

    Returns:
        commenter_names (list): 所有留言的使用者名稱
        comment_texts (list): 所有留言的內容

    Raises:
        LookupError: 如果無法獲取留言
    """
    gen = fs.get_posts(post_urls=[post_id], options={"comments": True, "progress": True})

    try:
        post = next(gen)
        comments = post["comments_full"]
    except LookupError as e:
        print(f"Error: Unable to retrieve comments for post {post_id}. {e}")
        return [], []

    commenter_names = [comment["commenter_name"] for comment in comments]
    comment_texts = [comment["comment_text"] for comment in comments]

    return commenter_names, comment_texts


def get_post(post):
    """
    解析丟過來的貼文訊息，之後再把post_id丟到get_comments以取得comment

    Args:
        post (dict): 取得的貼文訊息

    Returns:
        row (dict): 回傳一個有ID、貼文內容、貼文時間、留言者、留言訊息的dict

    Raises:
        None
    """
    post_id = post["post_id"]
    post_time = post["time"]
    post_text = post["text"]

    commenter_names, comment_texts = get_comments(post_id)

    # 將每個貼文的資料儲存為一個 dict
    row = {
        "post_id": post_id,
        "text": post_text,
        "time": post_time,
        "commenter_names": commenter_names,
        "comment_texts": comment_texts,
    }
    return row


def main():
    """
    程式進入點，將從套件取得的資料丟到get_post處理，再用posts儲存，等到全部爬完或使用者中斷時，再用pandas轉換並寫檔

    Raises:
        KeyboardInterrupt: 如果使用者中斷
    """
    posts = []
    try:
        while True:
            for post in fs.get_posts(GROUP_ID):
                row = get_post(post)
                posts.append(row)
                print("=======================")
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        df = pd.DataFrame(posts)
        df.to_csv(os.path.join(OUTPUT_PATH, OUTPUT_FILE), index=False)


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    main()

"""
測試爬蟲檔
"""
import pytest
from pytest_mock import MockFixture
from src.crawler import fs, get_comments, get_post


@pytest.fixture()
def comments_mock(mocker: MockFixture):
    """
    定義fs.get_posts回傳的測試資料，以測試程式是否正確取得文章的留言資訊。

    Args:
        mocker (pytest_mock.plugin.MockerFixture): 用來mock外部函式的物件。

    Returns:
        None

    Raises:
        None
    """
    mock_get_posts = mocker.patch.object(target=fs, attribute="get_posts")
    return_data = dict()
    return_data["post_id"] = 1
    return_data["text"] = "test post"
    return_data["time"] = "2023-04-18"
    return_data["comments_full"] = [
        {"commenter_name": "Alice", "comment_text": "Comment 1"},
        {"commenter_name": "Bob", "comment_text": "Comment 2"},
    ]
    mock_get_posts.return_value = iter([return_data])


# def test_main(comments_mock):
#     output_file = "costco_posts.csv"
#
#     main()
#
#     assert os.path.exists(output_file)
#     os.remove(output_file)


def test_get_post_data(comments_mock):
    """
    測試 get_post 函式是否能正常解析貼文資料

    Args:
        comments_mock: comments_mock fixture，用來模擬 fs.get_posts 函式回傳測試資料

    Returns:
        None

    Raises:
        AssertionError: 如果有任何一個測試項目失敗
    """
    test_post = {
        "post_id": 1,
        "text": "test post",
        "time": "2023-04-18",
    }

    row = get_post(test_post)
    assert isinstance(row, dict)
    assert row["post_id"] == test_post["post_id"]
    assert row["text"] == test_post["text"]
    assert row["time"] == test_post["time"]
    assert row["commenter_names"] == ["Alice", "Bob"]
    assert row["comment_texts"] == ["Comment 1", "Comment 2"]


def test_get_comments(comments_mock):
    """
    測試 get_comments 函式是否能正常解析留言

    Args:
        comments_mock: comments_mock fixture，用來模擬 fs.get_posts 函式回傳測試資料

    Returns:
        None

    Raises:
        AssertionError: 如果有任何一個測試項目失敗
    """
    post_id = 1
    commenter_names, comment_texts = get_comments(post_id)
    assert commenter_names == ["Alice", "Bob"]
    assert comment_texts == ["Comment 1", "Comment 2"]

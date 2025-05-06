from datetime import date
from typing import List, Optional, Dict
import re

class User:
    def __init__(self, user_id, username, email, password_hash, signup_date, last_login,
                 subscription_status, favorite_articles=None, read_history=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.signup_date = signup_date
        self.last_login = last_login
        self.subscription_status = subscription_status
        self.favorite_articles = favorite_articles or []
        self.read_history = read_history or []

def simulate_registration(name, email, password, role, simulate="success"):
    name = name.strip() if name else ""
    email = email.strip().lower() if email else ""

    if not name:
        return {"success": False, "error": "Tên không được để trống"}
    if len(name) > 255:
        return {"success": False, "error": "Tên quá dài"}

    if not email:
        return {"success": False, "error": "Email không được để trống"}
    if len(email) > 254:
        return {"success": False, "error": "Email quá dài"}
    if ".." in email or "@@" in email or email.startswith(".") or email.endswith("."):
        return {"success": False, "error": "Email không hợp lệ"}
    if "@" not in email or "." not in email.split("@")[-1]:
        return {"success": False, "error": "Email không hợp lệ"}

    if not password or len(password) < 6:
        return {"success": False, "error": "Mật khẩu quá ngắn"}

    if not role or role.lower() not in ["viewer", "poster", "admin"]:
        return {"success": False, "error": "Vai trò không hợp lệ"}

    if simulate == "duplicate":
        return {"success": False, "error": "Email đã được sử dụng"}
    if simulate == "no_confirm":
        return {"success": False, "error": "Email chưa xác nhận trong 24 giờ"}

    return {"success": True, "status": "Đăng ký thành công", "user_id": "fake123"}


def simulate_login(email, password, simulate="success"):
    email = email.strip().lower() if email else ""

    if simulate == "system_error":
        return {"success": False, "error": "Lỗi hệ thống, vui lòng thử lại"}

    if not email:
        return {"success": False, "error": "Email is required"}
    if len(email) > 254:
        return {"success": False, "error": "Email too long"}
    if ".." in email or "@@" in email or " " in email or "@" not in email or "." not in email.split("@")[-1]:
        return {"success": False, "error": "Invalid email format"}

    if not password:
        return {"success": False, "error": "Password is required"}
    if " " in password:
        return {"success": False, "error": "Password must not contain spaces"}

    if simulate == "incorrect_password":
        return {"success": False, "error": "Incorrect password"}
    if simulate == "lock_account":
        return {"success": False, "error": "Account locked after multiple failed attempts"}
    if simulate == "unverified":
        return {"success": False, "error": "Account not verified"}
    if simulate == "disabled":
        return {"success": False, "error": "Account is disabled"}
    if simulate == "sql_injection":
        return {"success": False, "error": "Suspicious input detected"}
    if simulate == "force_captcha":
        return {"success": False, "error": "Too many attempts. CAPTCHA required"}
    if simulate == "reset_success":
        return {"success": True, "message": "Login successful after password reset"}

    return {"success": True, "message": "Login successful"}

def simulate_account_deletion(logged_in=True, confirmation=True, simulate="success", has_active_subscription=False):
    if simulate == "system_error":
        return {"success": False, "error": "Lỗi hệ thống, vui lòng thử lại"}

    if not logged_in:
        return {"success": False, "error": "Unauthorized"}

    if simulate == "network_lost":
        return {"success": False, "error": "Mất kết nối mạng, hãy thử lại"}

    if simulate == "expired_session":
        return {"success": False, "error": "Phiên làm việc đã hết hạn"}

    if not confirmation:
        return {"success": False, "error": "Please confirm deletion"}

    if has_active_subscription:
        return {"success": False, "error": "Vui lòng hủy gói đăng ký trước khi xóa tài khoản"}

    return {"success": True, "message": "Tài khoản đã được xóa vĩnh viễn"}

def simulate_subscription_payment(card_info, simulate="success", is_already_premium=False, is_trial_user=False):
    if is_already_premium:
        return {"success": False, "error": "Already subscribed"}

    if is_trial_user:
        return {"success": False, "error": "Trial only once"}

    if simulate == "system_error":
        return {"success": False, "error": "System error, please try again or contact support"}

    if simulate == "network_lost":
        return {"success": False, "error": "Connection lost, try again"}

    if simulate == "cancelled":
        return {"success": False, "error": "Payment was cancelled"}

    if simulate == "unsupported_card":
        return {"success": False, "error": "Card not accepted"}

    if simulate == "invalid_currency":
        return {"success": False, "error": "Currency not supported"}

    if not card_info.get("card_number") or not card_info.get("cvv") or not card_info.get("exp") or not card_info.get("billing_address"):
        return {"success": False, "error": "Card info required"}

    if any(c.isalpha() or not c.isdigit() for c in card_info["card_number"]):
        return {"success": False, "error": "Invalid card number format"}

    if len(card_info["card_number"]) < 12:
        return {"success": False, "error": "Card number too short"}

    if not card_info["cvv"].isdigit():
        return {"success": False, "error": "Invalid CVV"}

    if card_info["exp"] < "05/24":  # Giả sử tháng/năm hiện tại là 05/24
        return {"success": False, "error": "Card expired"}

    return {"success": True, "message": "Premium subscription activated"}

def simulate_favorite_action(article_id, user_id=None, simulate="success", is_favorited=False):
    if not user_id:
        return {"success": False, "error": "User must be logged in to favorite articles"}

    if simulate == "system_error":
        return {"success": False, "error": "Unable to save article"}

    if is_favorited:
        return {"success": True, "action": "removed", "message": "Article removed from favorites"}

    return {"success": True, "action": "added", "message": "Article added to favorites"}


reading_history_mock = ["Article 1", "Article 2", "Article 3"] 

def simulate_reading_history(history):
    if not history:
        return {"success": False, "error": "No reading history available"}
    return {"success": True, "history": history}

def simulate_delete_history(history, confirm=True, delete_one=False, index_to_delete=None):
    if not confirm:
        return {"success": False, "error": "Deletion not confirmed"}

    if delete_one:
        if index_to_delete is not None and 0 <= index_to_delete < len(history):
            removed = history.pop(index_to_delete)
            return {"success": True, "message": f"Deleted: {removed}", "remaining": history}
        else:
            return {"success": False, "error": "Invalid item to delete"}

    history.clear()
    return {"success": True, "message": "All history deleted", "remaining": history}


class NewsArticle:
    existing_titles = {"Breaking News", "Latest Update"}
    existing_contents = {"This is a copied article content"}

    def __init__(self, title, content, author_id, status="Pending", simulate="success"):
        self.title = title.strip() if title else ""
        self.content = content.strip() if content else ""
        self.author_id = author_id
        self.status = status
        self.simulate = simulate

    def submit(self):
        if self.simulate == "offline":
            return {"success": False, "error": "No connection, article queued for later"}
        if self.simulate == "timeout":
            return {"success": False, "error": "Inactivity timeout, auto-logout triggered"}
        if self.simulate == "rejected":
            return {"success": False, "error": "Article rejected by admin: Inappropriate content"}
        if self.simulate == "admin_edit":
            return {"success": True, "message": "Article submitted with admin modifications", "edited_by_admin": True}
        if self.simulate == "profane":
            return {"success": False, "error": "Content contains profanity"}
        if self.simulate == "unsupported_image":
            return {"success": False, "error": "Image format not supported"}

        if not self.title:
            return {"success": False, "error": "Title is required"}
        if len(self.title) > 255:
            return {"success": False, "error": "Title too long"}
        if not self.content:
            return {"success": False, "error": "Content is required"}
        if self.title in NewsArticle.existing_titles:
            return {"success": False, "error": "Duplicate article"}
        if self.content in NewsArticle.existing_contents:
            return {"success": False, "error": "Duplicate content"}
        if "<script>" in self.content or "<iframe>" in self.content:
            return {"success": False, "error": "Disallowed HTML tags detected"}

        return {"success": True, "status": "Pending Approval"}
    
def simulate_read_article(article_id, logged_in=True, is_deleted=False, read_limit_exceeded=False):
        if not article_id or not isinstance(article_id, str):
            return {"success": False, "error": "Invalid article ID"}

        if is_deleted:
            return {"success": False, "error": "Article not found"}

        if not logged_in:
            return {"success": True, "prompt_login": True, "message": "Guest view or login required"}

        if read_limit_exceeded:
            return {"success": False, "error": "Reading limit exceeded"}

        return {"success": True, "content": "This is the article content"}

def simulate_search(keyword):
        if keyword is None or keyword.strip() == "":
            return {"success": False, "error": "Please enter a keyword"}

        if len(keyword) > 255:
            return {"success": False, "error": "Keyword length limit exceeded"}

        if keyword in "@#$%^&*":
            return {"success": False, "error": "No results found"}

        if keyword.lower() == "ai":
            return {"success": True, "results": ["AI in 2025", "The Future of AI"]}

        return {"success": True, "results": []}
    
def simulate_ai_summary(article_content, logged_in=True, is_deleted=False, simulate="success"):
    if not logged_in:
        return {"success": False, "error": "Please log in to use summarization"}

    if is_deleted:
        return {"success": False, "error": "Article not found"}

    if simulate == "overload":
        return {"success": False, "error": "Please try again later"}

    if simulate == "failure":
        return {"success": False, "error": "System error"}

    if not article_content or article_content.strip() == "":
        return {"success": False, "error": "Cannot summarize empty article"}

    if len(article_content) < 50:
        return {"success": False, "error": "Not enough text to summarize"}

    if len(article_content) > 20000:
        return {"success": True, "summary": "Summary generated for long article"}

    return {"success": True, "summary": "This is a summarized version of the article"}


def simulate_comment_action(content, action="post", simulate="success", logged_in=True, account_status="active"):
    if not logged_in:
        return {"success": False, "error": "User must be logged in to comment"}

    if account_status == "suspended":
        return {"success": False, "error": "Account is suspended"}

    if action == "report":
        return {"success": True, "message": "Comment reported successfully"}

    if simulate == "offline":
        return {"success": False, "error": "No connection, comment saved locally"}

    if simulate == "duplicate":
        return {"success": False, "error": "Comment already exists"}

    if simulate == "inappropriate" or simulate == "profanity":
        return {"success": False, "error": "Inappropriate content"}

    if content is None or content.strip() == "":
        return {"success": False, "error": "Comment cannot be empty"}

    if len(content) > 1000:
        return {"success": False, "error": "Text too long"}

    return {"success": True, "message": "Comment posted" if action == "post" else "Comment updated"}

def simulate_statistics_view(filter_type="all", simulate="success", dataset_exists=True):
    if simulate == "load_error":
        return {"success": False, "error": "Data loading error"}

    if not dataset_exists:
        return {"success": False, "error": "No data available"}

    stats = {
        "views": 1240,
        "likes": 320,
        "comments": 85,
        "filter": filter_type
    }

    return {"success": True, "statistics": stats}

def simulate_article_comparison(article_a_exists=True, article_b_exists=True):
    if not article_a_exists or not article_b_exists:
        return {"success": False, "error": "One or more articles not found"}

    comparison = {
        "articleA": {"views": 500, "likes": 100},
        "articleB": {"views": 800, "likes": 200}
    }

    return {"success": True, "comparison": comparison}

def simulate_search_articles(keyword):
    if keyword is None or keyword.strip() == "":
        return {"success": False, "error": "Please enter a keyword"}

    if len(keyword) > 255:
        return {"success": False, "error": "Keyword too long"}

    keyword_clean = keyword.lower().strip()

    if keyword_clean in ["ai", "artificial intelligence"]:
        return {"success": True, "results": ["AI in 2025", "Future of AI", "AI vs Humanity"]}

    if any(c in keyword_clean for c in "@#$%"):
        return {"success": False, "error": "No results found"}

    return {"success": False, "error": "No results found"}

def simulate_filter_articles(category):
    if category is None or category.strip() == "":
        return {"success": False, "error": "No matching articles found"}

    category = category.strip().lower()

    if category == "all":
        return {"success": True, "articles": ["AI in 2025", "SpaceX Launch", "Climate Crisis"]}

    if category == "technology":
        return {"success": True, "articles": ["AI in 2025", "The Rise of Quantum Computing"]}

    if not category.isalnum():
        return {"success": False, "error": "Invalid category"}

    return {"success": False, "error": "No matching articles found"}

def simulate_article_rating(rating, comment, simulate="success", is_update=False, rapid_submit=False):
    if rapid_submit:
        return {"success": False, "error": "Duplicate submission detected"}

    if rating is None or not (1 <= rating <= 5):
        return {"success": False, "error": "Please select a rating"}

    if comment and len(comment) > 1000:
        return {"success": False, "error": "Comment too long"}

    if simulate == "sanitize":
        clean_comment = comment.replace("<", "&lt;").replace(">", "&gt;")  # Basic sanitization
        return {"success": True, "message": "Rating saved with sanitized comment", "comment": clean_comment}

    action = "updated" if is_update else "saved"
    return {"success": True, "message": f"Rating {action} successfully"}


reported_articles = set()  # giả lập trạng thái báo cáo

def simulate_article_report(article_id, reason, simulate="success", allow_duplicate=False):
    if simulate == "system_error":
        return {"success": False, "error": "System error, please try again later"}

    if not reason or reason.strip() == "":
        return {"success": False, "error": "Please select a reason"}

    if len(reason) > 500:
        return {"success": False, "error": "Reason too long"}

    if not allow_duplicate and article_id in reported_articles:
        return {"success": False, "error": "Article already reported"}

    reported_articles.add(article_id)
    return {"success": True, "message": "Report submitted successfully"}

class Report:
    existing_reports = {}  # { (user_id, article_id): Report }

    def __init__(self, user_id, article_id, reason):
        self.user_id = user_id
        self.article_id = article_id
        self.reason = reason.strip()
        self.status = "submitted"

    @classmethod
    def submit_report(cls, user_id, article_id, reason, simulate="success"):
        key = (user_id, article_id)

        if simulate == "system_error":
            return {"success": False, "error": "System error, please try again later"}

        if not reason or reason.strip() == "":
            return {"success": False, "error": "Please select a reason"}

        if len(reason) > 500:
            return {"success": False, "error": "Reason too long"}

        if key in cls.existing_reports:
            return {"success": False, "error": "Article already reported"}

        report = Report(user_id, article_id, reason)
        cls.existing_reports[key] = report
        return {"success": True, "message": "Report submitted successfully"}




def simulate_recommendations(user_id=None, simulate="success", has_history=False, has_articles=True, see_more=False):
    if simulate == "system_error":
        return {"success": False, "error": "Recommendation system error"}

    if not has_articles:
        return {"success": False, "error": "No recommendations available"}

    if has_history:
        base_recs = ["AI and You", "Future of Robotics"]
    else:
        base_recs = ["Top Trending: Climate", "Breaking: Tech Updates"]

    if see_more:
        base_recs.extend(["More on AI", "SpaceX News", "Tech Mergers", "HealthTech 2030"])

    return {"success": True, "recommendations": base_recs}


class Comment:
    def __init__(self, comment_id, news_id, user_id, content, comment_date, is_approved=True):
        self.comment_id = comment_id
        self.news_id = news_id
        self.user_id = user_id
        self.content = content
        self.comment_date = comment_date
        self.is_approved = is_approved


class Subscription:
    def __init__(self, subscription_id, user_id, start_date, end_date, plan, status):
        self.subscription_id = subscription_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.plan = plan
        self.status = status

class Payment:
    def __init__(self, payment_id, user_id, subscription_id, amount, payment_date, payment_method):
        self.payment_id = payment_id
        self.user_id = user_id
        self.subscription_id = subscription_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method

class Admin:
    def __init__(self, admin_id, username, email, password_hash, role, created_date):
        self.admin_id = admin_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_date = created_date

class PendingArticle:
    def __init__(self, pending_id, user_id, title, content, submission_date, status, reviewed_by_admin_id=None):
        self.pending_id = pending_id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.submission_date = submission_date
        self.status = status
        self.reviewed_by_admin_id = reviewed_by_admin_id

class Statistics:
    def __init__(self, stats_id, news_id, views=0, likes=0, comments=0, interactions=None):
        self.stats_id = stats_id
        self.news_id = news_id
        self.views = views
        self.likes = likes
        self.comments = comments
        self.interactions = interactions or []

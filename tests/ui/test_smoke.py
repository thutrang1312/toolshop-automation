import re
import pytest
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage


@pytest.mark.smoke
def test_smoke_search_pliers(page):
    """Mục tiêu: Kiểm tra tìm kiếm trả về sản phẩm đúng từ khóa.
    Tiền điều kiện: Có sản phẩm trong hệ thống.
    Kết quả mong đợi: Mọi tên sản phẩm hiện ra đều chứa chữ 'pliers'."""
    home = HomePage(page).open()
    home.search("pliers")

    expect(home.search_completed).to_be_visible()
    count = home.product_names.count()
    assert count > 0
    for i in range(count):
        expect(home.product_names.nth(i)).to_contain_text(re.compile(r"pliers", re.IGNORECASE))


@pytest.mark.smoke
def test_smoke_add_claw_hammer_to_cart(page):
    """Mục tiêu: Thêm sản phẩm với số lượng tùy chỉnh cập nhật đúng badge giỏ hàng.
    Tiền điều kiện: Sản phẩm 'Claw Hammer' tồn tại.
    Kết quả mong đợi: Badge giỏ hàng trên menu hiện số 3."""
    home = HomePage(page).open()
    product = home.open_product("Claw Hammer")
    product.add_to_cart(quantity=3)

    expect(product.toast).to_contain_text("Product added to shopping cart")
    expect(product.cart_quantity).to_have_text("3")


@pytest.mark.smoke
def test_smoke_login_invalid_credentials(page):
    """Mục tiêu: Báo lỗi khi đăng nhập bằng thông tin không tồn tại.
    Tiền điều kiện: Dùng email ngẫu nhiên chưa đăng ký.
    Kết quả mong đợi: Hiện 'Invalid email or password' và URL vẫn là /auth/login."""
    login = LoginPage(page).open()
    login.login("nobody-here-random@example.com", "any-password-123")

    expect(login.error).to_contain_text("Invalid email or password")
    expect(page).to_have_url(re.compile(r"/auth/login$"))


@pytest.mark.smoke
def test_smoke_contact_empty_form(page):
    """Mục tiêu: Kiểm tra xác thực form khi gửi liên hệ trống.
    Tiền điều kiện: Người dùng đang ở trang Contact.
    Kết quả mong đợi: Hiện lỗi 'Subject is required' và 'Message is required'."""
    contact = ContactPage(page).open()
    contact.submit()

    expect(contact.subject_error).to_contain_text("Subject is required")
    expect(contact.message_error).to_contain_text("Message is required")
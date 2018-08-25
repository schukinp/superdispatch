from data import *
import pages

def test_goodreads(selenium):
    selenium.get(url)
    homepage = pages.HomePage(selenium)
    homepage.email_input = invalid_user['email']
    homepage.password_input = invalid_user['password']
    homepage.click_sign_in_button()
    assert(homepage.get_error() == invalid_user['message'])
    selenium.execute_script("window.history.go(-1)")
    homepage.email_input = registered_user['email']
    homepage.password_input = registered_user['password']
    homepage.click_sign_in_button()
    userpage = pages.UserPage(selenium)
    userpage.search_input = search_query
    userpage.click_search_results_button()
    userpage.mark_want_to_read()
    userpage.mark_as_read_and_leave_feedback(selenium)
    userpage.click_profile()
    userpage.click_sigin_out()


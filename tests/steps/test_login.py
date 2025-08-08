from pytest_bdd import given, when, then, scenarios

scenarios('../features/login.feature')

@given("I open the login page")
def open_login_page(login_page, auth_data):
    login_page.open(auth_data["base_url"] + auth_data["login_path"])

@when("I login with valid credentials")
def login_with_valid_credentials(login_page, auth_data):
    login_page.login(auth_data["email"], auth_data["password"])

@then("I am redirected to the Trading page and it is loaded")
def redirected_and_loaded(trading_page, auth_data):
    assert trading_page.wait_until_opened(auth_data["trading_url"])

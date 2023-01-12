import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_group_form(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                                home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="",
                                ayear="", notes="", address2="", phone2=""))
    app.session.logout()

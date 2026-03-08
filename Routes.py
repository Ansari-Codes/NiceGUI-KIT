SIGNUP = '/signup'
LOGIN = '/login'
HOME = '/home'
DASHBOARD = '/dashboard'

from Core.pages import page
from Pages.Auth.Signup import create_signup

page(SIGNUP)(create_signup)
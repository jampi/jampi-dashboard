from flask import Flask, render_template

import forms

app = Flask(__name__)


class ErrorHandler():
    # 400
    @app.errorhandler(400)
    def error_bad_request(error):
        return render_template('error/400.html', error_bad_request=True)

    # 404
    @app.errorhandler(404)
    def error_not_found(error):
        return render_template('error/404.html', error_not_found=True)


class PublicPages():
    # Hello page with login and register links
    # If the user is already logged in, its redirect to /home
    @app.route('/')
    def public_hello():
        return render_template('public/hello.html', public_hello=True)

    # Cookies
    @app.route('/cookies')
    def public_cookies():
        return render_template('public/cookies.html', public_cookies=True)

    # Privacy policy
    @app.route('/privacy-policy')
    def public_privacy():
        return render_template('public/privacy.html', public_privacy=True)

    # Terms of Services
    @app.route('/terms-of-services')
    def public_terms():
        return render_template('public/terms.html', public_terms=True)

    # Support
    @app.route('/support', methods=('GET', 'POST'))
    def public_support():
        form_support = forms.SupportForm(csrf_enabled=False)
        return render_template(
            'public/support.html', form_support=form_support)


class Authentication():
    # Login page
    @app.route('/auth/login', methods=('GET', 'POST'))
    def auth_login():
        form_login = forms.LoginForm(csrf_enabled=False)
        return render_template('auth/login.html', form_login=form_login)

    # Log out
    @app.route('/auth/logout')
    def auth_logout():
        return 'You are logged out!'

    # Forgot password page
    @app.route('/auth/forgot_password', methods=('GET', 'POST'))
    def auth_forgot_password():
        form_forgot = forms.ForgotPasswordForm(csrf_enabled=False)
        return render_template(
            'auth/forgot_password.html', form_forgot=form_forgot)

    # Registration page
    @app.route('/auth/register', methods=('GET', 'POST'))
    def auth_register():
        form_register = forms.RegistrationForm(csrf_enabled=False)
        return render_template(
            'auth/register.html', form_register=form_register)


class AdminCommon():
    # Home
    @app.route('/home')
    def admin_common_home():
        return render_template(
            'admin_common/home.html', admin_common_home=True)

if __name__ == '__main__':
    # Fancy error messages
    app.debug = True

    app.run()

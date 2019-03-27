def login_required(function_to_decorate):
    def check(*args, **kwargs):
        from flask_login import current_user
        from flask import redirect, url_for
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return function_to_decorate(*args, **kwargs)
    return check
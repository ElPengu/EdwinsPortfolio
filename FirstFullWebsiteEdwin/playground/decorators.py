#To lock non super users from playground app
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


#Using middleware, this is straight from Stackoverflow
def superuser_only(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='nonsuperuserPage'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
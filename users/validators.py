from django.core import validators
from django.utils.translation import gettext_lazy as _

#修改username的验证要求为只允许字母数字
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    #regex = r'^[\w.@+-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0
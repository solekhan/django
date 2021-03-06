# coding: utf-8
"""
Tests for forms/util.py module.
"""

tests = r"""
>>> from django.forms.util import *
>>> from django.core.exceptions import ValidationError
>>> from django.utils.translation import ugettext_lazy

###########
# flatatt #
###########

>>> from django.forms.util import flatatt
>>> flatatt({'id': "header"})
u' id="header"'
>>> flatatt({'class': "news", 'title': "Read this"})
u' class="news" title="Read this"'
>>> flatatt({})
u''

###################
# ValidationError #
###################

# Can take a string.
>>> print ErrorList(ValidationError("There was an error.").messages)
<ul class="errorlist"><li>There was an error.</li></ul>

# Can take a unicode string.
>>> print ErrorList(ValidationError(u"Not \u03C0.").messages)
<ul class="errorlist"><li>Not π.</li></ul>

# Can take a lazy string.
>>> print ErrorList(ValidationError(ugettext_lazy("Error.")).messages)
<ul class="errorlist"><li>Error.</li></ul>

# Can take a list.
>>> print ErrorList(ValidationError(["Error one.", "Error two."]).messages)
<ul class="errorlist"><li>Error one.</li><li>Error two.</li></ul>

# Can take a mixture in a list.
>>> print ErrorList(ValidationError(["First error.", u"Not \u03C0.", ugettext_lazy("Error.")]).messages)
<ul class="errorlist"><li>First error.</li><li>Not π.</li><li>Error.</li></ul>

>>> class VeryBadError:
...     def __unicode__(self): return u"A very bad error."

# Can take a non-string.
>>> print ErrorList(ValidationError(VeryBadError()).messages)
<ul class="errorlist"><li>A very bad error.</li></ul>

# Escapes non-safe input but not input marked safe.
>>> example = 'Example of link: <a href="http://www.example.com/">example</a>'
>>> print ErrorList([example])
<ul class="errorlist"><li>Example of link: &lt;a href=&quot;http://www.example.com/&quot;&gt;example&lt;/a&gt;</li></ul>
>>> print ErrorList([mark_safe(example)])
<ul class="errorlist"><li>Example of link: <a href="http://www.example.com/">example</a></li></ul>
"""

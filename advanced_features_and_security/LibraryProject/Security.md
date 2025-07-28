# Django Security Enhancements

1. `DEBUG=False` in production for security.
2. Browser protections: `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`.
3. `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` enforce HTTPS.
4. Forms include `{% csrf_token %}` for CSRF protection.
5. All queries use Django ORM to avoid SQL injection.
6. CSP headers configured using `django-csp` to prevent XSS.

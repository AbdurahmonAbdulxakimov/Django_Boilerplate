from django.core.handlers.wsgi import WSGIRequest


def get_domain_and_protocol(request: WSGIRequest) -> tuple:
    domain = request.get_host()  # Get the domain (including port if present)
    protocol = "https" if request.is_secure() else "http"

    return protocol, domain

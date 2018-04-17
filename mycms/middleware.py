import logging

from cms.utils.page_resolver import get_page_from_request, reverse
from django.utils.six.moves.urllib.parse import unquote


class UrlAuthenticationMiddleware(object):
    def process_request(self, request):
        logging.info('UrlAuthenticationMiddleware url=%s', request.path_info)
        # pages_root = unquote(reverse("pages-root"))
        # logging.info('pages-root=%s', pages_root)
        # page = get_page_from_request(request)
        # logging.info('page=%s', page.__repr__())
        # if hasattr(request, 'instance'):
        #     if hasattr(request['instance'], 'app_config'):
        #         logging.info(request['instance']['app_config'])

        # assert hasattr(request, 'session'), (
        #     "The Django authentication middleware requires session middleware "
        #     "to be installed. Edit your MIDDLEWARE_CLASSES setting to insert "
        #     "'django.contrib.sessions.middleware.SessionMiddleware' before "
        #     "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        # )
        # request.user = SimpleLazyObject(lambda: get_user(request))

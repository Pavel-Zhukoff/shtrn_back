from django.urls import reverse_lazy


def get_referer_url(request):
    return request.META.get('HTTP_REFERER') \
        if request.META.get('HTTP_REFERER') is not None \
        else reverse_lazy('home')

def get_videos():
    pass

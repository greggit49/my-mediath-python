from django.shortcuts import render, get_object_or_404
from bibliothecaire.models import Media

def media_list(request):
    medias = Media.objects.all()
    return render(request, 'index.html', {'medias': medias})


def media_detail(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    return render(request, 'media_detail.html', {'media': media})





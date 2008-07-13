from django.shortcuts import render_to_response, get_object_or_404
from apps.schoolbook.models import Schoolbook

def chapter_details(request, slug, number):
    schoolbook = get_object_or_404(Schoolbook, slug=slug)
    chapter = get_object_or_404(schoolbook.chapters, number=number)
    
    return render_to_response('chapter/chapter_details.html', {'object': chapter})
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)

from models import Flag
from forms import FlagForm

def index(request):
    if request.method == "POST":
        form = FlagForm(request.POST, request.FILES)
        if form.is_valid() and (form.cleaned_data['image'] or form.cleaned_data['tagline']):
            newflag = Flag()
            newflag.original = form.cleaned_data['image']
            newflag.name = form.cleaned_data['name']
            newflag.email = form.cleaned_data['email']
            newflag.location = form.cleaned_data['location']
            newflag.tagline = form.cleaned_data['tagline']
        
            newflag.save()
        
            return HttpResponseRedirect(reverse('flags.views.index'))
    else:
        form = FlagForm()
        
    flags = Flag.objects.order_by("-id")
    
    return render_to_response(
        'flags/index.html',
        {'flags': flags, 'form': form},
        context_instance=RequestContext(request)
    )

@never_cache
def getFlags(request):
    p = Paginator(Flag.objects.exclude(state='flagged').order_by("-id"), 10)
    page = request.GET.get('page', 1)
    curPage = p.page(page)
    
    flags = []
    for flag in curPage:
        flags.append(flag.as_json())
    
    return HttpResponse(json.dumps({
        'flags': flags,
        'page': page,
        'next': curPage.has_next(),
    }))

def flagFlag(request):
    data = json.loads(request.body)

    flag = Flag.objects.get(id=data['flagId'])
    if flag.state == 'approved':
        raise("Cannot delete approved flags")
    reason = data['reason']
    if flag.id and reason:
        flag.state = 'flagged'
        flag.flagReason = reason
    
    flag.save()
    return HttpResponse(json.dumps(flag.as_json()))
    
def terms(request):
    return render_to_response('flags/terms.html',)
    
def single(request, flagId):
    flags = Flag.objects.all()
    flag = Flag.objects.get(id=flagId)
    
    if flag.name and flag.location:
        author = flag.name + ', ' + flag.location
    elif not flag.location:
        author = flag.name
    else:
        author = flag.location
        
    return render_to_response('flags/single.html', {'flags': flags, 'flag': flag, 'author': author})
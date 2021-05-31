from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.apps import apps
from travello.models import Destination, Guide #to access a table from another app
from django.db.models import Count
from django.views import generic
from django.utils.decorators import method_decorator

def guides_assignment(destination, all_guides, *args, **kwargs):
        
    for guide in all_guides:
        #if this guide isnt availible at this time, skip to the next one
        if guide.isAvailible(destination.start_time, destination.end_time):
            destination.guides.add(guide)        
 

#@login_required(login_url='/accounts/login')
@method_decorator(login_required, name='dispatch')
class details(generic.DetailView): 
    template_name = "destinations/details.html" #by default, will try to use a template at appName/modelName_detail.html must define the proper template
    model = Destination
    
    def get(self, request, *args, **kwargs):
        dest = Destination.objects.get(name=self.kwargs.get("city_name"))
        
        #dest.guides.clear()
        dest_guides = dest.guides.all()

        return render(request, self.template_name, {"dest":dest, 
        "dest_guides":dest_guides,
        "dest_guides_count":len(dest_guides),
        "dest_start_time":dest.start_time.strftime("time: %H:%M %p, date: %d/%m/%Y, timezone: %Z"),
        "dest_end_time":dest.end_time.strftime("time: %H:%M %p, date: %d/%m/%Y, timezone: %Z"),
        })

    def post(self, request, *args, **kwargs):
        dest = Destination.objects.get(name=self.kwargs.get("city_name"))
        all_guides = Guide.objects.filter(is_active=True)

        guides_assignment(dest,all_guides)
        dest_guides = dest.guides.all()

        return render(request, self.template_name, {"dest":dest, 
        "dest_guides":dest_guides, 
        "dest_guides_count":len(dest_guides),
        "dest_start_time":dest.start_time.strftime("time: %H:%M %p, date: %d/%m/%Y, timezone: %Z"),
        "dest_end_time":dest.end_time.strftime("time: %H:%M %p, date: %d/%m/%Y, timezone: %Z"),
        })

    # return render(request, '%s.html' %city_name) #...and capture it as desired

class all_destinations(generic.ListView):
    template_name = 'destinations/all_destinations.html'

    #dests = get_list_or_404(Destination)
    #return render(request, 'destinations.html', {'dests':dests}) 
    """you need both of the following lines to achieve the functionality commented out above"""
    model = Destination
    context_object_name = 'dests'

    #if you wanted to have different models in your listview, should pass it in as additional context (shown below)
    def get_context_data(self, **kwargs):
        context = super(all_destinations, self).get_context_data(**kwargs)
        context.update({ 'guides': Guide.objects.all() })
        return context
    
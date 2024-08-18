//post model has lat and long
//users model has lat and long 
//formula

from geopy.distance import great_circle
user = (9.919287, 78.147862)
post_orphanage = (9.923401, 78.148200)
dist = great_circle(hotel,orphanage).miles
print (dist)
if (dist<1):
    print("Nearest orphanage available at ",orphanage)
else:
    print("Nearest orphanage available")

def meetingDetail(request, slug):
    post = get_object_or_404(Post, MSlug = slug)
    users=User.objects.all()
    return render(request, 'blog/meeting_detail.html', {'users':users,'post':post})

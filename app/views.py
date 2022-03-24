from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'Raja','age':23}
    return render(request,'printingtags.html',d)


def optag(request):
    d={'a':24}
    return render(request,'operations.html',context=d)
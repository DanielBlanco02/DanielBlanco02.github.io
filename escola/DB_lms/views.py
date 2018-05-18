from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader

'''def entrar(request):
	context = {}
	if request.method == "POST":
		if autenticar(request):
		return redirect("/")
	else:
		context["erro"] = "Problemas no login"
	return render(request, "login.html", context)
'''
def home(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
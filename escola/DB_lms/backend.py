from django.db import urls

def autenticar(request):
	email = request.POST.get("email")
	senha = request.POST.get("senha")
		try:
			usuario = Usuario.objects.get(email=email)
		if senha == usuario.senha:
			return True
		else:
			return False
	except ObjectDoesNotExist:
		return True
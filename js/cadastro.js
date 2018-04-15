
	function validar(){
		var password = document.getElementById("senha").value
		var password_confirm = document.getElementById("comfirma_senha").value
		var nascimento = document.getElementById("nascimento").value
		var cpf = document.getElementById("cpf").value

		//função para verificar a idade do usuário
		function getAge(dateString) {
			var today = new Date();
			var birthDate = new Date(dateString);
			var age = today.getFullYear() - birthDate.getFullYear();
			var m = today.getMonth() - birthDate.getMonth();
			if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
			  age--;
			}
			return age;
		  }

		//atribuindo o retorno da função(idade da pessoa) dentro da variavel idade
		var idade = getAge(nascimento)
		if(idade < 17){
			alert("idade não permitida")
		}


		//RegEx para verificar se senha possui numeros e letras
		var regex = /^(?=.*\d)(?=.*[a-z])(?!.*\s).*$/.test(password)

		if(!regex){
			alert("Senha deve letras e números")
		}


		//verifica se o valor dos campos de senha são iguais
		if (password != password_confirm) {
			alert("Confirmação deve ser igual a senha")
		}

		//função para validar cpf
		function validaCPF(cpf) {
			var numeros, digitos, soma, i, resultado, digitos_iguais;
			digitos_iguais = 1;
			if (cpf.length < 11)
				return false;
			for (i = 0; i < cpf.length - 1; i++)
				if (cpf.charAt(i) != cpf.charAt(i + 1))
						{
						digitos_iguais = 0;
						break;
						}
			if (!digitos_iguais)
				{
				numeros = cpf.substring(0,9);
				digitos = cpf.substring(9);
				soma = 0;
				for (i = 10; i > 1; i--)
						soma += numeros.charAt(10 - i) * i;
				resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
				if (resultado != digitos.charAt(0))
						return false;
				numeros = cpf.substring(0,10);
				soma = 0;
				for (i = 11; i > 1; i--)
						soma += numeros.charAt(11 - i) * i;
				resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
				if (resultado != digitos.charAt(1))
						return false;
				return true;
				}
			else
				return false;
		}

		//chamando a função para validar cpf, e passando a variavel cpf que guarda o valor do input
		var checkCpf = validaCPF(cpf);
		if(!checkCpf){
			alert("cpf inválido")
		}

		
	}

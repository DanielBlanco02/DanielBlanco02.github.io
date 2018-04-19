function validar(){
    
            var inputs = document.getElementsByTagName("input")
    
            var i = 0, aprovados = 0, cancelados = 0;
            for(i=0; i< inputs.length; i++){
                if(inputs[i].id == "status"){
                    if(inputs[i].value == "aprovado" && inputs[i].checked){
                        aprovados++
                    }
                    if(inputs[i].value == "cancelado" && inputs[i].checked){
                        cancelados++
                    }
                }
            }
    
            
    
        confirm(aprovados + ": alunos foram aprovados e "+ cancelados +": alunos foram reprovados." )
        }
        

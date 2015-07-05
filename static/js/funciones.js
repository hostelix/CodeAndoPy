$.ajaxSetup({
	cache : true
});
cargando = '<p class="form-registro"><img src="/static/images/ajax-loader.gif" alt="cargando"><p>';


function ejecutar(funcion, segundos){
	tmp = segundos / 0.001;
	setTimeout(funcion,tmp);
}

function refresh_pagina(tiempo,pagina){
    ejecutar(function(){
        location.href = pagina
    },tiempo);
}

function ajax(URL,METODO,ID){
	$.ajax({
		url: URL,
		type: METODO,
		beforeSend: function(){
			$("#"+ID).html(cargando);
		},
		success: function(res){
			$("#"+ID).html(res);
		}
	});

}

function div_alerta(tipo, texto){
   return "<div class='alert "+tipo+"'> " + texto+"</div";
}

function maneja_errores(errores){
    retorno  = "<div class='alert alert-danger'>"
    for(var i = 0; i < errores.length; i++){
        retorno += "<p>"+errores[i]+"</p>";
    }
    retorno += "</div>";
    return retorno;
}

function vaciar_campos(arreglo_id){
    for(var i = 0; i < arreglo_id.length; i++){
        $("#"+arreglo_id[i]).val(" ");
    }
}

function verificar_campos(id_formulario){
    vacios = 0;
    $("#"+id_formulario+" input").each(function(index, elemento) {
        if($(elemento).attr("type") == "text" || $(elemento).attr("type") == "password"){
            if($(elemento).val() == ""){
                vacios++;
            }
        }
    });
    return (vacios)?(true):(false);
}
function sin_espacios(_evento){
    var evento = window.event || _evento || event;
    var ESPACIO = 32;

    return (evento.type == "keydown" && evento.keyCode == ESPACIO)?(false):(true)
}


function registro_asignatura(e) {

    datos = $("#formulario-registro-asignatura").serialize();

    $.ajax({
        url: '/GestionAsignaturas/crear_asignatura',
        data: datos,
        type: "POST",
        beforeSend: function(){
            $("#mensajes").html(cargando);
        },
        success: function(res){
            if(res.exito){
                $("#contenido-ajax-registro-asignatura").html(res);
                vaciar_campos(["nombre","codigo"]);
            }
            else{
                $("#contenido-ajax-registro-asignatura").html(res);
            }
        }
    });
}

function crear_aula(e) {




    datos = $("#formulario-registro-aula").serialize()

    $.ajax({
        url: '/GestionAulas/crear_aula',
        data: datos,
        type: "POST",
        beforeSend: function(){
            $("#mensajes").html(cargando);
        },
        success: function(res){
            if(res.exito){
                $("#contenido-ajax-aula").html(res);
                vaciar_campos(["descripcion","limite"]);
            }
            else{
                $("#contenido-ajax-aula").html(res);
            }
        }
    });
}

function registro_profesor() {

    datos = $("#formulario-registro-profesor").serialize();

    $.ajax({
        url: '/GestionProfesores/crear_profesor',
        data: datos,
        type: "POST",
        beforeSend: function(){
            $("#mensajes").html(cargando);
        },
        success: function(res){

            if(res.exito){
                $("#contenido-ajax-registro-profesor").html(res);
                vaciar_campos(["especialidad-profesor"]);
                refresh_pagina(0.5,"/inicio");
            }
            else{
                $("#contenido-ajax-registro-profesor").html(res);
            }
        }
    });
}


function acceder_aula(id){
    location.href = "/Aulas/"+id;
}

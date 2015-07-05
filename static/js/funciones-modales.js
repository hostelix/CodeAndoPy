
$(document).ready(function(){

	//Ajax para formulario de inicio de sesion

	$("#modal-inicio-sesion").click(function(e){
		e.preventDefault();

        $.ajax({
            url: 'GestionUsuario/inicio_sesion',
            type: "GET",
            beforeSend: function(){
                $("#contenido-inicio-sesion").html(cargando);
            },
            success: function(res){
                $("#contenido-inicio-sesion").html(res);
            }
        });
			
	});


	$("#iniciar-sesion").click(function(e){

		e.preventDefault();

        if(!verificar_campos("formulario-inicio-sesion"))
        {
            datos = $("#formulario-inicio-sesion").serialize();

            $.ajax({
                url: '/GestionUsuario/inicio_sesion',
                type: "POST",
                data: datos,
                beforeSend: function () {
                    $("#contenido-inicio-sesion").html(cargando);
                },
                success: function (res) {
                    if (res.exito == "sesion-creada") {
                        $("#contenido-inicio-sesion").html('<div class="alert alert-success" role="alert"><strong>Inicio de sesion completado</strong></div>');

                        ejecutar(function () {
                            location.href = "/inicio"
                        }, 1.5);

                        return true;
                    }
                    else {
                        $("#contenido-inicio-sesion").html(res);
                    }

                }
            });
        }
        else
        {
           alert("Rellena todos los campos del formulario");
        }
		
	});


	//Ajax para registro de usuario
	$("#modal-registro").click(function(e){
		
		e.preventDefault();
        $.ajax({
            url: 'GestionUsuario/registro_usuario',
            type: "GET",
            beforeSend: function(){
                $("#contenido-registro").html(cargando);
            },
            success: function(res){
                $("#contenido-registro").html(res);
            }
        });
	});

	$("#registro-usuario").click(function(e){

		e.preventDefault();

        if(!verificar_campos("formulario-registro-usuario"))
        {
            datos = $("#formulario-registro-usuario").serialize();

            $.ajax({
                url: '/GestionUsuario/registro_usuario',
                type: "POST",
                data: datos,
                beforeSend: function(){
                    $("#contenido-registro").html(cargando);
                },
                success: function(res){
                    $("#contenido-registro").html(res);
                }
            });
        }
        else{
            alert("Rellena todos los campos del formulario");
        }
	});

	//Registo de datos personales

	$("#btn-open-modal-registro-persona").click(function(e){
		
		e.preventDefault();

		$.ajax({
			url: '/GestionPersona/registro_persona',
			type: "GET",
			beforeSend: function(){
				$("#contenido-ajax-registro-persona").html(cargando);
			},
			success: function(res){
				$("#contenido-ajax-registro-persona").html(res);
			}
		});
			
	});

	$("#btn-modal-registrar-datos").click(function(e){

        $("#usuario").val("{{usuario.id}}");
		$.ajax({
			url:'/GestionPersona/registro_persona',
			type: "POST",
			data: $("#formulario-registro-persona").serialize(),
			beforeSend: function(){
				$("#contenido-registro-datos-personales").html(cargando);
			},
			success: function(res){

			if(res.exito == "1"){
					$("#contenido-ajax-registro-persona").html("<p class='alert alert-success'> Se han a&ntilde;adido los datos satisfactoriamente </p>");

					ejecutar(function(){
						$("#btn-cerrar-modal").click()
					},1);

                    ejecutar(function(){
                        location.href = "/";
                    },0.5);

				}
				else{
					$("#contenido-ajax-registro-persona").html(res);
				}
			}
			
		});

	});



    $("#modal-registro-asignatura").on("click",function(e){
        e.preventDefault();

        $.ajax({
            url: '/GestionAsignaturas/crear_asignatura',
            type: "GET",
            beforeSend: function(){
                $("#contenido-ajax-registro-asignatura").html(cargando);
            },
            success: function(res){
                $("#contenido-ajax-registro-asignatura").html(res);
            }
        });
    });


    //Procedimientos para la creacion de aulas

    $("#mostrar-aulas").on("click",function(e){
        e.preventDefault();

        $.ajax({
            url: '/GestionAulas/mostrar_aulas',
            type: "GET",
            beforeSend: function(){
                $("#contenido-ajax-mostrar-aulas").html(cargando);
            },
            success: function(res){
                $("#contenido-ajax-mostrar-aulas").html(res);
            }
        });
    });


    $("#modal-crear-aula").click(function(e){

        e.preventDefault();
        $.ajax({
            url: '/GestionAulas/crear_aula',
            type: "GET",
            beforeSend: function(){
                $("#contenido-ajax-aula").html(cargando);
            },
            success: function(res){
                $("#contenido-ajax-aula").html(res);
            }
        });

    });

    $("#modal-registro-profesor").on("click",function(e){
        e.preventDefault();

        $.ajax({
            url: '/GestionProfesores/crear_profesor',
            type: "GET",
            beforeSend: function(){
                $("#contenido-ajax-registro-profesor").html(cargando);
            },
            success: function(res){
                $("#contenido-ajax-registro-profesor").html(res);
            }
        });
    });

});

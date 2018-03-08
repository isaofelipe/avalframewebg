$(document).ready(function() {
    $('.datatable').DataTable({
        "ordering": false,
        "bLengthChange": false
    });
});

$(document).ready(function () {
    $("#sel1").change(function () {
        var tipo = $("#sel1 option:checked").val();
        if (tipo == "A") {
            $("#relatorioAprendizagens").show();
            $("#relatorioCompetencias").hide();
        }
        else {
            $("#relatorioAprendizagens").hide();
            $("#relatorioCompetencias").show();
        }
    })
})

$(document).ready(function (){
    $("#gerar_perfil").click(function(){
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_perfil",
            data : form.serialize(),
            dataType : 'json',
            success : function(data){
                $("#perfil_recomendacao").val(data.retorno);
                $("#perfil_recomendacao_help").text("");
            },
            error : function(){
                $("#perfil_recomendacao_help").text("Preencha todos os campos");
            }
        })
    })
})

$(document).ready(function () {
    $("#id_codigo_jogo").change(function () {
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_niveis",
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                $("#id_codigo_nivel").find("option").not(':first').remove();
                for (i = 0; i < data.opcoes.length; i++) {
                    $("#id_codigo_nivel").append('<option value="' + data.opcoes[i].codigo + '">' + data.opcoes[i].nivel + ' - ' + data.opcoes[i].titulo + '</option>');
                }
            }
        })
    })
})

$(document).ready(function () {
    $("#id_codigo_nivel").change(function () {
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_fases",
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                $("#id_codigo_fase").find("option").not(':first').remove();
                for (i = 0; i < data.opcoes.length; i++) {
                    $("#id_codigo_fase").append('<option value="' + data.opcoes[i].codigo + '">' + data.opcoes[i].fase + ' - ' + data.opcoes[i].titulo + '</option>');
                }
            }
        })
    })
})










$(document).ready(function () {
    $("#id_codigo_jogo").change(function () {
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_niveis",
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                $("#id_nivel_jogo").find("option").not(':first').remove();
                for (i = 0; i < data.opcoes.length; i++) {
                    $("#id_nivel_jogo").append('<option value="' + data.opcoes[i].codigo + '">' + data.opcoes[i].nivel + ' - ' + data.opcoes[i].titulo + '</option>');
                }
            }
        })
    })
})

$(document).ready(function () {
    $("#id_nivel_jogo").change(function () {
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_fases",
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                $("#id_fase_jogo").find("option").not(':first').remove();
                for (i = 0; i < data.opcoes.length; i++) {
                    $("#id_fase_jogo").append('<option value="' + data.opcoes[i].codigo + '">' + data.opcoes[i].fase + ' - ' + data.opcoes[i].titulo + '</option>');
                }
            }
        })
    })
})

$(document).ready(function () {
    $("#id_fase_jogo").change(function () {
        var form = $(this).closest("form");
        $.ajax({
            url: "gerar_etapas",
            data: form.serialize(),
            dataType: 'json',
            success: function (data) {
                $("#id_etapa_jogo").find("option").not(':first').remove();
                for (i = 0; i < data.opcoes.length; i++) {
                    $("#id_etapa_jogo").append('<option value="' + data.opcoes[i].codigo + '">' + data.opcoes[i].etapa + ' - ' + data.opcoes[i].titulo + '</option>');
                }
            }
        })
    })
})
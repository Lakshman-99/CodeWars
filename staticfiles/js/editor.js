let editor;

window.onload = function() {
    ace.require("ace/ext/language_tools");
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/kr_theme");
    editor.session.setMode("ace/mode/python");
    editor.setOptions({
      fontSize: '14pt',
      enableBasicAutocompletion: true,
      enableSnippets: true,
      enableLiveAutocompletion: true
    });
};

function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'python')editor.session.setMode("ace/mode/python");
    else if(language == 'node')editor.session.setMode("ace/mode/javascript");


};
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("head").style.fontSize = "35px";
    document.getElementById("imag").style.width = "8%";
    document.getElementById("imag").style.height = "60px";



  } else {
    document.getElementById("head").style.fontSize = "50px";
    document.getElementById("imag").style.width = "15%";
    document.getElementById("imag").style.height = "100px";


  }
};

function executeCode() {

    $.ajax({

        url: "runcode/",

        type: "POST",

        data: {
            csrfmiddlewaretoken:'{{ csrf_token }}',
            language: $("#languages").val(),
            code: editor.getSession().getValue(),
        },

        success: function(response) {
            $('#output').html(response);
        }
    })

};

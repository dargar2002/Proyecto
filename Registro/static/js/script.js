
var tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds
var fechaActual = (new Date(Date.now() - tzoffset)).toISOString().slice(0, -1).slice(0,10)

window.onload = function(){
  document.getElementById('id_Fecha').value = fechaActual
}


document.getElementById("id_Nacimiento").type="date"
document.getElementById("id_Fecha").type="date"



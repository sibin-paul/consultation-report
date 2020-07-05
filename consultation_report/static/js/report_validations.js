function validateForm() {
  var x = document.forms["ConsultationForm"]["patient_contact"].value;
  var y = document.forms["ConsultationForm"]["physician_contact"].value;
  var phoneno = /^\d{10}$/;
  if (x.match(phoneno) && x.match(phoneno)) {
    return true;
  }else{
   alert("Invalid phoneno");
   return false;
  }
}

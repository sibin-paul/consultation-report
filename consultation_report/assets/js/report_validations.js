function validateForm() {
  var x = document.forms["ConsultationForm"]["clinic_name"].value;
  if (x == "xx") {
    alert("Name must be filled out");
    return false;
  }
}
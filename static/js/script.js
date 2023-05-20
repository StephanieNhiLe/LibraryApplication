console.log("SUP");
const input = document.getElementById("image");

function handleFileInputChange(event) {
  const label = document.querySelector(".file-upload");
  const fileName = input.files[0].name;
  if (fileName) {
    label.classList.add("has-file");
  } 
}

if (input) {
  input.addEventListener("change", handleFileInputChange);
}

setTimeout(function() {
  var error = document.querySelector('.error');
error.parentNode.removeChild(error);
}, 5000);


setTimeout(function() {
  var success = document.querySelector('.success');
  success.parentNode.removeChild(success);
}, 5000);
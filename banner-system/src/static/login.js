$(document).ready(function() {
  $("#button").click(function(event) {
    if($("#username").val() == "" || $("#password").val() == ""){
      alert('You must enter a valid username and password.');
      return;
    }
    console.log("Performing Ajax Call");
    $.ajax({
      data: {
        username: $("#username").val(),
        password: $("#password").val()
      },
      type: "POST",
      url: "http://localhost:5000/login",
      statusCode: {
        401: function(data) {
          if (data.error) {
            return alert(data.error);
          }
        },
        200: function(data) {
            console.log(data);
        }
      }
    });
    event.preventDefault;
  });
});

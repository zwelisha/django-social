$(document).ready(function() {
    $("#home-user-card").on("click", function(e) {
      e.preventDefault();
      let user_id = $("#user-details").text();
      console.log("Printed from front", user_id);
      $.ajax({
        method: "POST",
        contentType: false,
        url: "timeline/",
        data: {"user_id": user_id},
        dataType: "json",
        success: function(data) {
          console.log("Success data: ", data, "comes from success");
          window.location.href = "timeline/";
        },
      });
    });
  });
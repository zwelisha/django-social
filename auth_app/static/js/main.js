$(document).ready(function () {
  // When the button is clicked, send an Ajax request to the `/my-view` URL.
  $(".social-user").on("click", function (event) {
    event.preventDefault();
    let user_id = event.currentTarget.id;
    alert(`The user id is: ${user_id}`);
    console.log(user_id);
    $.ajax({
      // The `url` property specifies the URL of the view.
      url: "posts/",
      method: "POST",
      // The `data` property specifies the data that will be sent to the view.
      data: {
        user_id: user_id,
      },
      success: function (data) {
        console.log(data);
        // window.location.href = ""
      },
    });
  });
});

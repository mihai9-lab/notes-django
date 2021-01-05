$(document).ready(function () {
  $("#id_content").css("color", $("#id_colorText").val());
  $("#id_content").css("background-color", $("#id_colorBackground").val());
  $("#id_content").css("font-size", $("#id_fontSize").val() + "px");

  $("#id_colorText").change(function () {
    $("#id_content").css("color", this.value);
  });

  $("#id_colorBackground").change(function () {
    $("#id_content").css("background-color", this.value);
  });

  $("#id_fontSize").change(function () {
    $("#id_content").css("font-size", this.value + "px");
  });
});

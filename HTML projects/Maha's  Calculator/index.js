let calc = [];
$("button").click(function () {
  let pressed = $(this).attr("id");
  if (pressed === "=") {
    calc = calc.join("");
    $(".shape").html(eval(calc));
  } else if (pressed === "reset") {
    calc = [];
    $(".shape").html("");
  } else {
    calc.push(pressed);
    $(".shape").html(calc);
  }
});

$("button").mouseover(function (e) {
  $("this").addClass("mouseover");
});

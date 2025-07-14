let n = Math.floor(Math.random() * 2);
let player = [];
if (n === 1) {
  player = ["✖️", "⭕"];
} else {
  player = ["⭕", "✖️"];
}
let currentRoundNumber = 0;
$("body").keypress(function (pressed) {
  if (pressed.key === "Enter") {
    $("h2").html(player[0] + " player starts");
    currentRoundNumber++;
    $("body").addClass("o");
    $(".square").click(function () {
      if ($(this).html() !== "") {
        $("h2").html("You can't play here guy....!");
        return;
      }
      if (currentRoundNumber % 2 == 0) {
        $(this).html(player[1]);
        $("h2").html("player " + player[0] + "'s turn");
        $("body").addClass(player[0]).removeClass(player[1]);
        $(this)
          .addClass(player[1] + "s")
          .removeClass(player[0] + "s");
      } else {
        $(this).html(player[0]);
        $("h2").html("player " + player[1] + "'s turn");
        $(this)
          .addClass(player[0] + "s")
          .removeClass(player[1] + "s");
        $("body").addClass(player[1]).removeClass(player[0]);
      }
      currentRoundNumber++;
      let lines = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
      ];

      for (let i = 0; i < lines.length; i++) {
        let [a, b, c] = lines[i];
        let A = $("#" + a).html();
        let B = $("#" + b).html();
        let C = $("#" + c).html();

        if (currentRoundNumber > 9) {
          $("h2").text("Draw! No one wins 😊 ");
          $(".square").off("click");
          $("body").addClass("manycolor");
        }
        if (A !== "" && A === B && B === C) {
          $("h2").text(A + " players wins! 🥳");
          $(".square").off("click");
          $("#" + a)
            .fadeOut()
            .fadeIn()
            .fadeOut()
            .fadeIn();
          $("#" + b)
            .fadeOut()
            .fadeIn()
            .fadeOut()
            .fadeIn();
          $("#" + c)
            .fadeOut()
            .fadeIn()
            .fadeOut()
            .fadeIn();
        }
      }
    });
  }
});

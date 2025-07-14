const ROWS = 6;
const COLS = 7;

const board = [];
let currentPlayer = "red";
let gameOver = false;

const boardElement = document.getElementById("board");
const currentPlayerSpan = document.getElementById("current-player");
const messageElement = document.getElementById("message");
const resetBtn = document.getElementById("reset-btn");

// Initialize board data and UI
function initBoard() {
  boardElement.innerHTML = "";
  board.length = 0;
  for (let r = 0; r < ROWS; r++) {
    board[r] = [];
    for (let c = 0; c < COLS; c++) {
      board[r][c] = null;
      const cell = document.createElement("div");
      cell.classList.add("cell");
      cell.dataset.row = r;
      cell.dataset.col = c;
      cell.addEventListener("click", () => handleCellClick(c));
      boardElement.appendChild(cell);
    }
  }
  currentPlayer = "red";
  currentPlayerSpan.textContent = "Red";
  messageElement.textContent = "";
  gameOver = false;
}

// Handle player's move by column
function handleCellClick(col) {
  if (gameOver) return;

  // Find the lowest empty row in this column
  for (let row = ROWS - 1; row >= 0; row--) {
    if (!board[row][col]) {
      board[row][col] = currentPlayer;
      updateBoardUI();
      if (checkWin(row, col)) {
        messageElement.textContent = `${capitalize(currentPlayer)} wins!`;
        gameOver = true;
      } else if (isBoardFull()) {
        messageElement.textContent = `It's a draw!`;
        gameOver = true;
      } else {
        switchPlayer();
      }
      break;
    }
  }
}

// Update the UI based on board state
function updateBoardUI() {
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const cell = boardElement.querySelector(
        `.cell[data-row="${r}"][data-col="${c}"]`
      );
      cell.classList.remove("red", "yellow");
      if (board[r][c]) {
        cell.classList.add(board[r][c]);
      }
    }
  }
}

// Switch current player
function switchPlayer() {
  currentPlayer = currentPlayer === "red" ? "yellow" : "red";
  currentPlayerSpan.textContent = capitalize(currentPlayer);
}

// Check if the board is full (draw)
function isBoardFull() {
  return board.every((row) => row.every((cell) => cell !== null));
}

// Check for a win starting from placed disc
function checkWin(row, col) {
  return (
    checkDirection(row, col, 0, 1) || // horizontal
    checkDirection(row, col, 1, 0) || // vertical
    checkDirection(row, col, 1, 1) || // diagonal down-right
    checkDirection(row, col, 1, -1) // diagonal down-left
  );
}

// Check one direction for 4 in a row
function checkDirection(row, col, rowDir, colDir) {
  let count = 1;
  count += countDiscs(row, col, rowDir, colDir);
  count += countDiscs(row, col, -rowDir, -colDir);
  return count >= 4;
}

// Count consecutive discs in a direction
function countDiscs(row, col, rowDir, colDir) {
  let r = row + rowDir;
  let c = col + colDir;
  let count = 0;
  while (
    r >= 0 &&
    r < ROWS &&
    c >= 0 &&
    c < COLS &&
    board[r][c] === currentPlayer
  ) {
    count++;
    r += rowDir;
    c += colDir;
  }
  return count;
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

// Reset game
resetBtn.addEventListener("click", initBoard);

// Initialize on page load
initBoard();

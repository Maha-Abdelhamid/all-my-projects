const translations = {
  en: {
    mainTitle: "Memory Game",
    settingsTitle: "Settings",
    startGame: "Start Game",
    settings: "Settings",
    saveBack: "Save & Back",
    gameTitle: "Memory Game",
    moves: "Moves",
    player1: "Player 1",
    player2: "Player 2",
    computer: "Computer",
    turn: "Turn:",
    yourTurn: "Your turn!",
    compTurn: "Computer's turn!",
    p1Turn: "Player 1's turn!",
    p2Turn: "Player 2's turn!",
    match: "Match found! 🎉",
    notMatch: "No match, next player's turn!",
    win: "Game Over! Winner: ",
    draw: "Game Over! Draw!",
    boardSize: "Board Size:",
    initialReveal: "Initial Reveal Time (seconds):",
    gameMode: "Game Mode:",
    compDiff: "Computer Difficulty:",
    easy: "Easy",
    medium: "Medium",
    langLabel: "Language:",
    clickToStart: "Click any card to start!",
    memorize: "Memorize! Cards revealing for ",
    seconds: " seconds...",
    goFind: "Go! Find the pairs!",
    backToMenu: "Back to Menu",
    save: "Save & Back",
    twoPlayers: "Two Players",
    playerVsComputer: "Player vs Computer",
    player1NameLabel: "Player 1 Name:",
    player2NameLabel: "Player 2 Name:",
    themeLabel: "Theme:",
  },
  ar: {
    mainTitle: "لعبة الذاكرة",
    settingsTitle: "الإعدادات",
    startGame: "ابدأ اللعب",
    settings: "إعدادات",
    saveBack: "حفظ والرجوع",
    gameTitle: "لعبة الذاكرة",
    moves: "الحركات",
    player1: "اللاعب ١",
    player2: "اللاعب ٢",
    computer: "الكمبيوتر",
    turn: "الدور:",
    yourTurn: "دورك!",
    compTurn: "دور الكمبيوتر!",
    p1Turn: "دور اللاعب ١!",
    p2Turn: "دور اللاعب ٢!",
    match: "مبروك! لقيت زوج 👏",
    notMatch: "مش متشابهين.. دور اللي بعدك!",
    win: "اللعبة خلصت! الفائز: ",
    draw: "اللعبة خلصت! تعادل!",
    boardSize: "حجم اللوحة:",
    initialReveal: "زمن كشف الكروت في البداية (ثواني):",
    gameMode: "وضع اللعب:",
    compDiff: "صعوبة الكمبيوتر:",
    easy: "سهل",
    medium: "متوسط",
    langLabel: "اللغة:",
    clickToStart: "اضغط على أي كارت للبدء!",
    memorize: "احفظ أماكن الكروت! (",
    seconds: " ثانية)",
    goFind: "ابدأ اللعب!",
    backToMenu: "رجوع للقائمة",
    save: "حفظ والرجوع",
    twoPlayers: "لاعب ضد لاعب",
    playerVsComputer: "لاعب ضد كمبيوتر",
    player1NameLabel: "اسم اللاعب ١:",
    player2NameLabel: "اسم اللاعب ٢:",
    themeLabel: "الثيم:",
  },
};

let lang = "en";
let gameSettings = {
  gameMode: "playerVsPlayer",
  computerDifficulty: "easy",
  initialRevealTime: 3,
  boardRows: 4,
  boardCols: 4,
  boardSize: "4x4",
  totalCards: 16,
  themeIndex: 0,
};
let playerNames = ["Player 1", "Player 2"];
let cards = [];
let flippedCards = [];
let matchedPairs = 0;
let totalMoves = 0;
let lockBoard = false;
let currentPlayer = 1; // 1 or 2 or  'computer'
let scores = [0, 0];
let computerMemory = new Map();

const allCardIcons = [
  "fa-star",
  "fa-heart",
  "fa-gem",
  "fa-moon",
  "fa-sun",
  "fa-cloud",
  "fa-snowflake",
  "fa-leaf",
  "fa-bell",
  "fa-car",
  "fa-tree",
  "fa-fish",
  "fa-bug",
  "fa-anchor",
  "fa-flask",
  "fa-lightbulb",
  "fa-camera",
  "fa-cube",
  "fa-rocket",
  "fa-umbrella",
  "fa-wrench",
  "fa-headphones",
  "fa-mug-hot",
  "fa-pizza-slice",
];

// DOM Elements
const mainMenu = document.getElementById("mainMenu");
const settingsPage = document.getElementById("settingsPage");
const gamePage = document.getElementById("gamePage");
const startGameButton = document.getElementById("startGameButton");
const settingsButton = document.getElementById("settingsButton");
const saveSettingsButton = document.getElementById("saveSettingsButton");
const backToMenuButton = document.getElementById("backToMenuButton");
const gameModeSelect = document.getElementById("gameMode");
const computerDifficultyGroup = document.getElementById(
  "computerDifficultyGroup"
);
const computerDifficultySelect = document.getElementById("computerDifficulty");
const initialRevealTimeInput = document.getElementById("initialRevealTime");
const revealTimeValueSpan = document.getElementById("revealTimeValue");
const boardSizeSelect = document.getElementById("boardSize");
const langSelect = document.getElementById("langSelect");
const themeSelect = document.getElementById("themeSelect");
const player1NameInput = document.getElementById("player1Name");
const player2NameInput = document.getElementById("player2Name");
const player2NameGroup = document.getElementById("player2NameGroup");
const playerTurnDisplay = document.getElementById("playerTurnDisplay");
const movesDisplay = document.getElementById("moves");
const score1Display = document.getElementById("score1");
const score2Display = document.getElementById("score2");
const score1Box = document.getElementById("score1Box");
const score2Box = document.getElementById("score2Box");
const messageBox = document.getElementById("messageBox");
const gameBoard = document.getElementById("gameBoard");
const mainTitle = document.getElementById("mainTitle");
const settingsTitle = document.getElementById("settingsTitle");
const gameTitle = document.getElementById("gameTitle");
const langLabel = document.getElementById("langLabel");
const gameModeLabel = document.getElementById("gameModeLabel");
const compDiffLabel = document.getElementById("compDiffLabel");
const revealTimeLabel = document.getElementById("revealTimeLabel");
const boardSizeLabel = document.getElementById("boardSizeLabel");
const player1NameLabel = document.getElementById("player1NameLabel");
const player2NameLabel = document.getElementById("player2NameLabel");
const themeLabel = document.getElementById("themeLabel");

// Themes array for select options
const themes = [
  {
    name: "Default",
    vars: {
      "--bg-color": "#1a202c",
      "--text-color": "#e2e8f0",
      "--card-back-color": "#63b3ed",
      "--card-front-color": "#4a5568",
    },
  },
  {
    name: "Sunset",
    vars: {
      "--bg-color": "#ffecd2",
      "--text-color": "#5b4636",
      "--card-back-color": "#fcb69f",
      "--card-front-color": "#f6ae2d",
    },
  },
  {
    name: "Ocean",
    vars: {
      "--bg-color": "#034f84",
      "--text-color": "#ffffff",
      "--card-back-color": "#92a8d1",
      "--card-front-color": "#f7cac9",
    },
  },
  {
    name: "Forest",
    vars: {
      "--bg-color": "#2f5233",
      "--text-color": "#d9ead3",
      "--card-back-color": "#6aa84f",
      "--card-front-color": "#38761d",
    },
  },
  {
    name: "Lavender",
    vars: {
      "--bg-color": "#e6e6fa",
      "--text-color": "#4b0082",
      "--card-back-color": "#c8a2c8",
      "--card-front-color": "#9370db",
    },
  },
  {
    name: "Candy",
    vars: {
      "--bg-color": "#ffb6b9",
      "--text-color": "#6a0572",
      "--card-back-color": "#fcd5ce",
      "--card-front-color": "#f8a5c2",
    },
  },
  {
    name: "Mint",
    vars: {
      "--bg-color": "#d0f0c0",
      "--text-color": "#2f4f4f",
      "--card-back-color": "#a8dadc",
      "--card-front-color": "#457b9d",
    },
  },
  {
    name: "Peach",
    vars: {
      "--bg-color": "#ffe5b4",
      "--text-color": "#5c4033",
      "--card-back-color": "#ffccbc",
      "--card-front-color": "#ffab91",
    },
  },
  {
    name: "Night",
    vars: {
      "--bg-color": "#0b132b",
      "--text-color": "#ffffff",
      "--card-back-color": "#1c2541",
      "--card-front-color": "#3a506b",
    },
  },
  {
    name: "Rose",
    vars: {
      "--bg-color": "#ffc1cc",
      "--text-color": "#800020",
      "--card-back-color": "#ffb6b9",
      "--card-front-color": "#ff6f91",
    },
  },
  {
    name: "Sky",
    vars: {
      "--bg-color": "#87ceeb",
      "--text-color": "#003366",
      "--card-back-color": "#b0e0e6",
      "--card-front-color": "#4682b4",
    },
  },
  {
    name: "Gold",
    vars: {
      "--bg-color": "#fff8dc",
      "--text-color": "#b8860b",
      "--card-back-color": "#ffd700",
      "--card-front-color": "#daa520",
    },
  },
  {
    name: "Coral",
    vars: {
      "--bg-color": "#ff7f50",
      "--text-color": "#4b2e83",
      "--card-back-color": "#ff6f61",
      "--card-front-color": "#e76f51",
    },
  },
  {
    name: "Slate",
    vars: {
      "--bg-color": "#708090",
      "--text-color": "#f0f8ff",
      "--card-back-color": "#778899",
      "--card-front-color": "#2f4f4f",
    },
  },
  {
    name: "Peacock",
    vars: {
      "--bg-color": "#004953",
      "--text-color": "#a7c5bd",
      "--card-back-color": "#2a9d8f",
      "--card-front-color": "#264653",
    },
  },
  {
    name: "Tropical",
    vars: {
      "--bg-color": "#ffefd5",
      "--text-color": "#556b2f",
      "--card-back-color": "#98fb98",
      "--card-front-color": "#2e8b57",
    },
  },
  {
    name: "Berry",
    vars: {
      "--bg-color": "#800020",
      "--text-color": "#ffe4e1",
      "--card-back-color": "#c71585",
      "--card-front-color": "#db7093",
    },
  },
  {
    name: "Ice",
    vars: {
      "--bg-color": "#e0ffff",
      "--text-color": "#4682b4",
      "--card-back-color": "#afeeee",
      "--card-front-color": "#5f9ea0",
    },
  },
  {
    name: "Sunshine",
    vars: {
      "--bg-color": "#fffacd",
      "--text-color": "#b8860b",
      "--card-back-color": "#ffeb3b",
      "--card-front-color": "#fbc02d",
    },
  },
  {
    name: "Charcoal",
    vars: {
      "--bg-color": "#36454f",
      "--text-color": "#dcdcdc",
      "--card-back-color": "#4f5b66",
      "--card-front-color": "#2f4f4f",
    },
  },
];

// Fill theme select options
themes.forEach((theme, i) => {
  const option = document.createElement("option");
  option.value = i;
  option.textContent = theme.name;
  themeSelect.appendChild(option);
});

// Functions
function showPage(page) {
  mainMenu.classList.add("hidden");
  settingsPage.classList.add("hidden");
  gamePage.classList.add("hidden");
  page.classList.remove("hidden");
}

function updateLanguageTexts() {
  mainTitle.textContent = translations[lang].mainTitle;
  startGameButton.textContent = translations[lang].startGame;
  settingsButton.textContent = translations[lang].settings;
  settingsTitle.textContent = translations[lang].settingsTitle;
  langLabel.textContent = translations[lang].langLabel;
  gameModeLabel.textContent = translations[lang].gameMode;
  compDiffLabel.textContent = translations[lang].compDiff;
  revealTimeLabel.innerHTML = `${translations[lang].initialReveal} <span id="revealTimeValue">${gameSettings.initialRevealTime}</span>`;
  boardSizeLabel.textContent = translations[lang].boardSize;
  player1NameLabel.textContent = translations[lang].player1NameLabel;
  player2NameLabel.textContent = translations[lang].player2NameLabel;
  themeLabel.textContent = translations[lang].themeLabel;
  saveSettingsButton.textContent = translations[lang].saveBack;
  gameTitle.textContent = translations[lang].gameTitle;
  backToMenuButton.textContent = translations[lang].backToMenu;
  gameModeSelect.options[0].textContent = translations[lang].twoPlayers;
  gameModeSelect.options[1].textContent = translations[lang].playerVsComputer;
  computerDifficultySelect.options[0].textContent = translations[lang].easy;
  computerDifficultySelect.options[1].textContent = translations[lang].medium;
  boardSizeSelect.options[0].textContent =
    lang === "ar" ? "4x4 (16 كارت)" : "4x4 (16 cards)";
  boardSizeSelect.options[1].textContent =
    lang === "ar" ? "4x5 (20 كارت)" : "4x5 (20 cards)";
  boardSizeSelect.options[2].textContent =
    lang === "ar" ? "4x6 (24 كارت)" : "4x6 (24 cards)";
  boardSizeSelect.options[3].textContent =
    lang === "ar" ? "6x6 (36 كارت)" : "6x6 (36 cards)";
}

function applyTheme(index) {
  const theme = themes[index];
  for (const varName in theme.vars) {
    document.documentElement.style.setProperty(varName, theme.vars[varName]);
  }
  document.body.className = `theme-${index}`;
}

function updateGameDisplays() {
  movesDisplay.textContent = totalMoves;
  score1Display.textContent = scores[0];
  score2Display.textContent = scores[1];
  if (gameSettings.gameMode === "playerVsPlayer") {
    score1Box.innerHTML = `${playerNames[0]}: <span id="score1">${scores[0]}</span>`;
    score2Box.innerHTML = `${playerNames[1]}: <span id="score2">${scores[1]}</span>`;
    score2Box.style.display = "";
    playerTurnDisplay.textContent = `${playerNames[currentPlayer - 1]} ${
      translations[lang].turn
    }`;
    // Update background color for current player
    gamePage.classList.remove("player1-bg", "player2-bg");
    gamePage.classList.add(currentPlayer === 1 ? "player1-bg" : "player2-bg");
  } else {
    score1Box.innerHTML = `${playerNames[0]}: <span id="score1">${scores[0]}</span>`;
    score2Box.innerHTML = `${translations[lang].computer}: <span id="score2">${scores[1]}</span>`;
    score2Box.style.display = "";
    playerTurnDisplay.textContent =
      currentPlayer === 1
        ? translations[lang].yourTurn
        : translations[lang].compTurn;
    gamePage.classList.remove("player1-bg", "player2-bg");
  }
}

function displayMessage(message) {
  messageBox.textContent = message;
}

function initializeGame() {
  gameBoard.innerHTML = "";
  cards = [];
  flippedCards = [];
  matchedPairs = 0;
  totalMoves = 0;
  lockBoard = false;
  currentPlayer = 1;
  scores = [0, 0];
  computerMemory.clear();

  updateGameDisplays();
  displayMessage(lang === "ar" ? "اللعبة بدأت!" : "Game started!");

  const [rows, cols] = gameSettings.boardSize.split("x").map(Number);
  gameSettings.boardRows = rows;
  gameSettings.boardCols = cols;
  gameSettings.totalCards = rows * cols;

  gameBoard.className = `game-board cols-${gameSettings.boardCols}`;

  let numUniqueIcons = gameSettings.totalCards / 2;
  let availableIcons = allCardIcons.slice(0, numUniqueIcons);

  if (availableIcons.length < numUniqueIcons) {
    displayMessage(
      lang === "ar"
        ? "عدد الأيقونات غير كافي لهذا الحجم."
        : "Not enough icons for this board size."
    );
    return;
  }

  let gameCards = [...availableIcons, ...availableIcons];
  gameCards = shuffleArray(gameCards);

  gameCards.forEach((icon, index) => {
    const cardElement = document.createElement("div");
    cardElement.classList.add("card");
    cardElement.dataset.icon = icon;
    cardElement.dataset.index = index;
    cardElement.innerHTML = `
        <div class="card-inner">
          <div class="card-front"><i class="fas ${icon}"></i></div>
          <div class="card-back"><i class="fas fa-question"></i></div>
        </div>
      `;
    cardElement.addEventListener("click", () => handleCardClick(cardElement));
    gameBoard.appendChild(cardElement);

    cards.push({
      element: cardElement,
      icon: icon,
      isFlipped: false,
      isMatched: false,
    });
  });

  initialReveal();
}

function initialReveal() {
  lockBoard = true;
  displayMessage(
    translations[lang].memorize +
      gameSettings.initialRevealTime +
      (lang === "ar" ? translations.ar.seconds : translations.en.seconds)
  );
  cards.forEach((card) => card.element.classList.add("flipped"));
  setTimeout(() => {
    cards.forEach((card) => card.element.classList.remove("flipped"));
    lockBoard = false;
    displayMessage(translations[lang].goFind);
    if (gameSettings.gameMode === "playerVsComputer" && currentPlayer === 2) {
      setTimeout(computerTurn, 1000);
    }
  }, gameSettings.initialRevealTime * 1000);
}

function handleCardClick(clickedCardElement) {
  if (lockBoard) return;
  if (gameSettings.gameMode === "playerVsComputer" && currentPlayer === 2)
    return;
  const cardIndex = parseInt(clickedCardElement.dataset.index);
  flipCard(cardIndex);
}

function flipCard(index) {
  const currentCard = cards[index];
  if (currentCard.isFlipped || currentCard.isMatched) return;

  currentCard.element.classList.add("flipped");
  currentCard.isFlipped = true;
  flippedCards.push(currentCard);

  if (gameSettings.gameMode === "playerVsComputer" && currentPlayer === 2) {
    rememberCard(currentCard.icon, index);
  }

  if (flippedCards.length === 2) {
    totalMoves++;
    updateGameDisplays();
    lockBoard = true;
    setTimeout(() => {
      checkMatch();
    }, 900);
  }
}

function checkMatch() {
  const [card1, card2] = flippedCards;
  if (card1.icon === card2.icon) {
    card1.isMatched = true;
    card2.isMatched = true;
    card1.element.classList.add("matched");
    card2.element.classList.add("matched");
    matchedPairs++;
    if (currentPlayer === 1) scores[0]++;
    else scores[1]++;
    updateGameDisplays();
    displayMessage(translations[lang].match);
    if (gameSettings.gameMode === "playerVsComputer" && currentPlayer === 2) {
      computerMemory.delete(card1.icon);
    }
    if (matchedPairs === gameSettings.totalCards / 2) {
      let winnerMsg = "";
      if (scores[0] > scores[1])
        winnerMsg =
          translations[lang].win +
          (gameSettings.gameMode === "playerVsPlayer"
            ? playerNames[0]
            : playerNames[0]);
      else if (scores[1] > scores[0])
        winnerMsg =
          translations[lang].win +
          (gameSettings.gameMode === "playerVsPlayer"
            ? playerNames[1]
            : translations[lang].computer);
      else winnerMsg = translations[lang].draw;
      displayMessage(winnerMsg);
      lockBoard = true;
      currentPlayer = 0;
    } else {
      lockBoard = false;
      flippedCards = [];
      if (gameSettings.gameMode === "playerVsComputer" && currentPlayer === 2) {
        setTimeout(computerTurn, 1000);
      }
    }
  } else {
    setTimeout(() => {
      card1.isFlipped = false;
      card2.isFlipped = false;
      card1.element.classList.remove("flipped");
      card2.element.classList.remove("flipped");
      displayMessage(translations[lang].notMatch);
      switchTurn();
      lockBoard = false;
      flippedCards = [];
    }, 600);
  }
  updateGameDisplays();
}

function switchTurn() {
  if (gameSettings.gameMode === "playerVsPlayer") {
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    updateGameDisplays();
  } else if (gameSettings.gameMode === "playerVsComputer") {
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    updateGameDisplays();
    if (currentPlayer === 2) {
      lockBoard = true;
      setTimeout(computerTurn, 1200);
    }
  }
}

async function computerTurn() {
  if (matchedPairs === gameSettings.totalCards / 2) return;
  let firstCardIndex = -1,
    secondCardIndex = -1;
  const availableCardIndices = cards
    .map((card, idx) => ({ card, idx }))
    .filter((item) => !item.card.isFlipped && !item.card.isMatched)
    .map((item) => item.idx);

  if (availableCardIndices.length === 0) return;

  if (gameSettings.computerDifficulty === "easy") {
    firstCardIndex =
      availableCardIndices[
        Math.floor(Math.random() * availableCardIndices.length)
      ];
    await new Promise((res) => setTimeout(res, 700));
    flipCard(firstCardIndex);
    const remainingAvailable = availableCardIndices.filter(
      (idx) => idx !== firstCardIndex
    );
    if (remainingAvailable.length > 0) {
      secondCardIndex =
        remainingAvailable[
          Math.floor(Math.random() * remainingAvailable.length)
        ];
      await new Promise((res) => setTimeout(res, 700));
      flipCard(secondCardIndex);
    }
  } else if (gameSettings.computerDifficulty === "medium") {
    let foundMatch = false;
    for (const [icon, indices] of computerMemory.entries()) {
      const validIndices = indices.filter((idx) => !cards[idx].isMatched);
      if (validIndices.length === 2) {
        firstCardIndex = validIndices[0];
        secondCardIndex = validIndices[1];
        foundMatch = true;
        break;
      }
    }
    if (foundMatch) {
      await new Promise((res) => setTimeout(res, 700));
      flipCard(firstCardIndex);
      await new Promise((res) => setTimeout(res, 700));
      flipCard(secondCardIndex);
    } else {
      firstCardIndex =
        availableCardIndices[
          Math.floor(Math.random() * availableCardIndices.length)
        ];
      await new Promise((res) => setTimeout(res, 700));
      flipCard(firstCardIndex);
      const firstFlippedCard = cards[firstCardIndex];
      let potentialSecondCardIndex = -1;
      if (computerMemory.has(firstFlippedCard.icon)) {
        const knownIndices = computerMemory.get(firstFlippedCard.icon);
        potentialSecondCardIndex = knownIndices.find(
          (idx) => idx !== firstCardIndex && !cards[idx].isMatched
        );
      }
      if (
        potentialSecondCardIndex !== undefined &&
        potentialSecondCardIndex !== -1
      ) {
        secondCardIndex = potentialSecondCardIndex;
      } else {
        const remainingAvailable = availableCardIndices.filter(
          (idx) => idx !== firstCardIndex
        );
        if (remainingAvailable.length > 0) {
          secondCardIndex =
            remainingAvailable[
              Math.floor(Math.random() * remainingAvailable.length)
            ];
        }
      }
      if (secondCardIndex !== -1) {
        await new Promise((res) => setTimeout(res, 700));
        flipCard(secondCardIndex);
      }
    }
  }
}

function rememberCard(icon, index) {
  if (!computerMemory.has(icon)) {
    computerMemory.set(icon, []);
  }
  const indices = computerMemory.get(icon);
  if (!indices.includes(index)) {
    indices.push(index);
  }
}

// Event Listeners
startGameButton.addEventListener("click", () => {
  showPage(gamePage);
  initializeGame();
});

settingsButton.addEventListener("click", () => {
  showPage(settingsPage);
  gameModeSelect.value = gameSettings.gameMode;
  computerDifficultySelect.value = gameSettings.computerDifficulty;
  initialRevealTimeInput.value = gameSettings.initialRevealTime;
  revealTimeValueSpan.textContent = gameSettings.initialRevealTime;
  boardSizeSelect.value = gameSettings.boardSize;
  langSelect.value = lang;
  themeSelect.value = gameSettings.themeIndex;
  player1NameInput.value = playerNames[0];
  player2NameInput.value = playerNames[1];
  if (gameSettings.gameMode === "playerVsComputer") {
    computerDifficultyGroup.classList.remove("hidden");
    player2NameGroup.style.display = "none";
  } else {
    computerDifficultyGroup.classList.add("hidden");
    player2NameGroup.style.display = "";
  }
  updateLanguageTexts();
});

saveSettingsButton.addEventListener("click", () => {
  gameSettings.gameMode = gameModeSelect.value;
  gameSettings.computerDifficulty = computerDifficultySelect.value;
  gameSettings.initialRevealTime = parseInt(initialRevealTimeInput.value);
  const [rows, cols] = boardSizeSelect.value.split("x").map(Number);
  gameSettings.boardRows = rows;
  gameSettings.boardCols = cols;
  gameSettings.totalCards = rows * cols;
  gameSettings.boardSize = boardSizeSelect.value;
  lang = langSelect.value;
  gameSettings.themeIndex = parseInt(themeSelect.value);
  playerNames[0] =
    player1NameInput.value.trim() || (lang === "ar" ? "اللاعب ١" : "Player 1");
  playerNames[1] =
    player2NameInput.value.trim() || (lang === "ar" ? "اللاعب ٢" : "Player 2");
  updateLanguageTexts();
  applyTheme(gameSettings.themeIndex);
  showPage(mainMenu);
});

gameModeSelect.addEventListener("change", () => {
  if (gameModeSelect.value === "playerVsComputer") {
    computerDifficultyGroup.classList.remove("hidden");
    player2NameGroup.style.display = "none";
  } else {
    computerDifficultyGroup.classList.add("hidden");
    player2NameGroup.style.display = "";
  }
});

initialRevealTimeInput.addEventListener("input", () => {
  revealTimeValueSpan.textContent = initialRevealTimeInput.value;
});

langSelect.addEventListener("change", () => {
  lang = langSelect.value;
  updateLanguageTexts();
});

themeSelect.addEventListener("change", () => {
  applyTheme(parseInt(themeSelect.value));
});

backToMenuButton.addEventListener("click", () => {
  lockBoard = true;
  showPage(mainMenu);
});

window.onload = () => {
  showPage(mainMenu);
  revealTimeValueSpan.textContent = initialRevealTimeInput.value;
  updateLanguageTexts();
  applyTheme(gameSettings.themeIndex);
};

// Utility
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

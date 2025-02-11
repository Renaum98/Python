let board = Array(9).fill(null); // Represents the Tic-Tac-Toe board
let currentPlayer = 'X'; // X starts
let gameOver = false;
let mode = '2'; // Default to 2-player mode
let gameStatusElement = document.getElementById('game-status');
let cells = document.querySelectorAll('.cell');
let resetButton = document.getElementById('reset-button');
let gameModeSelect = document.getElementById('game-mode');
let toggleModeButton = document.getElementById('toggle-mode');

// Initialize event listeners
cells.forEach(cell => {
    cell.addEventListener('click', handleClick);
});

resetButton.addEventListener('click', resetGame);
gameModeSelect.addEventListener('change', changeGameMode);
toggleModeButton.addEventListener('click', toggleMode);

// Handle cell clicks
function handleClick(e) {
    if (gameOver || e.target.textContent !== '') return;

    let index = e.target.getAttribute('data-index');
    board[index] = currentPlayer;
    e.target.textContent = currentPlayer;

    if (checkWinner()) {
        gameStatusElement.textContent = `${currentPlayer} Wins!`;
        gameOver = true;
        return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    if (mode === '1' && currentPlayer === 'O' && !gameOver) {
        setTimeout(computerMove, 500);
    }
    if (!board.includes(null)) {
        gameStatusElement.textContent = "It's a draw!";
        gameOver = true;
    }
}

// Computer move for 1-player mode
function computerMove() {
    if (gameOver) return;

    let availableMoves = board.map((val, index) => val === null ? index : null).filter(val => val !== null);
    let randomMove = availableMoves[Math.floor(Math.random() * availableMoves.length)];
    board[randomMove] = 'O';
    document.querySelector(`[data-index="${randomMove}"]`).textContent = 'O';

    if (checkWinner()) {
        gameStatusElement.textContent = "O Wins!";
        gameOver = true;
        return;
    }

    currentPlayer = 'X';
}

// Check for winner
function checkWinner() {
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]             // Diagonals
    ];

    return winningCombinations.some(combination => {
        const [a, b, c] = combination;
        return board[a] && board[a] === board[b] && board[a] === board[c];
    });
}

// Reset the game
function resetGame() {
    board = Array(9).fill(null);
    currentPlayer = 'X';
    gameOver = false;
    gameStatusElement.textContent = '';
    cells.forEach(cell => {
        cell.textContent = '';
    });
}

// Change game mode (1 or 2 players)
function changeGameMode(e) {
    mode = e.target.value;
    resetGame();
}

// Toggle light/dark mode
function toggleMode() {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
    let currentMode = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    toggleModeButton.textContent = currentMode === 'dark' ? 'Modo Claro' : 'Modo Escuro';
}

// Set initial mode
document.body.classList.add('light-mode');

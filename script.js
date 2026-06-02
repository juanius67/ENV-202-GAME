// Global Variables
let allQuestions = [];
let currentQuestionPool = [];
let score = 0;
let timeLeft = 60;
let timer;
let currentOptions = [];
let correctAnswer = "";
let isBossMode = false;

// DOM Elements
const scoreEl = document.getElementById('score');
const timeEl = document.getElementById('time');
const timeContainer = document.getElementById('time-container');
const cardEl = document.getElementById('card');
const optionsContainer = document.getElementById('options-container');
const gameUI = document.getElementById('game-ui');
const startScreen = document.getElementById('start-screen');
const endScreen = document.getElementById('end-screen');
const subtitle = document.getElementById('subtitle');
const gameContainer = document.getElementById('game-container');
const examTimerEl = document.getElementById('countdown-timer');

// Init
window.onload = async () => {
    initExamCountdown();
    await loadServerData();
    await fetchQuestions();
};

// Exam Countdown Logic
function initExamCountdown() {
    const examDate = new Date("2026-06-29T09:15:00").getTime();

    const updateTimer = () => {
        const now = new Date().getTime();
        const distance = examDate - now;

        if (distance < 0) {
            examTimerEl.innerHTML = "EXAM TIME!";
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        examTimerEl.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }, 1000);
}

// Backend Communication
async function loadServerData() {
    try {
        const response = await fetch('/api/load');
        const data = await response.json();
        document.getElementById('menu-streak').innerText = data.streak || 0;
        document.getElementById('menu-high-score').innerText = data.high_score || 0;
    } catch (e) {
        console.error("Could not load save data from server:", e);
    }
}

async function saveScoreToServer(finalScore) {
    try {
        const response = await fetch('/api/save', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ score: finalScore })
        });
        const result = await response.json();
        if (result.status === "success") {
            // Update menu with new data
            document.getElementById('menu-streak').innerText = result.data.streak;
            document.getElementById('menu-high-score').innerText = result.data.high_score;
            document.getElementById('end-streak-msg').classList.remove('hidden');
        }
    } catch (e) {
        console.error("Could not save to server:", e);
    }
}

// Question Loading
async function fetchQuestions() {
    try {
        const res = await fetch('questions.json');
        allQuestions = await res.json();
    } catch (e) {
        console.error("Failed to load questions:", e);
        cardEl.innerText = "Error loading questions.json";
    }
}

// Game Logic
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function startGame() {
    if (allQuestions.length === 0) return;

    // Reset State
    score = 0;
    timeLeft = 60;
    currentQuestionPool = [...allQuestions];
    shuffle(currentQuestionPool);

    // UI Resets
    updateScoreDisplay();
    timeEl.innerText = timeLeft;
    timeContainer.classList.remove('time-warning');
    document.getElementById('end-streak-msg').classList.add('hidden');

    // Screen Toggles
    startScreen.classList.add('hidden');
    endScreen.classList.add('hidden');
    subtitle.classList.add('hidden');
    gameUI.classList.remove('hidden');
    gameContainer.classList.add('wiggle');

    nextQuestion();
    timer = setInterval(updateTime, 1000);
}

function updateTime() {
    timeLeft--;
    timeEl.innerText = timeLeft;

    if (timeLeft <= 10) {
        timeContainer.classList.add('time-warning');
    } else {
        timeContainer.classList.remove('time-warning');
    }

    if (timeLeft <= 0) {
        endGame();
    }
}

function nextQuestion() {
    if (currentQuestionPool.length === 0) {
        // Reshuffle if out of questions
        currentQuestionPool = [...allQuestions];
        shuffle(currentQuestionPool);
    }

    const qData = currentQuestionPool.pop();
    correctAnswer = qData.c;
    isBossMode = qData.type === "boss";

    // Set UI for Boss Mode
    if (isBossMode) {
        gameContainer.classList.add('boss-mode');
        cardEl.innerHTML = `<div class="boss-badge">BOSS BATTLE: ${qData.module}</div>` + qData.q;
    } else {
        gameContainer.classList.remove('boss-mode');
        cardEl.innerText = qData.q;
    }

    // Prepare options
    currentOptions = [qData.c, ...qData.w];
    shuffle(currentOptions);

    // Render buttons
    optionsContainer.innerHTML = '';
    currentOptions.forEach((opt, index) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.id = `btn-${index}`;
        btn.setAttribute('data-key', index + 1);
        btn.innerText = opt;
        btn.onclick = () => handleAnswer(opt, btn);
        optionsContainer.appendChild(btn);
    });
}

function handleAnswer(selected, buttonEl) {
    if (!buttonEl) return;

    if (selected === correctAnswer) {
        // Correct
        const points = isBossMode ? 15 : 5;
        const timeBonus = isBossMode ? 8 : 3;

        score += points;
        timeLeft += timeBonus;
        buttonEl.classList.add('flash-correct');
        updateEffects();
    } else {
        // Wrong
        const timePenalty = isBossMode ? 10 : 5;
        timeLeft -= timePenalty;
        buttonEl.classList.add('flash-wrong');

        // Show correct answer briefly by flashing it green
        const correctBtnIndex = currentOptions.indexOf(correctAnswer);
        if(correctBtnIndex !== -1) {
            document.getElementById(`btn-${correctBtnIndex}`).style.borderColor = '#10b981';
        }
    }

    timeEl.innerText = timeLeft;

    // Brief delay to see the flash before next question
    setTimeout(() => {
        if (timeLeft > 0) nextQuestion();
        else endGame();
    }, 600);
}

function updateScoreDisplay() {
    const scoreStr = score.toString();
    let html = '';
    for (let char of scoreStr) {
        html += `<span class="shake-char">${char}</span>`;
    }
    scoreEl.innerHTML = html;
}

function updateEffects() {
    updateScoreDisplay();

    // Intensity scales up to 100 points
    const intensityScale = Math.min(score / 100, 1);

    const pxShake = (intensityScale * 5).toFixed(1);
    const degShake = (intensityScale * 2).toFixed(1);

    document.documentElement.style.setProperty('--shake-intensity', `${pxShake}px`);
    document.documentElement.style.setProperty('--shake-deg', `${degShake}deg`);

    if(!isBossMode) {
        if(score > 50) {
             document.documentElement.style.setProperty('--box-shadow-color', `rgba(236, 72, 153, ${0.2 + (intensityScale * 0.5)})`);
        } else {
             document.documentElement.style.setProperty('--box-shadow-color', `rgba(0, 255, 136, ${0.2 + (intensityScale * 0.5)})`);
        }
    }
}

function endGame() {
    clearInterval(timer);

    // Save to Python server
    saveScoreToServer(score);

    // UI updates
    gameUI.classList.add('hidden');
    endScreen.classList.remove('hidden');
    subtitle.classList.remove('hidden');

    // Reset effects
    gameContainer.classList.remove('wiggle');
    gameContainer.classList.remove('boss-mode');
    document.documentElement.style.setProperty('--shake-intensity', `0px`);
    document.documentElement.style.setProperty('--shake-deg', `0deg`);
    document.documentElement.style.setProperty('--box-shadow-color', `rgba(0, 255, 136, 0.2)`);

    document.getElementById('end-score').innerText = score;
}

function returnToMenu() {
    endScreen.classList.add('hidden');
    startScreen.classList.remove('hidden');
}

// Keyboard Mapping
document.addEventListener('keydown', (e) => {
    if (gameUI.classList.contains('hidden')) return;
    const key = e.key;
    if (['1', '2', '3', '4'].includes(key)) {
        const index = parseInt(key) - 1;
        if(index < currentOptions.length) {
            handleAnswer(currentOptions[index], document.getElementById(`btn-${index}`));
        }
    }
});

const inputBox = document.querySelectorAll('.input-field');
const button = document.querySelector('.submit-button');
const Attempts = document.getElementById('attempts');
const resultsDiv = document.getElementById('results'); 
const gameResultImg = document.getElementById('game-result-img');
const AttemptsDiv = document.querySelector('.remaining-attempts');

// 0~9 숫자 중 3개의 난수 설정
let computer = [];
while (computer.length < 3) {
    const randomNumber = Math.floor(Math.random() * 10);
    if (!computer.includes(randomNumber)) {
        computer.push(randomNumber);
    }
}

// 시도 횟수 초기 화면에서 9로 설정
let attemptsLeft = 9;
Attempts.innerText = attemptsLeft;

function check_numbers() {
    const userNumbers = Array.from(inputBox).map(input => input.value);

    // 입력값이 비어 있는지 확인
    if (userNumbers.includes("")) {
        inputBox.forEach(input => (input.value = "")); 
        return;
    }

    let strikes = 0;
    let balls = 0;
    const checkedIndexes = []; 

    // 스트라이크 계산
    userNumbers.forEach((num, index) => {
        const userNum = Number(num);
        if (computer[index] === userNum) {
            strikes++; 
            checkedIndexes.push(index); 
        }
    });

    // 볼 계산
    userNumbers.forEach((num, index) => {
        const userNum = Number(num);
        if (computer.includes(userNum) && computer.indexOf(userNum) !== index && !checkedIndexes.includes(computer.indexOf(userNum)) ) {
            balls++; 
            checkedIndexes.push(computer.indexOf(userNum)); 
        }
    });


    // 결과 출력
    const resultText = document.createElement('div');

    if (strikes === 0 && balls === 0) {
        const userNumbersText = document.createTextNode(`${userNumbers.join(' ')} : `);
        const oText = document.createTextNode('O');
        const oSpan = document.createElement('span');
        oSpan.style.color = 'red';
        oSpan.style.fontWeight = 'bold';
        oSpan.appendChild(oText);

        resultText.appendChild(userNumbersText);
        resultText.appendChild(oSpan);
    } else {
        const userNumbersText = document.createTextNode(`${userNumbers.join(' ')} : `);

        const strikeSpan = document.createElement('span');
        strikeSpan.style.color = 'green';
        strikeSpan.style.fontWeight = 'bold';
        strikeSpan.textContent = `${strikes} S`;

        const spaceText = document.createTextNode(' ');

        const ballSpan = document.createElement('span');
        ballSpan.style.color = 'orange';
        ballSpan.style.fontWeight = 'bold';
        ballSpan.textContent = `${balls} B`;

        resultText.appendChild(userNumbersText);
        resultText.appendChild(strikeSpan);
        resultText.appendChild(spaceText);
        resultText.appendChild(ballSpan);
    }

    resultsDiv.appendChild(resultText);


    // 시도 횟수 감소
    attemptsLeft--;
    Attempts.innerText = attemptsLeft;

    // 승리 조건 
    if (strikes === 3) {
        gameResultImg.src = "./success.png"; 
        AttemptsDiv.style.display = 'none';
        button.disabled = true; 
        inputBox.forEach(input => (input.value = ""));
        return;
    }

    // 패배 조건 
    if (attemptsLeft === 0 && strikes < 3) {
        gameResultImg.src = "./fail.png"; 
        AttemptsDiv.style.display = 'none';
        button.disabled = true; 
        inputBox.forEach(input => (input.value = ""));
        return;
    }


    inputBox.forEach(input => (input.value = ""));
}

button.addEventListener('click', check_numbers);

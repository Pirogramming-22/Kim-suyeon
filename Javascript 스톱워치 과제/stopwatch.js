let tenMillis = 0;
let seconds = 0;

const appendTens = document.querySelector('#tenMillis');
const appendSeconds = document.querySelector('#seconds');
const buttonStart = document.querySelector('.stopwatchButtonStart');
const buttonStop = document.querySelector('.stopwatchButtonStop');
const buttonReset = document.querySelector('.stopwatchButtonReset');
const recordList = document.querySelector('.recordLetter');
const deleteButton = document.querySelector('.recordElement svg');

/* 버튼 start 기능 */
buttonStart.addEventListener('click', () => {
    intervalId = setInterval(operateTimer,10)
});

/* 버튼 stop 기능 */
buttonStop.addEventListener('click', () => {
    clearInterval(intervalId)
    addRecord()
});

/*버튼 reset 기능 */
buttonReset.addEventListener('click', () => {
    clearInterval(intervalId)
    tenMillis=0;
    seconds=0;
    appendTens.textContent="00"
    appendSeconds.textContent="00"
});


function operateTimer() {
    tenMillis++;
    appendTens.textContent = tenMillis
    if (tenMillis > 9) {
        tenMillis
    } else {
        '0' + tenMillis
    } 
    if(tenMillis>99) {
        seconds++;
        appendSeconds.textContent=seconds > 9 ? seconds : '0' + seconds
        if (seconds > 9) {
            seconds
        } else {
            '0' + seconds
        } 
        tenMillis=0
        appendTens = "00"
    }
};




/*구간 기록 기능*/
function addRecord() {
    const recordItem = document.createElement('li');
    recordItem.style.display = 'flex';
    recordItem.style.marginBottom = '10px';
    recordItem.style.flexDirection = 'row-reverse';

    // 버튼 생성
    const recordCheck = document.createElement('button');
    recordCheck.style.position = 'relative';
    recordCheck.style.width = '1.2rem';
    recordCheck.style.height = '1.2rem';
    recordCheck.style.borderRadius = '50%';
    recordCheck.style.backgroundColor = 'transparent';
    recordCheck.style.border = '2px solid black';
    recordCheck.style.margin = '3px 60px 0 0';

    const formattedTime = `${seconds > 9 ? seconds : '0' + seconds}:${tenMillis > 9 ? tenMillis : '0' + tenMillis}`;
    recordItem.textContent = `${formattedTime}`;
    recordList.appendChild(recordItem);
    recordItem.appendChild(recordCheck);

    // 버튼 클릭시 체크 모양 등장
    recordCheck.addEventListener('click', () => {
        let svgImage = recordCheck.querySelector('img');
        if (!svgImage) {
            const svgFilePath = 'check.svg';
            svgImage = document.createElement('img');
            svgImage.src = svgFilePath;
            svgImage.style.position = 'absolute';
            svgImage.style.top = '5%';
            svgImage.style.left = '5%';
            svgImage.classList.add('checked');
            recordCheck.appendChild(svgImage);
        } else {
            svgImage.remove();
        }
    });   
}


/* 삭제 기능*/
deleteButton.addEventListener('click', () => {
    const recordItems = document.querySelectorAll('.recordLetter li'); 
    recordItems.forEach((recordItem) => {
        const svgImage = recordItem.querySelector('button img');
        if (svgImage && svgImage.classList.contains('checked')) {
            recordItem.remove(); 
        }
    });
});


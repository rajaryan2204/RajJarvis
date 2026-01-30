// ============================
// SEND TEXT (OPTIONAL - IF INPUT BOX EXISTS)
// ============================
function addMessage(sender, text){

    const chat = document.getElementById("chat");

    if(!chat) return;

    const msg = document.createElement("div");

    msg.innerHTML = `<b>${sender}:</b> ${text}`;

    msg.style.margin = "6px 0";

    chat.appendChild(msg);

    chat.scrollTop = chat.scrollHeight;
}

function sendText(){

    let inp = document.getElementById("textInput");

    if(!inp) return;

    let txt = inp.value.trim();

    if(!txt) return;

    // Send to Python
    window.pywebview.api.process(txt);

    inp.value = "";
}



// ============================
// AUDIO VISUALIZER
// ============================

let audioCtx;
let analyser;
let mic;
let dataArray;

const canvas = document.getElementById("visualizer");
const ctx = canvas.getContext("2d");


// Resize canvas
function resizeCanvas(){

    if(!canvas) return;

    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}

window.addEventListener("resize", resizeCanvas);



// Start mic visualizer
function startVisualizer(){

    navigator.mediaDevices.getUserMedia({ audio: true })

    .then(stream => {

        audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        analyser = audioCtx.createAnalyser();

        mic = audioCtx.createMediaStreamSource(stream);

        mic.connect(analyser);

        analyser.fftSize = 256;

        let bufferLength = analyser.frequencyBinCount;

        dataArray = new Uint8Array(bufferLength);

        draw();

    })

    .catch(err => {

        console.log("Mic error:", err);

        alert("Microphone permission denied!");

    });
}



// Draw animation
function draw(){

    requestAnimationFrame(draw);

    if(!analyser) return;

    analyser.getByteFrequencyData(dataArray);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    let barWidth = canvas.width / dataArray.length;

    let x = 0;


    for(let i = 0; i < dataArray.length; i++){

        let barHeight = dataArray[i] / 2;

        ctx.fillStyle = "#00fff7";

        ctx.fillRect(
            x,
            canvas.height - barHeight,
            barWidth - 1,
            barHeight
        );

        x += barWidth;
    }
}



// ============================
// AUTO START
// ============================

window.onload = () => {

    resizeCanvas();

    startVisualizer();

};

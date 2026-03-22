const video = document.getElementById("webcam");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const fpsDisplay = document.getElementById("fps");

let lastTime = performance.now();
let frameCount = 0;

// Setup Webcam
async function setupWebcam() {
    const stream = await navigator.mediaDevices.getUserMedia({
        video: true
    });

    video.srcObject = stream;

    return new Promise((resolve) => {
        video.onloadedmetadata = () => {
            video.play();
            resolve(video);
        };
    });
}

// FPS Calculation
function updateFPS() {
    frameCount++;
    const now = performance.now();
    const diff = now - lastTime;

    if (diff >= 1000) {
        const fps = frameCount;
        fpsDisplay.innerText = "FPS: " + fps;

        frameCount = 0;
        lastTime = now;
    }
}

// Classification Loop
async function classifyFrame(model) {
    const predictions = await model.classify(video);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.font = "20px Arial";
    ctx.fillStyle = "red";

    // Show Top 3 predictions
    predictions.slice(0, 3).forEach((pred, index) => {
        ctx.fillText(
            `${pred.className} (${(pred.probability * 100).toFixed(2)}%)`,
            10,
            30 + index * 30
        );
    });

    updateFPS();

    requestAnimationFrame(() => classifyFrame(model));
}

// Main
async function main() {
    await setupWebcam();
    console.log("Webcam started");

    const model = await mobilenet.load();
    console.log("MobileNet Loaded");

    classifyFrame(model);
}

main();
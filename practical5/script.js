const video = document.getElementById("webcam");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

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

async function loadModel() {
    console.log("Loading model...");
    const model = await cocoSsd.load();
    console.log("Model Loaded!");
    return model;
}

async function detectFrame(video, model) {
    const predictions = await model.detect(video);

    // Clear previous frame
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.font = "16px Arial";
    ctx.textBaseline = "top";

    predictions.forEach(prediction => {
        const [x, y, width, height] = prediction.bbox;

        // Draw bounding box
        ctx.strokeStyle = "#00FFFF";
        ctx.lineWidth = 2;
        ctx.strokeRect(x, y, width, height);

        // Draw label background
        ctx.fillStyle = "#00FFFF";
        const text = `${prediction.class} (${Math.round(prediction.score * 100)}%)`;
        const textWidth = ctx.measureText(text).width;
        const textHeight = 16;

        ctx.fillRect(x, y, textWidth + 4, textHeight + 4);

        // Draw text
        ctx.fillStyle = "#000000";
        ctx.fillText(text, x + 2, y + 2);
    });

    requestAnimationFrame(() => {
        detectFrame(video, model);
    });
}

async function main() {
    await setupWebcam();
    console.log("Webcam started");

    const model = await loadModel();

    detectFrame(video, model);
}

main();
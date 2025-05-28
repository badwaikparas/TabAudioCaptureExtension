let recorder = null;
let chunks = [];
let stream = null;
let isRecording = false;

function saveToFile(blob, name) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";
    a.href = url;
    a.download = name;
    a.click();
    URL.revokeObjectURL(url);
    a.remove();
}

function startRecordingTabAudio(button) {
    chrome.tabCapture.capture({ audio: true, video: false }, (capturedStream) => {
        stream = capturedStream;

        const context = new AudioContext();
        const newStream = context.createMediaStreamSource(stream);
        newStream.connect(context.destination); // Allow audio playback

        recorder = new MediaRecorder(stream);
        chunks = [];

        recorder.ondataavailable = (e) => {
            chunks.push(e.data);
        };

        recorder.onstop = () => {
            saveToFile(new Blob(chunks), "test.wav");
            stream.getTracks().forEach(track => track.stop()); // Stop capturing tab
            stream = null;
            button.textContent = "Start Recording";
            isRecording = false;
        };

        recorder.start();
        isRecording = true;
        button.textContent = "Stop Recording";
    });
}

function stopRecording() {
    if (recorder && isRecording) {
        recorder.stop();
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById("share-audio-button");
    button.addEventListener("click", function () {
        if (!isRecording) {
            startRecordingTabAudio(button);
        } else {
            stopRecording();
        }
    });
});

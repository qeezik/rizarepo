const video = document.getElementById('video');
const playPauseBtn = document.getElementById('playPauseBtn');
const stopBtn = document.getElementById('stopBtn');
const seekBar = document.getElementById('seekBar');
const fullScreenBtn = document.getElementById('fullScreenBtn');

// Play/Pause video
playPauseBtn.addEventListener('click', () => {
    if (video.paused) {
        video.play();
        playPauseBtn.textContent = 'Pause';
    } else {
        video.pause();
        playPauseBtn.textContent = 'Play';
    }
});

// Stop video
stopBtn.addEventListener('click', () => {
    video.pause();
    video.currentTime = 0;
    playPauseBtn.textContent = 'Play';
});

// Update seek bar as video plays
video.addEventListener('timeupdate', () => {
    seekBar.value = (video.currentTime / video.duration) * 100;
});

// Seek video when seeking bar value changes
seekBar.addEventListener('input', () => {
    video.currentTime = (seekBar.value / 100) * video.duration;
});

// Fullscreen toggle
fullScreenBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
        video.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
});
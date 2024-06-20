document.addEventListener("DOMContentLoaded", function () {
    var audio = document.getElementById('background-sound');
    var playButton = document.getElementById('play-button');

    playButton.addEventListener('click', function () {
        audio.play().catch(function (error) {
            console.log('Playback was prevented:', error);
        });
    });
});
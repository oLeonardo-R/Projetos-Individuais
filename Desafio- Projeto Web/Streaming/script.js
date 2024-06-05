const video = document.getElementById("meuVideo");
const btnAudio = document.getElementById("btnAudio");

btnAudio.addEventListener("click", () => {
  if (video.muted) {
    video.muted = false;
    btnAudio.textContent = "Mudo";
  } else {
    video.muted = true;
    btnAudio.textContent = "Som";
  }
});

// ... (Em contrução) ...

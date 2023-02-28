const message = document.querySelector(".message");

if(message) {
    setTimeout(function() {
        message.style.display = "none";
    }, 3000);
}


// django channels
function addMessage(message, sender) {
    let chatBox = document.getElementById("chat-box");
    let msgDiv = document.createElement("div");
    msgDiv.className = sender === "user" ? "user-message" : "bot-message";
    msgDiv.innerText = message;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addOptions(options) {
    let chatBox = document.getElementById("chat-box");

    options.forEach(option => {
        let btn = document.createElement("button");
        btn.className = "option-btn";
        btn.innerText = option;
        btn.onclick = function() {
            sendToServer(option);
        };
        chatBox.appendChild(btn);
    });
}

function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;
    if(message.trim() === "") return;
    addMessage(message, "user");
    sendToServer(message);
    input.value = "";
}

function sendToServer(message) {
    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.reply, "bot");
        if(data.options.length > 0){
            addOptions(data.options);
        }
    });
}

window.onload = function(){
    sendToServer("start");
}
 
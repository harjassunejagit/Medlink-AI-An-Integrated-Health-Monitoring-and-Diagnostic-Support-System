// ---------------- CHATBOT ----------------

function sendMessage() {
    let msg = document.getElementById("msg").value;

    if (!msg) return;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        let chatbox = document.getElementById("chatbox");

        chatbox.innerHTML += 
            "<p class='user-message'><b>You:</b> " + msg + "</p>" +
            "<p class='bot-message'><b>Bot:</b> " + data.response + "</p>";

        document.getElementById("msg").value = "";
        chatbox.scrollTop = chatbox.scrollHeight;
    });
}

// ---------------- DISEASE PREDICTION ----------------

function predictDisease() {

    const data = {
        age: parseFloat(document.getElementById("age").value),
        sex: parseFloat(document.getElementById("sex").value),
        cp: parseFloat(document.getElementById("cp").value),
        trestbps: parseFloat(document.getElementById("trestbps").value),
        chol: parseFloat(document.getElementById("chol").value),
        fbs: parseFloat(document.getElementById("fbs").value),
        restecg: parseFloat(document.getElementById("restecg").value),
        thalach: parseFloat(document.getElementById("thalach").value),
        exang: parseFloat(document.getElementById("exang").value),
        oldpeak: parseFloat(document.getElementById("oldpeak").value),
        slope: parseFloat(document.getElementById("slope").value),
        ca: parseFloat(document.getElementById("ca").value),
        thal: parseFloat(document.getElementById("thal").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {

        if (result.error) {
            alert("Error: " + result.error);
            return;
        }

        const card = document.getElementById("resultCard");
        const riskBar = document.getElementById("riskBar");

        card.style.display = "block";

        document.getElementById("riskTitle").innerText = result.prediction;
        document.getElementById("confidence").innerText = result.confidence_percentage;
        document.getElementById("explanation").innerText = result.explanation;

        // Animate confidence bar
        riskBar.style.width = result.confidence_percentage + "%";

        if (result.prediction === "Low Risk") {
            riskBar.style.background = "#16a34a"; // Green
        } 
        else if (result.prediction === "Moderate Risk") {
            riskBar.style.background = "#f59e0b"; // Orange
        } 
        else {
            riskBar.style.background = "#dc2626"; // Red
        }
    })
    .catch(error => {
        console.error(error);
        alert("Server error occurred.");
    });
}


// ---------------- REPORT UPLOAD ----------------

document.addEventListener("DOMContentLoaded", function () {

    let uploadForm = document.getElementById("uploadForm");

    if (uploadForm) {

        uploadForm.addEventListener("submit", function (e) {

            e.preventDefault();

            let formData = new FormData();
            formData.append("file", document.getElementById("file").files[0]);

            fetch("/upload", {
                method: "POST",
                body: formData
            })
            .then(res => res.json())
            .then(data => {

                document.getElementById("reportResult").innerHTML =
                    "<pre>" + JSON.stringify(data, null, 2) + "</pre>";

            });
        });
    }

});

// ---------------- LOCATION ----------------

function getLocation() {

    if (!navigator.geolocation) {
        alert("Geolocation not supported by your browser.");
        return;
    }

    navigator.geolocation.getCurrentPosition(position => {

        fetch("/nearby", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                lat: position.coords.latitude,
                lng: position.coords.longitude
            })
        })
        .then(res => res.json())
        .then(data => {

            alert("Nearby Hospitals:\n\n" + JSON.stringify(data, null, 2));

        });

    });

}

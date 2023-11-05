let Globaldata = ""

window.onload = init;
let serverAddress;

const div_MeasurementA = document.getElementById("MeasurementA");
const div_MeasurementB = document.getElementById("MeasurementB");
const div_lastTime = document.getElementById("time");
const canvas = document.getElementById("pendulumCanvas");
const canvas_context = canvas.getContext("2d");


function loadData() {
    getJson(serverAddress + "api/data");
    updateScreen();
    
}

function init() {
    console.log("start")
    serverAddress = getAddress();
    window.setInterval(loadData, 200);
}


function getAddress() {
    tmpAddress = window.location.href;
    if (tmpAddress.search("#") === (tmpAddress.length - 1)) {
        answer = tmpAddress.slice(0, tmpAddress.length - 1);
        return answer
    } else {
        return tmpAddress
    }
}

function updateScreen() {
    div_MeasurementA.innerHTML = "A: " + Globaldata.status.currentA + "- DEG: " + calcDegree(Globaldata.status.currentA);
    div_MeasurementB.innerHTML = "B: " + Globaldata.status.currentB;
    div_lastTime.innerHTML = "Time: " + Globaldata.status.lastTime;
    //canvas_context.rotate((calcDegree(Globaldata.status.currentA) * Math.PI / 180) * -1);
    canvas_context.fillStyle = "red";
    canvas_context.fillRect(0, 0, 300, 300);
    canvas_context.fillStyle = "black";
    canvas_context.beginPath();
    canvas_context.arc(150, 150, 20, 0, 2 * Math.PI);
    canvas_context.stroke();

    let x = 150 + 50 * Math.cos((calcDegree(Globaldata.status.currentA) * Math.PI / 180) *0.017);

    let y = 150 + 50 * Math.sin((calcDegree(Globaldata.status.currentA) * Math.PI / 180) *0.017);

    canvas_context.beginPath();
    canvas_context.arc(x, y, 10, 0, 2 * Math.PI);
    canvas_context.stroke();

   
}

async function getJson(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("HTTP error" + response.status);
            }
            return response.json();
        })
        .then(json => {
            Globaldata = json
        })
        .catch(() => {
            this.dataError = true;
        })

}

function calcDegree(voltage, divider = 2, angle = 90) {
    return (voltage/divider)*100
}

function calcPercent(current, fulllength) {
    let wert=0;
    if (fulllength !== 0) {
        wert = current / fulllength
        wert = wert * 100
        Math.trunc(wert)
    }
    return wert.toString()
}

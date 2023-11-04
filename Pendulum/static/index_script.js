let Globaldata = ""

window.onload = init;
let serverAddress;

const div_MeasurementA = document.getElementById("MeasurementA");
const div_MeasurementB = document.getElementById("MeasurementB");
const div_lastTime = document.getElementById("time");


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
    div_MeasurementA.innerHTML ="A: " + Globaldata.status.currentA;
    div_MeasurementB.innerHTML = "B: " + Globaldata.status.currentB;
    div_lastTime.innerHTML = "Time: " + Globaldata.status.lastTime;
}

async function getJson(url) {
    fetch(url)
        .then(response => {
            console.log(response)
            if (!response.ok) {
                throw new Error("HTTP error" + response.status);
            }
            return response.json();
        })
        .then(json => {
            Globaldata = json
            console.log(Globaldata)
        })
        .catch(() => {
            this.dataError = true;
        })

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

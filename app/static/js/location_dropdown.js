let statesData = [];

let mandalData = {};

let villageData = {};


// ================= LOAD STATES + DISTRICTS =================

fetch('/static/data/india_states_districts.json')

.then(response => response.json())

.then(data => {

    console.log(
        "States Loaded:",
        data
    );

    statesData = data.states;

    loadStates();

})

.catch(error => {

    console.error(
        "State JSON Error:",
        error
    );

});


// ================= LOAD MANDALS =================

fetch('/static/data/telangana_mandals.json')

.then(response => response.json())

.then(data => {

    console.log(
        "Mandals Loaded:",
        data
    );

    mandalData = data;

})

.catch(error => {

    console.error(
        "Mandal JSON Error:",
        error
    );

});


// ================= LOAD VILLAGES =================

fetch('/static/data/telangana_villages.json')

.then(response => response.json())

.then(data => {

    console.log(
        "Villages Loaded:",
        data
    );

    villageData = data;

})

.catch(error => {

    console.error(
        "Village JSON Error:",
        error
    );

});


// ================= LOAD STATES =================

function loadStates() {

    const stateSelect =
        document.getElementById('state');

    statesData.forEach(item => {

        let option =
            document.createElement('option');

        option.value = item.state;

        option.textContent = item.state;

        stateSelect.appendChild(option);

    });

}


// ================= STATE CHANGE =================

document.getElementById('state')

.addEventListener('change', function () {

    const selectedState =
        this.value;

    const districtSelect =
        document.getElementById('district');

    districtSelect.innerHTML =
        '<option value="">Select District</option>';


    document.getElementById('mandal').innerHTML =
        '<option value="">Select Mandal</option>';


    document.getElementById('village').innerHTML =
        '<option value="">Select Village</option>';


    document.getElementById('assembly').value =
        '';

    document.getElementById('parliament').value =
        '';


    const stateObj =
        statesData.find(
            item => item.state === selectedState
        );

    if (!stateObj) {

        return;

    }


    stateObj.districts.forEach(district => {

        let option =
            document.createElement('option');

        option.value = district;

        option.textContent = district;

        districtSelect.appendChild(option);

    });

});


// ================= DISTRICT CHANGE =================

document.getElementById('district')

.addEventListener('change', function () {

    const district =
        this.value;

    const mandalSelect =
        document.getElementById('mandal');

    mandalSelect.innerHTML =
        '<option value="">Select Mandal</option>';


    document.getElementById('village').innerHTML =
        '<option value="">Select Village</option>';


    document.getElementById('assembly').value =
        '';

    document.getElementById('parliament').value =
        '';


    const mandals =
        mandalData[district];

    if (!mandals) {

        return;

    }


    mandals.forEach(mandal => {

        let option =
            document.createElement('option');

        option.value = mandal;

        option.textContent = mandal;

        mandalSelect.appendChild(option);

    });

});


// ================= MANDAL CHANGE =================

document.getElementById('mandal')

.addEventListener('change', function () {

    const district =
        document.getElementById('district').value;

    const mandal =
        this.value;

    const villageSelect =
        document.getElementById('village');

    villageSelect.innerHTML =
        '<option value="">Select Village</option>';


    document.getElementById('assembly').value =
        '';

    document.getElementById('parliament').value =
        '';


    if (
        !villageData[district] ||
        !villageData[district][mandal]
    ) {

        return;

    }


    const villages =
        villageData[district][mandal].villages;


    Object.keys(villages)

    .forEach(village => {

        let option =
            document.createElement('option');

        option.value = village;

        option.textContent = village;

        villageSelect.appendChild(option);

    });

});


// ================= VILLAGE CHANGE =================

document.getElementById('village')

.addEventListener('change', function () {

    const district =
        document.getElementById('district').value;

    const mandal =
        document.getElementById('mandal').value;

    const village =
        this.value;


    if (
        !villageData[district] ||
        !villageData[district][mandal]
    ) {

        return;

    }


    const villageInfo =
        villageData[district][mandal]
        .villages[village];


    document.getElementById('assembly')
    .value =
        villageInfo.assembly;


    document.getElementById('parliament')
    .value =
        villageInfo.parliament;

});
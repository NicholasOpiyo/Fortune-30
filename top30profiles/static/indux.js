
// This function obtains the value selected on the form and uses the value to set the form's 'action' attribute
function requestIndustry() {
        let listedIndustries = document.getElementById("industry");
        let selectedIndustry = listedIndustries.selectedIndex;
        let theForm = document.getElementById('fm');
        let desiredIndustry = '';
        if (selectedIndustry === 0) {
            desiredIndustry = '';
        } else {
            desiredIndustry = 'industries/' + listedIndustries.options[selectedIndustry].value;
        }
        theForm.setAttribute('action', desiredIndustry);
    }



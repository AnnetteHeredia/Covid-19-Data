//Load the available selections on page load
statesList = Array("AL","AK","AR", "AS","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY");

function loadPage(){
    //populate states list into state dropdown
    for (i=0; i<statesList.length; i++){
        state = statesList[i];
        d3.select("#State_Drop_Down_tag").append('option').attr('value', state).text(state);
    }
}

function getCharts(jsonData){
    //Get the chart values from the JSON string
    dates = jsonData.map(item => item.date);
    totCases = jsonData.map(item => item.total_cases);
    newCases = jsonData.map(item => item.new_cases);
    totDeaths = jsonData.map(item => item.total_deaths);
    newDeaths = jsonData.map(item => item.new_deaths);

    //build a placeholder for final data
    data_list = Array();

    //gather the checkboxes from the control line by element ID
    var total_cases = document.getElementById('total_Cases');
    var new_Cases = document.getElementById('new_Cases');
    var total_Deaths = document.getElementById('total_Deaths');
    var new_Deaths = document.getElementById('new_Deaths');

    //build the traces for each set of data
    if (total_cases.checked){
        total_case_trace = {
            x: dates,
            y: totCases,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Cases'
        };
        data_list.push(total_case_trace);
    };
    if (new_Cases.checked){
        new_cases_trace = {
            x: dates,
            y: newCases,
            mode: 'lines',
            type: 'scatter',
            name: 'New Cases'
        };
        data_list.push(new_cases_trace);
    };
    if (total_Deaths.checked){
        total_deaths_trace = {
            x: dates,
            y: totDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Deaths'
        };
        data_list.push(total_deaths_trace);
    };
    if (new_Deaths.checked){
        new_deaths_trace = {
            x: dates,
            y: newDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'New Deaths'
        };
        data_list.push(new_deaths_trace);
    };


    //display the graph
    Plotly.newPlot('graph', data_list, {responsive:true}); 
    //NOTE: 'graph' is the id of the div tag in US_Charts_Only.html
}
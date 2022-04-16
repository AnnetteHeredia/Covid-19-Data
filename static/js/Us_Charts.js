function loadPage(locations){
    //populate states list into state dropdown
    for (i=0; i<locations.length; i++){
        state = locations[i];
        d3.select("#State_Drop_Down_tag").append('option').attr('value', state).text(state);
    }
}

function testElement(jsonData){
    dates = jsonData.map(item => item.date);
    
    test_display = d3.select('#test_result');
    test_display.append("p").text(dates);

    console.log(dates);
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

    //Create the summary chart
    //get the element from the webpage
    summary_table_div = d3.select("#summary_data");
    summary_table_div.html("");
    //create the table
    summary_table_div.append("table").attr("id","sum_table");
    summary_table = d3.select('#sum_table');
    header = summary_table.append("tr");
    header.append("th").text("State: "+jsonData[0].state+"  ");
    header.append("th").text("Start Date: "+dates[0]+"  ");
    header.append("th").text("End Date: "+dates[dates.length - 1]);

    //Populate relevant selected data
    if (total_cases.checked){
        //build the trace for Plotly chart
        total_case_trace = {
            x: dates,
            y: totCases,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Cases'
        };
        data_list.push(total_case_trace);

        //get the summary chart data
        max_tot_cases = totCases[totCases.length - 1];

        //add the summary to the summary table
        tot_case_row = summary_table.append("tr");
        tot_row_data = tot_case_row.append("th").text("Total Cases: "+max_tot_cases);
    };
    if (new_Cases.checked){
        //build the trace for the Plotly chart
        new_cases_trace = {
            x: dates,
            y: newCases,
            mode: 'lines',
            type: 'scatter',
            name: 'New Cases'
        };
        data_list.push(new_cases_trace);

        //get the summary chart data
        sum_newCases = 0;
        for(k=0;k<newCases.length;k++){
            sum_newCases = sum_newCases+newCases[k];
        }
        average_new_cases = sum_newCases/newCases.length;

        //add the summary to the summary table
        new_case_row = summary_table.append("tr");
        new_case_data = new_case_row.append("th").text("Average New Cases: "+average_new_cases);
    };
    if (total_Deaths.checked){
        //build the trace for the Plotly chart
        total_deaths_trace = {
            x: dates,
            y: totDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'Total Deaths'
        };
        data_list.push(total_deaths_trace);

        //get the summary chart data
        max_tot_deaths = totDeaths[totDeaths.length - 1];

        //add the summary to the summary table
        tot_deaths_row = summary_table.append("tr");
        tot_deaths_data = tot_deaths_row.append("th").text("Total Deaths: "+max_tot_deaths);
    };
    if (new_Deaths.checked){
        //build the trace for the Plotly chart
        new_deaths_trace = {
            x: dates,
            y: newDeaths,
            mode: 'lines',
            type: 'scatter',
            name: 'New Deaths'
        };
        data_list.push(new_deaths_trace);

        //get the summary chart data
        sum_newDeaths = 0;
        for(l=0;l<newDeaths.length;l++){
            sum_newDeaths = sum_newDeaths+newDeaths[l];
        }
        average_new_Deaths = sum_newDeaths/newDeaths.length;

        //add the summary to the summary table
        new_deaths_row = summary_table.append("tr");
        new_deaths_data = new_deaths_row.append("th").text("Average New Deaths: "+average_new_Deaths);
    };


    //display the graph
    Plotly.newPlot('graph', data_list, {responsive:true}); 
    //NOTE: 'graph' is the id of the div tag in US_Charts_Only.html
}
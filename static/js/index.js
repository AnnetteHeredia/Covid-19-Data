function loadPage(states, continents, countries){
    //populate states list into state dropdown
    for (i=0; i<states.length; i++){
        state = states[i];
        d3.select("#State_Drop_Down_tag").append('option').attr('value', state).text(state);
    }
    //populate continent list into continent dropdown
    for (i=0; i<continents.length; i++){
        continent = continents[i];
        d3.select("#Continents_Drop_Down_tag").append('option').attr('value', continent).text(continent);
    }
    //populate country list into country dropdown
    for (i=0; i<countries.length; i++){
        country = countries[i];
        d3.select("#Country_Drop_Down_tag").append('option').attr('value', country).text(country);
    }
}
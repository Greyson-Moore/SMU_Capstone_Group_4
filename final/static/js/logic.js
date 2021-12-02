$(document).ready(function() {
  
    $("#filter").click(function() {
        console.log("test")
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var acc = $("#acc").val();
    var mph = $("#mph").val();
    var range = $("#range").val();
    var seats = $("#seats").val();
    var fast_charge = $("#fast_charge").val()
    var body_style = $("#body_style").val();
    var drive = $("#drive").val();

    // create the payload
    var payload = {
        "acc": acc,
        "mph": mph,
        "range": range,
        "seats": seats,
        "body_style": body_style,
        "drive": drive,
        "fast_charge":fast_charge
    }
    
    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        
        success: function(returnedData) {
            // print it
            //console.log(returnedData);
            
           $("#output").text(`Price Prediction: $${returnedData["prediction"]}`);
           
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
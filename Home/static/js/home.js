// Getting the dom elements 
const llmModel = document.getElementById("llmModel"); 
const metrics = document.getElementById("metrics"); 
const dataPoints = document.getElementById("dataPoints"); 
const benchmarkBtn = document.getElementById("benchmarkBtn"); 
const reloadBtn = document.getElementById("reloadBtn"); 
const ctx = document.getElementById("myChart").getContext('2d'); 

// Adding event for the reload button 
reloadBtn.addEventListener("click", (event) => {
    window.location.reload();
})

// Adding event listener for the benchmark button 
benchmarkBtn.addEventListener("click", (event) => {
    // If the datapoints was empty 
    if (dataPoints.value === "") {
        alert("Data point field required")
    }

    else {
        // Setting the request headers 
        const headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST', 
            'Access-Control-Allow-Headers': 'Content-Type',
        }; 

        // Setting the data body 
        const data = JSON.stringify({
            "llmModel": llmModel.value, 
            "metrics": metrics.value, 
            "dataPoints": dataPoints.value, 
        })

        // Setting the url 
        const url = "/simulateData"; 

        // Making a fetch request to the backend server 
        fetch(url, {
            method: 'POST', 
            headers: headers, 
            body: data, 
        })
        .then((response) => response.json())
        .then((responseData) => {
            console.log(responseData);
            
            // Ploting the graph 
            const data = {
                labels: Array(responseData["data"].length).fill(''), 
                datasets: [{
                    label: `${llmModel.value}: ${metrics.value}`, 
                    data: responseData["data"], 
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderWidth: 1            
                }]
            }; 

            // Setting the configurations 
            const config = {
                type: 'line', 
                data: data, 
                options: {
                    scales: {
                        x: {
                            ticks: {
                                display: false
                            }
                        }, 
                        y: {
                            ticks: {
                                display: false
                            }
                        }
                    }
                }
            }; 

            // Plotting the graph 
            const myChart = new Chart(ctx, config); 
        })

    }
 
})
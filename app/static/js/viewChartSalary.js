
$("button").on('click', function() {
	var listYears = $('input[name="years"]:checked').map(function () {
    			return this.value;
    		}).get();
	$.getJSON('/viewChartSalary', { 
		chartType: $('select[name="chartType"]').val(),
		comparator: $('select[name="comparator"]').val(),
		years: listYears,
	}, function(data) {
		chart(data.chartType, data.listDataChart);
    });
 });

function chart(chartType, listDataChart){
	var popCanvas = document.getElementById("popChart");    
    var barChart = new Chart(popCanvas, {
        type: chartType,    
        data: {
        	labels: listDataChart[0],  
            datasets: [
                        {
                            fill: true,
                            
                            label: "average salary for",
                            
                            data: listDataChart[1],
                            
                            borderWidth: 1,
                            
                            borderColor:  'rgba(225, 225, 225, 1)',
                            
                            backgroundColor:  'rgba(225, 225, 225, 0.4)',
                        }
                ]
            }
        });
}
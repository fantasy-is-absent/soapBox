var barChart;

$("button").on('click', function() {
	var listYears = $('input[name="years"]:checked').map(function () {
		return this.value;
	}).get();
	$.getJSON('/viewChartSalary', { 
		comparator: $('select[name="comparator"]').val(),
		years: listYears,
	}, function(data) {
		chart(data.listData, data.listComparator, data.listYears);
	});
});

function chart(listData, listComparator, listYears){
	var listDatasets = [];
	for(var i = 0; i < listData.length; i++){
		listDatasets[listDatasets.length] = {
			fill: true,
			label: 'average salary for ' + listYears[i],
			data: listData[i],
			borderWidth: 1,  
			borderColor:  'rgba(' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', 1)',
			backgroundColor:  'rgba(' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', 0.6)',
		}
	}

	if (barChart) {
        barChart.destroy();
    }

	var popCanvas = document.getElementById("popChart");
	barChart = new Chart(popCanvas, {
		type: 'bar',
		data: {
			labels: listComparator,  
			datasets: listDatasets,
		}
	});
}

function randomInteger(min, max) {
	var rand = min - 0.5 + Math.random() * (max - min + 1)
	rand = Math.round(rand);
	return rand;
}

var barChart;

$("button").on('click', function() {
	$.getJSON('/viewChartStatistics', { 
		comparator: $('select[name="comparator"]').val(),
		year: $('input[name="year"]').val(),
	}, function(data) {
		chart(data.listData, data.listComparator);
	});
});

function chart(listData, listComparator){
	var listDatasets = [];
	var newBorderColor = []; 
	var newBackgroundColor = [];
	for(var i = 0; i < listComparator.length; i++){
		newBackgroundColor[newBackgroundColor.length] = 'rgba(' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', 1)';
		newBorderColor[newBorderColor.length] = 'rgba(' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', ' + randomInteger(0, 225) + ', 0.6)';
	}

	listDatasets[listDatasets.length] = {
		fill: true,
		data: listData,
		borderWidth: 1,  
		borderColor:  newBorderColor,
		backgroundColor:  newBackgroundColor,
	}


	if (barChart) {
        barChart.destroy();
    }

	var popCanvas = document.getElementById("popChart");
	barChart = new Chart(popCanvas, {
		type: 'pie',
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

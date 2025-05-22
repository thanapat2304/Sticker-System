document.addEventListener("DOMContentLoaded", function() {
    console.log(window.chartData);
    var options = {
        series: window.chartData.counts,
        chart: {
            type: 'donut',
            height: '100%',
            width: '100%'
        },
        labels: window.chartData.topics,
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    height: '70%',
                    width: '100%'
                },
                legend: {
                    position: 'bottom'
                }
            }
        }],
        plotOptions: {
            donut: {
                donutWidth: 100,
                labels: {
                    show: true,
                    name: {
                        fontSize: '16px',
                    },
                    value: {
                        fontSize: '20px',
                    }
                }
            }
        }
    };

    var chart = new ApexCharts(document.querySelector("#chart"), options);
    chart.render();
});

document.addEventListener("DOMContentLoaded", function () {
    fetch('/monthly-data')
        .then(response => response.json())
        .then(data => {
            const allMonths = [
                "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", 
                "Sep", "Oct", "Nov", "Dec"
            ];
            const currentYear = new Date().getFullYear();
            const categories = allMonths;
            const seriesData = allMonths.map((month, index) => {
                const monthYear = `${currentYear}-${(index + 1).toString().padStart(2, '0')}`;
                const monthData = data.find(item => item.month_year === monthYear); 
                return monthData ? monthData.record_count : null;
            });

            var options = {
                series: [{
                    name: 'Records',
                    data: seriesData
                }],
                chart: {
                    width: '100%',
                    height: 290,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                        borderRadius: 10,
                        dataLabels: {
                            position: 'top',
                        },
                    }
                },
                dataLabels: {
                    enabled: true,
                    formatter: function (val) {
                        return val ? val.toString() : '';
                    },
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#304758"]
                    }
                },
                xaxis: {
                    categories: categories,
                    position: 'bottom',
                    axisBorder: {
                        show: false
                    },
                    axisTicks: {
                        show: false
                    },
                    tooltip: {
                        enabled: true,
                    }
                },
                yaxis: {
                    labels: {
                        formatter: function (val) {
                            return val.toString();
                        }
                    }
                },
            };

            var chart = new ApexCharts(document.querySelector("#chart2"), options);
            chart.render();
        })
        .catch(error => console.error("Error fetching monthly data:", error));
});

function showAlert() {
    var modal = document.getElementById("alertModal");
    modal.style.display = "flex";
}

function closeAlert() {
    var modal = document.getElementById("alertModal");
    modal.style.display = "none";
}
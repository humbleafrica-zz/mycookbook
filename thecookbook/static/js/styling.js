// Material Design example
$(document).ready(function() {

    /*############d3 svg charts styling##################*/
    var cuisine_data = 'api/cuisine_data/' // {% url "get_recipe_data" %}
    var recipe_data = 'api/recipe_data/' // {% url "get_recipe_data" %}
    var allergy_data = 'api/allergy_data/' // {% url "get_recipe_data" %}

    var colorHex = ['#006344', '#BD3B1B', '#D8A800', '#B6C61B', 'Yellow', '#B9D870', '#40E0D0']

    var defaultData = []
    var labels = []

    $.ajax({
        method: 'GET',
        url: cuisine_data,
        success: function(data) {
            labels = data.labels
            defaultData = data.default
            var cui = document.getElementById('myChart');
            var myPieChart = new Chart(cui, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        backgroundColor: colorHex,
                        borderWidth: .5,
                        borderColor: 'black',
                        data: defaultData,
                    }]
                },

                options: {
                    responsive: true,

                    legend: {
                        labels: {
                            // This more specific font property overrides the global property
                            fontColor: '#ffffff',
                            fontSize: 10,
                        },
                        position: 'left',
                    }
                }
            });
        },

    })

    $.ajax({
        method: 'GET',
        url: recipe_data,
        success: function(data) {
            labels = data.labels
            defaultData = data.default
            //console.log(labels);
            //console.log(data);
            var rec = document.getElementById('myChart1');

            var myPieChart = new Chart(rec, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        backgroundColor: colorHex,
                        borderWidth: .5,
                        borderColor: 'black',
                        data: defaultData,
                    }]
                },

                options: {
                    responsive: true,

                    legend: {
                        labels: {
                            // This more specific font property overrides the global property
                            fontColor: 'white',
                            fontSize: 10,
                        },
                        position: 'left',
                    }
                }
            });
        },

    })

    $.ajax({
        method: 'GET',
        url: allergy_data,
        success: function(data) {
            labels = data.labels
            defaultData = data.default
            //console.log(labels);
            console.log(data);
            var all = document.getElementById('myChart2');

            var myPieChart = new Chart(all, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        backgroundColor: colorHex,
                        borderWidth: .5,
                        borderColor: 'black',
                        data: defaultData,
                    }]
                },

                options: {
                    responsive: true,

                    legend: {
                        labels: {
                            // This more specific font property overrides the global property
                            fontColor: 'white',
                            fontSize: 10,
                        },
                        position: 'left',
                    }
                }
            });
        },

    })


    /*############datatables styling##################*/
    $('#dtBasic ').DataTable();

    $("#dtBasic").bind('tabsselect', function(event, ui) {
        if (ui.index === 1) {
            tables.statistics("metrics", "metric");
        }
    });

    $('#dtBasic_wrapper').find('label').each(function() {
        $(this).parent().append($(this).children());
    });
    $('#dtBasic_wrapper .dataTables_filter').find('input').each(function() {
        $('input').attr("placeholder", "Search");
        $('input').removeClass('form-control-sm');
    });
    $('#dtBasic_wrapper .dataTables_length').addClass('d-flex flex-row');
    $('#dtBasic_wrapper .dataTables_filter').addClass('md-form');
    $('#dtBasic_wrapper select').removeClass(
        'custom-select custom-select-sm form-control form-control-sm');
    $('#dtBasic_wrapper select').addClass('mdb-select');
    $('#dtBasic_wrapper .dataTables_filter').find('label').remove();

    $('.dataTables_length').addClass('bs-select');

});

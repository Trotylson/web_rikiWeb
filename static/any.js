console.log('Started')

    $('#btn1').click(function() {

        console.log('Calculating...')

        p1 = $('#param1').val();
        p2 = $('#param2').val();
        p3 = $('#param3').val();
        p4 = $('#param4').val();
        p5 = $('#param5').val();

        usedBars = p1 - p2
        usedLiters = usedBars * p3
        litersPerMin = usedLiters / p4
        rmv = litersPerMin / p5

        $('#sum').text(String(rmv) +' ' + 'l/min.')
        console.log('RMV= ', rmv)

        $('#param1').val('');
        $('#param2').val('');
        $('#param3').val('');
        $('#param4').val('');
        $('#param5').val('');

    })
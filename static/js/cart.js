var cart = [];
console.log("Yo")
$(document).ready( function () {
    inventory_DT = $('#inv_table').DataTable({
        columnDefs: [ {
            orderable: false,
            className: 'select-checkbox',
            targets:   0,
        } ],
        select: {style: 'multi'},
        order: [[ 1, 'asc' ]],
        dom: 'B<"clear">lfrtip',
        buttons: {
            name: 'primary',
            buttons: [ 'copy', 'csv', 'excel', 'pdf' ]
            }}
        );
    
    inventory_DT.on( 'select' , function () {
        var cart = [];
        inventory_DT.rows( { selected: true } ).every(function(rowIdx) {
            cart.push({itemID: inventory_DT.row(rowIdx).data()[1], name: inventory_DT.row(rowIdx).data()[3]})
        })
        console.log('cart', cart)

    } );        
} );
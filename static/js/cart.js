let cart = [];
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
        var rowData = inventory_DT.rows( { selected: true } ).data()[0];
        // now do what you need to do wht the row data
        cart.push(rowData)
        $('#checkedItems').append('<li> rowData[1] </li>')
        console.table(cart);
    } );        
} );
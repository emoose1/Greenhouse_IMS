let cart = new Array ()
class Item {
    constructor(name, id){
        this.name = name
        this.id = id
    }

    // function addToCart adds the current item that is being used, to the cart Set variable  
    addToCart() {
        //basic function to gather item info from datatable for use in modal popup
        var myItem = new Item(this.name, this.id)
        console.log("AddToCart item ", Item)
        $('#checkedItemName').text(this.name)
        $('#checkedItemID').text(this.id)
        console.log('AddToCart id/name: ', this.id, this.name)
        cart.push(myItem)
        console.log('AddToCart items:  ', cart)
    }
}
// function isAvailable take ins the item availability string, removes the html tags via ReGex, and passes back a boolean result
function isAvailable(itemAvailability) {
    itemAvailability = itemAvailability.replace(/<[^>]*>/g, '')
    var result = itemAvailability == 'Yes' ? result = true : result = false
    return result
}

function sortCart(cartArray){
    var sortedCart = cartArray.filter((item, index, self) =>
            index === self.findIndex((t) => (
                t.name === item.name && t.name === item.name
            ))
    )

    $('#checkedItemName').text(this.name)
    $('#checkedItemID').text(this.id)

    return sortedCart
}


$(document).ready( function () {
    inventory_DT = $('#inv_table').DataTable({
        columnDefs: [ {
            orderable: false,
            className: 'select-checkbox',
            targets:   0,
        } ],
        select: {
            style: 'multi',
            
        },
        order: [[ 1, 'asc' ]],
        dom: 'B<"clear">lfrtip',
        buttons: {
            name: 'primary',
            buttons: [ 'copy', 'csv', 'excel', 'pdf' ],
        }
    });
    
    inventory_DT.on( 'select' , function () {
        rowData = inventory_DT.rows( { selected: true } ).data().toArray();
        console.table(rowData)
        rowData.map( (element) => {
            var name  = element[1]
            var availability = isAvailable(element[2]);
            var id = element[3];
            var selectedItem = new Item(name, id)
            console.log('SI ', selectedItem)
            console.log('SI ID ',selectedItem.id)
            availability === true ? selectedItem.addToCart() : console.log('item is either not available or already checked to you ', availability)
        })
    });

    $('#checkOutToCartButton').click( function(){
        var myCart = sortCart(cart)
        myCart.map( item => {
            console.log('TESTING MODAL FUNCTION id/name: ', item.id, item.name )
            $('#checkedItemName').text(item.name);
            $('#checkedItemID').text(item.id);
        })
        $.each(cart, function(){
        console.table('SORTED CART TABLE' , sortCart(cart))
        })
    })


    
} );
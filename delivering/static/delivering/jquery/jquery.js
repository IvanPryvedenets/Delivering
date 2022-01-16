$( document ).ready(function() {

    // Adaptive design for product cards on a main page
    $(window).resize(function() {
        if ($(window).width() < 800) {
            $('.category').find('.col-sm-3').toggleClass('col-sm-3 col-sm-4')
        } else  {
            $('.category').find('.col-sm-4').toggleClass('col-sm-4 col-sm-3')
        }

        if ($(window).width() < 626) {
            $('.category').find('.col-sm-4').toggleClass('col-sm-4 col-sm-6')


        } else  {
            $('.category').find('.col-sm-6').toggleClass('col-sm-6 col-sm-4')
        }

    });

    // Page reload
    window.addEventListener( "pageshow", function ( event ) {
        var historyTraversal = event.persisted || ( typeof window.performance != "undefined" && window.performance.navigation.type === 2 );
        if ( historyTraversal ) {
            // Handle page restore.
            window.location.reload();
        }
    });

    // Quantification of stars in the comments what was adding
    $( '.comment' ).each( function () {
        var value = $( this ).children( 'input.marked' ).val()

        $( this ).children( '.fa-star' ).slice( value ).removeClass( 'checked' )

        console.log(value)
    })

    // Choice some number of stars in the adding comment
    $( '.comment-form .fa-star' ).click( function () {
        $( this ).addClass( 'checked' )
        $( this ).prevAll( '.fa-star' ).addClass( 'checked' )
        $( this ).nextAll( '.fa-star' ).removeClass( 'checked' )
        var Class = $( this ).attr( 'class' )
        $( 'input.mark' ).val( Class.replace(/[^\d]/g, '') )
    })

    $( '.info-message' ).animate( {'opacity': '1'}, 'slow' )

    // If a marker isn't on a page, reload it
    $( window ).load( function () {
        var $el = $('tbody tr').length
        var $mark = $('.marker').length
        console.log($el, $mark)

        if ( !$el && $mark ) {
            window.location.replace("http://127.0.0.1:8000/basket/");
        }
     });

    // Ajax function
    function DataEngine( form, data ) {

        var method = form.attr( 'method' );

        var action = form.attr( 'action' );

        $.ajax({

            type: method,
            url: action,
            data: data,
            dataType: 'json',

            success: function( data ) { // If data has been transmitted

                var product_count = Object.keys( data ).length // Sum of keys / products

                $('.basket div').html('<span>' + product_count + '</span>') // Sum of products in a basket

                $( '.drop-down' ).html( '' ) // Clear drop-down basket

                $( 'tbody' ).html( ' ' ) // Clear table in the basket page

                $( '.basket-products' ).html( '' )

                $( '.drop-down-buttons' ).remove()

                $( '.basket-buttons').remove()

                $( '.drop-down-total_price' ).remove()

                if (product_count > 0) { // If some products do next
                    $('.drop-down-auxiliary').html('<div class="drop-down-total_price">' +
                                                   '</div>' +

                                                    '<div class="drop-down-buttons">' +
                                                        '<a href="' + '/basket/' + '"><button type="button">Корзина</button></a>' +
                                                        '<a href="' + '/checkout/' + '"><button type="button">Оформити замовлення</button></a>' +
                                                    '</div>' )

                    $('.basket-auxiliary').html('<div class="drop-down-total_price">' +
                                                   '</div>' +

                                                    '<div class="basket-buttons">' +
                                                        '<a href="' + '/' + '"><button type="button">Продовжити покупки</button></a>' +
                                                        '<a href="' + '/checkout/' + '"><button type="button">Оформити замовлення</button></a>' +
                                                    '</div>' )

                } else if (product_count == 0) { // If basket empty do next

                    $('.basket-info').remove()

                    $('.drop-down-auxiliary').html('<div class="drop-down-buttons">' +
                                                        'Ваша корзина порожня!' +
                                                    '</div>' )

                    $('.basket-auxiliary').append('<div class="basket-buttons">' +
                                                        'Ваша корзина порожня!' +
                                                        '<a href="' + '/' + '"><button type="button">Продовжити покупки</button></a>' +
                                                    '</div>')

                };

                var total_price = 0

                $.each( data, function ( key, value ) { // Data sorting

//                    if ( value['amount'] === null ) {
//                        value['amount'] = ''
//                    }

                    total_price += parseFloat(value['total price']) // Get total price of all the products

                    $('.drop-down-total_price').html( '' )

                    $('.drop-down-total_price').append( 'Загалом: ' + total_price + ',00 грн')

                    $( '.drop-down' ).append( '<div class="drop-down-card">' +  // Adding data to the drop-down basket
                                                '<a href="' + value['url'] + '"><img class="drop-down-img" src="/media/' + value['image'] + '"></a>' +
                                                '<div class="drop-down-info">' +
                                                    '<div class="drop-down-name">' + value['name'] +
                                                    '</div>' +
                                                    '<div class="drop-down-price">' + parseFloat(value['price']) + ',00</div>' +
                                                    '<span class="product-delete" data-id="' + value['unit id'] + '"><span>&#215;</span></span>' +
                                                    '<div class="drop-down-number">' + value['number'] + 'шт.</div>' +
                                                '</div>' +
                                            '</div>' );

                    $( '.basket-info tbody' ).append('<tr>' + // Adding data to the basket page
                                                        '<td class="table-img" valign="top"><a href="' + value['url'] + '"><img class="basket-img" src="/media/' + value['image'] + '"></a></td>' +
                                                        '<td class="table-title" valign="top"><a href="' + value['url'] + '">' + value['name'] + '</a></td>' +
                                                        '<td class="table-price" valign="top">' + parseFloat(value['price']) + ',00</td>' +
                                                        '<td class="table-input" valign="top"><input class="basket-input" type="number" min="1" max="10" maxlength="2" value="' + value['number'] + '" data-id="' + value['unit id'] + '"></td>' +
                                                        '<td class="table-total_price" valign="top">' + parseFloat(value['total price']) + ',00</td>' +
                                                        '<td class="table-total_price" valign="top"><span class="product-delete" data-id="' + value['unit id'] + '"><span>&#215;</span></span></td>' +
                                                    '</tr>');

                });
            },

            error: function() { // If something was wrong ...
                console.log( 'error' );
            },
        });

    };


    // Do next if user clock on button of card product
    $( '.card-form' ).on( 'submit', function ( e ) {
        e.preventDefault();

        $( '.basket div' ).animate({'height': 25, 'width': 25, 'padding-top': 3}, 400) // Change size of basket div

        setTimeout( function () {
            $( '.basket div' ).animate({'width': 19, 'height': 19, 'padding-top': 0}, 300)
        }, 1000) // Do default size after 1 second

        var form = $( this ); // Get form

        var data = form.children( '.card-button' ).data(); // Get product data

        data['action'] = 'create';
        data['csrfmiddlewaretoken'] = $( '.card-form [name="csrfmiddlewaretoken"]' ).val();
        data['number'] = form.children( 'input[type=number]' ).val();

        data['price'] = parseFloat( data['price'] ); // Parse string ot number

        DataEngine( form, data );
    });


    // Deleting product
    $( document ).on( 'click', '.product-delete', function () {
        var form = $( '.basket-form' );

        var data = $( this ).data();

        data['csrfmiddlewaretoken'] = $( '.basket-form [name="csrfmiddlewaretoken"]' ).val();
        data['action'] = 'delete';

        DataEngine( form, data );
    });


    // Change number of product in the basket page
    $( document ).on( 'change', '.basket-input', function () {

        var form = $( '.basket-form' );

        var data = $( this ).data();

        data[ 'csrfmiddlewaretoken' ] = $( '.basket-form [name="csrfmiddlewaretoken"]' ).val();
        data[ 'action' ] = 'change';
        data[ 'number' ] = $( this ).val();

        DataEngine( form, data );
    });

});

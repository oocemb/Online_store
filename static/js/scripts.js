// Swiper-slider
const swiper = new Swiper('.swiper-category', {
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        // when window width is >= 480px
        480: {
            slidesPerView: 1,
            spaceBetween: 30
        },
        // when window width is >= 640px
        640: {
            slidesPerView: 3,
            spaceBetween: 40
        }
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },
});

$(document).ready(function(){
    
    function basketUpdating(product_id, nmb, is_delete){
        // Ajax обновляет данные в корзине при изменении количества товаров и удаляет при тэге is_delete
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        data["csrfmiddlewaretoken"] = $('#csrf_getting_form [name="csrfmiddlewaretoken"]').val();
        if (is_delete){
            data.is_delete = true;
        }
        
        var form_csrf = $('#csrf_getting_form');
        var url = form_csrf.attr("action"); // форма на базовом шаблоне для работы с корзиной

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data){
                    $('.list-unstyled.cart-list').html("");
                    $.each(data.products, function(key, value){
                        if (value.nmb > 0){
                            $('.list-unstyled.cart-list').append('\
                            <li class="d-flex mb-4 align-items-center"> \
                              <div class="me-4 flex-shrink-0"> \
                                  <a href="#"> \
                                      <img src="'+ value.image +'" alt="" class="width-80 h-auto rounded-3"> \
                                  </a> \
                              </div> \
                              <div class="position-relative pe-5 flex-grow-1"> \
                                  <span \
                                      class="btn btn-outline-secondary size-15 flex-center rounded-circle position-absolute end-0 top-50 translate-middle-y delete-item" \
                                       data-product_id = "' + value.id_prod_basket + '">&#10006;</span> \
                                  <h6 class="mb-1"><a href="#">' + value.name + '</a></h6> \
                                  <p class="mb-0"><span class="price text-muted small">&#8381;' + value.price_per_item + '</span> x ' + value.nmb + '</p> \
                              </div> \
                            </li>');
                        }
                    });
                    $('.list-unstyled.cart-amount').html("");
                    $('.list-unstyled.cart-amount').append('\
                    <li class="py-4 border-top border-bottom"> \
                        <div class="d-flex pb-2 mb-2 border-bottom justify-content-between align-items-center"> \
                            <small class="text-muted">Sub Total</small> \
                            <h6 class="mb-0">$ ' + data.total_basket_price + '</h6> \
                        </div> \
                        <div class="d-flex pb-2 mb-2 border-bottom justify-content-between align-items-center"> \
                            <small class="text-muted">Shipping charges</small> \
                            <h6 class="mb-0">$ 0.00</h6> \
                        </div> \
                        <div class="d-flex justify-content-between align-items-center"> \
                            <span class="text-muted">Total</span> \
                            <h5 class="mb-0">$ ' + data.total_basket_price + '</h5> \
                        </div> \
                    </li>');
                    $('.basket-detail').html("");
                    $.each(data.products, function(key, value){
                        $('.basket-detail').append('\
                        <li class="list-group-item">\
                         <div class="row align-items-center">\
                             <div class="col-4 col-md-3 mb-4 mb-sm-0">\
                                <a href="#!">\
                                 <img src="'+ value.image +'" class="img-fluid rounded-3" alt="">\
                                </a>\
                             </div>\
                             <div class="col-8 col-md-9">\
                                <div class="position-relative pe-5">\
                                    <!--Remove button-->\
                                    <a href="#!" class="text-muted position-absolute end-0 top-0 me-3 mt-3"><i class="far fa-trash-alt delete-item"\
                                        data-product_id="' + value.id_prod_basket + '"></i></a>\
                                     <!--Brand-->\
                                 <p class="mb-1 small"><a href="#!">'+ value.category +'</a></p>\
                                 <!--Product-->\
                                 <h5 class="mb-2">\
                                     <a href="#!">' + value.name + '</a>\
                                 </h5>\
                                 <!--Price-->\
                                 <p class="product-price-in-basket mb-3" id="product-price-in-basket">'+ value.price_per_item +'<small class="text-muted"><del>$ '+ value.price_per_item +'</del></small></p>\
                                 <!--Quantity-->\
                                    <div class="d-flex align-items-center mb-0">\
                                     <small class="text-muted me-3">QTY</small>\
                                     <div class="count-input">\
                                         <a class="incr-btn" data-action="decrease" href="#"\
                                         data-product_id="'+ value.id_prod +'">–</a>\
                                         <input class="quantity px-0 py-0 form-control bg-transparent" type="text" value="' + value.nmb + '" name="prod_nmb_' + value.id + '">\
                                         <a class="incr-btn" data-action="increase" href="#"\
                                         data-product_id="'+ value.id_prod +'">+</a>\
                                     </div>\
                                    </div>\
                                </div>\
                             </div>\
                         </div>\
                     </li>');
                    });
                    $('.basket-price-details').html("");
                    $('.basket-price-details').append('\
                    <h6 class="mb-3">Price details</h6>\
                     <ul class="list-group list-group-flush">\
                         <li class="list-group-item px-0 d-flex align-items-center justify-content-between">\
                             <span>Итого: </span>\
                             <span id="total-basket-amount">' + data.total_basket_price + '</span>\
                         </li>\
                         <li class="list-group-item px-0 d-flex align-items-center justify-content-between">\
                             <span>Coupon discount</span>\
                             <span><a href="#!" class="badge border text-primary me-2">Apply</a><span>$0 </span></span>\
                         </li>\
                         <li class="list-group-item px-0 d-flex align-items-center justify-content-between">\
                             <span>Shipping fee</span>\
                             <span><span class="text-success">Free </span><del class="opacity-75">$9.00</del></span>\
                         </li>\
                         <li class="list-group-item px-0 d-flex align-items-center justify-content-between">\
                             <strong>К оплате: </strong>\
                             <strong id="total-basket-amount-to-pay">' + data.total_basket_price + '</strong>\
                         </li>\
                     </ul>');

                
                
            },
            error: function (data){
                console.log('error basketUpdate')
            }
        });
    };


    $(document).on('click', '.button_add_to_basket', function(e){
        // Добавляет товар в количестве 1 шт в корзину (Страница: Главная / Товары)
        e.preventDefault();
        var nmb = 1
        basketUpdating($(this).data("product_id"), nmb, is_delete=false)    
    });

    var form_buying_product = $('#form_buying_product')
    form_buying_product.on('submit', function(e){
        // Добавляет товар в количестве на счётчике -> quantity шт в корзину (Страница: Товар)
        e.preventDefault();
        var nmb = $('#quantity').val();
        if (nmb > 0){
            basketUpdating($('#submit_btn').data("product_id"), nmb, is_delete=false)
        };     
    });

    $(document).on('click', '.delete-item', function(e){
        // Удаляет выбранный по ID товар из корзины
        e.preventDefault();
        product_id = $(this).data("product_id");
        console.log(product_id);
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true)

    });

    function clickQuantity(this1){
        // Только отображает и меняет количество (Страницы: Товар. Корзина)
        var $button = this1;
        var oldValue = $button.parent().find('.quantity').val();
        $button.parent().find('.incr-btn[data-action="decrease"]').removeClass('inactive');
        if ($button.data('action') == "increase") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below 1
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
                $button.addClass('inactive');
            }
        }
        $button.parent().find('.quantity').val(newVal);
        return nmb_quantity = (newVal - oldValue)
    }

    $(document).on("click", ".incr-btn", function (e) {
        // Ajax Обновялет количество данного товара в корзине (Страницы: Корзина)
        e.preventDefault();
        clickQuantity($(this))
        basketUpdating($(this).data("product_id"), (newVal-oldValue), is_delete=false)
        });

    $(document).on("click", ".incr-btn-only", function (e) {
        // Только отображает и меняет количество "добавляется кнопкой в корзину" (Страницы: Товар)
        e.preventDefault();
        clickQuantity($(this))
        });


});

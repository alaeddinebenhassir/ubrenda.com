var stripe = Stripe('pk_test_eJzUry98i0m3vipsD9oQr2sB0013oq5o3f');

// Create an instance of Elements.
var elements = stripe.elements();
var style = {
  
base: {

iconColor: '#666EE8',
color: '#31325F',

fontWeight: 300,
fontFamily: 'Helvetica Neue',
fontSize: '15px',

'::placeholder': {
  color: '#',
},
},
};
$('#check').prop('disabled', true);
var cardNumberElement = elements.create('cardNumber', {
style: style
});
cardNumberElement.mount('#card-number-element');

var cardExpiryElement = elements.create('cardExpiry', {
style: style
});
cardExpiryElement.mount('#card-expiry-element');

var cardCvcElement = elements.create('cardCvc', {
style: style
});
cardCvcElement.mount('#card-cvc-element');

// Handle real-time validation errors from the card Element.
var loader = document.querySelector('#fa');
function setOutcome(result) {
var successElement = document.querySelector('.success');
var errorElement = document.querySelector('.error');
var cardAdded = document.querySelector('.group');
var done = document.querySelector('.done');

cardAdded.classList.add('visible');
successElement.classList.remove('visible');
errorElement.classList.remove('visible');


if (result.token) {
// In this example, we're simply displaying the token
successElement.querySelector('.token').textContent = result.token.id;
successElement.classList.add('visible');
cardAdded.classList.add('invisible');
loader.classList.remove('visible');
done.classList.add('visible');
$('#check').prop('disabled', false);
var data = {
    'Token' : result.token.id ,
    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),

}
$.ajax({
    data : data ,
    url : 'checkout/',
    method : "POST",
    success :  function(data){
      console.log(data);
      result.token.id = null;
      
    },
    error : function(error){
        console.log(error);
       
    }
})
} else if (result.error) {
errorElement.textContent = result.error.message;
errorElement.classList.add('visible');
}
}

var cardBrandToPfClass = {
'visa': 'fa-cc-visa',
'mastercard': 'fa-cc-mastercard',
'amex': 'fa-cc-american-express',
'discover': 'fa-cc-discover',
'diners': 'fa-cc-diners',
'jcb': 'fa-cc-jcb',
'unknown': 'fa-cc-credit-card',
}

function setBrandIcon(brand) {
var brandIconElement = document.getElementById('brand-icon');
var pfClass = 'fa-credit-card';
if (brand in cardBrandToPfClass) {
pfClass = cardBrandToPfClass[brand];
}
for (var i = brandIconElement.classList.length - 1; i >= 0; i--) {
brandIconElement.classList.remove(brandIconElement.classList[i]);
}
brandIconElement.classList.add('fab');
brandIconElement.classList.add(pfClass);
}

cardNumberElement.on('change', function(event) {
// Switch brand logo
if (event.brand) {
setBrandIcon(event.brand);
}

setOutcome(event);
});



document.querySelector('.group').addEventListener('submit', function(e) {
e.preventDefault();
var options = {
address_zip: document.getElementById('postal-code').value,
};
stripe.createToken(cardNumberElement, options).then(setOutcome);
loader.classList.add('visible');
});
document.getElementById("check").onclick = function () { 
  var data = {
      
    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),

}
  $.ajax({
    
    data : data ,
    url : 'Order/',
    method : "POST",
    success :  function(data){
      console.log(data);
      alert('hello!');
    },
    error : function(error){
        console.log(error);
       
    }
})
  };
// Submit the form with the token ID.


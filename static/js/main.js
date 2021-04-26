
$(document).ready(() =>{

  $('.banned1').hide();
  $('.banned2').hide();
  $('.banned3').hide();
  $('.banned4').hide();
  $('.banned5').hide();
  $('.banned6').hide();
  $('.banned7').hide();
  $('.banned8').hide();
  $('.banned9').hide();
  $('.banned10').hide();

})

let openAll = document.querySelector('#open');

openAll.onclick = () => {
  $(document).ready(() =>{

    $('.banned1').show('slow');
    $('.banned2').show('slow');
    $('.banned3').show('slow');
    $('.banned4').show('slow');
    $('.banned5').show('slow');
    $('.banned6').show('slow');
    $('.banned7').show('slow');
    $('.banned8').show('slow');
    $('.banned9').show('slow');
    $('.banned10').show('slow');

  })

};


$( '#show1' ).click(function() {
  $( ".banned1" ).toggle( 'slow' );
});


$( '#show2' ).click(function() {
  $( ".banned2" ).toggle( "slow" );
});

$( '#show3' ).click(function() {
  $( ".banned3" ).toggle( "slow" );
});


$( '#show4' ).click(function() {
  $( ".banned4" ).toggle( "slow" );
});


$( '#show5' ).click(function() {
  $( ".banned5" ).toggle( "slow" );
});


$( '#show6' ).click(function() {
  $( ".banned6" ).toggle( "slow" );
});

$( '#show7' ).click(function() {
  $( ".banned7" ).toggle( "slow" );
});

$( '#show8' ).click(function() {
  $( ".banned8" ).toggle( "slow" );
});


$( '#show9' ).click(function() {
  $( ".banned9" ).toggle( "slow" );
});


$( '#show10' ).click(function() {
  $( ".banned10" ).toggle( "slow" );
});

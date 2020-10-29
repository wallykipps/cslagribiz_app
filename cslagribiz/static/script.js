$("#menu-toggle").click(function(e){
  e.preventDefault();
  $("#wrapper").toggleClass("menuDisplayed");

});


function myRefresh(){
  location.reload();
}

/*
function combineFunction() {
  var fname = document.forms["customerform"]["firstname"].value;
  var lname = document.forms["customerform"]["lastname"].value;
  var namespace =" ";
  if (fname!="" && lname!="") {
    var customername = fname.concat(namespace,lname);
    var x=document.getElementById("customername")
    alert(x);
    x.setAttribute("value", customername);
  } else {

  }
}

*/

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();
});


//Filter table

$(document).ready(function(){

  $("#myCustomer").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#customers tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});


//Register customer modal-form
$(document).ready(function(){

    $(document).on('click','#addCustomerBtn',function(e){
    e.preventDefault();
    $('#customerAdd').modal('show');
  });
});


//Edit customer modal -html
$(document).ready(function(){
    $(document).on('click','.updateBtn',function(e){
    e.preventDefault();
    var id = $(this).data('id');
    var url = $(this).data('url');
    //alert(url);
    $.ajax({
        url:url,
        type:"GET",
        data: {id: id},
        dataType: "html",
        success:function(data){
          //insert form data into modal
          $("#updateModal").find('.modal-body').html(data);
          $("#updateModal").modal("show");
        },
        error:function(){
                console.log('error');
        },
    });

    $('#updateModalForm').submit(function(e){
        e.preventDefault();
        $.ajax({
            url:url,
            type:'POST',
            data: $('#updateModalForm').serialize(),
            success:function(data){
              console.log('success')
              $('#updateModal').modal('hide');
              window.location.reload(true)
            },
            error:function(){
                console.log('error')
            },
        });
    });
  });
});


//Delete function
$(document).on('click','.deleteBtn',function(){
    var id = $(this).data('id');
    var url = $(this).data('url');
    //alert(url)
  $('#deleteModal').modal('show');

$('#deleteModalForm').submit(function(e){
  // $(document).on('click','#deleteBtn',function(e){
    e.preventDefault();
    $.ajax({
        url:url,
        type:'POST',
        data:{
            'id':id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            // 'csrfmiddlewaretoken': 'csrf_token',
        },
        success:function(data){
          console.log('success')
          $('#deleteModal').modal('hide');
          window.location.reload(true)
        },
        error:function(){
            console.log('error')
        },
    });
});

});




//  $('input:checkbox').click(function () {
//     if ($('input:checkbox').is(":checked")) {
//        $("#id_birds_stock_actual").attr("disabled", "true")
//     }
//     else {
//          $("#id_birds_stock_actual").removeAttr("disabled")
//     }
// });



// $(document).ready(function($) {
//   $('#id_birds_stock_actual').val('').prop('disabled', true);
//   $('#enableDisableChkBx').change(function(){
//       if ($('#enableDisableChkBx').is(':checked') == true){
//           $('#id_birds_stock_actual').val('').prop('disabled', false);
//           $('#id_birds_stock_actual').val('').prop('required', true);
//           console.log('checked');
//       } else {
//           $('#id_birds_stock_actual').val('').prop('disabled', true);
//           $('#id_birds_stock_actual').val('').prop('required', false);
//           console.log('unchecked');
//       }
//   });
//
// });


$(document).ready(function($) {
  $('.inputstatus').val('').prop('disabled', true);
  //$('.inputstatusChkBx').prop('indeterminate', true)
  $('.inputstatusChkBx').change(function(){
      if ($('.inputstatusChkBx').is(':checked') == true){
          $('.inputstatus').val('').prop('disabled', false);
          $('.inputstatus').val('').prop('required', true);
          console.log('checked');
      } else {
          $('.inputstatus').val('').prop('disabled', true);
          $('.inputstatus').val('').prop('required', false);
          console.log('unchecked');
      }
  });

});

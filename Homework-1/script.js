//  let Btn1 = document.getElementById("takeSurvey"); 
//  Btn1.addEventListener("click", function() {
//      location.href = "http://127.0.0.1:5000/survey"
//  } )

//  let Btn2 = document.getElementById("noThankYou"); 
//  Btn2.addEventListener("click", function() {
//      location.href = "http://127.0.0.1:5000/decline"
//  } )

//  let Btn3 = document.getElementById("submitForm"); 
//  Btn3.addEventListener("click", function() {
//      location.href = "http://127.0.0.1:5000/thanks"
//      $.ajax({
//         url:'postgres://ishika_database1_user:0B73TyZ8kDkzdbC1UUBzITeH9Q43Hq1X@dpg-cfmqts2rrk0eqlruie10-a.oregon-postgres.render.com/ishika_database1',
//         type:'post',
//         data:$("survey-form").serializeArray()})
//  } )



function myFunction() {
    var checkbox = document.getElementById("other");
    //var textbox = document.getElementById("otherValue")
    if(checkbox.checked){
        document.getElementById("otherValue").style.display = "block";
    }else{
        document.getElementById("otherValue").style.display = "none";
    }

  }

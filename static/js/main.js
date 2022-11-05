const currentPage = window.location.href;

const list = ["home", "API", "list", "collection", "mypage"];
const selectedColor = "#04b7cc";
for (let i = 0; i < 5; i++) {
  if (currentPage.toString().includes(list[i])) {
    const targetText = document.getElementsByClassName(list[i])[0];
    targetText.style.color = selectedColor;
  }
}

// mypage jQuery
$(".img-setting-inner input[type=file]").on("change", function () {
  var fileName = $(this).val();
  $(this).next().val(fileName);
});

// 취소 버튼 클릭
function cancel(){
     // const element = document.getElementById('popup_cancel');
     //
     // element.innerText = '';
     $("#text1").val("");
     $("#text2").val("");
     $("#bill1").val("");
     $("#bill2").val("");
     $("#bill3").val("");
     $("#bill4").val("");
     $("#bill5").val("");
     $("#bill6").val("");
     $("#bill7").val("");
     $("#bill8").val("");
     $("#opt1").val("");
     $("#opt2").val("");
     $("#opt3").val("");
     $("#opt4").val("");
     $("#opt5").val("");
     $("#opt6").val("");
     $("#opt7").val("");
     $("#opt8").val("");
     $("#bill0").val("");
     $("#word1").val("");
     $("#word2").val("");

     document.getElementById("selectAll").checked = false;
     document.getElementById("chk1").checked = false;
     document.getElementById("chk2").checked = false;
     document.getElementById("chk3").checked = false;
     document.getElementById("chk4").checked = false;
     document.getElementById("chk5").checked = false;
     document.getElementById("chk6").checked = false;
     document.getElementById("chk7").checked = false;
     document.getElementById("chk8").checked = false;
 }

 // 체크박스 해제
 function checkBtn(){
    document.getElementById("video_upload").checked = false;
    document.getElementById("mute").checked = false;
 }

 // 상세 페이지 취소 버튼 클릭
 function detailPage(){
    document.getElementById("video_upload").checked = false;
    document.getElementById("mute").checked = false;
 }

 // 상품 옵션 X 버튼 클릭
  function detailProductPage(){
    $("#text1").val("");
     $("#text2").val("");
     $("#bill1").val("");
     $("#bill2").val("");
     $("#bill3").val("");
     $("#bill4").val("");
     $("#bill5").val("");
     $("#bill6").val("");
     $("#bill7").val("");
     $("#bill8").val("");
     $("#opt1").val("");
     $("#opt2").val("");
     $("#opt3").val("");
     $("#opt4").val("");
     $("#opt5").val("");
     $("#opt6").val("");
     $("#opt7").val("");
     $("#opt8").val("");
     $("#bill0").val("");
     $("#word1").val("");
     $("#word2").val("");

     document.getElementById("selectAll").checked = false;
     document.getElementById("chk1").checked = false;
     document.getElementById("chk2").checked = false;
     document.getElementById("chk3").checked = false;
     document.getElementById("chk4").checked = false;
     document.getElementById("chk5").checked = false;
     document.getElementById("chk6").checked = false;
     document.getElementById("chk7").checked = false;
     document.getElementById("chk8").checked = false;
 }

 // 커스텀 설정 변경 취소 버튼 클릭
 function cancelCustom(){
    $("#textF1").val("");
    $("#textF2").val("");
    $("#textF3").val("");
    $("#textF4").val("");
    $("#textF5").val("");
    $("#textF6").val("");
    $("#textF7").val("");
    $("#textF8").val("");
    $("#textF9").val("");
    $("#textF10").val("");
    $("#textF11").val("");
    $("#textF12").val("");
    $("#textF13").val("");
    $("#textF14").val("");
    $("#textF15").val("");
    $("#textF16").val("");
    $("#textF17").val("");
    $("#textF18").val("");
    $("#textF19").val("");
    $("#textF20").val("");
 }

 // 커스텀 설정 변경 창 X 버튼 클릭
 function closeCustom() {
    $("#textF1").val("");
    $("#textF2").val("");
    $("#textF3").val("");
    $("#textF4").val("");
    $("#textF5").val("");
    $("#textF6").val("");
    $("#textF7").val("");
    $("#textF8").val("");
    $("#textF9").val("");
    $("#textF10").val("");
    $("#textF11").val("");
    $("#textF12").val("");
    $("#textF13").val("");
    $("#textF14").val("");
    $("#textF15").val("");
    $("#textF16").val("");
    $("#textF17").val("");
    $("#textF18").val("");
    $("#textF19").val("");
    $("#textF20").val("");
 }

// 카테고리 수정 취소 버튼 클릭
 function cancelCategory() {
    $("#autoInput1").val("");
    $("#autoInput2").val("");
    $("#autoInput3").val("");
    $("#autoInput4").val("");
    $("#autoInput5").val("");
    $("#autoInput6").val("");
    $("#autoInput7").val("");
 }

 // 카테고리 X 버튼 클릭
function detailCloseCategory() {
    $("#autoInput1").val("");
    $("#autoInput2").val("");
    $("#autoInput3").val("");
    $("#autoInput4").val("");
    $("#autoInput5").val("");
    $("#autoInput6").val("");
    $("#autoInput7").val("");
}

// 메인 사진 수정 취소 클릭
function cancelMainPic() {

}

// 메인 사진 수정 X 클릭
function closeMainPic() {

}

// 특수 문자 제거
function removeSpecial(str) {
    var reg = /[\{\}\[\]?,;:|*~`!^\_<>@\#$%&\\\=\'\"]/gi
    var str = $('input[name=optionValue]').val()

    if(reg.test(str)){
                console.log($('input[name=optionValue]').val())
                return $('input[name=optionValue]').attr('value', str.replace(reg, ""));
            }
    else {
                return str;
            }
}

// 커스텀 글자 변경
function changeCustomText(str) {
    var str1 = $('input[name=text_custom1]').val()
    var str2 = $('input[name=text_custom2]').val()
    var str3 = $('input[name=optionValue]').val()

    if(str3.includes(str1)) {
        return  $('input[name=optionValue]').attr('value', str3.replaceAll(str1, str2));
    }
}

// 카테고리 저장
function insertCategory(str) {
    var str = $('input[name=category]').attr('value', "생활/건강 > 공구 > 원예 공구 > 농기계");

    return str;
}

// 배송비 추가
function changeTax() {
    var num = $('input[name=beforeTax]').val();
    var amount = "130,000";

    return $('input[name=beforeTax]').attr('value', amount);
}

// 옵션명 A - Z 옵션
function changeNameLiteral() {
    var opn = $('input[name=optionValue]').val();
    
    return  $('input[name=optionValue]').attr('value', "A옵션");
}

// 옵션명 1 - N 옵션
function changeNameNumber() {
    var opn2 = $('input[name=optionValue]').val();
    
    return  $('input[name=optionValue]').attr('value', "1옵션");
}

// 글자 변경
function changeWord() {
    var word1 = $('input[name=prefix]').val()
    var word2 = $('input[name=suffix]').val()
    var word3 = $('input[name=optionValue]').val()

    if(word3.includes(word1)) {
        return  $('input[name=optionValue]').attr('value', word3.replaceAll(word1, word2));
    }
}

// 글자 변경
function toChinese() {
    var ch1 = $('button[name=beforeTrans]').val()
    var ko2 = $('button[name=afterTrans]').val()
    var opn3 = $('input[name=optionValue]').val()

    if(opn3.includes(ko2)) {
        return  $('input[name=optionValue]').attr('value', opn3.replaceAll(ko2, ch1));
    }
}

// 글자 변경
function toKorean() {
    var ch1 = $('button[name=beforeTrans]').val()
    var ko2 = $('button[name=afterTrans]').val()
    var opn3 = $('input[name=optionValue]').val()

    if(opn3.includes(ch1)) {
        return  $('input[name=optionValue]').attr('value', opn3.replaceAll(ch1, ko2));
    }
}



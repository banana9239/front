function show(num){
    var j = Number(num);
    var somethings = ["광고홍보_요건", "국어교육_요건", "동양어문학_요건", "문헌정보학_요건", "사회복지학_요건", "수학교육_요건"
,"신문방송학_요건", "영어영문학_요건", "융합실무법학_요건", "정치행정학_요건", "지적학_요건"];
    document.getElementById(num).innerHTML = somethings[j];
    
    
    /*var requirements = ["광고홍보문화콘텐츠전공의 졸업요건", "국어교육전공의 졸업요건", "동양어문한전공의 졸업요건","(정보 관련 자격증 2개 + 토익 400점 / 정보 관련 자격증 1개 + 토익 600점) + 졸업시험","사회복지학전공의 졸업요건", "수학교육전공의 졸업요건", "신문방송학전공의 졸업요건", "영어영문학의 졸업요건","융합실무법학전공의 졸업요건", "정치행정학전공의 졸업요건", "지적학전공의 졸업요건"];
    
    
    for(var i = 0;i<length(requirements);i++){
        if (i==j){
            document.getElementById("require").innerHTML = requirements[i];
        }
    } */
    
    
}
function hide(num){
    document.getElementById(num).innerHTML="";
}


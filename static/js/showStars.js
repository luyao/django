function click4AddFile(){
	var submitObj = document.getElementById("id_imgs");
	return submitObj.click();
}

function _setSingleValue(name){
	var submitObj = document.getElementById(name);
	var value = submitObj.getAttribute("star");
	submitObj = document.getElementById("id_" + name);
	submitObj.setAttribute("value", value);
}

function _getTextAreaValue(){
	var submitObj      = document.getElementById("content_submit");
	var submitObjWrite = document.getElementById("id_content");
	submitObjWrite.innerHTML = submitObj.innerHTML;
	submitObjWrite.setAttribute("value", submitObj.innerHTML);
}

function clickSubmit(){
	_setSingleValue("durability");
	_setSingleValue("color");
	_setSingleValue("ppr")
	_setSingleValue("anti_blooming")
	_setSingleValue("absorption")
	_getTextAreaValue();
	var submitObj = document.getElementById("comment_submit");
	return submitObj.click();
}

function mouseoverHandle(cnt, list){
	var i = 0;
	for(i=0; i<=cnt; i++){
		list[i].className = "red_star";
	}	
}

function mouseoutHandle(cnt, list){
	var i = 0;
	for(i=0; i<=cnt; i++){
		list[i].className = "";
	}	
}

var star_li = new Array();
(function() {
	var star_war = document.getElementById("star_war");
	var star     = star_war.getElementsByTagName("li");
	var j=0;
	for( j = 0; j<star.length; j++){
		star_li[j] = star[j].getElementsByTagName("b");
		star_li[j].index = j;
		var len = star_li[j].length;
		var i=0;
		var k=0;

		for(i=0; i<len; i++){
			//set some values for the functions' using
			star_li[j][i].starNum = len;
			star_li[j][i].fatherIndex = j;
			star_li[j][i].index = i;

			star_li[j][i].onmouseover = function(){
				for(k=0; k<=this.index; k++){
					star_li[this.fatherIndex][k].className = "red_star";
				}
			}
			star_li[j][i].onmouseout = function(){
				var end = star[this.fatherIndex].getAttribute('star');
				for(k=end; k<this.starNum; k++){
					star_li[this.fatherIndex][k].className = "";
				}
			}
			star_li[j][i].onclick = function(){
				star[this.fatherIndex].setAttribute('star',this.index+1);
			}
		}
	}
})();


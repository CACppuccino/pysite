//display or hide the relevant block
function funcShow(eid){
	var dis = document.getElementById(eid).style;
	if(dis.display=="block") {
		dis.display="none";
	}
	else {
	dis.display="block";
	}
}



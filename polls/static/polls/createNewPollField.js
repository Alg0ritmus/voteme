let index=5;
function createNewPollField(){
	form= document.getElementById("pollFormChoice");

	//create div
	makediv = document.createElement("div");
	var makedivClassAtt = document.createAttribute("class");
	makedivClassAtt.value = "input-field";
	makediv.setAttributeNode(makedivClassAtt);
	form.appendChild(makediv);

	//create input field inside div
	var input = document.createElement("input");
	var classInputAtt = document.createAttribute("class"); 
	classInputAtt.value = "form-control";
    input.type = "text";
    input.id="name"; 
    input.setAttributeNode(classInputAtt);
    input.name="choice"+index;
    input.required;
    makediv.appendChild(input);

    // create label
	index+=1;

	var label =document.createElement("label");
	var classAtt = document.createAttribute("class"); 
	var forAtt = document.createAttribute("for"); 
	classAtt.value="form-control-placeholder"; 
	forAtt.value="name";
	label.setAttributeNode(classAtt); 
	label.setAttributeNode(forAtt); 
	label.innerHTML = "Choice"
	makediv.appendChild(label);
}
function myfunction()
{
	var tr=document.createElement("TR");
	var td1=document.createElement("TD");
	var td2=document.createElement("TD");
	var td3=document.createElement("TD");
	var td4=document.createElement("TD");
	var task=document.getElementById("input").value;
	var node1=document.createTextNode(task);
	const d = new Date();
	let text = d.toLocaleDateString();
	var node2=document.createTextNode(text);
	var node3=document.createTextNode("\u2713");
	var node4=document.createTextNode("\u00D7");
	if(task=="")
	{
		alert("You must write something!");
		return;
	}
	td1.appendChild(node1);
	td2.appendChild(node2);
	// td3.setAttribute("onclick","this.parentElement.style.display='none'");
	td3.setAttribute("onclick","doneitem(this)");
	td3.classList.add("done")
	td3.appendChild(node3);
	// td4.setAttribute("onclick","this.parentElement.style.display='none'");
	td4.setAttribute("onclick","removeitem(this)");
	td4.classList.add("close");
	td4.appendChild(node4);
	tr.appendChild(td1);
	tr.appendChild(td2);
	tr.appendChild(td3);
	tr.appendChild(td4);
	document.getElementById("table").appendChild(tr);
	document.getElementById("input").value="";

}

// this code for confirmation

function removeitem(th){
	var r=confirm("You want to discard!");
	if(r==true)
		th.parentElement.style.display='none';

}

// this code for done

function doneitem(x)
{
	x.parentElement.classList.add("task-done");
}

function Checkname(username){
	var req= new XMLHttpRequest()
	req.onload=function(){
		
		if(this.responseText=="true")
		{
			
			document.getElementById('demo').innerHTML='username available'
			document.getElementById('demo').style.color='green'
			document.getElementById('submit').disabled=false
			if(username.length==0)
			{
				document.getElementById('demo').innerHTML=''
				document.getElementById('submit').disabled=true
			}
		}
		else{
			document.getElementById('demo').innerHTML='username already exits'
			document.getElementById('demo').style.color='red'
			document.getElementById('submit').disabled=true
		}
	}
	req.open("GET","http://127.0.0.1:8000/check-name?username="+username,true)
	req.send()
}

$(document).ready(function(){

	// Password varification 

	$('#ps').keyup(function(){
		let value = $(this).val()
		if(value.length==0)
		{
			$('#l1').css({'color':'black'}).text('Minimum 8 chars and Maximum 12 chars')
			$('#l2').css({'color':'black'})
			$('#l3').css({'color':'black'})
			$('#l4').css({'color':'black'})
		}
		if(value.length>=8 && value.length<=20)
		{
			$('#l1').css({'color':'green'}).text('Minimum 8 chars and Maximum 12 chars')	
		}
		else if(value.length>20)
		{
			$('#l1').css({'color':'red'}).text("Can't more than 12 chars")	
		}
		if(value.includes('@')||value.includes('#')||value.includes('&')||value.includes('$')||value.includes('%')){
			$('#l2').css({'color':'green'})
		}
		if(value.includes('0')||value.includes('1')||value.includes('2')||value.includes('3')||value.includes('4')||value.includes('5')||value.includes('6')||value.includes('7')||value.includes('8')||value.includes('9'))
		{
			$('#l3').css({'color':'green'})
		}
		for(var i=0;i<value.length;i++)
		{	
			if(value[i].charCodeAt(0)>=65 && value[i].charCodeAt(0)<=90)
			{
				$('#l4').css({'color':'green'})
			}
		}
	})



	// javascript code for visibility to singup page
	
	$('#visibility').click(function(){
		var get_text = $(this).text()
		// console.log(get_text)
		if(get_text=='visibility_off'){
			$('#ps').attr('type','text');
			$('#visibility').text('visibility');
		}
		else{
			$('#ps').attr('type','password');
			$('#visibility').text('visibility_off');
		}
	})

	// javascript code of visibility for login page

	$('#visit').click(function(){
		var get_text = $(this).text()
		if(get_text=='visibility_off'){
			$('#pas').attr('type','text');
			$('#visit').text('visibility');
		}
		else{
			$('#pas').attr('type','password');
			$('#visit').text('visibility_off');
		}

	})

	// Username verification Jquery and Ajax


	$('#unm').keyup(function(){
		let username = $(this).val()
		$.ajax({
			type:"GET",
			url:"/check-name/",
			data:{
				user:username,
			},
			success:function(data){
				if($('#unm').val()=='')
				{
					var temp=''
					$('#demo').text(temp)
					// $('#demo').remove()
				}
				else{
					if(data.value=='true')
					{
						let temp1 = $('#demo').text('Username available')
						temp1.css({'color':'green','font-style':'italic','font-size':'12px'})

					}
					else{
						let temp2 = $('#demo').text('Username alredy exit')
						temp2.css({'color':'red'})
					}
				}
			}
		})

	})
})
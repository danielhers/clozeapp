		var sum_scores = 0.0;
		
		function prepare_page() {
			//setting the popovers over the cloze words 
			set_cloze_attributes();
			
			$(".cloze-chunk").click(function() {
			   cloze_click(this.id);
			});
			
			//enabling the popovers 
			$(function () {
				$('[data-toggle="popover"]').popover({html: true});
			});
		};
		
		//this function sets the properties of the popover when the cloze word is clicked
		function set_cloze_attributes () {
			$(".cloze-chunk").each(function() {
				$(this).attr("data-container", "body");
				$(this).attr("data-toggle", "popover");
				$(this).attr("data-placement", "bottom");
				//TODO: to be replaced
				$(this).attr("data-content", "<button type=\"button\" class=\"btn btn-danger\" caller=\""+ this.id +"\" value=0 onclick=\"on_result_click(this)\">Forgot</button> " +
								"<button type=\"button\"; class=\"btn btn-warning\" caller=\""+ this.id +"\" value=1 onclick=\"on_result_click(this)\" >Hard</button> " + 
								"<button type=\"button\"; class=\"btn btn-success\" caller=\""+ this.id +"\" value=2 onclick=\"on_result_click(this)\">Easy</button>");
			
			});
		}
		
		//making the word visible in case of clicking
		function cloze_click(elem_id) {
			$("#"+elem_id).css("color", "rgba(0,0,0,1.0)");
		}
		
		//this function is activated when the user clicks on difficulty of a certain word
		function on_result_click(elem){
			var url = "/update/"+elem.getAttribute("caller"); 
			
			//color the word in the relevant color
			switch (elem.value) {
				case "0":
					var x = "#"+elem.getAttribute("caller");
					$("#"+elem.getAttribute("caller")).css("background-color", "red");
					break;
				
				case "1":
					$("#"+elem.getAttribute("caller")).css("background-color", "orange");
					break;
				
				case "2":
					$("#"+elem.getAttribute("caller")).css("background-color", "#49E20E");
					break;
			}
			//hide the popover 
			$("#"+elem.getAttribute("caller")).popover('hide');
			sum_scores = sum_scores + parseInt(elem.value);
			
			//sending the score to the server 
			$.ajax({
				type: "GET",
				url: url,
				data: {rating: elem.value}
			});
			
		}
		
		//calculating the grade
		function on_end_click() {
			var maximal_score = $(".cloze-chunk").length*2.0;
			var grade = sum_scores*100/maximal_score;
			$("#myModal_grade").html(grade.toFixed(1));
		}
		
		
		$(document).ready(prepare_page);
		
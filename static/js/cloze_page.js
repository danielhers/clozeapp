		var sum_scores = 0.0;
		var maximal_score = 6.0;
		
		function prepare_page() {
			set_cloze_attributes();
			
			$(".cloze-chunk").click(function() {
			   cloze_click(this.id);
			});
			
			var dec_id=3;
			var skip_url = "/skip/" + dec_id;
			$(".skip_button").attr("href",skip_url);
			
			$(function () {
				$('[data-toggle="popover"]').popover({html: true});
			});
		};
		
		function set_cloze_attributes () {
			$(".cloze-chunk").each(function() {
				$(this).attr("data-container", "body");
				$(this).attr("data-toggle", "popover");
				$(this).attr("data-placement", "bottom");
				$(this).attr("data-content", "<button type=\"button\" class=\"btn btn-danger\" caller=\""+ this.id +"\" value=0 onclick=\"on_result_click(this)\">Forgot</button> " +
								"<button type=\"button\"; class=\"btn btn-warning\" caller=\""+ this.id +"\" value=1 onclick=\"on_result_click(this)\" >Hard</button>" + 
								"<button type=\"button\"; class=\"btn btn-success\" caller=\""+ this.id +"\" value=2 onclick=\"on_result_click(this)\">Easy</button>");
			
			});
		}
		
		function cloze_click(elem_id) {
			$("#"+elem_id).css("color", "rgba(0,0,0,1.0)");
		}
		
		function on_result_click(elem){
			var url = "/update/"+elem.getAttribute("caller"); 
			
			switch (elem.value) {
				case "0":
					var x = "#"+elem.getAttribute("caller");
					$("#"+elem.getAttribute("caller")).css("background-color", "red");
					break;
				
				case "1":
					$("#"+elem.getAttribute("caller")).css("background-color", "orange");
					break;
				
				case "2":
					$("#"+elem.getAttribute("caller")).css("background-color", "green");
					break;
			}
			$("#"+elem.getAttribute("caller")).popover('hide');
			sum_scores = sum_scores + parseInt(elem.value);
			
			
			$.ajax({
				type: "POST",
				url: url,
				data: elem.value,
			});
			
		}
		
		function on_end_click() {
			var grade = sum_scores*100/maximal_score;
			$("#myModal_grade").html(grade.toFixed(1));
		}
		
		
		$(document).ready(prepare_page);
		
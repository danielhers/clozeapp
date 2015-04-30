		function prepare_page() {
			set_cloze_attributes();
			
			$(".cloze-chunk").click(function() {
			   cloze_click(this.id);
			});
			
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
			$("#"+elem_id).css("opacity", "1.0");
		}
		
		function on_result_click(elem){
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
			
		}
	
		
		$(document).ready(prepare_page);
		
		
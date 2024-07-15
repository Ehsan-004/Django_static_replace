# Replcae static addresses for Django
This code can replace all static file addresses in a template file with its django standard form, for example it'll replace ```HTML <script src="js/respond.min.js"></script>``` with ```HTML 	<script src="{% static 'js/respond.min.js' %}"></script>```.
Enter your code to be replaced in the input_file.txt and the run the replace.py file. The output will be in the output.txt file.
soon you can address a file and then replace it without copy and paste codes...

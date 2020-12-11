def read_cli_input(cli_input):
	if len(cli_input) < 5:
		raise Exception("Missing Arguments")
		

	dataset_folder = cli_input[1]
	noise_folder = cli_input[2]

	if len(cli_input) >= 5:
		source_a = cli_input[3]
		source_b = cli_input[4]

	if len(cli_input) >= 6:
		max_page = int(cli_input[5])
	else:
		max_page = None
	
	return dataset_folder, noise_folder, source_a, source_b, max_page
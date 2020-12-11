def read_cli_input(cli_input):
	if len(cli_input) < 4:
		raise Exception("Missing Arguments")
		

	dataset_folder = cli_input[1]


	if len(cli_input) >= 4:
		source_a = cli_input[2]
		source_b = cli_input[3]

	if len(cli_input) >= 5:
		max_page = int(cli_input[4])
	else:
		max_page = None

	return dataset_folder, source_a, source_b, max_page
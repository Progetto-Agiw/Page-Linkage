def accuracy(predicted_relationships, true_relationships):
		assert (len(predicted_relationships) == len(true_relationships)), "relationships should have the same length"
		sort_by_first_site = lambda predction: predction[0]
		predicted_relationships.sort(key=sort_by_first_site)
		true_relationships.sort(key=sort_by_first_site)

		good_predictions = 0

		for i in range(len(predicted_relationships)):
			if predicted_relationships[i] == true_relationships[i]:
				good_predictions += 1

		return good_predictions / len(true_relationships)


def precision_recall(predicted_relationships, true_relationships):
	precision = []
	recall = []

	true_positives = 0
	number_of_predictions = len(predicted_relationships)

	for i in range(number_of_predictions):
		p1, p2 = predicted_relationships[i]
		if (p1, p2) in true_relationships:
			true_positives += 1

		current_precision = true_positives/(i+1)
		current_recall = true_positives/len(true_relationships)
		precision.append(current_precision)
		recall.append(current_recall)

		if current_recall >= 1.0:
			break

	return precision, recall
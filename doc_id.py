class DocumentSearch:
	def __init__(self, docs):
		# Store documents as a list of (doc_id, text) tuples
		self.docs = docs

	def search(self, query):
		# Split the query to determine if it's a single word or a phrase
		query_words = query.split()

		# If there's only one word, do a word search
		if len(query_words) == 1:
			return self.search_word(query)
		# If it's a phrase (more than one word), do a phrase search
		else:
			return self.search_phrase(query)

	def search_word(self, word):
		# Return a list of doc IDs where the word is present
		result = []
		for doc_id, text in self.docs:
			if word in text.split():
				result.append(doc_id)
		return result

	def search_phrase(self, phrase):
		# Return a list of doc IDs where the exact phrase is present
		result = []
		for doc_id, text in self.docs:
			if phrase in text:
				result.append(doc_id)
		return result


# Example usage
docs = [
	[1, "confluent is a cloud computing company"],
	[2, "seattle is the new hub for cloud computing"]
]
search_engine = DocumentSearch(docs)

# Test cases
print(search_engine.search("cloud"))  # Output: [1, 2]
print(search_engine.search("confluent is a"))  # Output: [1]
print(search_engine.search("cloud computing"))  # Output: [1, 2]

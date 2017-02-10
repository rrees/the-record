import logging

def extract_tags(tag_string):
	tags = tag_string.lower().split(',')
	logging.info(tags)

	return [t.strip() for t in tags]